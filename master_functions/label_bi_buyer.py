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
    elif 'IT' in job_title_string_same_case:#
        row['BI Title'] = True
    elif 'technology' in job_title_string:
        row['BI Title'] = True
    elif 'architect' in job_title_string:
        row['BI Title'] = True
    elif 'bi ' in job_title_string: #same with BI
        row['BI Title'] = True
    elif 'CIO' in job_title_string_same_case: #same with BI
        row['BI Title'] = True
    #not in sales
    else:
       row['BI Title'] = False
    if row['BI Title'] == True:
        pass
        #print job_title_string
    return row