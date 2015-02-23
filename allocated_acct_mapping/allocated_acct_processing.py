__author__ = 'wkuffel'

import csv
from master_functions.clean_account_name import clean_account_name
import pickle


class process_allocated_accounts(object):

    def __init__(self, inpath, outpath):
        self.inpath = inpath
        self.outpath = outpath
        self.writing_field_names_ordered = [
            'ID',
            'Account Name',
            'Ticker Symbol',
            'Address',
            'Country',
            'State',
            'City',
            'Postal Code',
            'Fax',
            'Phone',
            'Website',
            'Lead Source',

            'Parent ID',
            'Parent Name',
            'Ultimate Parent ID',
            'Ultimate Parent Name',
            'EFX ID',
            ' Description',
            'Primary NAICS',
            'SIC (US)',
            'Industry Breakout (from Count Tab)',
            'Employees',
            'Owner',
            'Revenue(USD)',
            'Data Source(s)',
            ' Primary Industry',
            'Ownership',
            'is_parent',
            'is_child',
            'Clean Company Name'  ]
            #['Account ID', 'Account Name', 'InsideView Account ID', 'Account Status', 'Total Opportunities', 'Sales Team', 'Account Owner', 'Region', 'HQ Country', 'HQ State', 'HQ Zip', 'Total Won Opportunities', 'Total Won Opportunity Value', 'Total Open Opportunities',  'Industry', 'Company Employee Range', 'Annual Company Revenue Range',  'Parent Account ID', 'Parent Account','Account Type', 'is_parent', 'is_child', 'Clean Company Name']
        self.parent_account_ids = {}
        self.import_csv()
        self.determine_parent_accounts()
        for a in self.parent_account_ids:
            print a + " " + str(self.parent_account_ids[a])
        self.write_to_csv()
        pickle.dump(self.parent_account_ids , open( 'C:/Users/wkuffel/Desktop/Marketing Data/20150218 allocated acct analysis/allocated_accts_parent_account_dict.p', "wb" ) )


    def import_csv(self):
        count = 0
        with open(self.inpath) as f:
            reader = csv.DictReader(f)
            acct_list = []
            for row in reader:
                #update row
                update_row1 = self.determine_child_account(row)
                update_row1['Clean Company Name'] = clean_account_name(update_row1['Account Name'])
                acct_list.append(update_row1)
                #print update_row1
            self.acct_list = acct_list

    def determine_child_account(self, row):
        row['is_child'] = False
        if row['Parent ID'] != '':
            row['is_child'] = True
            if row['Parent ID'] not in self.parent_account_ids:
                self.parent_account_ids[row['Parent ID']] ={row['Parent ID']: {"Account Name": row['Parent Name'], "ID": row['Parent ID'], "Clean Account Name" : clean_account_name(row['Parent Name'])}}
            if row['Parent ID'] in self.parent_account_ids:
                self.parent_account_ids[row['Parent ID']][row['ID']] = {"Account Name": row['Account Name'], "ID": row['ID'], "Clean Account Name" : clean_account_name(row['Account Name'])}
                #print self.parent_account_ids[row['Parent Account ID']]
        return row

    def determine_parent_accounts(self):
        new_acct_list = []
        parent_keys = self.parent_account_ids.keys()
        for row in self.acct_list:

            if row['ID'] in parent_keys:
                row['is_parent'] = True
            else:
                row['is_parent'] = False
            new_acct_list.append(row)
        self.acct_list = new_acct_list

    def write_to_csv(self):
        with open(self.outpath, 'w') as write_csv:
            writer = csv.DictWriter(write_csv, fieldnames= self.writing_field_names_ordered, lineterminator = '\n')
            writer.writeheader()
            for row in self.acct_list:
                #print row.keys()
                #print row.keys()
                writer.writerow(row)


infile = 'C:/Users/wkuffel/Desktop/Marketing Data/20150218 allocated acct analysis/Birst allocated accounts.csv'
outfile = 'C:/Users/wkuffel/Desktop/Marketing Data/20150218 allocated acct analysis/Birst allocated accounts processed.csv'


process_allocated_accounts(infile, outfile)