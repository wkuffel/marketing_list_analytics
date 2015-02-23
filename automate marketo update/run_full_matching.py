__author__ = 'wkuffel'
from lead_account_matching_strict_parents import match_leads_to_accounts
from process_unranked_list import lead_list

class runFullMatch(object):

    def __init__(self, filedate_str):
        self.filedate_str = filedate_str
        self.infile_path_lead = 'C:/Users/wkuffel/Desktop/update unranked/'+self.filedate_str+'/'+self.filedate_str+' unranked.csv'
        self.outfile_path_lead = 'C:/Users/wkuffel/Desktop/update unranked/'+self.filedate_str+'/'+self.filedate_str+' unranked processed.csv'
        self.account_file = 'C:/Users/wkuffel/Desktop/update unranked/Target accounts/enterprise processed.csv'
        self.final_outfile = 'C:/Users/wkuffel/Desktop/update unranked/'+self.filedate_str+'/'+self.filedate_str+' unranked to load.csv'
        #self.infile_path_lead = 'C:/Users/wkuffel/Desktop/Marketing Data/20150218 webinar attendence/attendee list.csv'
        #self.outfile_path_lead = 'C:/Users/wkuffel/Desktop/Marketing Data/20150218 webinar attendence/attendee list processed.csv'
        #self.final_outfile = 'C:/Users/wkuffel/Desktop/Marketing Data/20150218 webinar attendence/attendee list matched.csv'
        
        lead_list(self.infile_path_lead, self.outfile_path_lead)
        match_leads_to_accounts(self.outfile_path_lead, self.account_file, self.final_outfile, marketo_upload=True)




input = 'C:/Users/wkuffel/Desktop/update unranked/20150206/20150206 unranked.csv'
output = 'C:/Users/wkuffel/Desktop/update unranked/20150206/20150206 unranked processed.csv'

runFullMatch("20150223")