__author__ = 'wkuffel'

import csv
import pickle

class combineEmbeddedEnterprise(object):
    "bring together Embedded and Enterprise accounts for matching overall"

    def __init__(self, emb_file, emb_pickle, enterprise_file, enterprise_pickle, out_file, out_pickle):
        self.emb_file=emb_file
        self.emb_pickle=emb_pickle
        self.enterprise_file=enterprise_file
        self.enterprise_pickle=enterprise_pickle
        self.out_file=out_file
        self.out_pickle=out_pickle
        self.writing_field_names_ordered = ['Account ID', 'Account Name', 'InsideView Account ID','Embedded Target', 'Account Status', 'Total Opportunities', 'Sales Team', 'Account Owner', 'Region', 'HQ Country', 'HQ State', 'HQ Zip', 'Total Won Opportunities', 'Total Won Opportunity Value', 'Total Open Opportunities',  'Industry', 'Company Employee Range', 'Annual Company Revenue Range',  'Parent Account ID', 'Parent Account','Account Type', 'is_parent', 'is_child', 'Clean Company Name', 'Billing State/Province', 'Last Modified Date', 'Last Activity']

        self.enterprise_accts=self.import_file(self.enterprise_file)
        self.embedded_accts = self.import_file(self.emb_file)

        self.enterprise_parent_dict = pickle.load(open( self.enterprise_pickle, "rb" ) )
        self.emb_parent_dict = pickle.load(open( self.emb_pickle, "rb" ) )

        self.combine_parent_dicts()

        self.combine_files()

        self.write_csv()




    def import_file(self, filepath):
        with open(filepath) as f:
            reader = csv.DictReader(f)
            acct_list = []
            for row in reader:
                acct_list.append(row)
            return acct_list

    def combine_files(self):
        acct_id_list = []
        self.all_targets = []
        for row_ent in self.enterprise_accts:
            self.all_targets.append(row_ent)
            acct_id_list.append(row_ent['Account ID'])
        print len(self.enterprise_accts)
        print len(self.embedded_accts)
        count = 0
        for row_emb in self.embedded_accts:
            if row_emb['Account ID'] not in acct_id_list:
                self.all_targets.append(row_emb)
            else:
                count +=1
                for i in range(len(self.all_targets)):
                    if self.all_targets[i]['Account ID'] == row_emb['Account ID']:
                        self.all_targets[i]['Embedded Target'] = 1
        print count
        print len(self.all_targets)

    def combine_parent_dicts(self):
        for key in self.emb_parent_dict:
            if key in self.enterprise_parent_dict:
              pass
            else:
                self.enterprise_parent_dict[key] = self.emb_parent_dict[key]
        pickle.dump(self.enterprise_parent_dict , open( self.out_pickle, "wb" ) )


    def write_csv(self):
        with open(self.out_file, 'w') as write_csv:
            writer = csv.DictWriter(write_csv, fieldnames= self.writing_field_names_ordered, lineterminator = '\n')
            writer.writeheader()
            for row in self.all_targets:
                writer.writerow(row)


emb_pickle = 'C:/Users/wkuffel/Desktop/Marketing Data/create account links/embedded_parent_account_dict.p'
enterprise_pickle = 'C:/Users/wkuffel/Desktop/Marketing Data/create account links/parent_account_dict.p'

emb_file = 'C:/Users/wkuffel/Desktop/Marketing Data/create account links/embedded accounts processed.csv'
enterprise_file = 'C:/Users/wkuffel/Desktop/Marketing Data/create account links/enterprise processed.csv'

all_accts_pickle = 'C:/Users/wkuffel/Desktop/Marketing Data/create account links/all_accts_pickle.p'
all_accts_csv = 'C:/Users/wkuffel/Desktop/Marketing Data/create account links/all target accts.csv'


combineEmbeddedEnterprise(emb_file,emb_pickle,enterprise_file,enterprise_pickle,all_accts_csv,all_accts_pickle)
