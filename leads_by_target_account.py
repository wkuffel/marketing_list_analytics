__author__ = 'wkuffel'

import csv

class lead_types_by_target_accounts(object):

    def __init__(self, path, target_path, out_path):
        self.path = path
        self.target_path = target_path
        self.out_path = out_path
        self.writing_field_names_ordered = ['Account Name', 'Account ID', 'Sales Buyers', 'Marketing Buyers', 'OEM Buyers','BI Buyers', 'Other Buyers']
        self.import_target_list()

        self.import_converged_csv()
        self.generate_target_dicts()

        self.write_to_csv()

    def import_target_list(self):
        with open(self.target_path) as target_file:
            target_file_reader = csv.DictReader(target_file)
            target_file = []
            for row in target_file_reader:
                target_file.append(row)
                #print row
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
                writer.writerow(row)



    def generate_target_dicts(self):
        output_dict = []
        target_name_dict = []
        for row in self.target_file:
            target_name_dict.append(row['Account Name'].strip())
            account_dict = {'Account Name': row['Account Name'], 'Account ID': row['Account ID'], 'BI Buyers': 0, 'Sales Buyers':0, 'Marketing Buyers':0, 'OEM Buyers':0, 'Other Buyers':0}
            output_dict.append(account_dict)

        count = 0
        for lead in self.merged_file:
            count +=1
            if count%10000 ==0:
                print count
            if lead['match'] == 'contains' or lead['match'] == 'equality':
                for item in range(len(output_dict)):
                    if lead['Account Name'].strip() == output_dict[item]['Account Name'].strip():
                        if lead['Sales Buyer']=='yes':
                            output_dict[item]['Sales Buyers'] +=1
                        if lead['Marketing Buyer']=='yes':
                            output_dict[item]['Marketing Buyers'] +=1
                        if lead['BI Buyer']=='yes':
                            output_dict[item]['BI Buyers'] +=1
                        if lead['OEM Buyer']=='yes':
                            output_dict[item]['OEM Buyers'] +=1
                        if lead['Sales Buyer']== 'no' and lead['Marketing Buyer']== 'no' and lead['BI Buyer']== 'no' and lead['OEM Buyer']== 'no':
                            output_dict[item]['Other Buyers'] +=1
                        #print output_dict[item]
        self.output_dict = output_dict

lead_types_by_target_accounts('C:/Users/wkuffel/Desktop/Marketing Data/combined full dataset equality and limited contains.csv', 'C:/Users/wkuffel/Desktop/Marketing Data/target account list 20140115 will manipulated.csv','C:/Users/wkuffel/Desktop/Marketing Data/target acct by buyer type.csv')
