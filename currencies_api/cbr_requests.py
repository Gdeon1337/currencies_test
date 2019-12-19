import logging

import requests

from .defaults import CBR_URL, REQUESTS_TIMEOUT


def parse_cbr_currencies():
    logging.info('Request cbr started')

    cbr_currencies = requests.get(CBR_URL, timeout=REQUESTS_TIMEOUT)
    if cbr_currencies.status_code != 200:
        logging.error(f'status requests cbr = {cbr_currencies.status_code}')
        raise requests.ConnectionError('Expected status code 200, but got {}'.format(cbr_currencies.status_code))

    cbr_currencies = cbr_currencies.json()
    currencies = cbr_currencies.get('Valute')

    if not currencies:
        logging.warning(f'cbr response not key Valute')
        raise Exception('CBR response not key Valute')
    return currencies
