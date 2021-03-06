__author__ = 'wkuffel'

import csv
from fuzzywuzzy import fuzz
import pickle

class match_leads_to_accounts(object):

    def __init__(self, lead_file, account_file, out_file, marketo_upload=False, picklepath = "C:/Users/wkuffel/Desktop/update unranked/Target accounts/parent_account_dict.p"):
        self.marketing_ds_filepath = lead_file
        self.target_account_ds_filepath = account_file
        self.out_path = out_file
        self.marketo_upload = marketo_upload
        self.parent_dict = pickle.load( open( picklepath, "rb" ) )
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

        'Sales Title',
        'Marketing Title',
        'OEM Title',
        'BI Title',
        'Analytics Title',
        'Operations Title',
        'Decision Maker',
        'Title Group',
        'Clean Company Name1',

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
        'Created At'

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

            if marketing_row["Matched"] == True and marketing_row["Title Group"] in ["Director", 'Chief', 'Vice President']:
                marketing_row["Lead Rank"] = 'A'
            elif marketing_row["Matched"] == True and marketing_row["Title Group"] in ["Below Director"]:
                marketing_row["Lead Rank"] = 'B'
            elif marketing_row["Matched"] == False and marketing_row["Title Group"] in ["Director", 'Chief', 'Vice President']:
                marketing_row["Lead Rank"] = 'C'
            elif marketing_row["Matched"] == False and marketing_row["Title Group"] in ["Below Director"]:
                marketing_row["Lead Rank"] = 'D'



            if marketing_row["Matched"] == True:
                for account_row in self.target_accounts_ds:
                    if account_row["Account ID"] == marketing_row["Matched Account ID"]:
                        #remove the added values
                        del marketing_row["Matched Clean Name"]
                        del marketing_row["Matched Account ID"]
                        del marketing_row["Matched is_child"]
                        del marketing_row["Matched is_parent"]
                        marketing_row['Account'] = account_row["Account ID"]
                        #add attach the new one
                        marketing_row.update(account_row)
                        final_ds.append(marketing_row)
                        break

            else:
                try:
                    del marketing_row["Matched is_child"]
                    del marketing_row["Matched is_parent"]
                except:
                    pass
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

    def match_parent_child(self):
        second_pass_new_ds = []
        for marketing_row in self.first_pass_new_ds:

            if marketing_row["Matched is_parent"] == "True" and (marketing_row['InsideView Account ID'] != marketing_row['InsideView Account ID Account']):
                comp_parent_dict = self.parent_dict[marketing_row["Matched Account ID"]]
                new_marketing_row = self.best_match(marketing_row,comp_parent_dict.values())


                second_pass_new_ds.append(new_marketing_row)
            elif marketing_row["Matched is_child"] == True and (marketing_row['InsideView Account ID'] != marketing_row['InsideView Account ID Account']):
                comp_parent_dict = self.parent_dict[marketing_row["Matched Parent Account ID"]]
                new_marketing_row = self.best_match(marketing_row,comp_parent_dict.values())
                second_pass_new_ds.append(new_marketing_row)
            else:
                second_pass_new_ds.append(marketing_row)

        self.second_pass_new_ds = second_pass_new_ds

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
            marketing_row["Matched is_child"] = None
            marketing_row["Matched is_parent"] = None

            for account_row in self.target_accounts_ds:
                if marketing_row["InsideView Account ID"] == account_row["InsideView Account ID"] and account_row["InsideView Account ID"] != '':
                    match_count +=1
                    marketing_row["Matched"] = True
                    marketing_row["Matched Clean Name"] = account_row['Clean Company Name']
                    marketing_row["Matched Account ID"] = account_row['Account ID']
                    marketing_row["Matched is_child"] = account_row['is_child']
                    marketing_row["Matched is_parent"] = account_row['is_parent']
                    marketing_row["InsideView Account ID Account"] = account_row["InsideView Account ID"]
                    marketing_row["Matched Parent Account ID"] = account_row["Parent Account ID"]
                    #self.first_pass_new_ds.append(marketing_row)
                    break
                elif marketing_row["Account"] == account_row["Account ID"] and account_row["Account ID"] != '':
                    match_count +=1
                    marketing_row["Matched"] = True
                    marketing_row["Matched Clean Name"] = account_row['Clean Company Name']
                    marketing_row["Matched Account ID"] = account_row['Account ID']
                    marketing_row["Matched is_child"] = account_row['is_child']
                    marketing_row["Matched is_parent"] = account_row['is_parent']
                    marketing_row["InsideView Account ID Account"] = account_row["InsideView Account ID"]
                    marketing_row["Matched Parent Account ID"] = account_row["Parent Account ID"]
                    #self.first_pass_new_ds.append(marketing_row)
                    break

            if marketing_row['Matched'] == False:
                for account_row in self.target_accounts_ds:
                    if marketing_row["Clean Company Name1"] == account_row["Clean Company Name"]:
                        match_count +=1
                        marketing_row["Matched"] = True
                        marketing_row["Matched Clean Name"] = account_row['Clean Company Name']
                        marketing_row["Matched Account ID"] = account_row['Account ID']
                        marketing_row["Matched is_child"] = account_row['is_child']
                        marketing_row["Matched is_parent"] = account_row['is_parent']
                        marketing_row["InsideView Account ID Account"] = account_row["InsideView Account ID"]
                        marketing_row["Matched Parent Account ID"] = account_row["Parent Account ID"]
                        #self.first_pass_new_ds.append(marketing_row)
                        break

            if marketing_row['Matched'] == False:
                for account_row in self.target_accounts_ds:
                    if account_row["Clean Company Name"] in marketing_row["Clean Company Name1"] and ((len(account_row["Clean Company Name"].split())==1  and len(account_row["Clean Company Name"])>=5 ) or (len(account_row["Clean Company Name"].split())>1))and fuzz.token_set_ratio(account_row["Clean Company Name"], marketing_row["Clean Company Name1"])>90:
                        match_count +=1
                        marketing_row["Matched"] = True
                        marketing_row["Matched Clean Name"] = account_row['Clean Company Name']
                        marketing_row["Matched Account ID"] = account_row['Account ID']
                        marketing_row["Matched is_child"] = account_row['is_child']
                        marketing_row["Matched is_parent"] = account_row['is_parent']
                        marketing_row["InsideView Account ID Account"] = account_row["InsideView Account ID"]
                        marketing_row["Matched Parent Account ID"] = account_row["Parent Account ID"]
                        #self.first_pass_new_ds.append(marketing_row)
                        break

                    elif marketing_row["Clean Company Name1"] in account_row["Clean Company Name"] and ((len(account_row["Clean Company Name"].split())==1  and len(account_row["Clean Company Name"])>=5 ) or (len(account_row["Clean Company Name"].split())>1)) and len(marketing_row["Clean Company Name1"])>=5 and fuzz.token_set_ratio(account_row["Clean Company Name"], marketing_row["Clean Company Name1"])>90:
                        match_count +=1
                        marketing_row["Matched"] = True
                        marketing_row["Matched Clean Name"] = account_row['Clean Company Name']
                        marketing_row["Matched Account ID"] = account_row['Account ID']
                        marketing_row["Matched is_child"] = account_row['is_child']
                        marketing_row["Matched is_parent"] = account_row['is_parent']
                        marketing_row["InsideView Account ID Account"] = account_row["InsideView Account ID"]
                        marketing_row["Matched Parent Account ID"] = account_row["Parent Account ID"]
                        #self.first_pass_new_ds.append(marketing_row)
                        break



            if marketing_row['Matched'] == False:
                for account_row in self.target_accounts_ds:
                     try:
                        if account_row["Clean Company Name"].split()[0] == marketing_row["Clean Company Name1"].split()[0] and fuzz.token_set_ratio(account_row["Clean Company Name"], marketing_row["Clean Company Name1"])>85:
                            match_count +=1
                            marketing_row["Matched"] = True
                            marketing_row["Matched Clean Name"] = account_row['Clean Company Name']
                            marketing_row["Matched Account ID"] = account_row['Account ID']
                            marketing_row["Matched is_child"] = account_row['is_child']
                            marketing_row["Matched is_parent"] = account_row['is_parent']
                            marketing_row["InsideView Account ID Account"] = account_row["InsideView Account ID"]
                            marketing_row["Matched Parent Account ID"] = account_row["Parent Account ID"]
                            #self.first_pass_new_ds.append(marketing_row)
                            break
                     except:
                        pass


            if marketing_row['Matched'] == True and (marketing_row['Clean Company Name1'] in ['a', 'unknown', 'test', 'private', 'store', 'retired'] or len(marketing_row['Clean Company Name1'])==1):
                marketing_row["Matched"] = False
                del marketing_row["Matched Clean Name"]
                del marketing_row["Matched Account ID"]
                marketing_row["Matched is_child"] =None
                marketing_row["Matched is_parent"] = None
                del marketing_row["Matched Parent Account ID"]
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
        if self.marketo_upload == True:

            self.write_fields = ['Id', "Matched", "Email Address", "Sales Title", "Marketing Title", "OEM Title", "BI Title", "Analytics Title","Operations Title", "Title Group", "Decision Maker", "Lead Rank", 'Tech Product', 'InsideView Account ID (L)', 'Marketo SFDC ID', 'Created At']
            self.additional_fields = ['Account']
            final_ds = []
            for row in self.final_ds:
                row['InsideView Account ID (L)'] = row['InsideView Account ID']
                del row['InsideView Account ID']

                if row['Matched']:
                    final_ds.append({field: row[field] for field in self.write_fields + self.additional_fields})
                else:
                    final_ds.append({field: row[field] for field in self.write_fields})
            self.final_ds = final_ds
            #self.final_ds = [{field: row[field] for field in self.write_fields} for row in self.final_ds]

        with open(self.out_path, 'w') as write_csv:
            writer = csv.DictWriter(write_csv, fieldnames=self.write_fields + self.additional_fields , lineterminator = '\n')
            writer.writeheader()
            for row in self.final_ds:
                #print row
                writer.writerow(row)



#match_leads_to_accounts('C:/Users/wkuffel/Desktop/Marketing Data/20150311 Marketing Database/20150311 Marketing List Processed.csv','C:/Users/wkuffel/Desktop/Marketing Data/create account links/all target accts.csv','C:/Users/wkuffel/Desktop/Marketing Data/20150311 Marketing Database/20150311 Marketing List Matched.csv',picklepath ='C:/Users/wkuffel/Desktop/Marketing Data/create account links/all_accts_pickle.p')


#lead_file = 'C:/Users/wkuffel/Desktop/Marketing Data/create account links/leads/marketing list processed.csv'
#account_file = 'C:/Users/wkuffel/Desktop/Marketing Data/create account links/account datasets/enterprise processed.csv'
#out_file = 'C:/Users/wkuffel/Desktop/Marketing Data/create account links/matched results.csv'
#match_leads_to_accounts(lead_file, account_file, out_file)

