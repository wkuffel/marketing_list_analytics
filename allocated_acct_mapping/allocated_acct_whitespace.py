__author__ = 'wkuffel'

import csv

class lead_types_by_target_accounts(object):

    def __init__(self, path, target_path, out_path):
        self.path = path
        self.target_path = target_path
        self.out_path = out_path

        self.writing_field_names_ordered = ['Account Name','Owner', 'Industry', 'Total Names', 'Sales Titles', 'Marketing Titles', 'Embedded Titles','BI Titles', 'Analyst Titles', 'Operations Titles', 'Decision Makers', 'Chief', 'Director', 'Vice President', 'Below Director',
        'Marketing - Chief',
        'Marketing - VP',
        'Marketing - Director',
        'Sales - Chief',
        'Sales - VP',
        'Sales - Director',
        'BI - Chief',
        'BI - VP',
        'BI - Director',
        'Operations - Chief',
        'Operations - VP',
        'Operations - Director']

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
            if count %1000 ==0:
                print count
            if row['Account Name'].strip() not in target_name_dict:
                target_name_dict.append(row['Account Name'].strip())
                account_dict = {'Account Name': row['Account Name'], 'Owner': row['Owner'], 'Industry': row[' Primary Industry'], 'Total Names':0,   'BI Titles': 0, 'Sales Titles':0, 'Marketing Titles':0, 'Embedded Titles':0, 'Analyst Titles':0, 'Operations Titles':0, 'Decision Makers':0, 'Chief':0, 'Director':0, 'Vice President':0, 'Below Director':0,
                'Marketing - Chief': 0,
                'Marketing - VP': 0,
                'Marketing - Director': 0,
                'Sales - Chief': 0,
                'Sales - VP': 0,
                'Sales - Director': 0,
                'BI - Chief': 0,
                'BI - VP': 0,
                'BI - Director': 0,
                'Operations - Chief': 0,
                'Operations - VP': 0,
                'Operations - Director': 0}
                #Company_dict = {'Company Name': row['Company Name'], 'Company ID': row['Company ID'], 'BI Titles': 0, 'Sales Titles':0, 'Marketing Titles':0, 'OEM Titles':0, 'Other Titles':0}
                output_dict.append(account_dict)

        count = 0

        for lead in self.merged_file:
            #print lead
            count +=1
            if count % 10000 ==0:
                print count
            #if lead["Matched"] == True:
            if lead["Matched"] == 'TRUE' :
                #and (lead['Sub Region'] == 'Core EMEA (non-UK)'  or lead['Sub Region'] == 'UK' or lead['Sub Region'] == 'Other EMEA')   :
                #print lead
                for item in range(len(output_dict)):
                    #print output_dict[item]
                    #print lead['Account Name'].strip(), output_dict[item]['Account Name'].strip()
                    if lead['Account Name'].strip() == output_dict[item]['Account Name'].strip():
                        output_dict[item]['Total Names'] +=1
                        if lead['Marketing Title']== 'TRUE':
                            output_dict[item]['Marketing Titles'] +=1
                        elif lead['Sales Title']=='TRUE':
                            output_dict[item]['Sales Titles'] +=1
                        elif lead['BI Title']=='TRUE':
                            output_dict[item]['BI Titles'] +=1
                        elif lead['OEM Title']=='TRUE':
                            output_dict[item]['Embedded Titles'] +=1
                        elif lead['Operations Title']=='TRUE':
                            output_dict[item]['Operations Titles'] +=1

                        elif lead['Analytics Title']=='TRUE':
                            output_dict[item]['Analyst Titles'] +=1

                        if lead['Marketing Title']=='TRUE' and  lead['Title Group'] == 'Chief':
                            output_dict[item]['Marketing - Chief'] +=1
                        if lead['Marketing Title']=='TRUE' and  lead['Title Group'] == 'Vice President':
                            output_dict[item]['Marketing - VP'] +=1
                        if lead['Marketing Title']=='TRUE' and  lead['Title Group'] == 'Director':
                            output_dict[item]['Marketing - Director'] +=1
                        if lead['Sales Title']=='TRUE' and  lead['Title Group'] == 'Chief':
                            output_dict[item]['Sales - Chief'] +=1
                        if lead['Sales Title']=='TRUE' and  lead['Title Group'] == 'Vice President':
                            output_dict[item]['Sales - VP'] +=1
                        if lead['Sales Title']=='TRUE' and  lead['Title Group'] == 'Director':
                            output_dict[item]['Sales - Director'] +=1
                        if lead['BI Title']=='TRUE' and  lead['Title Group'] == 'Chief':
                            output_dict[item]['BI - Chief'] +=1
                        if lead['BI Title']=='TRUE' and  lead['Title Group'] == 'Vice President':
                            output_dict[item]['BI - VP'] +=1
                        if lead['BI Title']=='TRUE' and  lead['Title Group'] == 'Director':
                            output_dict[item]['BI - Director'] +=1
                        if lead['Operations Title']=='TRUE' and  lead['Title Group'] == 'Chief':
                            output_dict[item]['Operations - Chief'] +=1
                        if lead['Operations Title']=='TRUE' and  lead['Title Group'] == 'Vice President':
                            output_dict[item]['Operations - VP'] +=1
                        if lead['Operations Title']=='TRUE' and  lead['Title Group'] == 'Director':
                            output_dict[item]['Operations - Director'] +=1
                        """
                        if lead['Sales Title']==True and (lead['Marketing Title']=='False' and lead['BI Title']=='False' and lead['OEM Title']=='False'):
                            output_dict[item]['Sales Titles'] +=1
                        if lead['Marketing Title']==True and (lead['Sales Title']=='False' and lead['BI Title']=='False' and lead['OEM Title']=='False'):
                            output_dict[item]['Marketing Titles'] +=1
                        if lead['BI Title']==True and (lead['Marketing Title']=='False' and lead['Sales Title']=='False' and lead['OEM Title']=='False'):
                            output_dict[item]['BI Titles'] +=1
                        if lead['OEM Title']==True and (lead['Marketing Title']=='False' and lead['BI Title']=='False' and lead['Sales Title']=='False'):
                            output_dict[item]['OEM Titles'] +=1
                        if (lead['OEM Title']==True and lead['BI Title']==True) or (lead['Sales Title']==True and lead['BI Title']==True) or (lead['Marketing Title']==True and lead['BI Title']==True) or (lead['OEM Title']==True and lead['Sales Title']==True) or (lead['OEM Title']==True and lead['Marketing Title']==True) or (lead['Sales Title']==True and lead['Marketing Title']==True):
                            output_dict[item]['Multiple Title Verticals'] +=1

                        if lead['Decision Maker'] == True:
                            output_dict[item]['Decision Makers'] +=1
                        if lead['Analytics Title']==True:
                            output_dict[item]['Analyst Titles'] +=1
                        """

                        if lead['Title Group'] == 'Chief':
                            output_dict[item]['Chief'] +=1
                        elif lead['Title Group'] == 'Vice President':
                            output_dict[item]['Vice President'] +=1
                        elif lead['Title Group'] == 'Director':
                            output_dict[item]['Director'] +=1
                        elif lead['Title Group'] == 'Below Director':
                            output_dict[item]['Below Director'] +=1
                        #print output_dict[item]

                        break

        self.output_dict = output_dict

