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


class loadNetproxpex(object):

    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile
        self.writing_fields = ['PersonID', 'First Name', 'Last Name','E-Mail','Phone 1','Phone 2', 'Title', 'Organization', 'Common Organization Name', 'Industries',  'Street','City',  'State', 'Postal', 'Country',
                               'Employees', 'Revenue', 'SIC Code', 'County', 'SIC Description',  'Job Function', 'Facebook Profile', 'Twitter Profile','Website', 'LinkedIn Profile',
                               'Job Level', 'Title Group', 'BI Title', 'Operations Title', 'Decision Maker','Marketing Title' , 'Sales Title', 'OEM Title', 'Analytics Title',
                               'Clean Company Name1']



        self.import_csv()
        self.write_csv()

    def import_csv(self):
        acct_list = []
        with open(self.infile) as f:
            reader = csv.DictReader(f)

            count = 0
            country_check = []
            for row in reader:
                row['Clean Company Name1'] = clean_account_name(row['Common Organization Name'])
                updated_row2 = label_decision_maker(row, title = 'Title')
                updated_row3 = label_title(updated_row2, title = 'Title')
                updated_row4 = label_sales_buyer(updated_row3, title = 'Title')
                updated_row5 = label_marketing_buyer(updated_row4, title = 'Title')
                updated_row6 = label_bi_buyer(updated_row5, title = 'Title')
                updated_row7 = label_embedded_buyer(updated_row6, title = 'Title')
                updated_row8 = label_analytics_buyer(updated_row7, title = 'Title')
                updated_row9 = label_operations_buyer(updated_row8, title = 'Title')
                acct_list.append(updated_row9)
                self.acct_list = acct_list

    def write_csv(self):
        with open(self.outfile, 'w') as write_csv:
            writer = csv.DictWriter(write_csv, fieldnames=self.writing_fields, lineterminator = '\n')
            writer.writeheader()
            for row in self.acct_list:
                #del row[]
                writer.writerow(row)




infile = 'C:/Users/wkuffel/Desktop/Marketing Data/20150223 BI purchase preview/all titles/Birst_AllLevels_Preview.csv'
outfile = 'C:/Users/wkuffel/Desktop/Marketing Data/20150223 BI purchase preview/all titles/Birst_AllLevels_Preview processed2.csv'

loadNetproxpex(infile, outfile)
