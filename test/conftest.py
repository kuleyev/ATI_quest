import pytest
import random
from pymongo import MongoClient
from utils import conf

@pytest.fixture
def supply_url():
    return 'http://localhost:8080'


@pytest.fixture
def name():
    name_array = ['Avdotya', 'Anisya', 'Victorina', 'Vladana', 'Domnika', 'Rusalina', 'Yarina']
    surname_array = ['Zemfirova', 'Ilyazirova', 'Iluzova', 'Mavludova', 'Hadieva', 'Shahinova']
    return random.choice(name_array), random.choice(surname_array)

@pytest.fixture
def get_random_user():
    collection = conf.COLLECTION.find({})
    arr = []
    for x in collection:
        arr.append(x)
    return random.choice(arr)



