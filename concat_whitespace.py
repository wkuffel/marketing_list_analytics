__author__ = 'wkuffel'

import csv

class concatWhiteSpace(object):
    def __init__(self, inpath, outpath):
        self.inpath = inpath
        self.outpath =outpath
        self.write_fields = [ 'Account ID', 'Account Name', 'Account Owner', 'Account Status', 'Account Type', 'Analytics Title', 'Annual Company Revenue Range', 'Annual Company Revenue Range (A)', 'BI Title', 'City', 'Clean Company Name', 'Clean Company Name1', 'Common Organization Name', 'Company Employee Range', 'Company Industries', 'Company Name', 'Country', 'County', 'Decision Maker', 'Email Address', 'E-Mail', 'Employees', 'Facebook Profile', 'First Name', 'Full Name', 'HQ Country', 'HQ State', 'HQ Zip', 'Id', 'Industry', 'InsideView Account ID', 'InsideView Account ID Account', 'is_child', 'is_parent', 'Job Title', 'Job Function', 'Job Level', 'Last Name', 'Lead Rank', 'LinkedIn Profile', 'Lead Score', 'Lead Source', 'Lead Status', 'Marketing Title', 'Matched', 'Matched Parent Account ID', 'OEM Title', 'Operations Title', 'Organization', 'Parent Account', 'Parent Account ID', 'Phone Number', 'PersonID', 'Phone 1', 'Phone 2', 'Postal', 'Region', 'Revenue', 'Sales Team', 'Sales Title', 'SFDC Type', 'SIC Code', 'SIC Description', 'State', 'Street', 'Title', 'Title Group', 'Total Open Opportunities', 'Total Opportunities', 'Total Won Opportunities', 'Total Won Opportunity Value', 'Updated At', 'Twitter Profile', 'Website', 'Industries']
        self.import_csv()
        self.export_csv()


    def import_csv(self):
        with open(self.inpath) as f:
            reader = csv.DictReader(f)
            self.acct_list = []
            for row in reader:
                if row['Title Group'] != "":
                    row["Job Level"] = row['Title Group']
                if row['Job Level'] != "":
                    row["Title Group"] = row['Job Level']
                self.acct_list.append(row)


    def export_csv(self):
        with open(self.outpath, 'w') as write_csv:
            writer = csv.DictWriter(write_csv, fieldnames=self.write_fields, lineterminator = '\n')
            writer.writeheader()
            count =0
            for row in self.acct_list:
                writer.writerow(row)

concatWhiteSpace('C:/Users/wkuffel/Desktop/Marketing Data/20150226 marketing list analysis/written.csv' , 'C:/Users/wkuffel/Desktop/Marketing Data/20150226 marketing list analysis/written2.csv' )