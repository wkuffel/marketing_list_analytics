__author__ = 'wkuffel'

import csv
#from fuzzywuzzy import fuzz
from  leads_by_target_account import lead_types_by_target_accounts

class target_coverage(object):
    def __init__(self, target_account_ds_filepath, marketing_ds_filepath, out_path, for_marketo = False, from_complete = False):
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
            writer = csv.DictWriter(write_csv, fieldnames= ['Id', 'Email Address', 'Decision Maker', 'Sales Title', 'Marketing Title', 'BI Title', 'OEM Title', 'Analytics Title', 'Target Account' ], lineterminator = '\n')
            writer.writeheader()
            for row in self.concatendated_ds:
                updated_row = {x: row[x] for x in row if x in ['Id', 'Email Address', 'Decision Maker', 'Sales Title', 'Marketing Title', 'BI Title', 'OEM Title', 'Analytics Title', 'Target Account']}
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
        try:
            with open(self.out_path, 'w') as write_csv:
                writer = csv.DictWriter(write_csv, fieldnames=['Id', 'First Name','Last Name', 'Email Address', 'Phone Number', 'SFDC Type', 'Company Name', 'Job Title','Annual Company Revenue Range', 'Company Industries', 'Annual Company Revenue Range (A)', 'Company Employee Range',   'Lead Status', 'Lead Source', 'Updated At', 'Lead Score', 'Decision Maker', 'Sales Title', 'Marketing Title', 'BI Title', 'OEM Title', 'Analytics Title', 'Title Group', 'Clean Company Name1', 'HQ Country','Country','Region', 'State', 'HQ State'] + ['Target Account', 'Account ID','Account Name','Equifax ID','Account Owner', 'Region', 'Sales Team', 'Account Type','Industry','Company Employee Range','Annual Company Revenue Range','Total Opportunities','Total Won Opportunities','Total Won Opportunity Value','Total Open Opportunities','HQ Country','HQ State','HQ Zip','Account Status','Clean Company Name'], lineterminator = '\n')

                #['Target Account', 'ID', 'Account Name', 'Primary Industry', 'Industry Breakout (from Count Tab)', 'Owner', 'Description', 'Revenue(USD)', 'Employees', 'Ownership', 'Ticker Symbol', 'SIC (US)', 'Primary NAICS', 'Address', 'City', 'State', 'Postal Code', 'Country', 'Phone', 'Fax', 'Website', 'Parent ID', 'Parent Name', 'Ultimate Parent ID', 'Ultimate Parent Name', 'Data Source(s)', 'Lead Source', 'EFX ID', ' Description', ' Primary Industry', 'Clean Company Name'], lineterminator = '\n')
                #'Target Account','Account ID','Account Name','Equifax ID','Account Owner', 'Region', 'Sales Team', 'Account Type','Industry','Company Employee Range','Annual Company Revenue Range','Total Opportunities','Total Won Opportunities','Total Won Opportunity Value','Total Open Opportunities','HQ Country','HQ State','HQ Zip','Account Status','Clean Company Name'], lineterminator = '\n')
                #['Clean Company Name', 'Industry', 'Revenue ($M)', 'Owner', 'Notes']
                #['Account ID','Account Name','Equifax ID','Account Owner', 'Region', 'Sales Team', 'Account Type','Industry','Company Employee Range','Annual Company Revenue Range','Total Opportunities','Total Won Opportunities','Total Won Opportunity Value','Total Open Opportunities','HQ Country','HQ State','HQ Zip','Account Status','Clean Company Name'], lineterminator = '\n')
                #['Target Account','Account ID','Account Name','Equifax ID','Account Owner', 'Region', 'Sales Team', 'Account Type','Industry','Company Employee Range','Annual Company Revenue Range','Total Opportunities','Total Won Opportunities','Total Won Opportunity Value','Total Open Opportunities','HQ Country','HQ State','HQ Zip','Account Status','Clean Company Name']
                writer.writeheader()
                for row in self.concatendated_ds:
                    writer.writerow(row)
        except:
            with open('C:/Users/wkuffel/Desktop/Marketing Data/exception file/exception.csv', 'w') as write_csv:
                writer = csv.DictWriter(write_csv, fieldnames=['Id', 'First Name','Last Name', 'Email Address', 'Phone Number', 'SFDC Type', 'Company Name', 'Job Title','Annual Company Revenue Range', 'Company Industries', 'Annual Company Revenue Range (A)', 'Company Employee Range',   'Lead Status', 'Lead Source', 'Updated At', 'Lead Score', 'Decision Maker', 'Sales Title', 'Marketing Title', 'BI Title', 'OEM Title', 'Analytics Title', 'Title Group', 'Clean Company Name1', 'HQ Country','Country','Region', 'State', 'HQ State'] + ['Target Account', 'Account ID','Account Name','Equifax ID','Account Owner', 'Region', 'Sales Team', 'Account Type','Industry','Company Employee Range','Annual Company Revenue Range','Total Opportunities','Total Won Opportunities','Total Won Opportunity Value','Total Open Opportunities','HQ Country','HQ State','HQ Zip','Account Status','Clean Company Name'], lineterminator = '\n')

                #['Target Account', 'ID', 'Account Name', 'Primary Industry', 'Industry Breakout (from Count Tab)', 'Owner', 'Description', 'Revenue(USD)', 'Employees', 'Ownership', 'Ticker Symbol', 'SIC (US)', 'Primary NAICS', 'Address', 'City', 'State', 'Postal Code', 'Country', 'Phone', 'Fax', 'Website', 'Parent ID', 'Parent Name', 'Ultimate Parent ID', 'Ultimate Parent Name', 'Data Source(s)', 'Lead Source', 'EFX ID', ' Description', ' Primary Industry', 'Clean Company Name'], lineterminator = '\n')
                #'Target Account','Account ID','Account Name','Equifax ID','Account Owner', 'Region', 'Sales Team', 'Account Type','Industry','Company Employee Range','Annual Company Revenue Range','Total Opportunities','Total Won Opportunities','Total Won Opportunity Value','Total Open Opportunities','HQ Country','HQ State','HQ Zip','Account Status','Clean Company Name'], lineterminator = '\n')
                #['Clean Company Name', 'Industry', 'Revenue ($M)', 'Owner', 'Notes']
                #['Account ID','Account Name','Equifax ID','Account Owner', 'Region', 'Sales Team', 'Account Type','Industry','Company Employee Range','Annual Company Revenue Range','Total Opportunities','Total Won Opportunities','Total Won Opportunity Value','Total Open Opportunities','HQ Country','HQ State','HQ Zip','Account Status','Clean Company Name'], lineterminator = '\n')
                #['Target Account','Account ID','Account Name','Equifax ID','Account Owner', 'Region', 'Sales Team', 'Account Type','Industry','Company Employee Range','Annual Company Revenue Range','Total Opportunities','Total Won Opportunities','Total Won Opportunity Value','Total Open Opportunities','HQ Country','HQ State','HQ Zip','Account Status','Clean Company Name']
                writer.writeheader()
                for row in self.concatendated_ds:
                    writer.writerow(row)




