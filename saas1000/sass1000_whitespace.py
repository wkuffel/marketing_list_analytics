__author__ = 'wkuffel'

__author__ = 'wkuffel'

import csv

class lead_types_by_target_accounts(object):

    def __init__(self, path, target_path, out_path):
        self.path = path
        self.target_path = target_path
        self.out_path = out_path
        self.writing_field_names_ordered = ['Account Name', 'Category 1', 'Category 2', 'Category 3', 'Category 4', "Marketing (included in other counts)"]

        print "start"
        self.import_target_list()
        print "imported target"
        self.import_converged_csv()
        print "imported converged"
        self.generate_target_dicts()

        self.write_to_csv()

    def import_target_list(self):
        with open(self.target_path) as target_file:
            target_file_reader = csv.DictReader(target_file)
            target_file = []
            for row in target_file_reader:
                target_file.append(row)
            self.target_file = target_file

    def import_converged_csv(self):
         with open(self.path) as merged_file:
            merged_file_reader = csv.DictReader(merged_file)
            merged_file = []
            for row in merged_file_reader:
                row["Matched"] = bool(row["Matched"])
                merged_file.append(row)
                #print row
            self.merged_file = merged_file


    def write_to_csv(self):
        with open(self.out_path, 'w') as write_csv:
            writer = csv.DictWriter(write_csv, fieldnames= self.writing_field_names_ordered, lineterminator = '\n')
            writer.writeheader()
            for row in self.output_dict:
                #print row
                writer.writerow(row)



    def generate_target_dicts(self):
        output_dict = []
        target_name_dict = []
        count=0
        for row in self.target_file:
            count+=1
            if count %100 ==0:
                print count
            if row['Company Name'].strip() not in target_name_dict:
                target_name_dict.append(row['Company Name'].strip())
                account_dict = {'Account Name': row['Company Name'],
                "Category 1":0,
                "Category 2":0,
                "Category 3":0,
                "Category 4":0,
                "Marketing (included in other counts)":0
                }
                output_dict.append(account_dict)
        count = 0
        for lead in self.merged_file:
            if lead["Matched"] == 'True' or lead["Matched"] == True:
                for item in range(len(output_dict)):
                    #print output_dict[item]
                    #print lead['Account Name'].strip(), output_dict[item]['Account Name'].strip()

                    if lead['Write Company Name'] == output_dict[item]['Account Name']:
                        if lead['Lead Rank'] == "Category 1":
                            output_dict[item]["Category 1"] +=1
                        elif lead['Lead Rank'] == "Category 2":
                            output_dict[item]["Category 2"] +=1
                        elif lead['Lead Rank'] == "Category 3":
                            output_dict[item]["Category 3"] +=1
                        elif lead['Lead Rank'] == "Category 4":
                            output_dict[item]["Category 4"] +=1
                        if bool(lead['Marketing Title']) == True and lead['Title Group'] in ['Chief', 'Vice President', 'Director']:
                            output_dict[item]["Marketing (included in other counts)"] +=1
                        break

        self.output_dict = output_dict

#all_leads = 'C:/Users/wkuffel/Desktop/Marketing Data/20150213 marketing list analysis/marketing list raw matched.csv'
#targets = 'C:/Users/wkuffel/Desktop/Marketing Data/create account links/account datasets/enterprise processed.csv'
#outpath = 'C:/Users/wkuffel/Desktop/Marketing Data/20150213 marketing list analysis/marketing list by accounts.csv'

all_leads = 'C:/Users/wkuffel/Desktop/Marketing Data/All OEM/leads matched to all oem accounts.csv'
targets = 'C:/Users/wkuffel/Desktop/Marketing Data/All OEM/all oem account processed.csv'
outpath = 'C:/Users/wkuffel/Desktop/Marketing Data/All OEM/all oem whitespace.csv'


lead_types_by_target_accounts(all_leads,targets,outpath)



#lead_types_by_target_accounts('C:/Users/wkuffel/Desktop/Marketing Data/20150120 allocated accounts/matched_results.csv', 'C:/Users/wkuffel/Desktop/Marketing Data/20150120 allocated accounts/Birst allocated accounts manipulated.csv','C:/Users/wkuffel/Desktop/Marketing Data/20150120 allocated accounts/allocated account mapping.csv')
#lead_types_by_target_accounts('C:/Users/wkuffel/Desktop/Marketing Data/20150121 marketo update/results/Birst allocated accounts manipulated Full.csv','C:/Users/wkuffel/Desktop/Marketing Data/20150120 allocated accounts/Birst allocated accounts manipulated.csv','C:/Users/wkuffel/Desktop/Marketing Data/20150121 marketo update/leads by account/allocated accounts manipulated counts by acct.csv')
#lead_types_by_target_accounts('C:/Users/wkuffel/Desktop/Marketing Data/20150121 marketo update/results/Birst top 30 EMEA prospects maniplated Full.csv','C:/Users/wkuffel/Desktop/Marketing Data/20150120 marketo update/output files/EMEA top 30 prospects 2015 manipulated.csv','C:/Users/wkuffel/Desktop/Marketing Data/20150121 marketo update/leads by account/top 30 EMEA prospects counts by acct.csv')
#lead_types_by_target_accounts('C:/Users/wkuffel/Desktop/Marketing Data/20150122 carl request/Birst accounts manipulated Full.csv','C:/Users/wkuffel/Desktop/Marketing Data/20150119 marketo update/output files/target account list 20150119 manipulated.csv','C:/Users/wkuffel/Desktop/Marketing Data/20150122 carl request/combined full dataset counts by acct.csv')