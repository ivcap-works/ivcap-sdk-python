import sys, os
sys.path.append(os.path.join(os.getcwd(), '../src'))

from ivcap_client import AuthenticatedClient
from ivcap_client.api.order import order_create, order_read
from ivcap_client.models import OrderRequestT, ParameterT, OrderRequestT, OrderStatusRT
import pprint
pp = pprint.PrettyPrinter(indent=2)

ivcap_url= os.getenv('IVCAP_URL', 'https://api.ivcap.net')
token = os.environ['IVCAP_JWT']
account_id = os.environ['IVCAP_ACCOUNT_ID']
client = AuthenticatedClient(base_url=ivcap_url, token=token)

img_url = 'https://juststickers.in/wp-content/uploads/2016/07/go-programming-language.png'
service_id = 'urn:ivcap:service:85f4586e-af1e-5200-94ba-0be8651740ed'
p = [
    ParameterT(name='msg', value='Hello World'),
    ParameterT(name='img-url', value=img_url)
]
req = OrderRequestT(name='test 1', parameters=p, service_id=service_id , account_id=account_id)
order_resp = order_create.sync_detailed(client=client, json_body=req)
order:OrderStatusRT = order_resp.parsed
if not order:
    raise Exception(f'Order request failed: ${order_resp.status_code}')
pp.pprint(order.to_dict())

order_read.sync_detailed(client=client, id=order.id)

