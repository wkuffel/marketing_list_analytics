__author__ = 'wkuffel'

def unique_buyer_type(row, buyer_type_string ):
    row["Buyer Type"] = ""

    if buyer_type_string == "Sales":

        if row['Sales Title']:
            row["Buyer Type"] = "Sales Buyer"
        elif row['BI Title']:
            row["Buyer Type"] = "BI/IT Buyer"
        elif row['Marketing Title']:
            row["Buyer Type"] = "Marketing Buyer"
        elif row['OEM Title']:
            row["Buyer Type"] = "Embedded Buyer"
        elif row['Operations Title']:
            row["Buyer Type"] = "Operations Buyer"
        else:
           row["Buyer Type"] = "Other Buyer"

    elif buyer_type_string == "Marketing":

        if row['Marketing Title']:
            row["Buyer Type"] = "Marketing Buyer"
        elif row['BI Title']:
            row["Buyer Type"] = "BI/IT Buyer"
        elif row['Sales Title']:
            row["Buyer Type"] = "Sales Buyer"
        elif row['OEM Title']:
            row["Buyer Type"] = "Embedded Buyer"
        elif row['Operations Title']:
            row["Buyer Type"] = "Operations Buyer"
        else:
           row["Buyer Type"] = "Other Buyer"

    elif buyer_type_string == "Embedded":

        if row['OEM Title']:
            row["Buyer Type"] = "Embedded Buyer"
        elif row['BI Title']:
            row["Buyer Type"] = "BI/IT Buyer"
        elif row['Marketing Title']:
            row["Buyer Type"] = "Marketing Buyer"
        elif row['Sales Title']:
            row["Buyer Type"] = "Sales Buyer"
        elif row['Operations Title']:
            row["Buyer Type"] = "Operations Buyer"
        else:
           row["Buyer Type"] = "Other Buyer"

    elif buyer_type_string == "Operations":
        if row['Operations Title']:
            row["Buyer Type"] = "Operations Buyer"
        elif row['BI Title']:
            row["Buyer Type"] = "BI/IT Buyer"
        elif row['Marketing Title']:
            row["Buyer Type"] = "Marketing Buyer"
        elif row['Sales Title']:
            row["Buyer Type"] = "Sales Buyer"
        elif row['OEM Title']:
            row["Buyer Type"] = "Embedded Buyer"
        else:
           row["Buyer Type"] = "Other Buyer"

    else:
        if row['BI Title'] :
            row["Buyer Type"] = "BI/IT Buyer"
        elif row['Marketing Title']:
            row["Buyer Type"] = "Marketing Buyer"
        elif row['Sales Title']:
            row["Buyer Type"] = "Sales Buyer"
        elif row['OEM Title']:
            row["Buyer Type"] = "Embedded Buyer"
        elif row['Operations Title']:
            row["Buyer Type"] = "Operations Buyer"
        else:
           row["Buyer Type"] = "Other Buyer"

    return row