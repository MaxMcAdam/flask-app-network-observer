#!/usr/bin/python

from flask import Flask,request,jsonify
import couchdb

app = Flask(__name__)

@app.route('/api/auth-hosts/add/', methods=['POST'])
def new_auth_host():
    if not request.json:
        abort(400)

    auth_host = {
            'hostname': {
        	'name': request.json.get('name'),
        	'type': request.json.get('type')
    	    },
            'persistent': request.json.get('persistent'),
            'devdesc': request.json.get('devdesc')
    }

    couchserver = couchdb.Server("http://admin:p4ssw0rd@127.0.0.1:5984/")
    db = couchserver['auth-hosts']
    doc_id, doc_rev = db.save(auth_host)
    return jsonify({'auth-host': auth_host}), 201

@app.route('/api/auth-hosts/remove/<host_id>', methods=['DELETE'])
def remove_auth_host(host_id):
    couchserver = couchdb.Server("http://admin:p4ssw0rd@127.0.0.1:5984/")
    db = couchserver['auth-hosts']
    doc = db[host_id]
    db.delete(doc)
    return jsonify({'doc': doc}), 201

@app.route('/api/auth-hosts/toggle-persistence/<host_id>', methods=['PUT'])
def toggle_host_persistence(host_id):
    couchserver = couchdb.Server("http://admin:p4ssw0rd@127.0.0.1:5984/")
    db = couchserver['auth-hosts']
    doc = db[host_id]
    if (doc['persistent'] == "true"):
        doc['persistent'] = "false"
    else :
        doc['persistent'] = "true"
    db[doc.id] = doc
    return jsonify({db[doc]}), 201

@app.route('/api/live-hosts/', methods=['GET'])
def display_live_hosts():
    couchserver = couchdb.Server("http://admin:p4ssw0rd@127.0.0.1:5984/")
    disp_rows = []
    db = couchserver['live-hosts']
    for row in db.view(host_view):
        disp_rows.append(row)
    return disp_rows

def host_view(doc):
    if 'hostname.name' in doc:
        yield doc['hostname.name'], doc
    else:
        yield doc['ipaddress.addr'], doc

if __name__ == '__main__':
    app.run(debug=True)
