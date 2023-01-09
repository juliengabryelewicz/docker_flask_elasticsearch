from flask import Flask, jsonify, make_response
from elasticsearch import Elasticsearch
from datetime import datetime


es = Elasticsearch(["http://elasticsearch:9200/"])

app = Flask(__name__)

@app.route("/")
def app_root():
    return "Hello world"

@app.route("/elasticsearch/info")
def elasticsearch_details():
    return jsonify(dict(es.info()))

@app.route("/elasticsearch/health")
def elasticsearch_health():
    return jsonify(dict(es.cluster.health()))
