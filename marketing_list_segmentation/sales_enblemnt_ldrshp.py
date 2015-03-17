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
from master_functions.unique_buyer_type import unique_buyer_type


class segment_enblmnt_ldrshp(object):
    def __init__(self, in_path, out_path):
        self.in_path = in_path
        self.outpath = out_path
        self.import_dataset()

    def import_dataset(self):
        lead_list = []
        with open(self.in_path) as f:
            reader = csv.DictReader(f)
            count =0
            other = 0
            sales_analytics = 0
            sales_leadership = 0
            sales =0
            sales_leader =0
            bi_leader = 0
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
                updated_row  = self.segment(updated_row9)

                count +=1
                if count % 10000==0:
                    print count
                if updated_row['Segment']=='Other':
                    other +=1
                if updated_row['Segment']=='Sales Analytics/Enablement':
                    sales_analytics +=1
                if updated_row['Segment']=='Sales Leadership':
                    sales_leadership +=1
                #print updated_row
                if updated_row['Sales Title'] == True:
                    sales +=1
                if updated_row['Sales Title'] == True and updated_row['Title Group'] in ["Vice President", "Chief", "Director"]:
                    sales_leader+=1
                if updated_row['BI Title'] == True and updated_row['Title Group'] in ["Vice President", "Chief", "Director"]:
                    bi_leader +=1
                lead_list.append(updated_row)
        print "other"
        print other
        print "sales analytics"
        print sales_analytics
        print "sales_leadership"
        print sales_leadership
        print "total"
        print count
        print "sales"
        print sales
        print "sales_leader"
        print sales_leader
        print "bi leader"
        print bi_leader

    def segment(self, row):
        updated_row = row
        row['Segment'] = None
        job_title = row['Job Title'].lower()
        job_title_same_case = row['Job Title']

        director_title = 0
        if row['Title Group'] in ["Vice President", "Chief", "Director"]:
           director_title = 1


        if director_title == 1 and row['Operations Title'] == True and (row['Sales Title'] == True or row['Marketing Title'] == True or 'business' in job_title):
            row['Segment'] = "Sales Analytics/Enablement"
        elif director_title == 1 and row['Sales Title'] == True and 'enable' in job_title:
            row['Segment'] = "Sales Analytics/Enablement"
        elif director_title == 1 and row['Sales Title'] == True and row['Analytics Title'] == True:
            row['Segment'] = "Sales Analytics/Enablement"
        elif director_title == 1 and (('customer' in job_title or 'market' in job_title or 'sale' in job_title or 'consumer' in job_title or 'shopper' in job_title) and "insight" in job_title):
            row['Segment'] = "Sales Analytics/Enablement"

        elif director_title == 1 and (updated_row['Sales Title'] == True or updated_row['Sales Title'] =='1'):
            row['Segment'] = "Sales Leadership"
        elif job_title == 'cro' or 'CRO' in job_title_same_case:
            row['Segment'] = "Sales Leadership"
        elif job_title == 'cso' or 'CSO' in job_title_same_case and 'CIO' not in job_title_same_case:
            row['Segment'] = "Sales Leadership"
        elif "managing director" in job_title:
            row['Segment'] = "Sales Leadership"
        elif director_title == 1 and "alliance" in job_title:
            row['Segment'] = "Sales Leadership"
        elif director_title == 1 and "partner" in job_title and 'CEO' not in job_title_same_case and 'supply chain' not in job_title and 'partners gp' not in job_title:
            row['Segment'] = "Sales Leadership"
        elif director_title == 1 and "channel" in job_title :
            row['Segment'] = "Sales Leadership"

        else:
            row['Segment'] = "Other"

        #if row['Segment'] == "Sales Leadership":
        #    print job_title
        return row


segment_enblmnt_ldrshp('C:/Users/wkuffel/Desktop/Marketing Data/20150311 Marketing Database/20150311 Marketing List.csv','')