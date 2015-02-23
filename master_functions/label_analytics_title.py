__author__ = 'wkuffel'

def label_analytics_buyer(row, title = 'Job Title'):
    row['Analytics Title'] = ''
    job_title_string = row[title].lower().strip()
    job_title_string_same_case =  row[title].strip()
    #is in sales
    if 'analytic' in job_title_string:
        row['Analytics Title'] = True
    elif 'analyst' in job_title_string:
        row['Analytics Title'] = True
    #not in sales
    else:
       row['Analytics Title'] = False

    if row['Analytics Title'] == True:
        pass
        #print job_title_string
    return row