import pytest

import requests

from app.settings import CURRENT_APP_HOST


def test_get_wallet_with_address():
    r = requests.post(f'{CURRENT_APP_HOST}/wallet/',
                      json={'address': 'TLa2f6VPqDgRE67v1736s7bJ8Ray5wYjU7'})

    assert r.status_code == 200
    
    data = r.json()

    assert data['address'] == 'TLa2f6VPqDgRE67v1736s7bJ8Ray5wYjU7'
    assert 'balance' in data
    assert 'energy' in data
    assert 'bandwidth' in data