class target_from_complete(object):
    def __init__(self, filepath, outpath):
        self.filepath =filepath
        self.outpath = outpath

        self.import_file()
        self.write_to_csv_marketo()


    def import_file(self):
        with open(self.filepath) as complete_file_obj:
            complete_file_reader = csv.DictReader(complete_file_obj)
            complete_file = []
            for row in complete_file_reader:
               complete_file.append(row)
            self.complete_file = complete_file

    def write_to_csv_marketo(self):
        with open(self.outpath, 'w') as write_csv:
            writer = csv.DictWriter(write_csv, fieldnames= ['Id', 'Email Address', 'Decision Maker', 'Sales Title', 'Marketing Title', 'BI Title', 'OEM Title', 'Analytics Title','Target Account' ], lineterminator = '\n')
            writer.writeheader()
            for row in self.complete_file:
                updated_row = {x: row[x] for x in row if x in ['Id', 'Email Address', 'Decision Maker', 'Sales Title', 'Marketing Title', 'BI Title', 'OEM Title', 'Analytics Title',  'Target Account']}
                writer.writerow(updated_row)


#target_from_complete('C:/Users/wkuffel/Desktop/Marketing Data/combined full dataset.csv','C:/Users/wkuffel/Desktop/Marketing Data/combined full updated dataset marketo Kelly.csv')

#target_coverage('C:/Users/wkuffel/Desktop/Marketing Data/target account list 20140115 will manipulated.csv','C:/Users/wkuffel/Desktop/Marketing Data/all Birst leads 20140115 will manipulated.csv', 'C:/Users/wkuffel/Desktop/Marketing Data/combined full dataset.csv')

all_leads = 'C:/Users/wkuffel/Desktop/Marketing Data/all Birst leads 20140122 will manipulated title.csv'
targets = 'C:/Users/wkuffel/Desktop/Marketing Data/20150119 marketo update/output files/target account list 20150119 manipulated.csv'
outpath = 'C:/Users/wkuffel/Desktop/Marketing Data/20150122 carl request/converged all leads.csv'
#target_coverage(targets, all_leads, outpath)
lead_types_by_target_accounts(outpath,targets,'C:/Users/wkuffel/Desktop/Marketing Data/20150122 carl request/combined full dataset counts by acct.csv')
