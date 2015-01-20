__author__ = 'wkuffel'
import marketo
print dir(marketo)


client = marketo.Client(soap_endpoint='https://na-q.marketo.com/soap/mktows/2_0',
                        user_id='bigcorp1_461839624B16E06BA2D663',
                        encryption_key='899756834129871744AAEE88DDCC77CDEEDEC1AAAD66')
lead = client.get_lead(email='ilya@segment.io')
print dir(lead)