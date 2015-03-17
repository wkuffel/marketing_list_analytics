__author__ = 'wkuffel'


def label_tech_product( row, title = 'Job Title'):
    row['Tech Product'] = False
    job_title_string = row[title].lower().strip()
    job_title_string_same_case =  row[title].strip()
    #is in sales
    if 'product' in job_title_string and 'sales' not in job_title_string:
        row['Tech Product'] = True
    elif 'technology' in job_title_string and 'sales' not in job_title_string and 'information' not in job_title_string:
        row['Tech Product'] = True
    elif 'strategy'  in job_title_string:
        row['Tech Product'] = True
    elif job_title_string in ['cpo', 'cto']:
        row['Tech Product'] = True


    #not in sales
    else:
       row['Tech Product'] = False

    for chief_title in ['CPO', 'CTO',  'Cto', 'Cpo']:
        if (chief_title+' ' in job_title_string_same_case or  ' '+chief_title in job_title_string_same_case or chief_title  == job_title_string_same_case)and "assis" not in job_title_string:
            row['Tech Product'] = True

    if row['Tech Product'] == True:
        pass
        #print job_title_string
    return row