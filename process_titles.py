__author__ = 'wkuffel'

import csv

class process_titles(object):

    def __init__(self, in_path, out_path):
        self.path = in_path
        self.out_path = out_path
        self.writing_field_names_ordered = ['Job Level', 'Job Title', 'Decision Maker', 'Analytics Title', 'Sales Title', 'BI Title', 'Marketing Title']
        self.import_csv()
        self.write_to_csv()

    def write_to_csv(self):
        with open(self.out_path, 'w') as write_csv:
            writer = csv.DictWriter(write_csv, fieldnames=self.writing_field_names_ordered, lineterminator = '\n')
            writer.writeheader()
            for row in self.acct_list:
                writer.writerow(row)

    def import_csv(self):
        with open(self.path) as f:
            reader = csv.DictReader(f)
            acct_list = []
            print reader
            for row in reader:
                #print row
                updated_row1 = self.label_title(row)
                updated_row2 = self.label_decision_maker(updated_row1)
                updated_row3 = self.label_analytics_buyer(updated_row2)
                updated_row4 = self.label_sales_buyer(updated_row3)
                updated_row5 = self.label_bi_buyer(updated_row4)
                updated_row6 = self.label_marketing_buyer(updated_row4)

                acct_list.append(updated_row6)
                print updated_row2
            self.acct_list = acct_list
                #except:
                #    pass

                #if row['Region'] == 'EMEA' or row['Country'].lower().strip() in ['netherlands','united kingdown','palestinian territory','denmark','croatia','gbr', 'finland', 'nigeria','austria','bosnia-herzegovina', 'lb','sd','pl', "cote d'ivoire (ivory coast)",'al','md','om','jo','ni','england','ao','dk', 'syrian arab republic','ug','cy','bw', 'belgium',False,'dz','ireland (eire)','sudan','slovak republic','bh', 'ua','kw','eg','ro','netherlands, the','tr','sk', 'by', 'cz','lt', 'tn','gr','the netherlands','deutschland', 'se','spain','qa','ae', 'ch','et','russia','hr','hu', 'ir','fi','nl','sa','ie','ma', 'uk', 'it', 'pt', 'united kingdom', 'gb','france', 'ad', 'fr', 'germany', 'ke', 'az', 'il', 'es', 'bg','ru', 'za','de', 'croatia (hrvatska)', 'u.a.e.', 'uae','scotland', 'at', 'ng','yu', 'si','gh',  ]:



    def label_title(self, row):
        row['Job Level'] = ''
        job_title_string = row['Job Title'].lower().strip()
        job_title_string_same_case =  row['Job Title'].strip()

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

    def label_decision_maker(self, row):
        row['Decision Maker'] = ''
        job_title_string = row['Job Title'].lower().strip()
        job_title_string_same_case =  row['Job Title'].strip()

        #yes, is decision maker
        if row['Job Level'] == 'Director' or row['Job Level'] == 'VP' or row['Job Level'] == 'Chief':
            row['Decision Maker'] = 1
        else:
            row['Decision Maker'] = 0
        return row


    def label_analytics_buyer(self, row):
        row['Analytics Title'] = ''
        job_title_string = row['Job Title'].lower().strip()
        job_title_string_same_case =  row['Job Title'].strip()
        #is in sales
        if 'analytic' in job_title_string:
            row['Analytics Title'] = 1
        elif 'analyst' in job_title_string:
            row['Analytics Title'] = 1
        #not in sales
        else:
           row['Analytics Title'] = 0

        if row['Analytics Title'] == 1:
            pass
            #print job_title_string
        return row


    def label_sales_buyer(self, row):
        row['Sales Title'] = ''
        job_title_string = row['Job Title'].lower().strip()
        job_title_string_same_case =  row['Job Title'].strip()

        if 'sales' in job_title_string:
            row['Sales Title'] = 1
        elif 'channel' in job_title_string:
            row['Sales Title'] = 1
        elif 'field operations' in job_title_string:
            row['Sales Title'] = 1
        elif 'strategic accounts' in job_title_string:
            row['Sales Title'] = 1
        elif 'business development' in job_title_string:
            row['Sales Title'] = 1
        elif 'area' in job_title_string:
            row['Sales Title'] = 1
        elif 'region' in job_title_string:
            row['Sales Title'] = 1
        elif 'account executive' in job_title_string:
            row['Sales Title'] = 1
        elif 'field' in job_title_string:
            row['Sales Title'] = 1
        elif 'development' in job_title_string and 'product' not in job_title_string:
            row['Sales Title'] = 1
        elif 'cro' == job_title_string:
            row['Sales Title'] = 1
        elif 'revenue' in job_title_string:
            row['Sales Title'] = 1

        #not in sales
        else:
           row['Sales Title'] = 0

        return row

    def label_marketing_buyer(self, row):
        row['Marketing Title'] = ''
        job_title_string = row['Job Title'].lower().strip()
        job_title_string_same_case =  row['Job Title'].strip()

        #is in sales
        if 'marketing' in job_title_string:
            row['Marketing Title'] = 1
        elif 'demand generation' in job_title_string:
            row['Marketing Title'] = 1
        elif 'digital' in job_title_string:
            row['Marketing Title'] = 1
        elif 'online' in job_title_string:
            row['Marketing Title'] = 1
        elif 'advertising' in job_title_string:
            row['Marketing Title'] = 1
        elif 'media' in job_title_string:
            row['Marketing Title'] = 1
        elif 'consumer programs' in job_title_string:
            row['Marketing Title'] = 1
        elif 'commerce' in job_title_string:
            row['Marketing Title'] = 1
        elif 'campaign' in job_title_string: #
            row['Marketing Title'] = 1
        elif 'consumer' in job_title_string: #
            row['Marketing Title'] = 1
        elif 'strateg' in job_title_string: #covers stategy and stragegic
            row['Marketing Title'] = 1
        elif 'product' in job_title_string: #covers stategy and stragegic
            row['Marketing Title'] = 1
        elif 'creative' in job_title_string:
            row['Marketing Title'] = 1
        elif 'cmo' == job_title_string:
            row['Marketing Title'] = 1
        elif 'communication' in job_title_string:
            row['Marketing Title'] = 1
        elif 'brand' in job_title_string:
            row['Marketing Title'] = 1
        elif 'br&' in job_title_string:
            row['Marketing Title'] = 1
        elif 'merchandising' in job_title_string:
            row['Marketing Title'] = 1
        #not in marketing
        else:
           row['Marketing Title'] = 0

        if row['Marketing Title'] == 1:
            pass
            #print job_title_string
        return row

    def label_bi_buyer(self, row):
        row['BI Title'] = ''
        job_title_string = row['Job Title'].lower().strip()
        job_title_string_same_case =  row['Job Title'].strip()
        #is in BI
        if 'BI' in job_title_string_same_case: #BI
            row['BI Title'] = 1
        elif 'business intelligence' in job_title_string: #BI
            row['BI Title'] = 1
        elif 'analytics' in job_title_string: #analytics
            row['BI Title'] = 1
        elif 'data' in job_title_string: #analytics
            row['BI Title'] = 1
        elif 'cloud' in job_title_string: #IT, number of counts
            row['BI Title'] = 1
        elif 'cdo' == job_title_string: #
            row['BI Title'] = 1
        elif 'cio' == job_title_string:
            row['BI Title'] = 1
        elif 'information' in job_title_string:
            row['BI Title'] = 1
        elif 'IT' in job_title_string_same_case:#
            row['BI Title'] = 1
        elif 'technology' in job_title_string:
            row['BI Title'] = 1
        elif 'architect' in job_title_string:
            row['BI Title'] = 1
        elif 'bi ' in job_title_string: #same with BI
            row['BI Title'] = 1
        #not in sales
        else:
           row['BI Title'] = 0
        if row['BI Title'] == 1:
            pass
            #print job_title_string
        return row



infile ='C:/Users/wkuffel/Desktop/Marketing Data/20150203 attendence titles/titles only.csv'
outfile ='C:/Users/wkuffel/Desktop/Marketing Data/20150203 attendence titles/WBN_2015_02_18_Analytics_to_Revenue_Registered Titles.csv'

process_titles(infile,outfile)