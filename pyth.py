from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '36',
    'limit': '1',


}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '1cf44eba-c918-46f5-8db5-4e1b3b6774f4',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    json_string = json.dumps(data['data'])

    print(json_string)
    print("hello")
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

