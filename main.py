from aiohttp import web
import json
from utils import conf

collection = conf.COLLECTION.find({})
arr = []
for x in collection:
    arr.append(x)
    print(x)


async def get_user(request):
    try:
        user_id = request.query['id']
        user = conf.COLLECTION.find_one({'_id': int(user_id)})
        response = {'status': 'success', 'id': user['_id'], 'name': user['name'], 'surname': user['surname']}
        return web.Response(text=json.dumps(response))
    except Exception as e:
        response = {'status': 'fail', 'reason': str(e)}
        return web.Response(text=json.dumps(response), status=500)


async def new_user(request):
    try:
        name = request.query['name']
        new_id = conf.COUNTER.find({'_id': 'counter'})
        for x in new_id:
            res_id = x['COUNT']
        surname = request.query['surname']
        post = {'_id': res_id, 'name': name, 'surname': surname}
        conf.COLLECTION.insert_one(post)
        conf.COUNTER.update_one({'_id': 'counter'}, {'$inc': {'COUNT': 1}})
        print('New user created! Name: ', name, ' ', surname)
        response = {'status': 'success', 'name': name, 'surname': surname}
        return web.Response(text=json.dumps(response))
    except Exception as e:
        response = {'status': 'fail', 'reason': str(e)}
        return web.Response(text=json.dumps(response), status=500)


async def update_user(request):
    try:
        id_for_update = request.query['id']
        name = request.query['name']
        surname = request.query['surname']
        conf.COLLECTION.update_one({'_id': int(id_for_update)}, {'$set': {'name': name, 'surname': surname}})
        print('User updated! ', name, ' ', surname)
        response = {'status': 'success', 'updated id': id_for_update}
        return web.Response(text=json.dumps(response))
    except Exception as e:
        response = response = {'status': 'fail', 'reason': str(e)}
        return web.Response(text=json.dumps(response), status=500)


async def delete_user(request):
    try:
        user_id = request.query['id']
        conf.COLLECTION.delete_one({'_id': int(user_id)})
        response = {'status': 'success', 'id': user_id}
        return web.Response(text=json.dumps(response))
    except Exception as e:
        response = {'status': 'fail', 'reason': str(e)}
        return web.Response(text=json.dumps(response), status=500)


app = web.Application()
app.router.add_get('/', get_user)
app.router.add_post('/user', new_user)
app.router.add_post('/update', update_user)
app.router.add_post('/delete', delete_user)

web.run_app(app)
