import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8');


import os
import fnmatch
from ppg import BASE_DIR
from ppg.params import PPG_SAMPLE_RATE
from ppg.utils import exist, load_text, dump_json
from ppg.signal import smooth_ppg_signal
from ppg.feature import extract_ppg45

import math
from ppg.learn import logistic_regression_classifier
from ppg.learn import support_vector_classifier
from ppg.learn import decision_tree_classifier
from ppg.learn import random_forest_classifier, adaboost_classifier

from sklearn.preprocessing import MinMaxScaler
from sklearn import metrics


def convert():
    splited_data_dir = os.path.join(BASE_DIR, 'data', 'splited')
    output_data = {}
    with open('ppg.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            participant = row[0]
            signal = row[2:-1]
            signal_value = [float(s) for s in signal]
            if participant not in output_data.keys():
                output_data[participant] = []
            output_data[participant].append(signal_value)
            
    feature_data = {}
    for label,signal_list in output_data.items():
        feature_signals = []
        for signal in signal_list:
            smooth_signal = smooth_ppg_signal(signal)
            sig  = extract_ppg45(smooth_signal)
            if len(sig) != 0:
                feature_signals.append(sig)
        if len(feature_signals) != 0:
            feature_data[label] = feature_signals
    output_filename = "feature_data.json"
    dump_json(data=feature_data, pathname=os.path.join(splited_data_dir, output_filename), overwrite=True)
    return feature_data

def Normalization(feature_data):
    signal_lens = []
    final_output = {}
    global_signal_list = []
    for value in feature_data.values():
        signals = len(value)
        signal_lens.append(signals)
        global_signal_list.extend(value)
    x_scaler = MinMaxScaler()
    scaled_signals = x_scaler.fit_transform(global_signal_list)
    count  = 0 
    labels = feature_data.keys()
    for index,lens  in  enumerate(signal_lens):
        signal_list = []
        for i in range(lens):
            signal_list.append(scaled_signals[count])
            count = count + 1
        final_output[labels[index]] = signal_list
    return final_output
        

def train_test_split(feature_data,train_ratio=0.8):
    train_label = []
    train_feature = []
    test_label = []
    test_feature = []
    
    for label,signal_list in feature_data.items():
        index = math.ceil(len(signal_list)*train_ratio)
        index = int(index)
        for i in range(len(signal_list)):
            if len(signal_list) == 1:
                train_label.append(label)
                train_feature.append(signal_list[i])
                test_feature.append(signal_list[i])
                test_label.append(label)
            else:
                if i < index:
                    train_label.append(label)
                    train_feature.append(signal_list[i])
                else:
                    test_label.append(label)
                    test_feature.append(signal_list[i])
    return (train_feature,train_label,test_feature,test_label)


def classify(train_feature,train_label,test_feature,test_label):
    classifiers = [
    ('logistic_regression', logistic_regression_classifier, ),
    ('support_vector', support_vector_classifier, ),
    ('decision_tree', decision_tree_classifier, ),
    ('random_forest', random_forest_classifier, ),
    ('adaboost', adaboost_classifier, ),
    ]
    
    for classifier_name, classifier_object in classifiers:
        classifier = classifier_object(features=train_feature, labels=train_label)
        score = classifier.score(test_feature,test_label)
        print(classifier_name , score)
        
        pred_label = classifier.predict(test_feature)
        
        for ind,value_label in enumerate(test_label):
            print(value_label,pred_label[ind])
            
        print("Confusion Matrix")
        print("-----------------------------------------")
        print(metrics.confusion_matrix(test_label,pred_label))
        print("-------------------------------------------------")
        print("Classification Report")
        print("-----------------------------------------------")
        print(metrics.classification_report(test_label,pred_label))
        print("---------------------------------------------------") 



if __name__ == '__main__':
    feature_data = convert()
    feature_data = Normalization(feature_data)
    train_feature,train_label,test_feature,test_label = train_test_split(feature_data)
    classify(train_feature,train_label,test_feature,test_label)
    
    
    
