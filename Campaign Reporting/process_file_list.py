__author__ = 'wkuffel'
from lead_account_matching_strict_parents import match_leads_to_accounts
from process_unranked_list import lead_list

class processFileList(object):
    def __init__(self, raw_file_list):
        self.file_dict = raw_file_dict
        self.account_file = 'C:/Users/wkuffel/Desktop/update unranked/Target accounts/enterprise processed.csv'
        for raw_file in self.file_dict:
            processed_file_path = raw_file[:-4].replace('Raw Data', 'Processed Data') + ' processed.csv'
            matched_file_path = raw_file[:-4].replace('Raw Data', 'Matched Data') + ' matched.csv'
            lead_list(raw_file, processed_file_path, buyer_type = self.file_dict[raw_file])
            match_leads_to_accounts(processed_file_path, self.account_file, matched_file_path)



raw_file_dict = {
                 'C:/Users/wkuffel/Desktop/Campaign Reporting/BI - IT/20150316 Reporting Week/Raw Data/ES_2015_1_15_Gartner_BI_Gartner_Filled_Out_Form_BI.csv': 'BI',
                 'C:/Users/wkuffel/Desktop/Campaign Reporting/BI - IT/20150316 Reporting Week/Raw Data/Gartner_2_teir_WP_BI_LI_Filled_Out_Form.csv': 'BI',
                 'C:/Users/wkuffel/Desktop/Campaign Reporting/BI - IT/20150316 Reporting Week/Raw Data/Gartner_2_teir_WP_BI_SB_Filled_Out_Form.csv':'BI'
                 }

processFileList(raw_file_dict)


