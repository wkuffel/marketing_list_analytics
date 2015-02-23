__author__ = 'wkuffel'
def label_consultant( row, title = 'Job Title'):
    row['Consultant'] = ''
    job_title_string = row[title].lower().strip()
    job_title_string_same_case =  row[title].strip()
    #is in sales
    if 'consultant' in job_title_string:
        row['Consultant'] = True
    else:
       row['Consultant'] = False

    return row