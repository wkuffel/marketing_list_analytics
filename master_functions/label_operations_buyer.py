__author__ = 'wkuffel'

def label_operations_buyer( row, title = 'Job Title'):
        row['Operations Title'] = ''
        job_title_string = row[title].lower().strip()
        job_title_string_same_case =  row[title].strip()
        if 'operat' in job_title_string:
            row['Operations Title'] = True
        elif ' ops ' in job_title_string:
            row['Operations Title'] = True
        elif ' ops' == job_title_string[-4:]:
            row['Operations Title'] = True
        elif 'ops ' == job_title_string[:4]:
            row['Operations Title'] = True
        elif 'HR' == job_title_string_same_case:
            row['Operations Title'] = True
        elif 'human resources' == job_title_string:
            row['Operations Title'] = True
        elif 'inventory' == job_title_string:
            row['Operations Title'] = True
        elif 'supply' == job_title_string:
            row['Operations Title'] = True
        elif 'logistic' == job_title_string:
            row['Operations Title'] = True
        elif 'coo' == job_title_string:
            row['Operations Title'] = True
        elif 'CIO' in job_title_string_same_case:
            row['Operations Title'] = True
        else:
           row['Operations Title'] = False
            #print job_title_string
        return row