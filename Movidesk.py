import requests
import json
import http
import ratelimit as ratelimit
import urllib3.exceptions
from backoff import on_exception, expo
from requests import Response
import clients_data

import requests
import warnings
import urllib3

warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings("ignore", category=UserWarning)

class HelpdeskMovidesk:
    def __init__(self, token_movidesk: str):
        self.token_movidesk = token_movidesk

    def person_validation(self, id_persons) -> requests.status_codes:
        url = f'https://movidesk-api.internal/public/v1/persons?id={id_persons}&token={clients_data.token_movidesk_destin}'

        return requests.get(url=url, verify=False).status_code
    # @ratelimit.limits(calls=29, period=30)
    # @on_exception(expo, ratelimit.exception.RateLimitException, max_tries=10)
    # @on_exception(expo, requests.exceptions.ConnectionError, max_tries=10)
    # @on_exception(expo, requests.exceptions.HTTPError, max_tries=10)
    # @on_exception(expo, urllib3.exceptions.ProtocolError, max_tries=10)
    # @on_exception(expo, http.client.RemoteDisconnected, max_tries=10)
    def get_persons_movidesk(self, id_persons: str) -> requests.status_codes:
        url = f'https://movidesk-api.internal/public/v1/persons?id={id_persons}&token={self.token_movidesk}'

        return requests.get(url=url, verify=False).json()

    def get_persons_all_movidesk(self, top: int, skip: int) -> dict:
        # url = (f'https://movidesk-api.internal/public/v1/persons?token={self.token_movidesk}&$filter=personType eq {clients_data.person_type}&$orderby=id '
        #        f'desc&$top={top}&$skip={skip}')
        url = (
            f'{clients_data.movidesk_url_api}persons?token={self.token_movidesk}&$filter=personType eq {clients_data.person_type}&$orderby=id '
            f'desc&$top={top}&$skip={skip}')
        b = requests.get(url=url, verify=False)

        return [b.json(), b, url]

    def patch_persons_movidesk(self, id_persons: int, data: dict) -> requests.status_codes:
        url = f'https://localhost:4443/public/v1/persons?id={id_persons}&token={self.token_movidesk}'
        headers = {'Content-Type': 'application/json'}
        body_json = json.dumps(data)

        return requests.patch(url=url, data=body_json, headers=headers, verify=False).status_code

    def post_persons_movidesk(self, id_persons: str, data: dict):
        url = f'https://movidesk-api.internal/public/v1/persons?id={id_persons}&token={clients_data.token_movidesk_destin}'
        headers = {'Content-Type': 'application/json'}
        body_json = json.dumps(data)

        response = requests.post(url=url, data=body_json, headers=headers, verify=False)
        return response

    def get_tickets_movidesk(self, id_tickets: str) -> requests.status_codes:
        url = f'https://localhost:4443/public/v1/tickets?id={id_tickets}&token={self.token_movidesk}'

        return requests.get(url=url, verify=False).json()

    def patch_tickets_movidesk(self, id_tickets: int, data: dict) -> requests.status_codes:
        url = f'https://localhost:4443/public/v1/tickets?id={id_tickets}&token={self.token_movidesk}'
        headers = {'Content-Type': 'application/json'}
        body_json = json.dumps(data)

        return requests.patch(url=url, data=body_json, headers=headers, verify=False).status_code

    def post_tickets_movidesk(self, id_tickets: int, data: dict) -> requests.status_codes:
        url = f'https://localhost:4443/public/v1/tickets?id={id_tickets}&token={self.token_movidesk}'
        headers = {'Content-Type': 'application/json'}
        body_json = json.dumps(data)

        return requests.post(url=url, data=body_json, headers=headers, verify=False).status_code

    def write_record(self, file_path, record):
        file = open(file_path, 'a', encoding="utf-8")
        file.write(f'{record}\n')
        file.close()


class Attachment(HelpdeskMovidesk):
    def __init__(self, token_movi):
        super().__init__(token_movi)

    def _get_content_type(self, file_name):
        try:
            file_extension = f'.{file_name.split(".")[1]}'
        except IndexError as error:
            file_extension = f'.text'

        dict_mime_types = clients_data.dict_ext_mime
        if str(file_extension).lower() in dict_mime_types.keys():
            mime_type = dict_mime_types[str(file_extension).lower()][0]
        else:
            mime_type = 'text/html'

        return mime_type

    def _get_attachment_raw(self, url):
        headers = {
            "Content-Type": "multipart/form-data"
        }

        response = requests.get(url=url, headers=headers, stream=True, verify=False)
        if response.status_code == 200:
            response.raw.decode_content = True

        return response

    def send_attachment(self, ticket_id: int, action_id: int, file_name: str, url_attachment: str):
        url = f"{clients_data.movidesk_url_api_interna}{clients_data.movidesk_endpoint_ticket_file}?token={self.token_movidesk}&id={ticket_id}&actionId={action_id}"

        headers = {
            "Content-Type": "multipart/form-data"
        }
        content_type = self._get_content_type(file_name)
        file_raw = self._get_attachment_raw(url_attachment)
        files = {
            'file': (file_name, file_raw.raw, content_type)
        }
        response = requests.post(url=url, headers=headers, files=files, verify=False)

        return response

    def send_attachment_stream(self, ticket_id: int, action_id: int, file_name: str, url_attachment: str) -> Response:
        content_type = self._get_content_type(file_name)
        payload = {}
        headers = {
            "Content-Type": "multipart/form-data"
        }
        response = requests.get(url=url_attachment, headers=headers, stream=True, verify=False)
        if response.status_code == 200:
            response.raw.decode_content = True  # decompress as you read
        files = {
            'file': (file_name, response.raw, content_type)
        }

        url_movi = f"{clients_data.movidesk_url_api_interna}{clients_data.movidesk_endpoint_ticket_file}?token={self.token_movidesk}&id={ticket_id}&actionId={action_id}"

        return requests.post(url=url_movi, data=payload, files=files, verify=False)