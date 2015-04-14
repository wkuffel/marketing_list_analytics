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
from master_functions.label_consultant import label_consultant
from master_functions.label_non_work_email import  label_non_work_email

class process_titles(object):

    def __init__(self, in_path, out_path):
        self.path = in_path
        self.out_path = out_path
        self.writing_field_names_ordered = ['Lead ID', 'Full Name',  'Job Title', 'Email Address',   'Phone Number', 'Company Name', 'Operations Title',  'Sales Title', 'Marketing Title', 'BI Title', 'OEM Title', 'Decision Maker', 'Analytics Title', 'Consultant', 'Non Work Email', 'Clean Company Name1', 'Title Group']
        #['Job Level', 'Job Title', 'Decision Maker', 'Analytics Title', 'Sales Title', 'BI Title', 'Marketing Title']
        self.import_csv()
        self.write_to_csv()

    def write_to_csv(self):
        with open(self.out_path, 'w') as write_csv:
            writer = csv.DictWriter(write_csv, fieldnames=self.writing_field_names_ordered, lineterminator = '\n')
            writer.writeheader()
            count =0
            for row in self.acct_list:
                writer.writerow(row)
                count +=1
            print count

    def import_csv(self):
        with open(self.path) as f:
            reader = csv.DictReader(f)
            acct_list = []
            print reader
            for row in reader:
                row['Clean Company Name1'] = clean_account_name(row['Company Name'])
                updated_row2 = label_decision_maker(row)
                updated_row3 = label_title(updated_row2)
                updated_row4 = label_sales_buyer(updated_row3)
                updated_row5 = label_marketing_buyer(updated_row4)
                updated_row6 = label_operations_buyer(updated_row5)
                updated_row7 = label_embedded_buyer(updated_row6)
                updated_row8 = label_analytics_buyer(updated_row7)
                updated_row9 = label_bi_buyer(updated_row8)
                updated_row10 = label_consultant(updated_row9)
                #updated_row11 = label_non_work_email(updated_row10)
                acct_list.append(updated_row10)
            self.acct_list = acct_list
                #except:
                #    pass

                #if row['Region'] == 'EMEA' or row['Country'].lower().strip() in ['netherlands','united kingdown','palestinian territory','denmark','croatia','gbr', 'finland', 'nigeria','austria','bosnia-herzegovina', 'lb','sd','pl', "cote d'ivoire (ivory coast)",'al','md','om','jo','ni','england','ao','dk', 'syrian arab republic','ug','cy','bw', 'belgium',False,'dz','ireland (eire)','sudan','slovak republic','bh', 'ua','kw','eg','ro','netherlands, the','tr','sk', 'by', 'cz','lt', 'tn','gr','the netherlands','deutschland', 'se','spain','qa','ae', 'ch','et','russia','hr','hu', 'ir','fi','nl','sa','ie','ma', 'uk', 'it', 'pt', 'united kingdom', 'gb','france', 'ad', 'fr', 'germany', 'ke', 'az', 'il', 'es', 'bg','ru', 'za','de', 'croatia (hrvatska)', 'u.a.e.', 'uae','scotland', 'at', 'ng','yu', 'si','gh',  ]:






infile ='C:/Users/wkuffel/Desktop/Marketing Data/Stalled Opportunities/Stalled Opp Job Titles.csv'
outfile ='C:/Users/wkuffel/Desktop/Marketing Data/Stalled Opportunities/Stalled Opp Job Titles written.csv'

process_titles(infile,outfile)