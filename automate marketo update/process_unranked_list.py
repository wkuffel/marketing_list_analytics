
import csv
from master_functions.clean_account_name import clean_account_name
from master_functions.label_analytics_title import label_analytics_buyer
from master_functions.label_bi_buyer import label_bi_buyer
from master_functions.label_sales_buyer import label_sales_buyer
from master_functions.label_embedded_buyer import label_embedded_buyer
from master_functions.label_maketing_buyer import label_marketing_buyer
from master_functions.label_titles import label_decision_maker, label_title
from master_functions.label_operations_buyer import label_operations_buyer
from master_functions.unique_buyer_type import unique_buyer_type
from master_functions.label_tech_product import label_tech_product

class lead_list(object):

    def __init__(self, in_path, out_path, buyer_type = None):
        self.path = in_path
        self.out_path = out_path
        self.writing_input_names = ['Id', 'Full Name', 'Job Title', 'Email Address', 'Phone Number', 'Lead Source',  'Company Name', 'Campaign Name','State', 'Postal Code', 'Marketo SFDC ID', 'Created At', 'Sub Region', 'Country', 'Sub Region (L)']
        self.writing_add_titles = ['Clean Company Name1', 'Title Group', 'Sales Title',  'Marketing Title', 'OEM Title', 'BI Title', 'Operations Title','Tech Product', 'Analytics Title', 'Decision Maker', 'InsideView Account ID', 'Account', 'Region', 'Operations Buyer', 'Lead Rank' ]
        self.buyer_type = buyer_type
        self.import_csv()
        self.write_to_csv()

    def write_to_csv(self):
        with open(self.out_path, 'w') as write_csv:
            writer1 = csv.DictWriter(write_csv, fieldnames=self.writing_input_names +  self.writing_add_titles, lineterminator = '\n')
            #writer2 = csv.DictWriter(write_csv.replace('.csv', ' 2') +".csv", fieldnames=self.writing_input_names +  self.writing_add_titles, lineterminator = '\n')

            writer1.writeheader()
            #writer2.writeheader()
            count =0
            print "here"
            for row in self.acct_list[:200000]:
                writer1.writerow(row)
            print row


    def import_csv(self):
        acct_list = []
        with open(self.path) as f:
            reader = csv.DictReader(f)

            count = 0
            country_check = []
            for row in reader:
                count +=1
                if count%20000==0:
                    print count

                try:
                    for key in ['Title Group', 'Sales Buyer', 'Target Account', 'Inferred Country', 'Marketing Buyer', 'BI Buyer']:
                        del row[key]
                except:
                    pass
                row['InsideView Account ID'] = row['InsideView Account ID (L)']
                del row['InsideView Account ID (L)']

                row['Clean Company Name1'] = clean_account_name(row['Company Name'])
                updated_row2 = label_decision_maker(row)
                updated_row3 = label_title(updated_row2)
                updated_row4 = label_sales_buyer(updated_row3)
                updated_row5 = label_marketing_buyer(updated_row4)
                updated_row6 = label_operations_buyer(updated_row5)
                updated_row7 = label_embedded_buyer(updated_row6)
                updated_row8 = label_analytics_buyer(updated_row7)
                updated_row9 = label_bi_buyer(updated_row8)
                updated_row10 = label_tech_product(updated_row9)
                if self.buyer_type is not None:
                    updated_row11 = unique_buyer_type(updated_row10, self.buyer_type)
                    acct_list.append(updated_row11)
                else:
                    acct_list.append(updated_row10)
            self.acct_list = acct_list


lead_list('C:/Users/wkuffel/Desktop/Marketing Data/20150414 Marketo Update/raw marketing data.csv','C:/Users/wkuffel/Desktop/Marketing Data/20150414 Marketo Update/processed marketing data.csv')
