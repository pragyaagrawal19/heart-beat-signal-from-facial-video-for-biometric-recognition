import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8');

import os
import fnmatch
from ppg import BASE_DIR
from ppg.params import PPG_SAMPLE_RATE
from ppg.utils import exist, load_text, dump_json

raw_data_dir = os.path.join(BASE_DIR, 'data', 'raw')

def convert():
    with open('ppg.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # import pdb;pdb.set_trace()
            participant = row[0]
            label  = row[1]
            signal = row[2:-1]
            
            filename = '%s-%s.txt'%(participant,label)
            output_filename = os.path.join(raw_data_dir,filename)
            signal_value = [float(s) for s in signal]
            # with open(output_filename,'w') as file:
                # writer = csv.writer(file)
                # writer.writerows(signal_value)
            file_object = open(output_filename,'w+')
            for value in signal_value:
                value = str(value)
                file_object.write(value)
                file_object.write("\n")
            
            # file_object.writelines(signal)
            # file_object.close()

if __name__ == '__main__':
    convert()
