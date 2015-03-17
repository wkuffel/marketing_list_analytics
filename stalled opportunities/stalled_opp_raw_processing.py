__author__ = 'wkuffel'

import csv


class stalledOpportunityProcess(object):
    "process the merged stalled opportunity data to get competitor and data source info"

    def __init__(self, in_path, out_path):
        self.in_path = in_path
        self.out_path = out_path
        self.import_dataset()

    def import_dataset(self):
        acct_list = []
        with open(self.in_path) as f:
            reader = csv.DictReader(f)
            self.data_sources = []
            self.competitors = []
            for row in reader:
                competitor_list = row['Competitors'].split(';')
                data_source_list = row['Data Sources'].split(';')
                for item in competitor_list:
                    if item not in self.competitors:
                        self.competitors.append(item)

                for item in data_source_list:
                    if item not in self.data_sources:
                        self.data_sources.append(item)
            self.data_sources.remove(''). remove('None').remove('Unknown')
            self.competitors.remove('')

            new_data = []

            for row in reader:
                for item in self.data_sources:
                    if item in row['Data Sources'].split(';'):
                        row['Source_'+item] = 1
                    else:
                        row['Source_'+item] = 0
                for item in self.competitors:
                    if item in row['Competitors'].split(';'):
                        row['Competitor_'+item] = 1
                    else:
                        row['Competitor_'+item] = 0
                new_data.append(row)



    def split_data_sources(self, row):
        data_source_list = row['Data Sources'].split(';')

        row['Source_Excel'] = 0
        if 'Excel' in data_source_list:
            row['Source_Excel'] = 1

        row['Source_MySQL'] = 0
        if 'MySQL' in data_source_list:
            row['Source_MySQL'] = 1

        row['Source_Salesforce.com'] = 0
        if 'Salesforce.com' in data_source_list:
            row['Source_Salesforce.com'] = 1

        row['Source_Oracle'] = 0
        if 'Oracle' in data_source_list or 'Oracle DB' in data_source_list:
            row['Source_Oracle'] = 1

        row['Source_Hadoop'] = 0
        if 'Hadoop' in data_source_list:
            row['Source_Hadoop'] = 1

        row['Source_Microsoft SQL Server'] = 0
        if 'Microsoft SQL Server' in data_source_list:
            row['Source_Microsoft SQL Server'] = 1

        row['Source_Other'] = 0
        if 'Other' in data_source_list:
            row['Source_Other'] = 1




        for competitor in ['Other','Microsoft SQL Server','Oracle DB', 'Excel', 'MySQL','Salesforce.com','Oracle','Hadoop']:
            if competitor in data_source_list:
                data_source_list.remove(competitor)
        if data_source_list != [] and data_source_list != ['']:
            print data_source_list


infile = 'C:/Users/wkuffel/Desktop/Marketing Data/Stalled Opportunities/Stalled Opportunity Data to process.csv'
outfile = 'C:/Users/wkuffel/Desktop/Marketing Data/Stalled Opportunities/Stalled Opportunity Data processed.csv'

stalledOpportunityProcess(infile, outfile)