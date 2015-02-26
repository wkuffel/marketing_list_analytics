__author__ = 'wkuffel'

import csv
from master_functions.oem_search import oem_search

class insideViewAccts(object):
    """Imports the insideView account data so it can find accts
    that could be embedded targets
    """

    def __init__(self, infile, outfile):
        """ Initialize the object, call infile, manipulate and outfile commands"""
        self.acct_infile = infile
        self.outfile = outfile
        self.write_fields = ['OEM Account',
                            'Insideview ID',
                            'Account Name',
                            'Annual Company Revenue Range',
                            'Industry',
                            'IV_Industry (sub)',
                            'Description',

                            'City','State',  'Country', 'Ticker Symbol', 'Parent ID', 'Parent Name', 'Ultimate Parent ID','NAICS',
                             'EFX ID', 'Annual Revenue','Website', 'Fax',
                             'FYE', 'Company Status', 'Phone',  'Ownership', 'Address',
                            'Segment', 'Ultimate Parent Name', 'Employees', 'SIC (US)', 'Postal Code',
                            'SFDC Dupe',  'Region',  'Company Employee Range', 'OEM Account Match Method']
        self.read_csv()
        self.manipulated_oem()
        self.write_csv()

    def read_csv(self):
        """Read the CSV to python"""
        self.acct_list = []
        with open(self.acct_infile) as f:
            acct_reader = csv.DictReader(f)
            for row in acct_reader:
                try:
                    del row['']
                except:
                    pass
                self.acct_list.append(row)

    def manipulated_oem(self):
        self.processed_accts = []
        for account_row in self.acct_list:
            updated_row = oem_search(account_row)
            self.processed_accts.append(updated_row)

    def write_csv(self):
        with open(self.outfile, 'w') as write_csv:
            writer = csv.DictWriter(write_csv, fieldnames=self.write_fields , lineterminator = '\n')
            writer.writeheader()
            for row in self.processed_accts:
                writer.writerow(row)




insideViewAccts('C:/Users/wkuffel/Desktop/Marketing Data/OEM labeling/insideview acct data.csv', 'C:/Users/wkuffel/Desktop/Marketing Data/OEM labeling/insideview acct manipulated.csv')