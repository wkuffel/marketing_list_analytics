__author__ = 'wkuffel'

import csv

class lead_list(object):

    def __init__(self, in_path, out_path):
        self.path = in_path
        self.out_path = out_path
        self.writing_field_names_ordered =['Id', 'First Name','Last Name', 'Email Address', 'Phone Number', 'SFDC Type', 'Company Name', 'Job Title','Annual Company Revenue Range', 'Company Industries', 'Annual Company Revenue Range (A)', 'Company Employee Range',   'Lead Status', 'Lead Source', 'Updated At', 'Lead Score', 'Decision Maker', 'Job Level', 'Sales Title', 'Marketing Title', 'BI Title', 'OEM Title', 'Analytics Title', 'Clean Company Name1', 'HQ Country','Country','Region', 'State', 'HQ State']


        self.import_csv()
        self.count = 0
        self.get_counts()
        #self.get_counts_by_var()
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

                updated_row1 = self.clean_company_names(row)
                updated_row2 = self.label_decision_maker(updated_row1)
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
                #except:
                #    pass

                #if row['Region'] == 'EMEA' or row['Country'].lower().strip() in ['netherlands','united kingdown','palestinian territory','denmark','croatia','gbr', 'finland', 'nigeria','austria','bosnia-herzegovina', 'lb','sd','pl', "cote d'ivoire (ivory coast)",'al','md','om','jo','ni','england','ao','dk', 'syrian arab republic','ug','cy','bw', 'belgium',False,'dz','ireland (eire)','sudan','slovak republic','bh', 'ua','kw','eg','ro','netherlands, the','tr','sk', 'by', 'cz','lt', 'tn','gr','the netherlands','deutschland', 'se','spain','qa','ae', 'ch','et','russia','hr','hu', 'ir','fi','nl','sa','ie','ma', 'uk', 'it', 'pt', 'united kingdom', 'gb','france', 'ad', 'fr', 'germany', 'ke', 'az', 'il', 'es', 'bg','ru', 'za','de', 'croatia (hrvatska)', 'u.a.e.', 'uae','scotland', 'at', 'ng','yu', 'si','gh',  ]:



                """
                if row['Decision Maker'] == True:
                    if row['Sales Title'] == False and row['Marketing Title'] == False and row['BI Title'] == False and row['OEM Title'] == False:
                        job_title_string = row['Job Title'].lower().strip()
                        print job_title_string
                """
            """
            all_tokens =[]
            for row in acct_list:
                if row['Sales Title'] == False and row['Marketing Title'] == False and row['BI Title'] == False and row['OEM Title'] == False and row['Decision Maker'] == True:
                    #if row['BI Title'] == True and row['Sales Title'] == True:
                    #print row['Job Title'].lower().strip()
                    #all_tokens.append(row['Job Title'].lower().strip().split())
                    all_tokens.append(row['Job Title'].lower().strip())

            #all_token_list = [token for token_list in all_tokens[:15000] for token in token_list]
            #result_dict = {token: all_tokens.countstr(token) for token in all_token_list}
            #print ['ab', 'ab'].count('ab')
            #print all_token_list
            #print all_tokens
            result_dict = {token: all_tokens.count(token) for token in all_tokens}
            f= open('C:/Users/wkuffel/Desktop/Marketing Data/other job titles.csv', 'w')
            writer = csv.DictWriter(f,fieldnames=['title', 'count'], lineterminator = '\n' )
            writer.writeheader()
            for a in result_dict:
                if result_dict[a]>150:
                    writer.writerow({'title': a, 'count': result_dict[a]})
            """

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

    def get_counts(self):
        all_count = 0
        decision_maker = 0
        sales_buyer=0
        marketing_buyer=0
        bi_buyer=0
        oem_buyer=0
        analytics_buyer = 0
        decision_maker_no_business = 0
        marketing_and_sales = 0
        bi_and_oem=0
        sales_and_bi = 0
        sales_and_oem = 0
        marketing_and_bi = 0
        marketing_and_oem =0
        analytics_and_marketing= 0
        analytics_and_bi = 0
        analytics_and_sales = 0
        analytics_and_oem=0
        for row in self.acct_list:
            all_count+=1
            if row['Decision Maker'] == True :
                decision_maker +=1
            if row['Sales Title'] == True and row['Decision Maker'] == True:
                sales_buyer +=1
            if row['Marketing Title'] == True and row['Decision Maker'] == True:
                marketing_buyer +=1
            if row['BI Title'] == True and row['Decision Maker'] == True:
                bi_buyer +=1
            if row['OEM Title'] == True and row['Decision Maker'] == True:
                oem_buyer +=1
            if row['Analytics Title'] == True and row['Decision Maker'] == True:
                analytics_buyer += 1
            #combinations
            if  row['Sales Title'] == True and row['Marketing Title'] == True and row['Decision Maker'] == True:
                marketing_and_sales +=1
            if row['BI Title'] == True and row['OEM Title'] == True and row['Decision Maker'] == True:
                bi_and_oem +=1

            if  row['Sales Title'] == True and row['BI Title'] == True and row['Decision Maker'] == True:
                sales_and_bi +=1
            if row['Sales Title'] == True and row['OEM Title'] == True and row['Decision Maker'] == True:
                sales_and_oem +=1
            if  row['Marketing Title'] == True and row['BI Title'] == True and row['Decision Maker'] == True:
                marketing_and_bi +=1
            if row['Marketing Title'] == True and row['OEM Title'] == True and row['Decision Maker'] == True:
                marketing_and_oem +=1
            #if row['Analytics Title'] == True and row['Marketing Title'] == True:
            #    analytics_and_marketing +=1
            #if row['Analytics Title'] == True and row['Sales Title'] == True:
            #    analytics_and_sales +=1
            #if row['Analytics Title'] == True and row['BI Title'] == True:
            #    analytics_and_bi +=1
            #if row['Analytics Title'] == True and row['OEM Title'] == True:
            #    analytics_and_oem +=1
            if row['Decision Maker'] == True and row['Sales Title'] == False and row['Marketing Title'] == False and row['BI Title'] == False and row['OEM Title'] == False:
                decision_maker_no_business +=1

        print "all count: " +str(all_count) #2191246
        print "decision makers: "+ str(decision_maker) #160287
        print "sales buyer: " + str(sales_buyer)
        print "marketing_buyer: " + str(marketing_buyer)
        print "bi buyer: " + str(bi_buyer)
        print "oem buyer: " + str(oem_buyer)
        print "analytics buyer: " + str(analytics_buyer)
        print "marketing and sales: " + str(marketing_and_sales)
        print "bi and oem: " + str(bi_and_oem)
        print "sales and bi: " + str(sales_and_bi)
        print "sales and oem: " + str(sales_and_oem)
        print "marketing and bi: " + str(marketing_and_bi)
        print "marketing and oem: " + str(marketing_and_oem)
        print "decision maker, no buyer type: " + str(decision_maker_no_business)


    def get_counts_by_var(self, var='Cleaned Revenue'):
        all_count = {'title':'All Leads'}
        decision_maker = {'title':'Decision Makers'}
        sales_buyer={'title':'Sales Title'}
        marketing_buyer={'title':'Marketing Title'}
        bi_buyer={'title':'BI Title'}
        oem_buyer={'title':'OEM Title'}
        analytics_buyer={'title': 'Analytics Title'}
        marketing_and_sales = {'title':'Marketing and Sales'}
        bi_and_oem={'title':'BI and OEM'}
        sales_and_bi = {'title':'Sales and BI'}
        sales_and_oem = {'title':'Sales and OEM'}
        marketing_and_bi = {'title':'Marketing and BI'}
        marketing_and_oem ={'title':'Marketing and OEM'}
        decision_maker_no_business = {'title':'Decision Maker No Business'}

        for row in self.acct_list:
                updated_row = self.clean_revenue(row)
                if updated_row[var] not in all_count:
                    all_count[updated_row[var]]=0
                    decision_maker[updated_row[var]]=0
                    sales_buyer[updated_row[var]]=0
                    marketing_buyer[updated_row[var]]=0
                    bi_buyer[updated_row[var]]=0
                    oem_buyer[updated_row[var]]=0
                    marketing_and_sales[updated_row[var]]=0
                    bi_and_oem[updated_row[var]]=0
                    sales_and_bi[updated_row[var]]=0
                    sales_and_oem[updated_row[var]]=0
                    marketing_and_bi[updated_row[var]]=0
                    marketing_and_oem[updated_row[var]]=0
                    decision_maker_no_business[updated_row[var]]=0
                else:
                    pass
        for row in self.acct_list:
            all_count[row[var]]+=1
            if row['Decision Maker'] == True:
                 decision_maker[row[var]] +=1
            if row['Sales Title'] == True and row['Decision Maker'] == True:
                print row
                print sales_buyer[row[var]]
                sales_buyer[row[var]] +=1
            if row['Marketing Title'] == True and row['Decision Maker'] == True:
                marketing_buyer[row[var]] +=1
            if row['BI Title'] == True and row['Decision Maker'] == True:
                bi_buyer[row[var]] +=1
            if row['OEM Title'] == True and row['Decision Maker'] == True:
                oem_buyer[row[var]] +=1
            #combinations
            if  row['Sales Title'] == True and row['Marketing Title'] == True and row['Decision Maker'] == True:
                marketing_and_sales[row[var]] +=1
            if row['BI Title'] == True and row['OEM Title'] == True and row['Decision Maker'] == True:
                bi_and_oem[row[var]] +=1

            if  row['Sales Title'] == True and row['BI Title'] == True and row['Decision Maker'] == True:
                sales_and_bi[row[var]] +=1
            if row['Sales Title'] == True and row['OEM Title'] == True and row['Decision Maker'] == True:
                sales_and_oem[row[var]] +=1
            if  row['Marketing Title'] == True and row['BI Title'] == True and row['Decision Maker'] == True:
                marketing_and_bi[row[var]] +=1
            if row['Marketing Title'] == True and row['OEM Title'] == True and row['Decision Maker'] == True:
                marketing_and_oem[row[var]] +=1
            if row['Decision Maker'] == True and row['Sales Title'] == False and row['Marketing Title'] == False and row['BI Title'] == False and row['OEM Title'] == False:
                decision_maker_no_business[row[var]] +=1

        """
        print "all count: " +str(all_count) #2191246
        print "decision makers: "+ str(decision_maker) #160287
        print "sales buyer: " + str(sales_buyer)
        print "marketing_buyer: " + str(marketing_buyer)
        print "bi buyer: " + str(bi_buyer)
        print "oem buyer: " + str(oem_buyer)
        print "marketing and sales: " + str(marketing_and_sales)
        print "bi and oem: " + str(bi_and_oem)
        print "sales and bi: " + str(sales_and_bi)
        print "sales and oem: " + str(sales_and_oem)
        print "marketing and bi: " + str(marketing_and_bi)
        print "marketing and oem: " + str(marketing_and_oem)
        print "decision maker, no buyer type: " + str(decision_maker_no_business)
        """
        ordered_field_names= ['title', '1 - Over $5 Billion' , '2 - $2.5 - $5 Billion','3 - $1 - $2.5 Billion', '4 - $500 Million - $1 Billion', '5 - $250 - $500 Million', '6 - $100 - $250 Million','7 - $50 - $100 Million', '8 - Under $50 Million', '9 - Unknown']


        with open('C:/Users/wkuffel/Desktop/Marketing Data/counts by revenue.csv', 'w') as write_csv:
            writer = csv.DictWriter(write_csv, fieldnames= ordered_field_names, lineterminator = '\n')
            writer.writeheader()
            writer.writerow(all_count)
            writer.writerow(decision_maker)
            writer.writerow(sales_buyer)
            writer.writerow(marketing_buyer)
            writer.writerow(bi_buyer)
            writer.writerow(oem_buyer)
            writer.writerow(marketing_and_sales)
            writer.writerow(bi_and_oem)
            writer.writerow(sales_and_bi)
            writer.writerow(sales_and_oem)
            writer.writerow(marketing_and_bi)
            writer.writerow(marketing_and_oem)
            writer.writerow(decision_maker_no_business)

    def clean_revenue(self, row):
        updated_row = row
        updated_row['Cleaned Revenue'] = ''
        revenue_string = row['Annual Company Revenue Range']
        if revenue_string.lower()[:3] in ['1 -', '2 -','3 -','4 -','5 -','6 -','7 -','8 -','9 -','Unk']:
            #print row['Annual Company Revenue Range']
            updated_row['Cleaned Revenue'] = row['Annual Company Revenue Range']
        else:
            if row['Annual Company Revenue Range'].strip() == '' or row['Annual Company Revenue Range'] in ['Unknown', '#N/A', '--']:
                updated_row['Cleaned Revenue'] = '9 - Unknown'
            elif  row['Annual Company Revenue Range'] in ['$500,001-$1,000,000','$0-20M','Under $10 million', "Under 1M", 'Less than $1 mil' "$0-$500,000", '$0 - 1M', '$1 - 10M', '$10 - 50M', 'Less than $25 million', '$10 mil to less than $25 mil', 'Less than $1 mil', '$10 mil to less than $25 mil', '$5 mil to less than $10 mil', '$1 mil to less than $5 mil', '$25 mil to less than $50 mil', 'Under $20 Million', '$25 million to $50 million', '$26 million to $50 million', 'Less than $10 million', '1M - 10M' ]:
                updated_row['Cleaned Revenue'] ='8 - Under $50 Million'
            elif  row['Annual Company Revenue Range'] in ['$21-100M','$20 - $100 Million','$51 - 100 Million','$50 mil to less than $100 mil','$50 - 100M', '$50 million to $100 million', '$25 to $99 million', 'Less than $100 mil', 'Less than $100 million', '$25 million - $99 million','$10,000,001-$100,000,000', 'Less than $100 million annual revenue' ]:
                updated_row['Cleaned Revenue'] ='7 - $50 - $100 Million'
            elif  row['Annual Company Revenue Range'] in ['$50 - $250 Million','$100 million - $250 million','$100 million to $249 million','101M - 250M','$100 million to $249 mil','$101 - 250 Million','$50 Million - $250 Million','101 to 250','$101-250M','$100 mil to less than $250 mil', '$100to $499 million','$100 - 250M', '$100 million to $250 million', '$100 to $199 million', '$238.80M', '$200 to $299 million']:
                updated_row['Cleaned Revenue'] ='6 - $100 - $250 Million'
            elif  row['Annual Company Revenue Range'] in ['$251 - 500 Million','$100 to $499 million','$300 to $399 million','$100 to $499 million','$251 - $500 Million','$250 - 500M', '$250 mil to less than $500 mil', '$250 million to $500 million', '$250  - $500 Million', '$101 million - $500 million']:
                updated_row['Cleaned Revenue'] ='5 - $250 - $500 Million'
            elif  row['Annual Company Revenue Range'] in ['$501 - 750 Million','$500 million - $999 million','$500M to $1B','$500M - 1B','$501 million - $1 billion', '$500 Million to $1 Billion', '$500 - $1 Billion', '$500 to $999 million', '$250 Million - $1 Billion', '$100 million - $499 million', '$500 mil to less than $1 bil', '$750 to $999 million',]:
                updated_row['Cleaned Revenue'] ='4 - $500 Million - $1 Billion'
            elif  row['Annual Company Revenue Range'] in ['$1 - $2,5 Billion','$2 billion','$1 - $2,5 Billion' '$1 bil and above', 'More than $1 Billion', '$1 billion to $2.5 billion', '$1 -$2.5 Billion', '$1 billion - $2.5 billion', 'Over $1 Billion', '$1 billion or more', '$1.30B', '> $1B']:
                updated_row['Cleaned Revenue'] ='3 - $1 - $2.5 Billion'
            elif  row['Annual Company Revenue Range'] in ['$1 Billion - $5 Billion', '$2.5 billion to $5 billion', '$2.5  - $5 Billion', '$1 billion to $5 billion', '$1 bil and above','$1 Billion and over']:
                updated_row['Cleaned Revenue'] ='2 - $2.5 - $5 Billion'
            elif  row['Annual Company Revenue Range'] in ['Over 5 Billion', 'More than $50 billion','10B','$7 billion','']:
                updated_row['Cleaned Revenue'] ='1 - Over $5 Billion'
            else:
                try:
                    dollar_value = int(row['Annual Company Revenue Range'].replace('$','').replace(',','').replace('.00','').replace('M','').replace('m','').replace('.50','').replace('.10','').replace('.20','').replace('.30','').replace('.40','').replace('.50','').replace('.60','').replace('.70','').replace('.80','').replace('.90',''))
                    if dollar_value < 1000:
                        dollar_value = dollar_value*1000000
                    if dollar_value<50000000:
                        updated_row['Cleaned Revenue'] ='8 - Under $50 Million'
                    elif  dollar_value <100000000:
                        updated_row['Cleaned Revenue'] ='7 - $50 - $100 Million'
                    elif  dollar_value <250000000:
                        updated_row['Cleaned Revenue'] ='6 - $100 - $250 Million'
                    elif  dollar_value <500000000:
                        updated_row['Cleaned Revenue'] ='5 - $250 - $500 Million'
                    elif  dollar_value <1000000000:
                        updated_row['Cleaned Revenue'] ='4 - $500 Million - $1 Billion'
                    elif  dollar_value <2500000000:
                        updated_row['Cleaned Revenue'] ='3 - $1 - $2.5 Billion'
                    elif  dollar_value <=5000000000:
                        updated_row['Cleaned Revenue'] ='2 - $2.5 - $5 Billion'
                    elif  dollar_value >500000000:
                        updated_row['Cleaned Revenue'] ='1 - Over $5 Billion'
                except:
                    updated_row['Cleaned Revenue'] = '9 - Unknown'

        if updated_row['Cleaned Revenue'] not in ['9 - Unknown','8 - Under $50 Million','7 - $50 - $100 Million', '6 - $100 - $250 Million', '5 - $250 - $500 Million', '4 - $500 Million - $1 Billion','3 - $1 - $2.5 Billion','2 - $2.5 - $5 Billion',  '1 - Over $5 Billion'  ]:
            updated_row['Cleaned Revenue'] = '9 - Unknown'

        #if  updated_row['Cleaned Revenue'] == '9 - Unknown' and 'unknown' not in row['Annual Company Revenue Range'].lower() :
        #    print row['Annual Company Revenue Range']
        print updated_row
        return updated_row

input = 'C:/Users/wkuffel/Desktop/Marketing Data/20150130 marketo update/input files/raw marketing list.csv'
output = 'C:/Users/wkuffel/Desktop/Marketing Data/20150130 marketo update/output files/marketing list processed.csv'

lead_list(input,output)