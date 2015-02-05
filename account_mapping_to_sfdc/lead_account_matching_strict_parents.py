__author__ = 'wkuffel'

import csv
from fuzzywuzzy import fuzz
import pickle

class match_leads_to_accounts(object):

    def __init__(self, lead_file, account_file, out_file):
        self.marketing_ds_filepath = lead_file
        self.target_account_ds_filepath = account_file
        self.out_path = out_file
        self.parent_dict = pickle.load( open( "C:/Users/wkuffel/Desktop/Marketing Data/create account links/parent_account_dict.p", "rb" ) )
        self.write_fields = ['Id',
        'First Name',
        'Last Name',
        'Job Title',
        'Phone Number',
        'Email Address',
        'Country',
        'State',
        'Region',
        'Annual Company Revenue Range (A)',
        'Company Industries',
        'Lead Score',
        'Lead Source',
        'Lead Status',

        'Sales Title',
        'Marketing Title',
        'OEM Title',
        'BI Title',
        'Analytics Title',
        'Decision Maker',
        'Job Level',
        'Matched',
        'Clean Company Name1',
        'Clean Company Name',
        'Updated At',
        'Company Employee Range',
        'Annual Company Revenue Range',
        'SFDC Type',

        'Account ID',
        'Parent Account',
        'Account Name',
        'Account Owner',
        'HQ Country',
        'HQ State'
         'HQ Zip',
        'Account Status',
        'Industry',
        'Total Won Opportunity Value',
        'Total Open Opportunities',
        'Total Opportunities',
         'Sales Team'
        'is_child',
        'is_parent',
        'Parent Account ID'

        ]


        self.import_marketing_ds()
        self.import_target_account_ds()
        self.match_first()
        self.match_parent_child()
        self.final_clean_up()


        self.write_to_csv()

    def final_clean_up(self):
        final_ds = []
        for marketing_row in self.second_pass_new_ds:
            if marketing_row["Matched"] == True:
                for account_row in self.target_accounts_ds:
                    if account_row["Account ID"] == marketing_row["Matched Account ID"]:
                        #remove the added values
                        del marketing_row["Matched Clean Name"]
                        del marketing_row["Matched Account ID"]
                        del marketing_row["Matched is_child"]
                        del marketing_row["Matched is_parent"]
                        del marketing_row["Matched Parent Account ID"]
                        #add attach the new one
                        marketing_row.update(account_row)
                        final_ds.append(marketing_row)
                        break

            else:
                final_ds.append(marketing_row)

        for row in final_ds:
            if row["Matchd"] == True:
                print row.keys()
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

    def match_parent_child(self):
        second_pass_new_ds = []
        for marketing_row in self.first_pass_new_ds:
            if marketing_row["Matched is_parent"] == "True":
                comp_parent_dict = self.parent_dict[marketing_row["Matched Account ID"]]
                new_marketing_row = self.best_match(marketing_row,comp_parent_dict.values())


                second_pass_new_ds.append(new_marketing_row)
            elif marketing_row["Matched is_child"] == True:
                comp_parent_dict = self.parent_dict[marketing_row["Matched Parent Account ID"]]
                new_marketing_row = self.best_match(marketing_row,comp_parent_dict.values())
                second_pass_new_ds.append(new_marketing_row)
            else:
                second_pass_new_ds.append(marketing_row)

        self.second_pass_new_ds = second_pass_new_ds

    def best_match(self, marketing_row, list_of_options):
        print marketing_row['Clean Company Name1']
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
        for marketing_row in self.marketing_ds[:500]:
            record_count +=1
            count = 0
            marketing_row["Matched"] = False
            marketing_row["Matched is_child"] = None
            marketing_row["Matched is_parent"] = None

            for account_row in self.target_accounts_ds:
                if marketing_row["Clean Company Name1"] == account_row["Clean Company Name"]:
                    count +=1
                    marketing_row["Matched"] = True
                    marketing_row["Matched Clean Name"] = account_row['Clean Company Name']
                    marketing_row["Matched Account ID"] = account_row['Account ID']
                    marketing_row["Matched is_child"] = account_row['is_child']
                    marketing_row["Matched is_parent"] = account_row['is_parent']
                    marketing_row["Matched Parent Account ID"] = account_row["Parent Account ID"]
                    self.first_pass_new_ds.append(marketing_row)
                    break

            if marketing_row['Matched'] == False:
                for account_row in self.target_accounts_ds:
                    if account_row["Clean Company Name"] in marketing_row["Clean Company Name1"] and len(account_row["Clean Company Name"])>=4 and fuzz.token_set_ratio(account_row["Clean Company Name"], marketing_row["Clean Company Name1"])>90:
                        count +=1
                        marketing_row["Matched"] = True
                        marketing_row["Matched Clean Name"] = account_row['Clean Company Name']
                        marketing_row["Matched Account ID"] = account_row['Account ID']
                        marketing_row["Matched is_child"] = account_row['is_child']
                        marketing_row["Matched is_parent"] = account_row['is_parent']
                        marketing_row["Matched Parent Account ID"] = account_row["Parent Account ID"]
                        self.first_pass_new_ds.append(marketing_row)
                        break

                    elif marketing_row["Clean Company Name1"] in account_row["Clean Company Name"] and len(marketing_row["Clean Company Name1"])>=4 and fuzz.token_set_ratio(account_row["Clean Company Name"], marketing_row["Clean Company Name1"])>90:
                        count +=1
                        marketing_row["Matched"] = True
                        marketing_row["Matched Clean Name"] = account_row['Clean Company Name']
                        marketing_row["Matched Account ID"] = account_row['Account ID']
                        marketing_row["Matched is_child"] = account_row['is_child']
                        marketing_row["Matched is_parent"] = account_row['is_parent']
                        marketing_row["Matched Parent Account ID"] = account_row["Parent Account ID"]
                        self.first_pass_new_ds.append(marketing_row)
                        break



            if marketing_row['Matched'] == False:
                for account_row in self.target_accounts_ds:
                     try:
                        if account_row["Clean Company Name"].split()[0] == marketing_row["Clean Company Name1"].split()[0] and fuzz.token_set_ratio(account_row["Clean Company Name"], marketing_row["Clean Company Name1"])>85:
                            count +=1
                            marketing_row["Matched"] = True
                            marketing_row["Matched Clean Name"] = account_row['Clean Company Name']
                            marketing_row["Matched Account ID"] = account_row['Account ID']
                            marketing_row["Matched is_child"] = account_row['is_child']
                            marketing_row["Matched is_parent"] = account_row['is_parent']
                            marketing_row["Matched Parent Account ID"] = account_row["Parent Account ID"]
                            self.first_pass_new_ds.append(marketing_row)
                            break
                     except:
                        pass
            if marketing_row['Matched'] == False:
                self.first_pass_new_ds.append(marketing_row)

        print len(self.first_pass_new_ds)
    """
    def match_datasets(self):
        match_count = 0, record_count = 0
        concatenated_ds = []
        for row_marketing in self.marketing_ds[:10000]:
            record_count +=1
            if record_count %5000 ==0:
                print "row count: " + str(record_count)

            row_marketing["Target Account"] = False

            # 1) equality match
            for row_target in self.target_accounts_ds:
                if row_marketing["Clean Company Name1"] == row_target["Clean Company Name"]:
                    row_marketing.update(row_target)
                    row_marketing["Target Account"] = True
                    #concatenated_ds.append(row_marketing)
                    match_count +=1
                    if match_count %5000 ==0:
                        print "match count: " + str(match_count)
                    break

            # 2) contains match, robust

            if row_marketing["Target Account"] == False:
                for row_target in self.target_accounts_ds:
                    if row_target["Clean Company Name"] in row_marketing["Clean Company Name1"] and len(row_target["Clean Company Name"])>=4:
                        if fuzz.token_set_ratio(row_target["Clean Company Name"], row_marketing["Clean Company Name1"])>90:
                            if match_count %5000 ==0:
                                print "match count: " + str(match_count)

                            if not row_target['is_parent'] and not row_target['is_child']:
                                row_marketing.update(row_target)
                                row_marketing["Target Account"] = True
                                #concatenated_ds.append(row_marketing)
                                match_count +=1
                            elif row_target['is_parent']:

                            elif row_target['is_child']:


                            break

                    elif row_marketing["Clean Company Name1"] in row_target["Clean Company Name"] and len(row_marketing["Clean Company Name1"])>=4:
                        if fuzz.token_set_ratio(row_target["Clean Company Name"], row_marketing["Clean Company Name1"])>90:
                            if match_count %5000 ==0:
                                print "match count: " + str(match_count)

                            if not row_target['is_parent'] and not row_target['is_child']:
                                row_marketing.update(row_target)
                                row_marketing["Target Account"] = True
                                #concatenated_ds.append(row_marketing)
                                match_count +=1
                            elif row_target['is_parent']:

                            elif row_target['is_child']:


                            break

            if row_marketing["Target Account"] == False:
                for row_target in self.target_accounts_ds:
                    try:
                        if row_target["Clean Company Name"].split()[0] == row_marketing["Clean Company Name1"].split()[0]:
                            if fuzz.token_set_ratio(row_target["Clean Company Name"], row_marketing["Clean Company Name1"])>85:
                                if match_count %5000 ==0:
                                print "match count: " + str(match_count)

                            if not row_target['is_parent'] and not row_target['is_child']:
                                row_marketing.update(row_target)
                                row_marketing["Target Account"] = True
                                #concatenated_ds.append(row_marketing)
                                match_count +=1
                            elif row_target['is_parent']:

                            elif row_target['is_child']:


                            break
                    except:
                        pass

            if row_marketing['Target Account'] == True and row_marketing["Clean Company Name1"] in ['test', 'self']:
                row_marketing['Target Account'] = False


            concatenated_ds.append(row_marketing)



        self.concatendated_ds = concatenated_ds
    """

    def write_to_csv(self):
        #try:
        with open(self.out_path, 'w') as write_csv:
            writer = csv.DictWriter(write_csv, fieldnames=self.write_fields , lineterminator = '\n')

            #['Target Account', 'ID', 'Account Name', 'Primary Industry', 'Industry Breakout (from Count Tab)', 'Owner', 'Description', 'Revenue(USD)', 'Employees', 'Ownership', 'Ticker Symbol', 'SIC (US)', 'Primary NAICS', 'Address', 'City', 'State', 'Postal Code', 'Country', 'Phone', 'Fax', 'Website', 'Parent ID', 'Parent Name', 'Ultimate Parent ID', 'Ultimate Parent Name', 'Data Source(s)', 'Lead Source', 'EFX ID', ' Description', ' Primary Industry', 'Clean Company Name'], lineterminator = '\n')
            #'Target Account','Account ID','Account Name','Equifax ID','Account Owner', 'Region', 'Sales Team', 'Account Type','Industry','Company Employee Range','Annual Company Revenue Range','Total Opportunities','Total Won Opportunities','Total Won Opportunity Value','Total Open Opportunities','HQ Country','HQ State','HQ Zip','Account Status','Clean Company Name'], lineterminator = '\n')
            #['Clean Company Name', 'Industry', 'Revenue ($M)', 'Owner', 'Notes']
            #['Account ID','Account Name','Equifax ID','Account Owner', 'Region', 'Sales Team', 'Account Type','Industry','Company Employee Range','Annual Company Revenue Range','Total Opportunities','Total Won Opportunities','Total Won Opportunity Value','Total Open Opportunities','HQ Country','HQ State','HQ Zip','Account Status','Clean Company Name'], lineterminator = '\n')
            #['Target Account','Account ID','Account Name','Equifax ID','Account Owner', 'Region', 'Sales Team', 'Account Type','Industry','Company Employee Range','Annual Company Revenue Range','Total Opportunities','Total Won Opportunities','Total Won Opportunity Value','Total Open Opportunities','HQ Country','HQ State','HQ Zip','Account Status','Clean Company Name']
            writer.writeheader()
            for row in self.final_ds:
                writer.writerow(row)













lead_file = 'C:/Users/wkuffel/Desktop/Marketing Data/create account links/leads/marketing list processed.csv'
account_file = 'C:/Users/wkuffel/Desktop/Marketing Data/create account links/account datasets/enterprise processed.csv'
out_file = 'C:/Users/wkuffel/Desktop/Marketing Data/create account links/matched results.csv'
match_leads_to_accounts(lead_file, account_file, out_file)