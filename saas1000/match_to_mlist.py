__author__ = 'wkuffel'
__author__ = 'wkuffel'

import csv
from fuzzywuzzy import fuzz
import pickle

class match_leads_to_accounts(object):

    def __init__(self, lead_file, account_file, out_file):
        self.marketing_ds_filepath = lead_file
        self.target_account_ds_filepath = account_file
        self.out_path = out_file
        self.write_fields = ['Id',
        'Marketo SFDC ID',
        'Full Name',
        'First Name',
        'Last Name',
        'Job Title',
        'Phone Number',
        'Email Address',
        'Lead Source',
        'Company Name',
        'Lead Status',
        'Lead Score',
        'Country',
        'Region',
        'Company Industries',
        'Annual Company Revenue Range (A)',
        'State',
        'InsideView Account ID',
        'Matched Clean Name',

        'Sales Title',
        'Marketing Title',
        'OEM Title',
        'BI Title',
        'Analytics Title',
        'Operations Title',
        'Decision Maker',
        'Title Group',
        'Clean Company Name1',
        'Tech Product',

        'Updated At',
        'Company Employee Range',
        'Annual Company Revenue Range',
        'SFDC Type',
        'Company Name',
        "Lead Rank",
        'Clean Company Name1',

        'Matched',
        'Clean Company Name',
        'Account ID',
        'Parent Account',
        'Parent Account ID',
        'Account Name',
        'Account Type',
        'Account Owner',
        'HQ Country',
        'HQ State',
        'HQ Zip',
        'Account Status',
        'Industry',
        'Total Won Opportunity Value',
        'Total Open Opportunities',
        'Total Opportunities',
        'Total Won Opportunities',
        'Sales Team',
        'is_child',
        'is_parent',
        'Parent Account ID',
        'InsideView Account ID Account',
        '18-Char AccountId', 'Campaign Name',
        'Matched Parent Account ID',
        'Account',
        'Operations Buyer',
        'Postal Code',
        'Embedded Target',
        'Billing State/Province',
        'Last Modified Date',
        'Last Activity',
        'Created At',
        'Write Company Name'

        ]


        self.import_marketing_ds()
        self.import_target_account_ds()
        self.match_first()
        self.final_clean_up()


        self.write_to_csv()



    def final_clean_up(self):
        final_ds = []
        for marketing_row in self.first_pass_new_ds:
            #if marketing_row["Matched"] == True:
            #    print marketing_row["Title Group"], marketing_row['Tech Product']

            if marketing_row["Matched"] == True and (marketing_row["Title Group"] == 'Chief' or marketing_row["Title Group"] == 'Vice President') and marketing_row['Tech Product']=='True':
                marketing_row["Lead Rank"] = 'Category 1'
            elif marketing_row["Matched"] == True and marketing_row["Title Group"] =="Director" and marketing_row['Tech Product']=='True':
                marketing_row["Lead Rank"] = 'Category 2'
            elif marketing_row["Matched"] == True and marketing_row["Title Group"] =="Below Director" and marketing_row['Tech Product']=='True':
                marketing_row["Lead Rank"] = 'Category 3'
            elif marketing_row["Matched"] == True :
                marketing_row["Lead Rank"] = 'Category 4'
            else:
                marketing_row["Lead Rank"] = 'Outside targets'
            #if marketing_row["Matched"] == True:
            #    print marketing_row["Lead Rank"]

            final_ds.append(marketing_row)

        self.final_ds = final_ds

    def import_target_account_ds(self):
        with open(self.target_account_ds_filepath) as target_acct_file:
            target_acct_file_reader = csv.DictReader(target_acct_file)
            target_accounts_ds = []
            for row in target_acct_file_reader:
                target_accounts_ds.append(row)
            self.target_accounts_ds = target_accounts_ds

    def import_marketing_ds(self):
        with open(self.marketing_ds_filepath) as marketing_file:
            marketing_ds_reader = csv.DictReader(marketing_file)
            marketing_ds = []
            for row in marketing_ds_reader:
               marketing_ds.append(row)
            self.marketing_ds = marketing_ds



    def best_match(self, marketing_row, list_of_options):
        #print marketing_row['Clean Company Name1']
        best_row = None
        for row in list_of_options:
            if marketing_row['Clean Company Name1'] == row['Clean Account Name']:
                best_row = row
                break

        if best_row == None:
            highest_token_score = 0
            best_token_row = None
            for row in list_of_options:
                fuzz_val = fuzz.token_set_ratio(marketing_row['Clean Company Name1'], row['Clean Account Name'])
                if fuzz_val > highest_token_score:
                    highest_token_score = fuzz_val
                    best_token_row = row
            best_row = best_token_row

        marketing_row["Matched Clean Name"] = best_row['Clean Account Name']
        marketing_row["Matched Account ID"] = best_row['Account ID']

        return marketing_row

    def match_first(self):
        match_count = 0; record_count = 0
        self.first_pass_new_ds = []
        for marketing_row in self.marketing_ds:
            record_count +=1
            marketing_row["Matched"] = False

            if marketing_row['Matched'] == False:
                for account_row in self.target_accounts_ds:
                    if marketing_row["Clean Company Name1"] == account_row["Clean Company Name"]:
                        match_count +=1
                        marketing_row['Write Company Name'] = account_row['Company Name']
                        marketing_row["Matched"] = True
                        marketing_row["Matched Clean Name"] = account_row['Clean Company Name']
                        #self.first_pass_new_ds.append(marketing_row)
                        break

            if marketing_row['Matched'] == False:
                for account_row in self.target_accounts_ds:
                    if account_row["Clean Company Name"] in marketing_row["Clean Company Name1"] and ((len(account_row["Clean Company Name"].split())==1  and len(account_row["Clean Company Name"])>=5 ) or (len(account_row["Clean Company Name"].split())>1))and fuzz.token_set_ratio(account_row["Clean Company Name"], marketing_row["Clean Company Name1"])>90:
                        match_count +=1
                        marketing_row['Write Company Name'] = account_row['Company Name']
                        marketing_row["Matched"] = True
                        marketing_row["Matched Clean Name"] = account_row['Clean Company Name']
                        #self.first_pass_new_ds.append(marketing_row)
                        break

                    elif  marketing_row['Matched'] == False and marketing_row["Clean Company Name1"] in account_row["Clean Company Name"] and ((len(account_row["Clean Company Name"].split())==1  and len(account_row["Clean Company Name"])>=5 ) or (len(account_row["Clean Company Name"].split())>1)) and len(marketing_row["Clean Company Name1"])>=5 and fuzz.token_set_ratio(account_row["Clean Company Name"], marketing_row["Clean Company Name1"])>90:
                        match_count +=1
                        marketing_row['Write Company Name'] = account_row['Company Name']
                        marketing_row["Matched"] = True
                        marketing_row["Matched Clean Name"] = account_row['Clean Company Name']
                        #self.first_pass_new_ds.append(marketing_row)
                        break



            if marketing_row['Matched'] == False:
                for account_row in self.target_accounts_ds:
                     try:
                        if account_row["Clean Company Name"].split()[0] == marketing_row["Clean Company Name1"].split()[0] and fuzz.token_set_ratio(account_row["Clean Company Name"], marketing_row["Clean Company Name1"])>85:
                            match_count +=1
                            marketing_row['Write Company Name'] = account_row['Company Name']
                            marketing_row["Matched"] = True
                            marketing_row["Matched Clean Name"] = account_row['Clean Company Name']
                            #self.first_pass_new_ds.append(marketing_row)
                            break
                     except:
                        pass


            if marketing_row['Matched'] == True and (marketing_row['Clean Company Name1'] in ['a', 'unknown', 'test', 'private', 'store', 'retired'] or len(marketing_row['Clean Company Name1'])==1):
                marketing_row["Matched"] = False
                del marketing_row["Matched Clean Name"]
                match_count -=1

            if match_count %1000 == 0:
                print "Match Count: " + str(match_count)
                match_count +=1
            if record_count % 1000 == 0 :
                print "Row Count: " + str(record_count)

            self.first_pass_new_ds.append(marketing_row)

        print len(self.first_pass_new_ds)


    def write_to_csv(self):
        #try:
        self.additional_fields= []

        with open(self.out_path, 'w') as write_csv:
            writer = csv.DictWriter(write_csv, fieldnames=self.write_fields + self.additional_fields , lineterminator = '\n')
            writer.writeheader()
            for row in self.final_ds:
                #print row
                writer.writerow(row)




match_leads_to_accounts('C:/Users/wkuffel/Desktop/Marketing Data/Saas 1000/Product Tagged Leads.csv','C:/Users/wkuffel/Desktop/Marketing Data/All OEM/all oem account processed.csv', 'C:/Users/wkuffel/Desktop/Marketing Data/All OEM/leads matched to all oem accounts.csv')