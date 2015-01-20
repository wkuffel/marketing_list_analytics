__author__ = 'wkuffel'

from lead_list_processing2 import lead_list
from account_list_processing import account_list
from target_coverage import target_coverage

class produce_update_list(object):
    def __init__(self, filedate_str):
        self.filedate_str= filedate_str

        #Generate New Lead List
        self.lead_filepath = 'C:/Users/wkuffel/Desktop/Marketing Data/'+self.filedate_str+' marketo update/input files/all Birst leads '+ self.filedate_str+ '.csv'
        self.lead_out_filepath = 'C:/Users/wkuffel/Desktop/Marketing Data/'+self.filedate_str+' marketo update/output files/all Birst leads '+ self.filedate_str+ ' manipulated.csv'
        lead_list(self.lead_filepath, self.lead_out_filepath)
        print "lead list completed"

        #Generate New Target Accounts
        self.target_account_filepath = 'C:/Users/wkuffel/Desktop/Marketing Data/'+self.filedate_str+' marketo update/input files/target account list '+self.filedate_str +'.csv'
        self.target_account_out_filepath = 'C:/Users/wkuffel/Desktop/Marketing Data/'+self.filedate_str+' marketo update/output files/target account list '+self.filedate_str +' manipulated.csv'
        account_list(self.target_account_filepath,self.target_account_out_filepath)
        print "target list completed"

        #Match the two files, put in Marketo format
        self.converged_filepath = 'C:/Users/wkuffel/Desktop/Marketing Data/'+self.filedate_str+' marketo update/result/converged leads targets '+self.filedate_str +'.csv'
        target_coverage(self.target_account_out_filepath,self.lead_out_filepath,self.converged_filepath, for_marketo = True)


produce_update_list('20150119')   