__author__ = 'wkuffel'


def label_sales_buyer( row, title = 'Job Title'):
    row['Sales Title'] = ''
    job_title_string = row[title].lower().strip()
    job_title_string_same_case =  row[title].strip()

    if 'sales' in job_title_string:
        row['Sales Title'] = True
    elif 'channel' in job_title_string:
        row['Sales Title'] = True
    elif 'field operations' in job_title_string:
        row['Sales Title'] = True
    elif 'strategic accounts' in job_title_string:
        row['Sales Title'] = True
    elif 'business development' in job_title_string:
        row['Sales Title'] = True
    elif 'area' in job_title_string:
        row['Sales Title'] = True
    elif 'region' in job_title_string:
        row['Sales Title'] = True
    elif 'account executive' in job_title_string:
        row['Sales Title'] = True
    elif 'field' in job_title_string:
        row['Sales Title'] = True
    elif 'development' in job_title_string and 'product' not in job_title_string:
        row['Sales Title'] = True
    elif 'cro' == job_title_string:
        row['Sales Title'] = True
    elif 'revenue' in job_title_string:
        row['Sales Title'] = True
    elif 'partner' in job_title_string:
        row['Sales Title'] = True
    elif 'managing director' in job_title_string:
        row['Sales Title'] = True
    #not in sales
    else:
       row['Sales Title'] = False

    return row