__author__ = 'wkuffel'

def clean_account_name(account_name):

    account_name = account_name.lower().strip()
    account_name = account_name.replace('.', '')
    account_name = account_name.replace(',', '')
    account_name = account_name.replace('"', '')

    if  account_name[-4:] ==" inc":
        account_name = account_name[:-4]
        #print account_name
    if  account_name[-4:] ==" llc":
        account_name = account_name[:-4]
        #print account_name
    if  account_name[-3:] ==" lp":
        account_name = account_name[:-3]
        #print account_name

    if  account_name[-4:] ==" ltd":
        account_name = account_name[:-4]
        #print account_name
    if  account_name[-4:] ==" plc":
        account_name = account_name[:-4]
        #print account_name
    """
    if  account_name[-14:] ==" international":
        account_name = account_name[:-14]
        #print account_name
    """
    if  account_name[-6:] ==" group":
        account_name = account_name[:-6]
        #print account_name
    """
    if  account_name[-7:] ==" system":
        account_name = account_name[:-7]
        #print account_name
    if  account_name[-8:] ==" systems":
        account_name = account_name[:-8]
        #print account_name
    """

    if  account_name[-3:] ==" sa":
        account_name = account_name[:-3]
        #print account_name
    if  account_name[-4:] ==" llp":
        account_name = account_name[:-4]
        #print account_name
    if  account_name[-5:] ==" corp":
        account_name = account_name[:-5]
        #print account_name
    if  account_name[-3:] ==" co":
        account_name = account_name[:-3]
        #print account_name

    account_name = account_name.replace(' corporation', '')
    account_name = account_name.replace(' corp', '')
    account_name = account_name.replace(' company', '')
    account_name = account_name.replace('the', '')


    account_name = account_name.replace('-', ' ')
    account_name = account_name.replace(' and ', ' & ')
    account_name = account_name.replace(' + ', ' & ')
    account_name = account_name.replace('  ', ' ')
    account_name = account_name.replace("'", '')
    account_name = account_name.strip()

    return account_name

#limited,technologies, operations,