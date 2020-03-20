import pytest
import requests
import json
from utils import conf

def test_create_user(supply_url, name):
    url = supply_url + '/user?'
    resp = requests.post(url + 'name=' + name[0] + '&surname=' + name[1])
    j = json.loads(resp.text)
    assert j['status'] == 'success'


def test_get_user(supply_url, get_random_user):
    url = supply_url + '/'
    resp = requests.get(url + '?id=' + str(get_random_user['_id']))
    j = json.loads(resp.text)
    assert j['status'] == 'success'

def test_update_user(supply_url, get_random_user, name):
    url = supply_url + '/update?'
    id_to_update = get_random_user['_id']
    old_name = get_random_user['name']
    old_surname = get_random_user['surname']
    resp = requests.post(url + 'id=' + str(id_to_update) + '&name=' + name[0] + '&surname=' + name[1])
    j = json.loads(resp.text)
    updated_resp = requests.get(supply_url + '/?id=' + str(id_to_update))
    u_j = json.loads(updated_resp.text)
    assert j['status'] == 'success'
    assert u_j['name'] == name[0]
    assert u_j['surname'] == name[1]

def test_delete_user(supply_url, get_random_user):
    url = supply_url + '/delete?'
    id_to_delete = get_random_user['_id']
    resp = requests.post(url + 'id=' + str(id_to_delete))
    j = json.loads(resp.text)
    assert j['status'] == 'success'
    assert conf.COLLECTION.find_one({'_id': id_to_delete}) == None


