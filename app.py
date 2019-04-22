#!/usr/bin/python

from flask import Flask,request,jsonify
import couchdb

app = Flask(__name__)

@app.route('/api/v0.0.1/auth-hosts', methods=['POST'])
def new_auth_host():
    if not request.json:
        abort(400)
    #post_content=request.get_json()
    auth_host = {
            'hostname': {
        	'name': request.json.get('name'),
        	'type': request.json.get('type')
    	    },
            'persistent': request.json.get('persistent'),
            'devdesc': request.json.get('devdesc')
    }
    print("Auth-host extracted from post data")
    post_auth_hosts_db(auth_host)
    return jsonify({'auth-host': auth_host}), 201

def post_auth_hosts_db(auth_host):
    couchserver = couchdb.Server("http://127.0.0.1:5984/")
    db = couchserver['auth-hosts']
    doc_id, doc_rev = db.save(auth_host)


if __name__ == '__main__':
    app.run(debug=True)
