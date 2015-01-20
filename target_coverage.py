__author__ = 'wkuffel'

import csv
from fuzzywuzzy import fuzz


class target_coverage(object):
    def __init__(self, target_account_ds_filepath, marketing_ds_filepath, out_path, for_marketo = False):
        self.marketing_ds_filepath = marketing_ds_filepath
        self.target_account_ds_filepath = target_account_ds_filepath
        self.out_path = out_path

        self.import_marketing_ds()
        self.import_target_account_ds()
        self.match_datasets()

        if for_marketo == False:
            self.write_to_csv()
        else:
            self.write_to_csv_marketo()


    def write_to_csv_marketo(self):
        with open(self.out_path, 'w') as write_csv:
            writer = csv.DictWriter(write_csv, fieldnames= ['Id', 'Email Address', 'Decision Maker', 'Sales Buyer', 'Marketing Buyer', 'BI Buyer', 'OEM Buyer', 'Target Account' ], lineterminator = '\n')
            writer.writeheader()
            for row in self.concatendated_ds:
                updated_row = {x: row[x] for x in row if x in ['Id', 'Email Address', 'Decision Maker', 'Sales Buyer', 'Marketing Buyer', 'BI Buyer', 'OEM Buyer', 'Target Account']}
                writer.writerow(updated_row)


    def import_marketing_ds(self):

        with open(self.marketing_ds_filepath) as marketing_file:
            marketing_ds_reader = csv.DictReader(marketing_file)
            marketing_ds = []
            for row in marketing_ds_reader:
               marketing_ds.append(row)
            self.marketing_ds = marketing_ds

    def import_target_account_ds(self):
        with open(self.target_account_ds_filepath) as target_acct_file:
            target_acct_file_reader = csv.DictReader(target_acct_file)
            target_accounts_ds = []
            for row in target_acct_file_reader:
               target_accounts_ds.append(row)
            self.target_accounts_ds = target_accounts_ds

    def match_datasets(self):
        match_count = 0
        record_count = 0
        concatenated_ds = []
        for row_marketing in self.marketing_ds:
            record_count +=1
            if record_count %10000 ==0:
                print "row count: " + str(record_count)
            max_fuzz_record = None
            max_fuzz_value = 0

            for row_target in self.target_accounts_ds:
                #fuzz_value = fuzz.token_set_ratio(row_marketing["Clean Company Name1"], row_target["Clean Company Name"])

                if row_marketing["Clean Company Name1"] == row_target["Clean Company Name"]:
                    row_marketing.update(row_target)
                    row_marketing["Target Account"] = True
                    concatenated_ds.append(row_marketing)
                    match_count +=1
                    if match_count %10000 ==0:
                        print "match count: " + str(match_count)
                    break

                elif row_target["Clean Company Name"] in row_marketing["Clean Company Name1"] and len(row_target["Clean Company Name"])>=7:
                    row_marketing.update(row_target)
                    row_marketing["Target Account"] = True
                    concatenated_ds.append(row_marketing)
                    match_count +=1
                    break
                elif row_marketing["Clean Company Name1"] in row_target["Clean Company Name"] and len(row_marketing["Clean Company Name1"])>=7:
                    row_marketing.update(row_target)
                    row_marketing["Target Account"] = True
                    concatenated_ds.append(row_marketing)
                    match_count +=1
                    break
            else:
                row_marketing["Target Account"] = False
                concatenated_ds.append(row_marketing)



        self.concatendated_ds = concatenated_ds

    def write_to_csv(self):
        with open(self.out_path, 'w') as write_csv:
            writer = csv.DictWriter(write_csv, fieldnames= ['Id', 'First Name','Last Name', 'Email Address', 'Phone Number', 'SFDC Type', 'Company Name', 'Job Title','Annual Company Revenue Range', 'Company Industries', 'Annual Company Revenue Range (A)', 'Company Employee Range',   'Lead Status', 'Lead Source', 'Updated At', 'Lead Score', 'Decision Maker', 'Sales Buyer', 'Marketing Buyer', 'BI Buyer', 'OEM Buyer', 'Analytics Buyer', 'Clean Company Name1', 'HQ Country','Country','Region', 'State', 'HQ State'] + ['Account ID','Account Name','Equifax ID','Account Owner', 'Region', 'Sales Team', 'Account Type','Industry','Company Employee Range','Annual Company Revenue Range','Total Opportunities','Total Won Opportunities','Total Won Opportunity Value','Total Open Opportunities','HQ Country','HQ State','HQ Zip','Account Status','Clean Company Name'], lineterminator = '\n')
            writer.writeheader()
            for row in self.concatendated_ds:
                writer.writerow(row)





#target_coverage('C:/Users/wkuffel/Desktop/Marketing Data/target account list 20140115 will manipulated.csv','C:/Users/wkuffel/Desktop/Marketing Data/all Birst leads 20140115 will manipulated.csv', 'C:/Users/wkuffel/Desktop/Marketing Data/combined full dataset.csv')