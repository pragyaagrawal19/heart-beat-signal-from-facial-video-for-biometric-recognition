# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8');
import math

import os
import fnmatch
from ppg import BASE_DIR
from ppg.utils import exist, load_json, dump_json, load_model, dump_model, export_csv
from ppg.learn import get_feature_set
from ppg.learn import logistic_regression_classifier
# from ppg.learn import support_vector_classifier
from ppg.learn import gaussian_naive_bayes_classifier
from ppg.learn import decision_tree_classifier
from ppg.learn import random_forest_classifier, adaboost_classifier, gradient_boosting_classifier
from ppg.learn import voting_classifier



def classify():
    extracted_data_dir = os.path.join(BASE_DIR, 'data', 'splited')
    result_dir = os.path.join(BASE_DIR, 'results')

    train_ratio = 0.8
    classifiers = [
        ('logistic_regression', logistic_regression_classifier, ),
        # ('support_vector', support_vector_classifier, ),
        ('gaussian_naive_bayes', gaussian_naive_bayes_classifier, ),
        ('decision_tree', decision_tree_classifier, ),
        ('random_forest', random_forest_classifier, ),
        ('adaboost', adaboost_classifier, ),
        ('gradient_boosting', gradient_boosting_classifier, ),
        #('voting', voting_classifier, ), # voting classifier has to be the LAST item in the list
    ]

    if exist(pathname=extracted_data_dir):
        train_features = []
        train_labels = []
        test_features = []
        test_labels = []
        for filename_with_ext in fnmatch.filter(os.listdir(extracted_data_dir), '*.json'):
            pathname = os.path.join(extracted_data_dir, filename_with_ext)
            json_data = load_json(pathname=pathname)
            if json_data is not None:
                participant = filename_with_ext.split('.')[0]
                signal_list = []
                count = 0
                for label in json_data:
                    signal_list.append = json_data[label]['signal']
                    if len(signal) == 0:
                        continue
                    else:
                        for s in signal:
                            signal_list.append(s)
                            count = count + 1
                if len(signal_list) == 0:
                    continue
                if signal_list == 1:
                    train_features.append(signal_list[0])
                    train_features.append(participant)
                else:
                    for index,signal in enumerate(signal_list):
                        if index == len(signal_list) - 1:
                            test_features.append(signal)
                            test_labels.append(participant)
                        else:
                            train_features.append(signal)
                            train_labels.append(participant)

                        # train_features, train_labels, test_features, test_labels = get_feature_set(data=json_data, label_set=label_set, feature_type_set=feature_type_set)
    estimators = []
    for classifier_name, classifier_object in classifiers:
        import pdb;pdb.set_trace()
        classifier = classifier_object(features=train_features, labels=train_labels)
        score = classifier.score(test_features,test_labels)
        
        # if classifier_name not in result_data[label_set_name][feature_type_set_name]:
            # result_data[label_set_name][feature_type_set_name][classifier_name] = {}
            # model_pathname = os.path.join(model_dir, label_set_name, feature_type_set_name, classifier_name, '%s.model' % participant)
                            # classifier = load_model(pathname=model_pathname)
                            # if classifier is None:
                                # if classifier_name == 'voting':
                                    # classifier = classifier_object(estimators=estimators, features=train_features, labels=train_labels)
                                # else:
                                    # classifier = classifier_object(features=train_features, labels=train_labels)
                                # dump_model(model=classifier, pathname=model_pathname)
                            # score = classifier.score(test_features, test_labels)
                            # print participant, score, label_set_name, feature_type_set_name, classifier_name
                            # result_data[label_set_name][feature_type_set_name][classifier_name][participant] = score

                            # prepare estimators for the training of voting classifier
                            # if classifier_name != 'voting':
                                # if hasattr(classifier, 'best_estimator_'):
                                    # estimators.append((classifier_name, classifier.best_estimator_, ))
                                # else:
                                    # estimators.append((classifier_name, classifier, ))

        # for label_set_name in result_data:
            # dump_json(data=result_data[label_set_name], pathname=os.path.join(result_dir, '%s.json' % label_set_name), overwrite=True)
            # csv_data = []
            # for feature_type_set in feature_type_sets:
                # feature_type_set_name = '-'.join(feature_type_set)
                # csv_row = {
                    # 'feature_set': feature_type_set_name,
                # }
                # for classifier_name in result_data[label_set_name][feature_type_set_name]:
                    # csv_row[classifier_name] = sum(result_data[label_set_name][feature_type_set_name][classifier_name].values()) / len(result_data[label_set_name][feature_type_set_name][classifier_name])
                # csv_data.append(csv_row)
            # fieldnames = ['feature_set'] + [val[0] for val in classifiers]
            # export_csv(data=csv_data, fieldnames=fieldnames, pathname=os.path.join(result_dir, '%s.csv' % label_set_name), overwrite=True)


if __name__ == '__main__':
    classify()