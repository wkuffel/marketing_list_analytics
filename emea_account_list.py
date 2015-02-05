__author__ = 'wkuffel'
__author__ = 'wkuffel'

import csv
from fuzzywuzzy import fuzz


class account_list(object):

    def __init__(self, path, out_path):
        self.path = path
        self.out_path = out_path
        self.writing_field_names_ordered = ['Clean Company Name', 'Industry', 'Revenue ($M)', 'Owner', 'Notes', 'Company Name']
        self.import_csv()
        self.write_to_csv()
        #self.inspect_duplicates()

    def import_csv(self):
        with open(self.path) as f:
            reader = csv.DictReader(f)
            acct_list = []
            for row in reader:
                updated_row1 = self.gen_clean_account_name(row)
                acct_list.append(updated_row1)
                #print updated_row1
                #print row
            self.acct_list = acct_list

    def write_to_csv(self):
        with open(self.out_path, 'w') as write_csv:
            writer = csv.DictWriter(write_csv, fieldnames= self.writing_field_names_ordered, lineterminator = '\n')
            writer.writeheader()
            for row in self.acct_list:
                #print row.keys()
                writer.writerow(row)


    def gen_clean_account_name(self, row):
        row['Clean Company Name'] = row['Company Name'].lower().strip()
        row['Clean Company Name'] = row['Clean Company Name'].replace('.', '')
        row['Clean Company Name'] = row['Clean Company Name'].replace(',', '')
        row['Clean Company Name'] = row['Clean Company Name'].replace('"', '')

        if  row['Clean Company Name'][-4:] ==" inc":
            row['Clean Company Name'] = row['Clean Company Name'][:-4]
            #print row['Clean Company Name']
        if  row['Clean Company Name'][-4:] ==" llc":
            row['Clean Company Name'] = row['Clean Company Name'][:-4]
            #print row['Clean Company Name']
        if  row['Clean Company Name'][-3:] ==" lp":
            row['Clean Company Name'] = row['Clean Company Name'][:-3]
            #print row['Clean Company Name']
        if  row['Clean Company Name'][-5:] ==" corp":
            row['Clean Company Name'] = row['Clean Company Name'][:-5]
            #print row['Clean Company Name']
        if  row['Clean Company Name'][-5:] ==" co":
            row['Clean Company Name'] = row['Clean Company Name'][:-3]
            #print row['Clean Company Name']

        row['Clean Company Name'] = row['Clean Company Name'].replace('corporation', '')
        row['Clean Company Name'] = row['Clean Company Name'].replace('corp', '')
        row['Clean Company Name'] = row['Clean Company Name'].replace('company', '')
        row['Clean Company Name'] = row['Clean Company Name'].replace('the', '')

        row['Clean Company Name'] = row['Clean Company Name'].replace('-', ' ')
        row['Clean Company Name'] = row['Clean Company Name'].replace(' and ', ' & ')
        row['Clean Company Name'] = row['Clean Company Name'].replace(' + ', ' & ')
        row['Clean Company Name'] = row['Clean Company Name'].strip()

        #print row['Clean Company Name']
        return row








account_list('C:/Users/wkuffel/Desktop/Marketing Data/20150120 marketo update/EMEA top 30 prospects 2015.csv', 'C:/Users/wkuffel/Desktop/Marketing Data/20150120 marketo update/EMEA top 30 prospects 2015 manipulated.csv')
