__author__ = 'wkuffel'


def label_marketing_buyer( row, title = 'Job Title'):
    row['Marketing Title'] = ''
    job_title_string = row[title].lower().strip()
    job_title_string_same_case =  row[title].strip()

    #is in sales
    if 'marketing' in job_title_string:
        row['Marketing Title'] = True
    elif 'demand generation' in job_title_string:
        row['Marketing Title'] = True
    elif 'digital' in job_title_string:
        row['Marketing Title'] = True
    elif 'online' in job_title_string:
        row['Marketing Title'] = True
    elif 'advertising' in job_title_string:
        row['Marketing Title'] = True
    elif 'media' in job_title_string:
        row['Marketing Title'] = True
    elif 'consumer programs' in job_title_string:
        row['Marketing Title'] = True
    elif 'commerce' in job_title_string:
        row['Marketing Title'] = True
    elif 'campaign' in job_title_string: #
        row['Marketing Title'] = True
    elif 'consumer' in job_title_string: #
        row['Marketing Title'] = True
    elif 'strateg' in job_title_string and "IT" not in job_title_string_same_case: #covers stategy and stragegic
        row['Marketing Title'] = True
    elif 'product' in job_title_string: #covers stategy and stragegic
        row['Marketing Title'] = True
    elif 'creative' in job_title_string:
        row['Marketing Title'] = True
    elif 'CMO' in job_title_string_same_case:
        row['Marketing Title'] = True
    elif 'cmo' == job_title_string:
        row['Marketing Title'] = True
    elif 'cmo ' in job_title_string:
        row['Marketing Title'] = True
    elif 'communication' in job_title_string:
        row['Marketing Title'] = True
    elif 'brand' in job_title_string:
        row['Marketing Title'] = True
    elif 'br&' in job_title_string:
        row['Marketing Title'] = True
    elif 'merchandising' in job_title_string:
        row['Marketing Title'] = True
    elif 'mktg' in job_title_string:
        row['Marketing Title'] = True
    elif 'public relations' in job_title_string:
        row['Marketing Title'] = True
    elif 'PR' in job_title_string_same_case:
        row['Marketing Title'] = True
    elif ' pr ' in job_title_string:
        row['Marketing Title'] = True
    elif 'consumer insight' in job_title_string:
        row['Marketing Title'] = True
    elif 'customer insight' in job_title_string:
        row['Marketing Title'] = True
    #not in marketing
    else:
       row['Marketing Title'] = False

    if row['Marketing Title'] == True:
        pass
        #print job_title_string
    return row