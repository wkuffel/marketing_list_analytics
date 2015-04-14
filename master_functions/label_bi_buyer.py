__author__ = 'wkuffel'

def label_bi_buyer(row, title = 'Job Title'):
    row['BI Title'] = ''
    job_title_string = row[title].lower().strip()
    job_title_string_same_case =  row[title].strip()
    #is in BI
    if 'BI' in job_title_string_same_case: #BI
        row['BI Title'] = True
    elif 'business intelligence' in job_title_string: #BI
        row['BI Title'] = True
    elif 'analytics' in job_title_string: #analytics
        row['BI Title'] = True
    elif 'data' in job_title_string: #analytics
        row['BI Title'] = True
    elif 'cloud' in job_title_string: #IT, number of counts
        row['BI Title'] = True
    elif 'cdo' == job_title_string: #
        row['BI Title'] = True
    elif 'cio' == job_title_string:
        row['BI Title'] = True
    elif 'information' in job_title_string:
        row['BI Title'] = True
    elif 'info ' in job_title_string:
        row['BI Title'] = True
    elif 'IT' in job_title_string_same_case:#
        row['BI Title'] = True
    elif 'technology' in job_title_string:
        row['BI Title'] = True
    elif 'architect' in job_title_string:
        row['BI Title'] = True
    elif 'bi ' in job_title_string: #same with BI
        row['BI Title'] = True
    elif 'reporting' in job_title_string: #same with BI
        row['BI Title'] = True
    elif 'business system' in job_title_string: #same with BI
        row['BI Title'] = True
    elif 'CIO' in job_title_string_same_case: #same with BI
        row['BI Title'] = True
    elif 'CTO ' in job_title_string_same_case or ' CTO' in job_title_string_same_case or job_title_string_same_case =='CTO': #same with BI
        row['BI Title'] = True
    elif 'ETL' in job_title_string_same_case:
        row['BI Title'] = True
    elif 'HIM' in job_title_string_same_case:
        row['BI Title'] = True
    elif ' IS ' in job_title_string_same_case or 'IS '== job_title_string_same_case[:3] or ' is'== job_title_string[-3:] or job_title_string == 'is':
        row['BI Title'] = True
    elif ' MIS ' in job_title_string_same_case or 'MIS '== job_title_string_same_case[:4] or ' MIS'== job_title_string[-4:]:
        row['BI Title'] = True
    elif ' HIM ' in job_title_string_same_case or 'HIM '== job_title_string_same_case[:4] or ' HIM'== job_title_string[-4:]:
        row['BI Title'] = True
    elif 'business analyst' in job_title_string and (row['Operations Title'] == False and row['OEM Title'] == False and row['Marketing Title'] == False and row['Sales Title'] == False and row['Operations Title'] == False):
        row['BI Title'] = True
    elif 'it' == job_title_string:
        row['BI Title'] = True
    elif ' cto' == job_title_string[-4:] or 'cto '== job_title_string[:4]:
        row['BI Title'] = True
    elif 'business intellig' == job_title_string:
        row['BI Title'] = True
    elif ' it ' in job_title_string:
        row['BI Title'] = True
    #not in sales
    else:
       row['BI Title'] = False
    if row['BI Title'] == True:
        pass
        #print job_title_string
    return row