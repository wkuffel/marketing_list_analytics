__author__ = 'wkuffel'

def label_non_work_email( row, title = 'Email Address'):
    row['Non Work Email'] = ''
    job_title_string = row[title].lower().strip()
    job_title_string_same_case =  row[title].strip()
    #is in sales
    if '@gmail' in job_title_string:
        row['Non Work Email'] = True
    elif '@aol' in job_title_string:
        row['Non Work Email'] = True
    elif '@yahoo' in job_title_string:
        row['Non Work Email'] = True
    elif '@comcast' in job_title_string:
        row['Non Work Email'] = True
    elif '@hotmail' in job_title_string:
        row['Non Work Email'] = True
    elif '@bellsouth' in job_title_string:
        row['Non Work Email'] = True
    else:
       row['Non Work Email'] = False

    return row