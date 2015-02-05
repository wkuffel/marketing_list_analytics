__author__ = 'wkuffel'

"""
import suds_marketo
print dir(suds_marketo)

client = suds_marketo.Client(soap_endpoint='https://299-OVS-376.mktoapi.com',
                        user_id='birst1_7027134750887544EFB6D5',
                        encryption_key='99885325486705325500888877554456EEFFCD30201')


#print client.getMultipleLeads.__module__
#client.get_lead('rama.achanti@xerox.com')
#client.ParamsGetMultipleLeads.lastUpdatedAt = "2015-02-02T08:15:30-05:00"
#client.getMultipleLeads()

lead_key = client.LeadKey # You need to create the proper object to pass to the function
lead_key.keyType = client.LeadKeyRef.EMAIL
lead_key.keyValue = 'rama.achanti@xerox.com'
resp = client.call_service('getLead', lead_key)

"""
import hmac
import hashlib
import datetime
import time
from suds.client import Client

def _utc_offset(date, use_system_timezone):
    if isinstance(date, datetime.datetime) and date.tzinfo is not None:
        return _timedelta_to_seconds(date.dst() or date.utcoffset())
    elif use_system_timezone:
        if date.year < 1970:
            # We use 1972 because 1970 doesn't have a leap day (feb 29)
            t = time.mktime(date.replace(year=1972).timetuple())
        else:
            t = time.mktime(date.timetuple())
        if time.localtime(t).tm_isdst: # pragma: no cover
            return -time.altzone
        else:
            return -time.timezone
    else:
        return 0

def rfc3339(date, utc=False, use_system_timezone=True):
    # Try to convert timestamp to datetime
    try:
        if use_system_timezone:
            date = datetime.datetime.fromtimestamp(date)
        else:
            date = datetime.datetime.utcfromtimestamp(date)
    except TypeError:
        pass

    if not isinstance(date, datetime.date):
        raise TypeError('Expected timestamp or date object. Got %r.' %
                        type(date))

    if not isinstance(date, datetime.datetime):
        date = datetime.datetime(*date.timetuple()[:3])
    utc_offset = _utc_offset(date, use_system_timezone)
    if utc:
        return _string(date + datetime.timedelta(seconds=utc_offset), 'Z')
    else:
        return _string(date, _timezone(utc_offset))

def _string(d, timezone):
    return ('%04d-%02d-%02dT%02d:%02d:%02d%s' %
            (d.year, d.month, d.day, d.hour, d.minute, d.second, timezone))

def sign(message, encryption_key):
    digest = hmac.new(encryption_key, message, hashlib.sha1)
    return digest.hexdigest().lower()

def set_header(client, user_id, encryption_key):
    h = client.factory.create('AuthenticationHeaderInfo')
    h.mktowsUserId = user_id
    h.requestTimestamp = rfc3339(datetime.datetime.now())
    h.requestSignature = sign(h.requestTimestamp + user_id, encryption_key)
    client.set_options(soapheaders=h)

url = 'https://299-OVS-376.mktoapi.com/soap/mktows/2_7'
client = Client(url)

"""
set_header(client, 'birst1_7027134750887544EFB6D5', '99885325486705325500888877554456EEFFCD30201')

leadKey = client.factory.create('LeadKey')
leadKeyRef = client.factory.create('LeadKeyRef')

leadKey.keyType = leadKeyRef.EMAIL
leadKey.keyValue = 'rama.achanti@xerox.com'

print client.service.getLead(leadKey=leadKey)
"""