__author__ = 'wkuffel'

import csv

class lead_types_by_target_accounts(object):

    def __init__(self, path, target_path, out_path):
        self.path = path
        self.target_path = target_path
        self.out_path = out_path
        self.writing_field_names_ordered = ['Account Name', 'Sales Titles', 'Marketing Titles', 'OEM Titles','BI Titles', 'Analyst Titles', 'Decision Makers', 'Chief', 'Director', 'VP', 'Below VP', 'Multiple Title Verticals']
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
                account_dict = {'Account Name': row['Account Name'], 'BI Titles': 0, 'Sales Titles':0, 'Marketing Titles':0, 'OEM Titles':0, 'Analyst Titles':0, 'Decision Makers':0, 'Chief':0, 'Director':0, 'VP':0, 'Below VP':0, 'Multiple Title Verticals':0}
                #Company_dict = {'Company Name': row['Company Name'], 'Company ID': row['Company ID'], 'BI Titles': 0, 'Sales Titles':0, 'Marketing Titles':0, 'OEM Titles':0, 'Other Titles':0}
                output_dict.append(account_dict)

        count = 0
        for lead in self.merged_file:
            #print lead
            count +=1
            if count % 10000 ==0:
                print count
            if lead["Target Account"] == 'True':


                for item in range(len(output_dict)):
                    #print output_dict[item]
                    #print lead['Account Name'].strip(), output_dict[item]['Account Name'].strip()
                    if lead['Account Name'].strip() == output_dict[item]['Account Name'].strip():
                        if lead['Sales Title']=='True' and (lead['Marketing Title']=='False' and lead['BI Title']=='False' and lead['OEM Title']=='False'):
                            output_dict[item]['Sales Titles'] +=1
                        if lead['Marketing Title']=='True' and (lead['Sales Title']=='False' and lead['BI Title']=='False' and lead['OEM Title']=='False'):
                            output_dict[item]['Marketing Titles'] +=1
                        if lead['BI Title']=='True' and (lead['Marketing Title']=='False' and lead['Sales Title']=='False' and lead['OEM Title']=='False'):
                            output_dict[item]['BI Titles'] +=1
                        if lead['OEM Title']=='True' and (lead['Marketing Title']=='False' and lead['BI Title']=='False' and lead['Sales Title']=='False'):
                            output_dict[item]['OEM Titles'] +=1
                        if (lead['OEM Title']=='True' and lead['BI Title']=='True') or (lead['Sales Title']=='True' and lead['BI Title']=='True') or (lead['Marketing Title']=='True' and lead['BI Title']=='True') or (lead['OEM Title']=='True' and lead['Sales Title']=='True') or (lead['OEM Title']=='True' and lead['Marketing Title']=='True') or (lead['Sales Title']=='True' and lead['Marketing Title']=='True'):
                            output_dict[item]['Multiple Title Verticals'] +=1

                        if lead['Decision Maker'] == 'True':
                            output_dict[item]['Decision Makers'] +=1
                        if lead['Analytics Title']=='True':
                            output_dict[item]['Analyst Titles'] +=1

                        if lead['Title Group'] == 'Chief':
                            output_dict[item]['Chief'] +=1
                        elif lead['Title Group'] == 'VP':
                            output_dict[item]['VP'] +=1
                        elif lead['Title Group'] == 'Director':
                            output_dict[item]['Director'] +=1
                        elif lead['Title Group'] == 'Below VP':
                            output_dict[item]['Below VP'] +=1
                        #print output_dict[item]

                        break

        self.output_dict = output_dict

all_leads = 'C:/Users/wkuffel/Desktop/Marketing Data/all Birst leads 20140122 will manipulated title.csv'
targets = 'C:/Users/wkuffel/Desktop/Marketing Data/20150119 marketo update/output files/target account list 20150119 manipulated.csv'
outpath = 'C:/Users/wkuffel/Desktop/Marketing Data/20150122 carl request/converged all leads.csv'
#target_coverage(targets, all_leads, outpath)
lead_types_by_target_accounts(outpath,targets,'C:/Users/wkuffel/Desktop/Marketing Data/20150122 carl request/combined full dataset counts by acct 2.csv')



#lead_types_by_target_accounts('C:/Users/wkuffel/Desktop/Marketing Data/20150120 allocated accounts/matched_results.csv', 'C:/Users/wkuffel/Desktop/Marketing Data/20150120 allocated accounts/Birst allocated accounts manipulated.csv','C:/Users/wkuffel/Desktop/Marketing Data/20150120 allocated accounts/allocated account mapping.csv')
#lead_types_by_target_accounts('C:/Users/wkuffel/Desktop/Marketing Data/20150121 marketo update/results/Birst allocated accounts manipulated Full.csv','C:/Users/wkuffel/Desktop/Marketing Data/20150120 allocated accounts/Birst allocated accounts manipulated.csv','C:/Users/wkuffel/Desktop/Marketing Data/20150121 marketo update/leads by account/allocated accounts manipulated counts by acct.csv')
#lead_types_by_target_accounts('C:/Users/wkuffel/Desktop/Marketing Data/20150121 marketo update/results/Birst top 30 EMEA prospects maniplated Full.csv','C:/Users/wkuffel/Desktop/Marketing Data/20150120 marketo update/output files/EMEA top 30 prospects 2015 manipulated.csv','C:/Users/wkuffel/Desktop/Marketing Data/20150121 marketo update/leads by account/top 30 EMEA prospects counts by acct.csv')
#lead_types_by_target_accounts('C:/Users/wkuffel/Desktop/Marketing Data/20150122 carl request/Birst accounts manipulated Full.csv','C:/Users/wkuffel/Desktop/Marketing Data/20150119 marketo update/output files/target account list 20150119 manipulated.csv','C:/Users/wkuffel/Desktop/Marketing Data/20150122 carl request/combined full dataset counts by acct.csv')