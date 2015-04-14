__author__ = 'wkuffel'

import csv
#import pandas



class mqlAnalysis(object):
    "help determine who should be an MQL"

    def __init__(self, infile):
        self.infile = infile
        self.import_data()
        self.analyze()


    def import_data(self):
        with open(self.infile, mode = "rb") as f:
            file_reader = csv.DictReader(f)
            self.opportunity_list = []
            for row in file_reader:
                #will be ignoring pipeline becuase it can go either way
                row["Success"] = None
                if row["Stage"] == "7 Lost":
                    row["Success"] = 0
                elif row["Stage"] == "6 Closed":
                    row["Success"] = 1
                #print row["Success"]
                self.opportunity_list.append(row)
            #print len(self.opportunity_list)

    def analyze(self):
        total_success = 0
        total_failure = 0
        for row in self.opportunity_list:
            if row["Success"] == 0:
                total_failure +=1
            if row["Success"] == 1:
                total_success +=1
        print total_failure
        print total_success
mqlAnalysis('C:/Users/wkuffel/Desktop/Sales Data/Deal Size Analysis/Birst Opportunities with Lead Info.csv')