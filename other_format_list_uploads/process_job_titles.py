__author__ = 'wkuffel'

import csv

from master_functions.clean_account_name import clean_account_name
from master_functions.label_analytics_title import label_analytics_buyer
from master_functions.label_bi_buyer import label_bi_buyer
from master_functions.label_sales_buyer import label_sales_buyer
from master_functions.label_embedded_buyer import label_embedded_buyer
from master_functions.label_maketing_buyer import label_marketing_buyer
from master_functions.label_titles import label_decision_maker, label_title
from master_functions.label_operations_buyer import label_operations_buyer
from master_functions.unique_buyer_type import unique_buyer_type
from master_functions.label_tech_product import label_tech_product


class processJobTitles(object):
    def __init__(self, filepath, outpath):
        self.in_path = filepath
        self.out_path = outpath
        self.added_keys =['Sales Title', 'Operations Title', 'Clean Company Name1', 'Marketing Title', 'BI Title', 'OEM Title', 'Decision Maker', 'Analytics Title', 'Title Group', 'Tech Product']
        self.import_csv()
        self.write_to_csv()


    def import_csv(self):
        acct_list = []
        with open(self.in_path) as f:
            reader = csv.DictReader(f)
            self.lead_list = []
            for row in reader:
                self.initial_keys = row.keys()
                try:
                    #row['Clean Company Name1'] = clean_account_name(row['Account Name'])
                    updated_row2 = label_decision_maker(row)
                    updated_row3 = label_title(updated_row2)
                    updated_row4 = label_sales_buyer(updated_row3)
                    updated_row5 = label_marketing_buyer(updated_row4)
                    updated_row6 = label_operations_buyer(updated_row5)
                    updated_row7 = label_embedded_buyer(updated_row6)
                    updated_row8 = label_analytics_buyer(updated_row7)
                    updated_row9 = label_bi_buyer(updated_row8)
                    updated_row10 = label_tech_product(updated_row9)
                    self.lead_list.append(updated_row10)
                except AttributeError:
                    pass

    def write_to_csv(self):
        with open(self.out_path, 'w') as write_csv:
            writer = csv.DictWriter(write_csv, fieldnames=self.initial_keys +  self.added_keys, lineterminator = '\n')
            writer.writeheader()
            for row in self.lead_list:
                #print row
                writer.writerow(row)
                #print row

processJobTitles('C:/Users/wkuffel/Desktop/Marketing Data/20150413 marketing list clean up/prelim clean up raw.csv', 'C:/Users/wkuffel/Desktop/Marketing Data/20150413 marketing list clean up/prelim clean up processed.csv')