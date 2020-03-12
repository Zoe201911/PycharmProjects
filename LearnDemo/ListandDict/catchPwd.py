#!/usr/bin/env python
import rethinkdb

did_list = [
    '7cc1f1b3-6f42-47b3-bdcb-d310474a0839',
    'b8623ab0-a957-42ae-8df6-3e2fea8458e0',
    '159b0635-ebd5-4ab9-ae04-959608d1f0d3',
    '969b1a7f-8940-4b29-aaa0-d8251b9b54fa',
    'bd9aab98-45c6-4281-843f-6ee02852d0c1',
    '2b6b1003-165d-46d8-90e4-feb9b589cbb0',
    '0902e9f7-4ecb-45d1-a2ec-3d44e9c3ce43'
]

r = rethinkdb.RethinkDB()
conn = r.connect(host='10.108.6.11', port=28015, db='dim', user='dim', password='vo4YCSEx')
cursor = r.table('devices').run(conn)
for doc in cursor:
    for did in did_list:
        if did == doc['id']:
            print(doc['id'], doc['password'])