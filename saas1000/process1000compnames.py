__author__ = 'wkuffel'

from master_functions.clean_account_name import clean_account_name
import csv

class processlistCompNames(object):
    def __init__(self, in_path, out_path):
        self.in_path = in_path
        self.out_path = out_path
        self.competitor_list = ['birst',
                                'actuate',
                                'alteryx',
                                'bimeanalytics',
                                'birt-exchange',
                                'businessobjects',
                                'cloud9analytics',
                                'Cognos',
                                'domo',
                                'fmr',
                                'gooddata',
                                'Ibi',
                                'ibm',
                                'Indicee',
                                'jaspersoft',
                                'JInfoNet',
                                'logixml',
                                'microstrategy',
                                'oco-inc',
                                'oracle',
                                'pentaho',
                                'pivotlink',
                                'qliktech',
                                'qlikview',
                                'tableau software',
                                'yellowfinbi',
                                'Edgespring',
                                'sisense',
                                '9Lenses',
                                'sfdc',
                                'salesforce',
                                'salesforce.com',
                                'BECKON',
                                'Agilone',
                                'Origami Logic',
                                'C9',
                                'Cloud9',
                                'tableau']
        self.competitors_fixed = ['sap', 'businessintelligence', 'business intelligence', 'informationbuilders', 'information builders']
        self.write_fields=['Company Name', 'Website', 'City', 'Solution \nArea', 'Ticker Symbol', 'Clean Company Name', 'Business Model', 'Country', 'Region', 'State', 'Montclare SaaS 250 Rank', 'Revenue Range', 'Public / Private',]
        self.import_csv()
        self.write_to_csv()


    def import_csv(self):
        with open(self.in_path) as f:
            reader = csv.DictReader(f)
            acct_list = []
            acct_names = []
            for row in reader:
                row['Clean Company Name'] = clean_account_name(row['Company Name'])
                for competitor_name in self.competitor_list:
                    if competitor_name.lower() in row['Clean Company Name']  or row['Clean Company Name']  in competitor_name.lower():
                        print row['Clean Company Name']
                        continue
                for competitor_name in self.competitors_fixed:
                    if competitor_name.lower() == row['Clean Company Name']:
                        print row['Clean Company Name']
                        continue
                if row['Clean Company Name'] not in acct_names:
                    acct_names.append(row['Clean Company Name'])
                    acct_list.append(row)

            self.acct_list = acct_list

    def write_to_csv(self):
        with open(self.out_path, 'w') as write_csv:
            writer = csv.DictWriter(write_csv, fieldnames=self.write_fields, lineterminator = '\n')
            writer.writeheader()
            for row in self.acct_list:
                #print row.keys()
                writer.writerow(row)
            #print row

processlistCompNames('C:/Users/wkuffel/Desktop/Marketing Data/All OEM/all oem account raw.csv', 'C:/Users/wkuffel/Desktop/Marketing Data/All OEM/all oem account processed.csv')