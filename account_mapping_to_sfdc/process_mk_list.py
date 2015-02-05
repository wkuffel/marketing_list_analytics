__author__ = 'wkuffel'

import csv
from clean_account_name import clean_account_name

class lead_list(object):

    def __init__(self, in_path, out_path):
        self.path = in_path
        self.out_path = out_path
        self.writing_field_names_ordered =['Id', 'First Name','Last Name', 'Email Address', 'Phone Number', 'SFDC Type', 'Company Name', 'Job Title','Annual Company Revenue Range', 'Company Industries', 'Annual Company Revenue Range (A)', 'Company Employee Range',   'Lead Status', 'Lead Source', 'Updated At', 'Lead Score', 'Decision Maker', 'Job Level', 'Sales Title', 'Marketing Title', 'BI Title', 'OEM Title', 'Analytics Title', 'Clean Company Name1', 'HQ Country','Country','Region', 'State', 'HQ State']

        self.import_csv()
        self.write_to_csv()

    def write_to_csv(self):
        with open(self.out_path, 'w') as write_csv:
            writer = csv.DictWriter(write_csv, fieldnames=self.writing_field_names_ordered, lineterminator = '\n')
            writer.writeheader()
            for row in self.acct_list:
                writer.writerow(row)


    def clean_company_names(self, row):
        row['Clean Company Name1'] = row['Company Name'].lower().strip()
        row['Clean Company Name1'] = row['Clean Company Name1'].replace('.', '')
        row['Clean Company Name1'] = row['Clean Company Name1'].replace(',', '')
        row['Clean Company Name1'] = row['Clean Company Name1'].replace('"', '')


        if  row['Clean Company Name1'][-4:] ==" inc":
            row['Clean Company Name1'] = row['Clean Company Name1'][:-4]
            #print row['Clean Company Name']
        if  row['Clean Company Name1'][-4:] ==" llc":
            row['Clean Company Name1'] = row['Clean Company Name1'][:-4]
            #print row['Clean Company Name']
        if  row['Clean Company Name1'][-3:] ==" lp":
            row['Clean Company Name1'] = row['Clean Company Name1'][:-3]
            #print row['Clean Company Name']
        if  row['Clean Company Name1'][-5:] ==" corp":
            row['Clean Company Name1'] = row['Clean Company Name1'][:-5]
            #print row['Clean Company Name']
        if  row['Clean Company Name1'][-3:] ==" co":
            row['Clean Company Name1'] = row['Clean Company Name1'][:-3]
            #print row['Clean Company Name']

        row['Clean Company Name1'] = row['Clean Company Name1'].replace('corporation', '')
        row['Clean Company Name1'] = row['Clean Company Name1'].replace('corp', '')
        row['Clean Company Name1'] = row['Clean Company Name1'].replace('company', '')
        row['Clean Company Name1'] = row['Clean Company Name1'].replace('the ', '')


        row['Clean Company Name1'] = row['Clean Company Name1'].replace('-', ' ')
        row['Clean Company Name1'] = row['Clean Company Name1'].replace(' and ', ' & ')
        row['Clean Company Name1'] = row['Clean Company Name1'].replace(' + ', ' & ')
        row['Clean Company Name1'] = row['Clean Company Name1'].strip()
        return row
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
                updated_row2 = self.label_decision_maker(row)
                updated_row3 = self.label_title(updated_row2)
                updated_row4 = self.label_sales_buyer(updated_row3)
                updated_row5 = self.label_marketing_buyer(updated_row4)
                updated_row6 = self.label_bi_buyer(updated_row5)
                updated_row7 = self.label_oem_buyer(updated_row6)
                updated_row8 = self.label_analytics_buyer(updated_row7)
                ##print updated_row
                #if updated_row1 is not None:
                #    count +=1
                #acct_list.append(updated_row5)
                acct_list.append(updated_row8)
                self.acct_list = acct_list


    def label_decision_maker(self, row):
        row['Decision Maker'] = ''
        job_title_string = row['Job Title'].lower().strip()
        job_title_string_same_case =  row['Job Title'].strip()

        #yes, is decision maker
        if 'chief' in job_title_string:
            row['Decision Maker'] = True
        elif 'director' in job_title_string:
            row['Decision Maker'] = True
        elif 'evp' in job_title_string:
            row['Decision Maker'] = True
        elif 'vice president' in job_title_string:
            row['Decision Maker'] = True
        elif 'vp' in job_title_string:
            row['Decision Maker'] = True
        elif 'head' in job_title_string:
            row['Decision Maker'] = True
        elif 'president' in job_title_string:
            row['Decision Maker'] = True
        elif 'lead' in job_title_string:
            row['Decision Maker'] = True
        elif 'executive' in job_title_string:
            row['Decision Maker'] = True
        elif 'owner' in job_title_string:
            row['Decision Maker'] = True
        elif 'general manager' in job_title_string:
            row['Decision Maker'] = True
        elif job_title_string in ['ceo', 'cfo', 'coo', 'cio', 'cto', 'vp', 'cmo', 'cdo']:
            row['Decision Maker'] = True

        else:
            row['Decision Maker'] = False
        return row
        """
        elif 'manager' in job_title_string:
            row['Decision Maker'] = True
        elif 'mgr ' in job_title_string:
            row['Decision Maker'] = True
        """

    def label_title(self, row):
        row['Job Level'] = ''
        job_title_string = row['Job Title'].lower().strip()
        job_title_string_same_case =  row['Job Title'].strip()

        #yes, is decision maker
        #yes, is decision maker
        if 'chief' in job_title_string:
            row['Job Level'] = 'Chief'
        elif 'director' in job_title_string:
            row['Job Level'] = 'Director'
        elif 'evp' in job_title_string:
            row['Job Level'] = 'VP'
        elif 'vice president' in job_title_string:
            row['Job Level'] = 'VP'
        elif 'vp' in job_title_string:
            row['Job Level'] = 'VP'
        elif 'head' in job_title_string:
            row['Job Level'] = 'Director'
        elif 'president' in job_title_string:
            row['Job Level'] = 'Chief'
        elif 'founder' in job_title_string:
            row['Job Level'] = 'Chief'
        elif 'lead' in job_title_string:
            row['Job Level'] = 'Director'
        elif 'executive' in job_title_string:
            row['Job Level'] = 'Chief'
        elif 'owner' in job_title_string:
            row['Job Level'] = 'Chief'
        elif 'general manager' in job_title_string:
            row['Job Level'] = 'Director'
        elif job_title_string in ['ceo', 'cfo', 'coo', 'cio', 'cto', 'vp', 'cmo', 'cdo']:
            row['Job Level'] = 'Chief'
        elif len(job_title_string)>3 and  job_title_string[:4] == 'dir ':
            row['Job Level'] = 'Director'
        elif job_title_string == 'dir':
            row['Job Level'] = 'Director'
        else:
            row['Job Level'] = 'Below Director'
        return row


    def label_sales_buyer(self, row):
        row['Sales Title'] = ''
        job_title_string = row['Job Title'].lower().strip()
        job_title_string_same_case =  row['Job Title'].strip()

        if 'sales' in job_title_string:
            row['Sales Title'] = True
        elif 'channel' in job_title_string:
            row['Sales Title'] = True
        elif 'field operations' in job_title_string:
            row['Sales Title'] = True
        elif 'strategic accounts' in job_title_string:
            row['Sales Title'] = True
        elif 'business development' in job_title_string:
            row['Sales Title'] = True
        elif 'area' in job_title_string:
            row['Sales Title'] = True
        elif 'region' in job_title_string:
            row['Sales Title'] = True
        elif 'account executive' in job_title_string:
            row['Sales Title'] = True
        elif 'field' in job_title_string:
            row['Sales Title'] = True
        elif 'development' in job_title_string and 'product' not in job_title_string:
            row['Sales Title'] = True
        elif 'cro' == job_title_string:
            row['Sales Title'] = True
        elif 'revenue' in job_title_string:
            row['Sales Title'] = True

        #not in sales
        else:
           row['Sales Title'] = False

        return row

    def label_marketing_buyer(self, row):
        row['Marketing Title'] = ''
        job_title_string = row['Job Title'].lower().strip()
        job_title_string_same_case =  row['Job Title'].strip()

        #is in sales
        if 'marketing' in job_title_string:
            row['Marketing Title'] = True
        elif 'demand generation' in job_title_string:
            row['Marketing Title'] = True
        elif 'digital' in job_title_string:
            row['Marketing Title'] = True
        elif 'online' in job_title_string:
            row['Marketing Title'] = True
        elif 'advertising' in job_title_string:
            row['Marketing Title'] = True
        elif 'media' in job_title_string:
            row['Marketing Title'] = True
        elif 'consumer programs' in job_title_string:
            row['Marketing Title'] = True
        elif 'commerce' in job_title_string:
            row['Marketing Title'] = True
        elif 'campaign' in job_title_string: #
            row['Marketing Title'] = True
        elif 'consumer' in job_title_string: #
            row['Marketing Title'] = True
        elif 'strateg' in job_title_string: #covers stategy and stragegic
            row['Marketing Title'] = True
        elif 'product' in job_title_string: #covers stategy and stragegic
            row['Marketing Title'] = True
        elif 'creative' in job_title_string:
            row['Marketing Title'] = True
        elif 'cmo' == job_title_string:
            row['Marketing Title'] = True
        elif 'communication' in job_title_string:
            row['Marketing Title'] = True
        elif 'brand' in job_title_string:
            row['Marketing Title'] = True
        elif 'br&' in job_title_string:
            row['Marketing Title'] = True
        elif 'merchandising' in job_title_string:
            row['Marketing Title'] = True
        #not in marketing
        else:
           row['Marketing Title'] = False

        if row['Marketing Title'] == True:
            pass
            #print job_title_string
        return row

    def label_bi_buyer(self, row):
        row['BI Title'] = ''
        job_title_string = row['Job Title'].lower().strip()
        job_title_string_same_case =  row['Job Title'].strip()
        #is in BI
        if 'BI' in job_title_string_same_case: #BI
            row['BI Title'] = True
        elif 'business intelligence' in job_title_string: #BI
            row['BI Title'] = True
        elif 'analytics' in job_title_string: #analytics
            row['BI Title'] = True
        elif 'data' in job_title_string: #analytics
            row['BI Title'] = True
        elif 'cloud' in job_title_string: #IT, number of counts
            row['BI Title'] = True
        elif 'cdo' == job_title_string: #
            row['BI Title'] = True
        elif 'cio' == job_title_string:
            row['BI Title'] = True
        elif 'information' in job_title_string:
            row['BI Title'] = True
        elif 'IT' in job_title_string_same_case:#
            row['BI Title'] = True
        elif 'technology' in job_title_string:
            row['BI Title'] = True
        elif 'architect' in job_title_string:
            row['BI Title'] = True
        elif 'bi ' in job_title_string: #same with BI
            row['BI Title'] = True
        #not in sales
        else:
           row['BI Title'] = False
        if row['BI Title'] == True:
            pass
            #print job_title_string
        return row


    def label_oem_buyer(self, row):
        row['OEM Title'] = ''
        job_title_string = row['Job Title'].lower().strip()
        job_title_string_same_case =  row['Job Title'].strip()
        #is in sales
        if 'engineer' in job_title_string:
            row['OEM Title'] = True
        elif 'product' in job_title_string:
            row['OEM Title'] = True
        elif 'strateg' in job_title_string:
            row['OEM Title'] = True
        elif 'application' in job_title_string:
            row['OEM Title'] = True
        elif 'r&d' in job_title_string:
            row['OEM Title'] = True
        elif 'cto' == job_title_string:
            row['OEM Title'] = True
        elif 'ceo' == job_title_string:
            row['OEM Title'] = True
        elif 'technology' in job_title_string:
            row['OEM Title'] = True
        elif 'developer' in job_title_string:
            row['OEM Title'] = True
        #not in sales
        else:
           row['OEM Title'] = False


        if row['OEM Title'] == True:
            pass
            #print job_title_string
        return row


    def label_analytics_buyer(self, row):
        row['Analytics Title'] = ''
        job_title_string = row['Job Title'].lower().strip()
        job_title_string_same_case =  row['Job Title'].strip()
        #is in sales
        if 'analytic' in job_title_string:
            row['Analytics Title'] = True
        elif 'analyst' in job_title_string:
            row['Analytics Title'] = True
        #not in sales
        else:
           row['Analytics Title'] = False

        if row['Analytics Title'] == True:
            pass
            #print job_title_string
        return row




input = 'C:/Users/wkuffel/Desktop/Marketing Data/create account links/leads/raw marketing list.csv'
output = 'C:/Users/wkuffel/Desktop/Marketing Data/create account links/leads/marketing list processed.csv'

lead_list(input,output)