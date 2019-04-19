from flask import NewRequest
import couchdb

@app.route('/api/v0.0.1/auth-hosts', methods=['POST'])
def new_auth_host():
    if not request.json:
        abort(400)
    auth-host-name = {
        'name': request.json['hostname.name'],
        'type': request.json['hostname.type']
    }
    auth-host = {
            'address': auth-host-name,
            'persistent': request.json['persistent'],
            'devdesc': request.json['devdesc']
    }
    add_to_auth_host_db(auth-host)
    return jsonify({'auth-host': auth-host}), 201

def post_auth_host_db(auth_host):
    couchserver = couchdb.Server("http://127.0.0.1:5984"/auth-hosts/)
    doc_id, doc_rev = couchserver.save(auth-host)
