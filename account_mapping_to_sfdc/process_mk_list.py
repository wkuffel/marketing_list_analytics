__author__ = 'wkuffel'

import csv
from master_functions.clean_account_name import clean_account_name
from master_functions.label_analytics_title import label_analytics_buyer
from master_functions.label_bi_buyer import label_bi_buyer
from master_functions.label_sales_buyer import label_sales_buyer
from master_functions.label_embedded_buyer import label_embedded_buyer
from master_functions.label_maketing_buyer import label_marketing_buyer
from master_functions.label_titles import label_decision_maker, label_title
from master_functions.label_operations_buyer import label_operations_buyer


class lead_list(object):

    def __init__(self, in_path, out_path):
        self.path = in_path
        self.out_path = out_path
        self.writing_field_names_ordered =['Id', 'First Name','Last Name', 'Full Name', 'Email Address', 'InsideView Account ID', 'Phone Number', 'SFDC Type', 'Company Name', 'Job Title','Annual Company Revenue Range', 'Company Industries', 'Annual Company Revenue Range (A)', 'Company Employee Range',   'Lead Status', 'Lead Source', 'Updated At', 'Lead Score', 'Decision Maker', 'Job Level', 'Sales Title', 'Marketing Title', 'BI Title', 'OEM Title', 'Analytics Title', 'Operations Title', 'Clean Company Name1', 'HQ Country','Country','Region', 'State', 'HQ State']

        self.import_csv()
        self.write_to_csv()

    def write_to_csv(self):
        with open(self.out_path, 'w') as write_csv:
            writer = csv.DictWriter(write_csv, fieldnames=self.writing_field_names_ordered, lineterminator = '\n')
            writer.writeheader()
            for row in self.acct_list:
                #print row
                writer.writerow(row)


        #'& co'
        #"'"-what to do about apostrophes

    def import_csv(self):
        acct_list = []
        with open(self.path) as f:
            reader = csv.DictReader(f)

            count = 0
            country_check = []
            for row in reader:
                #try:
                    #if row['Region'] == 'EMEA' or row['Country'].lower().strip() in ['lu', 'se', 'dk','no', 'de','be','netherlands','united kingdown','palestinian territory','denmark','croatia','gbr', 'finland', 'nigeria','austria','bosnia-herzegovina', 'lb','sd','pl', "cote d'ivoire (ivory coast)",'al','md','om','jo','ni','england','ao','dk', 'syrian arab republic','ug','cy','bw', 'belgium','no','dz','ireland (eire)','sudan','slovak republic','bh', 'ua','kw','eg','ro','netherlands, the','tr','sk', 'by', 'cz','lt', 'tn','gr','the netherlands','deutschland', 'se','spain','qa','ae', 'ch','et','russia','hr','hu', 'ir','fi','nl','sa','ie','ma', 'uk', 'it', 'pt', 'united kingdom', 'gb','france', 'ad', 'fr', 'germany', 'ke', 'az', 'il', 'es', 'bg','ru', 'za','de', 'croatia (hrvatska)', 'u.a.e.', 'uae','scotland', 'at', 'ng','yu', 'si','gh',  ]:
                    #if row['Country'].lower().strip() in ['united kingdown','gbr','england','gb','scotland','united kingdom' ]:
                    #if row['Region'] == 'EMEA' or row['Country'].lower().strip() in ['netherlands','united kingdown','denmark','gbr', 'finland','england','dk', 'belgium','no','be', 'fr', 'gr','netherlands, the','de','the netherlands','deutschland','fi','nl' 'uk', 'united kingdom', 'gb','france', 'fr', 'germany','de', 'croatia (hrvatska)','lu', 'se' ]:

                row['Clean Company Name1'] = clean_account_name(row['Company Name'])
                updated_row2 = label_decision_maker(row)
                updated_row3 = label_title(updated_row2)
                updated_row4 = label_sales_buyer(updated_row3)
                updated_row5 = label_marketing_buyer(updated_row4)
                updated_row6 = label_operations_buyer(updated_row5)
                updated_row7 = label_embedded_buyer(updated_row6)
                updated_row8 = label_analytics_buyer(updated_row7)
                updated_row9 = label_bi_buyer(updated_row8)
                ##print updated_row
                #if updated_row1 is not None:
                #    count +=1
                #acct_list.append(updated_row5)
                acct_list.append(updated_row9)
                self.acct_list = acct_list





input = 'C:/Users/wkuffel/Desktop/Marketing Data/20150213 marketing list analysis/marketing list raw updated.csv'
output = 'C:/Users/wkuffel/Desktop/Marketing Data/20150213 marketing list analysis/marketing list raw processed.csv'

lead_list(input,output)