#!/bin/python3

from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, from Terre's Server!"

@app.get("/events")
def get_events():
    start = request.args.get("start")
    end = request.args.get("end")

    if not end: end = start

    url = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"

    sparql_args = {"start": start, "end": end}

    sparql = """SELECT ?event ?eventLabel ?lon ?lat WHERE {{
    ?event wdt:P580 ?start; wdt:P582 ?end; p:P625 ?coordinate.
    ?coordinate psv:P625 ?coordinate_node.
    ?coordinate_node wikibase:geoLongitude ?lon; wikibase:geoLatitude ?lat.
    FILTER (YEAR(?start) <= {start} && (YEAR(?end) >= {end} || !BOUND(?end))).
    SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" }}
    }}""".format(**sparql_args)

    response = requests.get(url, params={"query": sparql}, headers={"Accept": "application/json"})

    return response.json()["results"]["bindings"]

app.run(host="localhost", port=3000)