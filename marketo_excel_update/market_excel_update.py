__author__ = 'wkuffel'

#from lead_list_processing2 import lead_list
#from account_list_processing import account_list
from target_coverage import target_coverage

class produce_update_list(object):
    def __init__(self, filedate_str):
        self.filedate_str= filedate_str

        #Generate New Lead List
        self.lead_filepath = 'C:/Users/wkuffel/Desktop/Marketing Data/'+self.filedate_str+' marketo update/input files/all Birst leads '+ self.filedate_str+ '.csv'
        self.lead_out_filepath = 'C:/Users/wkuffel/Desktop/Marketing Data/all Birst leads 20140122 will manipulated title.csv'

        #'C:/Users/wkuffel/Desktop/Marketing Data/'+self.filedate_str+' marketo update/output files/all Birst leads '+ self.filedate_str+ ' manipulated.csv'

        """
        lead_list(self.lead_filepath, self.lead_out_filepath)
        print "lead list completed"
        """

        """
        #Generate New Target Accounts
        self.target_account_filepath = 'C:/Users/wkuffel/Desktop/Marketing Data/'+self.filedate_str+' marketo update/input files/target account list '+self.filedate_str +'.csv'
        self.target_account_out_filepath = 'C:/Users/wkuffel/Desktop/Marketing Data/'+self.filedate_str+' marketo update/output files/target account list '+self.filedate_str +' manipulated.csv'
        account_list(self.target_account_filepath,self.target_account_out_filepath)
        print "target list completed"
        """
        #EMEA target accounts
        #self.target_account_filepath = 'C:/Users/wkuffel/Desktop/Marketing Data/20150120 allocated accounts/Birst allocated accounts.csv'
        #self.target_account_out_filepath = 'C:/Users/wkuffel/Desktop/Marketing Data/20150120 allocated accounts/Birst allocated accounts manipulated.csv'
        #account_list(self.target_account_filepath,self.target_account_out_filepath)

        #Match the two files, put in Marketo format
        #self.converged_filepath = 'C:/Users/wkuffel/Desktop/Marketing Data/'+self.filedate_str+' marketo update/results/converged leads targets '+self.filedate_str +' EMEA for Marketo.csv'
        #self.converged_filepath = 'C:/Users/wkuffel/Desktop/Marketing Data/20150120 allocated accounts/matched_results for marketo.csv'
        self.target_account_out_filepath = 'C:/Users/wkuffel/Desktop/Marketing Data/20150121 marketo update/target account files/Birst allocated accounts manipulated.csv'
        #self.target_account_out_filepath = 'C:/Users/wkuffel/Desktop/Marketing Data/20150121 marketo update/target account files/EMEA top 30 prospects 2015 manipulated.csv'


        self.lead_out_filepath = 'C:/Users/wkuffel/Desktop/Marketing Data/all Birst leads 20140122 will manipulated title.csv'
        self.converged_filepath = 'C:/Users/wkuffel/Desktop/Marketing Data/20150122 carl request/Birst accounts manipulated Full.csv'

        target_coverage(self.target_account_out_filepath,self.lead_out_filepath,self.converged_filepath, for_marketo = False)


produce_update_list('20150120')