#all_leads = 'C:/Users/wkuffel/Desktop/Marketing Data/20150213 marketing list analysis/marketing list raw matched.csv'
#targets = 'C:/Users/wkuffel/Desktop/Marketing Data/create account links/account datasets/enterprise processed.csv'
#outpath = 'C:/Users/wkuffel/Desktop/Marketing Data/20150213 marketing list analysis/marketing list by accounts.csv'

all_leads = 'C:/Users/wkuffel/Desktop/Marketing Data/20150331 List Analytics/Marketing List Parts/with sub region info/Birst Marketing List matched.csv'
targets = 'C:/Users/wkuffel/Desktop/Marketing Data/20150331 List Analytics/Birst allocated accounts processed.csv'
outpath = 'C:/Users/wkuffel/Desktop/Marketing Data/20150331 List Analytics/Marketing List Parts/with sub region info/Birst Marketing List Whitespace All Allocated Accounts.csv'


lead_types_by_target_accounts(all_leads,targets,outpath)



#lead_types_by_target_accounts('C:/Users/wkuffel/Desktop/Marketing Data/20150120 allocated accounts/matched_results.csv', 'C:/Users/wkuffel/Desktop/Marketing Data/20150120 allocated accounts/Birst allocated accounts manipulated.csv','C:/Users/wkuffel/Desktop/Marketing Data/20150120 allocated accounts/allocated account mapping.csv')
#lead_types_by_target_accounts('C:/Users/wkuffel/Desktop/Marketing Data/20150121 marketo update/results/Birst allocated accounts manipulated Full.csv','C:/Users/wkuffel/Desktop/Marketing Data/20150120 allocated accounts/Birst allocated accounts manipulated.csv','C:/Users/wkuffel/Desktop/Marketing Data/20150121 marketo update/leads by account/allocated accounts manipulated counts by acct.csv')
#lead_types_by_target_accounts('C:/Users/wkuffel/Desktop/Marketing Data/20150121 marketo update/results/Birst top 30 EMEA prospects maniplated Full.csv','C:/Users/wkuffel/Desktop/Marketing Data/20150120 marketo update/output files/EMEA top 30 prospects 2015 manipulated.csv','C:/Users/wkuffel/Desktop/Marketing Data/20150121 marketo update/leads by account/top 30 EMEA prospects counts by acct.csv')
