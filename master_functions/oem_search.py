__author__ = 'wkuffel'

def oem_search(row, relevant_key = 'Description'):
    """ Take a row from an account dataset and based off substrings
    in a long text field decide if the account is a potential Powered by Birst target
    """

    row['OEM Account Match Method'] = False
    clean_search_term_case = row[relevant_key].replace('-', ' ')
    clean_search_term = row[relevant_key].lower().replace('-', ' ')

    #search for lowercase terms in the description string
    #removed recurring
    lcase_search_list = ['saas', 'software as a service', 'web based', 'business application' ]
    for search_term in lcase_search_list:
        if row['OEM Account Match Method'] == False and search_term in clean_search_term:
            row['OEM Account Match Method'] = search_term

    if row['OEM Account Match Method'] == False and 'cloud' in clean_search_term and "st. cloud" not in clean_search_term and "saint cloud" not in clean_search_term:
        row['OEM Account Match Method'] = 'cloud'

    #search for samecase terms in the description string
    same_case_search_list = [ 'BPM'] # 'CRM', 'ERP',
    for search_term in same_case_search_list:
        if row['OEM Account Match Method'] == False and search_term in clean_search_term_case:
            row['OEM Account Match Method'] = search_term

    #cloud hardware exclusion (use same case as printed)
    hardware_exclude = ['T1', 'VPN', 'fiber', 'Fiber']
    if row['OEM Account Match Method'] == 'cloud':
        for term in hardware_exclude:
            if term in  clean_search_term_case:
                 row['OEM Account Match Method'] = False

    #this is only in the case that something has not been
    if row['OEM Account Match Method'] == False:
        #search by industry
        if row['IV_Industry (sub)']=="Application Service Providers (ASPs)":
            row['OEM Account Match Method'] = 'ASP'
        elif row['IV_Industry (sub)']=='Enterprise Resource Planning Software':
            row['OEM Account Match Method'] = 'ERP'
        elif row['IV_Industry (sub)']=='E-Commerce Software':
            row['OEM Account Match Method'] = 'e-commerce'
        elif row['IV_Industry (sub)']=='Customer Relationship Management':
            row['OEM Account Match Method'] = 'CRM'


        #?Include consulting as limit
        elif 'subscription' in clean_search_term:
            subscription_exclude_list = ['publish', 'magazine', 'newspaper', 'periodical', 'media']
            row['OEM Account Match Method'] = 'subscription'
            for item in subscription_exclude_list:
                if item in clean_search_term:
                    row['OEM Account Match Method'] = False

        #search for samecase terms in the description string
    same_case_search_list = [ 'CRM'] # 'CRM', 'ERP',
    for search_term in same_case_search_list:
        if row['OEM Account Match Method'] == False and search_term in clean_search_term_case:
            row['OEM Account Match Method'] = 'CRM1'

    #for false industries
    false_sub_industries = ['Food Wholesale Distributors',
                                'Application Hosting Services',
                                'Asphalt & Roofing Materials',
                                'Computer Hardware',
                                'Coal Mining',
                                'Chemicals - Commodity',
                                'Broadcasting',
                                'Consumer Electronics',
                                'Electronic Parts & Equipment',
                                'Food Processing',
                                'Greeting Cards',
                                'Optical, Magnetic & Mass Storage',
                                'Peripherals, Computers & Accessories',
                                'Local Exchange Carriers',
                                'Semiconductors',
                                'Telecommunications Equipment',
                                'Wood Window and Door Manufacturing',
                                'Wireless Telecommunications Equipment',
                                'Wireless Telephone Handsets',
                                'Servers & Mainframes',
                                'Semiconductor Equipment & Testing',
                                'Wood Products',
                                'Professional Sports Teams',
                                'Videoconferencing Equipment',
                                'Computer Storage Devices'
                                ]
    if row['OEM Account Match Method'] != False:
        if row['Industry']=="Agriculture, Energy & Utilities":
            row['OEM Account Match Method'] = False
        for sub_industry in false_sub_industries:
            if row['IV_Industry (sub)']==sub_industry:
                row['OEM Account Match Method'] = False


    account_elim = ['Bechtel Plant Machinery',
                    'Talend Inc',
                    'Teradata Corporation',
                    'salesforce.com, inc.'
                    ]
    
    for client in  account_elim:
        if row['Account Name'] == client:
            row['OEM Account Match Method'] = False

    
    if  row['OEM Account Match Method'] != False:
         row['OEM Account'] = True
    else:
        row['OEM Account'] = False
    return row