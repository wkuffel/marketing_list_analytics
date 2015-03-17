__author__ = 'wkuffel'

import csv
from master_functions.label_titles import label_title
from master_functions.label_operations_buyer import label_operations_buyer

class import_and_add(object):
    def __init__(self, inpath,outpath):
        self.inpath = inpath
        self.outpath = outpath

        self.import_file()
        self.write_to_csv()

    def import_file(self):
        with open(self.inpath) as target_file:
            file_reader = csv.DictReader(target_file)
            file = []
            for row in file_reader:
                row1 = label_title(row)
                row2 = label_operations_buyer(row1)
                file.append(row2)
            self.file = file
            self.keys = self.file[0].keys()

    def write_to_csv(self):
        with open(self.outpath, 'w') as write_csv:
            writer = csv.DictWriter(write_csv, fieldnames= self.keys, lineterminator = '\n')
            writer.writeheader()
            for row in self.file:
                #print row
                writer.writerow(row)

#import_and_add('C:/Users/wkuffel/Desktop/Marketing Data/20150121 marketo update/results/combined full dataset.csv','C:/Users/wkuffel/Desktop/Marketing Data/20150121 marketo update/results/combined full dataset updated.csv')