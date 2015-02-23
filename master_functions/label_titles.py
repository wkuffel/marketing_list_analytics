__author__ = 'wkuffel'

def label_decision_maker(row, title = 'Job Title'):
    row['Decision Maker'] = ''
    job_title_string = row[title].lower().strip()
    job_title_string_same_case =  row[title].strip()

    #yes, is decision maker
    if 'chief' in job_title_string:
        row['Decision Maker'] = True
    elif 'director' in job_title_string:
        row['Decision Maker'] = True
    elif 'evp' in job_title_string:
        row['Decision Maker'] = True
    elif 'vice president' in job_title_string:
        row['Decision Maker'] = True
    elif 'vp' in job_title_string:
        row['Decision Maker'] = True
    elif 'head' in job_title_string:
        row['Decision Maker'] = True
    elif 'president' in job_title_string:
        row['Decision Maker'] = True
    elif 'lead' in job_title_string:
        row['Decision Maker'] = True
    elif 'executive' in job_title_string and "account" not in job_title_string:
        row['Decision Maker'] = True
    elif 'owner' in job_title_string:
        row['Decision Maker'] = True
    elif 'general manager' in job_title_string:
        row['Decision Maker'] = True
    elif job_title_string in ['ceo', 'cfo', 'coo', 'cio', 'cto', 'vp', 'cmo', 'cdo']:
        row['Decision Maker'] = True
    elif len(job_title_string)>3 and  job_title_string[:4] == 'dir ':
        row['Decision Maker'] = True
    elif job_title_string == 'dir':
        row['Decision Maker'] = True
    elif "architect" in job_title_string and 'enterprise' in job_title_string:
        row['Decision Maker'] = True
    else:
        row['Decision Maker'] = False

    for chief_title in ['CEO', 'CFO', 'COO', 'CIO', 'CTO', 'CMO', 'CDO', 'Ceo', 'Cfo', 'Coo', 'Cio', 'Cto', 'Cmo', 'Cdo']:
        if chief_title in job_title_string_same_case and "assis" not in job_title_string:
            row['Decision Maker'] = True

    return row

def label_title(row, title = 'Job Title'):
    row['Title Group'] = ''
    job_title_string = row[title].lower().strip()
    job_title_string_same_case =  row[title].strip()

    #yes, is decision maker
    if 'chief' in job_title_string:
        row['Title Group'] = 'Chief'
    elif 'director' in job_title_string:
        row['Title Group'] = 'Director'
    elif 'evp' in job_title_string:
        row['Title Group'] = 'Vice President'
    elif 'vice president' in job_title_string:
        row['Title Group'] = 'Vice President'
    elif 'vp' in job_title_string:
        row['Title Group'] = 'Vice President'
    elif 'head' in job_title_string:
        row['Title Group'] = 'Director'
    elif 'president' in job_title_string:
        row['Title Group'] = 'Chief'
    elif 'lead' in job_title_string:
        row['Title Group'] = 'Director'
    elif 'executive' in job_title_string and "account" not in job_title_string:
        row['Title Group'] = 'Chief'
    elif 'owner' in job_title_string:
        row['Title Group'] = 'Chief'
    elif 'general manager' in job_title_string:
        row['Title Group'] = 'Director'
    elif job_title_string in ['ceo', 'cfo', 'coo', 'cio', 'cto', 'cmo', 'cdo']:
        row['Title Group'] = 'Chief'
    elif len(job_title_string)>3 and  job_title_string[:4] == 'dir ':
        row['Title Group'] = 'Director'
    elif job_title_string == 'dir':
        row['Title Group'] = 'Director'
    elif "architect" in job_title_string and 'enterprise' in job_title_string:
        row['Title Group'] = 'Director'

    else:
        row['Title Group'] = 'Below Director'

    for chief_title in ['CEO', 'CFO', 'COO', 'CIO', 'CTO', 'CMO', 'CDO', 'Ceo', 'Cfo', 'Coo', 'Cio', 'Cto', 'Cmo', 'Cdo']:
        if chief_title in job_title_string_same_case and "assis" not in job_title_string:
            row['Title Group'] = 'Chief'

    return row
