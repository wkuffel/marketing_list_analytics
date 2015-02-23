__author__ = 'wkuffel'

def label_embedded_buyer( row, title = 'Job Title'):
    row['OEM Title'] = ''
    job_title_string = row[title].lower().strip()
    job_title_string_same_case =  row[title].strip()
    #is in sales
    if 'engineer' in job_title_string:
        row['OEM Title'] = True
    elif 'product' in job_title_string:
        row['OEM Title'] = True
    elif 'strateg' in job_title_string:
        row['OEM Title'] = True
    elif 'application' in job_title_string:
        row['OEM Title'] = True
    elif 'r&d' in job_title_string:
        row['OEM Title'] = True
    elif 'cto' == job_title_string:
        row['OEM Title'] = True
    elif 'ceo' == job_title_string:
        row['OEM Title'] = True
    elif 'technology' in job_title_string:
        row['OEM Title'] = True
    elif 'developer' in job_title_string:
        row['OEM Title'] = True
    #not in sales
    else:
       row['OEM Title'] = False


    if row['OEM Title'] == True:
        pass
        #print job_title_string
    return row