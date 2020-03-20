from pymongo import MongoClient

CLIENT = MongoClient()
DB = CLIENT['ati_test']
COLLECTION = DB['test']
COUNTER = DB['counter']
COUNTER_INIT = {'_id': 'counter', 'COUNT': 0, 'NOTE': 'counter for users'}
if COUNTER.count_documents({}) == 0:
    print('Counter created')
    COUNTER.insert_one(COUNTER_INIT)
