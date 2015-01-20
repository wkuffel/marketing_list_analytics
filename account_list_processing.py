__author__ = 'wkuffel'

import csv
from fuzzywuzzy import fuzz


class account_list(object):

    def __init__(self, path, out_path):
        self.path = path
        self.out_path = out_path
        self.writing_field_names_ordered = ['Account ID','Account Name','Equifax ID','Account Owner', 'Region', 'Sales Team', 'Account Type','Industry','Company Employee Range','Annual Company Revenue Range','Total Opportunities','Total Won Opportunities','Total Won Opportunity Value','Total Open Opportunities','HQ Country','HQ State','HQ Zip','Account Status','Clean Company Name']
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
                #print row
            self.acct_list = acct_list[:-7]

    def write_to_csv(self):
        with open(self.out_path, 'w') as write_csv:
            writer = csv.DictWriter(write_csv, fieldnames= self.writing_field_names_ordered, lineterminator = '\n')
            writer.writeheader()
            for row in self.acct_list:
                writer.writerow(row)


    def gen_clean_account_name(self, row):
        row['Clean Company Name'] = row['Account Name'].lower().strip()
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

    def inspect_duplicates(self):
        total_dups =0
        updated_accts = []
        for check_row in self.acct_list:
            check_row['Duplicate'] = 0
            for target_row in self.acct_list:
                if check_row['Account ID'] != target_row['Account ID']:
                    if fuzz.token_set_ratio(check_row['Clean Company Name'], target_row['Clean Company Name'])>90 :
                        #print "token_set ratio: " + check_row['Clean Company Name'] + ' | ' + target_row['Clean Company Name']
                        check_row['Duplicate'] = 1
                        total_dups +=1

            updated_accts.append(check_row)
        self.acct_list = updated_accts
        print total_dups








#account_list('C:/Users/wkuffel/Desktop/Marketing Data/target account list 20140115.csv', 'C:/Users/wkuffel/Desktop/Marketing Data/target account list 20140115 will manipulated.csv')
