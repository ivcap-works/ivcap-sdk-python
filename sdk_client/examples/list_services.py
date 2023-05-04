import sys, os
sys.path.append(os.path.join(os.getcwd(), '../src'))

from ivcap_client import AuthenticatedClient
from ivcap_client.api.service import service_list
from ivcap_client.models import ServiceListRT
import pprint
pp = pprint.PrettyPrinter(indent=2)

ivcap_url= os.getenv('IVCAP_URL', 'https://api.ivcap.net')
token = os.environ['IVCAP_JWT']
account_id = os.environ['IVCAP_ACCOUNT_ID']
client = AuthenticatedClient(base_url=ivcap_url, token=token)

services: ServiceListRT = service_list.sync(client=client, limit=50)
pp.pprint(list(map(lambda el: el.to_dict(), services.services)))
