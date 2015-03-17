__author__ = 'wkuffel'
def split_competitors( row):
    competitor_list = row['Competitors'].split(';')

    row['Competitor_Domo'] = 0
    if 'Domo' in competitor_list:
        row['Competitor_Domo'] = 1

    row['Competitor_Good_Data'] = 0
    if 'Good Data' in competitor_list:
        row['Competitor_Good_Data'] = 1

    row['Competitor_Tableau'] = 0
    if 'Tableau' in competitor_list:
        row['Competitor_Tableau'] = 1

    row['Competitor_LogiAnalytics'] = 0
    if 'LogiAnalytics' in competitor_list:
        row['Competitor_LogiAnalytics'] = 1

    row['Competitor_Qlikview'] = 0
    if 'Qlikview' in competitor_list:
        row['Competitor_Qlikview'] = 1

    row['Competitor_Tibco Sporfire'] = 0
    if 'Tibco Sporfire' in competitor_list:
        row['Competitor_Tibco Sporfire'] = 1

    row['Competitor_Yellowfin'] = 0
    if 'Yellowfin' in competitor_list:
        row['Competitor_Yellowfin'] = 1

    row['Competitor_IBM Cognos'] = 0
    if 'IBM Cognos' in competitor_list:
        row['Competitor_IBM Cognos'] = 1

    row['Competitor_SAP Business Objects'] = 0
    if 'SAP/ Business Objects' in competitor_list or 'SAP' in competitor_list:
        row['Competitor_SAP Business Objects'] = 1

    row['Competitor_Oracle'] = 0
    if 'Oracle' in competitor_list:
        row['Competitor_Oracle'] = 1

    row['Competitor_Pentaho'] = 0
    if 'Pentaho' in competitor_list:
        row['Competitor_Pentaho'] = 1

    row['Competitor_MicroStrategy'] = 0
    if 'MicroStrategy' in competitor_list or 'MicroStrateg' in competitor_list:
        row['Competitor_MicroStrategy'] = 1

    row['Competitor_JasperSoft'] = 0
    if 'JasperSoft' in competitor_list:
        row['Competitor_JasperSoft'] = 1

    row['Competitor_iDashboard'] = 0
    if 'iDashboard' in competitor_list:
        row['Competitor_iDashboard'] = 1

    row['Competitor_Bime'] = 0
    if 'Bime' in competitor_list:
        row['Competitor_Bime'] = 1

    row['Competitor_Microsoft'] = 0
    if 'Microsoft' in competitor_list:
        row['Competitor_Microsoft'] = 1

    row['Competitor_Information Builders'] = 0
    if 'Information Builders' in competitor_list:
        row['Competitor_Information Builders'] = 1

    row['Competitor_Build vs Buy'] = 0
    if 'Build vs Buy' in competitor_list:
        row['Competitor_Build vs Buy'] = 1

    row['Competitor_Sisense'] = 0
    if 'Sisense' in competitor_list:
        row['Competitor_Sisense'] = 1

    row['Competitor_Actuate'] = 0
    if 'Actuate' in competitor_list:
        row['Competitor_Actuate'] = 1

    row['Competitor_Cloud9'] = 0
    if 'Cloud9' in competitor_list:
        row['Competitor_Cloud9'] = 1

    row['Competitor_Board'] = 0
    if 'Board' in competitor_list:
        row['Competitor_Board'] = 1

    row['Competitor_PivotLink'] = 0
    if 'PivotLink' in competitor_list:
        row['Competitor_PivotLink'] = 1

    row['Competitor_SFDC Analytics'] = 0
    if 'SFDC Analytics' in competitor_list or 'SFDC Wave' in competitor_list:
        row['Competitor_SFDC Analytics'] = 1

    row['Competitor_JReport'] = 0
    if 'JReport' in competitor_list:
        row['Competitor_JReport'] = 1

    row['Competitor_SAS'] = 0
    if 'SAS' in competitor_list:
        row['Competitor_SAS'] = 1

    row['Competitor_Dundas'] = 0
    if 'Dundas' in competitor_list:
        row['Competitor_Dundas'] = 1


    for competitor in ['SAP','Dundas','SAS', 'JReport', 'SFDC Analytics','SFDC Wave', 'PivotLink', 'Board', 'Cloud9', 'MicroStrateg','Sisense','Actuate','Cloud9','Board', 'Domo','Good Data','Tableau','LogiAnalytics','Qlikview','Tibco Sporfire','Yellowfin', 'SAP/ Business Objects','IBM Cognos','Oracle','Pentaho', 'MicroStrategy', 'JasperSoft','iDashboard', 'Bime', 'Microsoft', 'Information Builders', 'Build vs Buy', 'Custom Built Solution', 'None', 'Unknown'  ]:
        if competitor in competitor_list:
            competitor_list.remove(competitor)
    if competitor_list != [] and competitor_list != ['']:
        print competitor_list


    new_row = row
    return new_row