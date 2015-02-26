__author__ = 'wkuffel'

from lead_account_matching_strict_parents import match_leads_to_accounts
from process_unranked_list import lead_list

class processFileList(object):
    def __init__(self, raw_file, buyer_type):
        self.file_dict = raw_file
        self.buyer_type = buyer_type
        self.account_file = 'C:/Users/wkuffel/Desktop/update unranked/Target accounts/enterprise processed.csv'
        processed_file_path = raw_file[:-4] + ' processed.csv'
        matched_file_path = raw_file[:-4] + ' matched.csv'
        lead_list(raw_file, processed_file_path, buyer_type = self.buyer_type)
        match_leads_to_accounts(processed_file_path, self.account_file, matched_file_path)



raw_file = 'C:/Users/wkuffel/Desktop/Campaign Reporting/BI - IT/20150302 Reporting Week/Gartner 2-tier webinar/_Membership__Campaign_id___6255_.csv'

processFileList(raw_file, 'BI')
