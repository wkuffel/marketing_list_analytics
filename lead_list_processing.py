__author__ = 'wkuffel'

import csv

class lead_list(object):

    def __init__(self, path):
        self.path = path
        self.import_csv()
        self.count = 0

    def import_csv(self):
        acct_list = []
        with open(self.path) as f:
            reader = csv.DictReader(f)

            count = 0
            for row in reader:
                updated_row1 = self.label_job_type(row)
                updated_row2 = self.label_decision_maker(updated_row1)
                #print updated_row
                if updated_row2 is not None:
                    count +=1
                acct_list.append(updated_row2)
            """
            all_tokens =[]
            for row in acct_list:
                if row['Buyer Type'] == 'Lost':
                    #print row['Job Title'].lower().strip().split()
                    all_tokens.append(row['Job Title'].lower().strip().split())
            all_token_list = [token for token_list in all_tokens[30000:] for token in token_list]
            #result_dict = {token: all_tokens.countstr(token) for token in all_token_list}
            #print ['ab', 'ab'].count('ab')
            #print all_token_list
            result_dict = {token: all_token_list.count(token) for token in all_token_list}
            for a in result_dict:
                if result_dict[a]>45:
                    print a, result_dict[a]
            """

    def label_decision_maker(self, row):
        row['Decision Maker'] = ''
        job_title_string = row['Job Title'].lower().strip()
        job_title_string_same_case =  row['Job Title'].strip()

        #yes, is decision maker
        if 'chief' in job_title_string:
            row['Decision Maker'] = 'yes'
        elif 'director' in job_title_string:
            row['Decision Maker'] = 'yes'
        elif 'evp' in job_title_string:
            row['Decision Maker'] = 'yes'
        elif 'vice president' in job_title_string:
            row['Decision Maker'] = 'yes'
        elif 'vp' in job_title_string:
            row['Decision Maker'] = 'yes'
        elif 'head' in job_title_string:
            row['Decision Maker'] = 'yes'
        elif 'president' in job_title_string:
            row['Decision Maker'] = 'yes'
        elif 'lead' in job_title_string:
            row['Decision Maker'] = 'yes'
        elif 'lead' in job_title_string:
            row['Decision Maker'] = 'yes'
        elif job_title_string in ['ceo', 'cfo', 'coo', 'cio', 'cto', 'vp', 'cmo', 'cdo']:
            row['Decision Maker'] = 'yes'

        #No, not a decision maker
        else:
            row['Decision Maker'] = 'no'
            print job_title_string_same_case
        return row

    def label_job_type(self, row):
        row['Buyer Type'] = ''
        job_title_string = row['Job Title'].lower().strip()
        job_title_string_same_case =  row['Job Title'].strip()

        # SALES
        if 'sale' in job_title_string:
            row['Buyer Type'] = 'Sales'
        elif 'field' in job_title_string:
            row['Buyer Type'] = 'Sales'
        elif 'business development' in job_title_string or 'BD' in job_title_string_same_case:
            row['Buyer Type'] = 'Sales'
        elif 'area' in job_title_string:
            row['Buyer Type'] = 'Sales'
        elif 'enablement' in job_title_string:
            row['Buyer Type'] = 'Sales'
        elif 'account' in job_title_string and 'accounting' not in job_title_string:
            row['Buyer Type'] = 'Sales'
        elif 'CRM' in job_title_string_same_case:
            row['Buyer Type'] = 'Sales'
        elif 'relationship' in job_title_string:
            row['Buyer Type'] = 'Sales'

        #Marketing
        elif 'market' in job_title_string:
            row['Buyer Type'] = 'Marketing'
        elif 'consumer' in job_title_string:
            row['Buyer Type'] = 'Marketing'
        elif 'CMO' == job_title_string_same_case:
            row['Buyer Type'] = 'OEM'
        elif 'demand generation' in job_title_string:
            row['Buyer Type'] = 'Marketing'
        elif 'digital' in job_title_string:
            row['Buyer Type'] = 'Marketing'
        elif 'online' in job_title_string:
            row['Buyer Type'] = 'Marketing'
        elif 'demand' in job_title_string:
            row['Buyer Type'] = 'Marketing'
        elif 'creative' in job_title_string:
            row['Buyer Type'] = 'Marketing'
        elif 'strateg' in job_title_string:
            row['Buyer Type'] = 'Marketing'
        elif 'art director' in job_title_string:
            row['Buyer Type'] = 'Marketing'
        elif 'advertising' in job_title_string:
            row['Buyer Type'] = 'Marketing'
        elif 'br&' in job_title_string:
            row['Buyer Type'] = 'Marketing'
        elif 'Brand' in job_title_string.title():
            row['Buyer Type'] = 'Marketing'
        elif 'Media' in job_title_string.title():
            row['Buyer Type'] = 'Marketing'


        #BI/Analytics
        elif 'business intelligence' in job_title_string:
            row['Buyer Type'] = 'BI'
        elif 'IT' in job_title_string_same_case:
            row['Buyer Type'] = 'BI'
        elif 'CIO' in job_title_string_same_case:
            row['Buyer Type'] = 'BI'
        elif 'BI' in job_title_string_same_case:
            row['Buyer Type'] = 'BI'
        elif 'architect' in job_title_string:
            row['Buyer Type'] = 'BI'
        elif 'information' in job_title_string:
            row['Buyer Type'] = 'BI'
        elif 'data' in job_title_string:
            row['Buyer Type'] = 'BI'
        elif 'technology' in job_title_string:
            row['Buyer Type'] = 'BI'
        elif 'dba' in job_title_string:
            row['Buyer Type'] = 'BI'
        elif 'Bi ' in job_title_string.title() :
            row['Buyer Type'] = 'BI'

        #suspect assumption
        elif 'analy' in job_title_string:
            row['Buyer Type'] = 'BI'
        #Embedded
        elif 'product' in job_title_string:
            row['Buyer Type'] = 'OEM'
        elif 'CEO' in job_title_string_same_case:
            row['Buyer Type'] = 'OEM'
        elif 'CTO' in job_title_string_same_case:
            row['Buyer Type'] = 'OEM'
        elif 'president' == job_title_string:
            row['Buyer Type'] = 'OEM'
        elif 'owner' == job_title_string:
            row['Buyer Type'] = 'OEM'
        elif 'founder' == job_title_string:
            row['Buyer Type'] = 'OEM'

        #suspect
        elif 'engineer' in job_title_string:
            row['Buyer Type'] = 'OEM'
        #suspect
        elif 'developer' in job_title_string:
            row['Buyer Type'] = 'OEM'
        #suspect
        elif 'programmer' in job_title_string:
            row['Buyer Type'] = 'OEM'
        #suspect
        elif 'technical' in job_title_string:
            row['Buyer Type'] = 'OEM'

        #Other
        elif 'CFO' in job_title_string_same_case:
            row['Buyer Type'] = 'Other'
        elif 'financ' in job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'HR' in job_title_string_same_case:
            row['Buyer Type'] = 'Other'
        elif '' == job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'vp' == job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'director' == job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'evp' == job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'consultant' == job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'manager' == job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'VP/general manager' in job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'COO' in job_title_string_same_case:
            row['Buyer Type'] = 'Other'
        elif 'principal' == job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'supply' in job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'general manager' == job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'partner' in job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'chairman' == job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'human resource' in job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'legal' in job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'customer' in job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'client' in job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'vice president' == job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'tax' in job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'portfolio' in job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'accounting' in job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'audit' in job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'other' in job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'controller' in job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'Senior Management (SVP/GM/Director)' == job_title_string_same_case:
            row['Buyer Type'] = 'Other'
        elif 'vp/general manager' == job_title_string:
            row['Buyer Type'] = 'Other'

        elif 'executive director' == job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'senior director' == job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'associate director' == job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'managing director' == job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'project manager' == job_title_string:
            row['Buyer Type'] = 'Other'
        elif 'recru' == job_title_string:
            row['Buyer Type'] = 'Other'
        elif len(job_title_string) ==1:
            row['Buyer Type'] = 'Other'
        elif 'operation' in job_title_string:
            row['Buyer Type'] = 'Other'

        else:
            row['Buyer Type'] = 'Lost'
            #print job_title_string_same_case
        return row






lead_list('C:/Users/wkuffel/Desktop/Marketing Data/all Birst leads 20140115.csv')