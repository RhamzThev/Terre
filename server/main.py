#!/bin/python3

from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

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

    # response = requests.get(url, params={"query": sparql}, headers={"Accept": "application/json"})

    # return response.json()["results"]["bindings"]
    return [
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q709261"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Hundred Regiments Offensive",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "37.45"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "116.3"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q24946580"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Zbylitowska Góra massacre",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.985361"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "20.899806"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q682452"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Siege of Malta",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "35.89777777778"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "14.5125"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q11713311"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Intelligenzaktion Litzmannstadt",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.776667"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "19.454722"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q7802238"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Tillamook Burn",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "45.54"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-123.29"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q6983410"
            },
            "eventLabel": {
                "type": "literal",
                "value": "German crimes against Poles",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.216666666667"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "21.0"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1400309"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Uzdborjád",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "46.5938967"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "18.5790599"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q708217"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battles of Narvik",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "68.420555555556"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "17.56"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q150939"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Operation Weserübung",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "64.0"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-12.0"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1402470"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Freifeld Airport",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "48.1819"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "9.90417"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q116780967"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q116780967"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.9689"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "12.0848"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q109469096"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q109469096"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.108917"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "17.025861"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q2238977"
            },
            "eventLabel": {
                "type": "literal",
                "value": "German occupation of the Channel Islands",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.429681"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-2.593152"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q4224417"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Kliuchove",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "46.761017777778"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "33.353190833333"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q8000575"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Wild Cat",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "40.2882"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-76.6535"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q11245903"
            },
            "eventLabel": {
                "type": "literal",
                "value": "JGR Kanpu Ferry",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "34.0"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "130.0"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q18216807"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Siege of Giarabub",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "29.7425"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "24.5169"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q12053257"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Bolling Field",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "38.8428"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-77.0161"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q3975722"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Bombing of Milan in World War II",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "45.46416667"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "9.19027778"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q115141935"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Cox Family Papers",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "39.325434"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-82.1024125"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q115142296"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Nelson Holmes Van Vorhes Papers",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "39.325434"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-82.1024125"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q682452"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Siege of Malta",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "35.8833"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "14.45"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q3641948"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Bombing of Naples in World War II",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "40.83333333"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "14.25"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q16902595"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Ventnor West railway station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "50.5923"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-1.21911"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q112084834"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q112084834"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "48.921666666667"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "10.538888888889"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q154494"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Aktion T4",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.511"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "13.369"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q154494"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Aktion T4",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.511"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "13.369"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q11636595"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of Boulogne",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "50.72638889"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "1.61472222"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q3687151"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Capture of Kassala",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "16.0"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "36.0"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q911972"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Dunkirk evacuation",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.033333333333"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "2.3666666666667"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q120755368"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Kutras Aggregate Plant",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "40.5883"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-122.37696"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q106600727"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q106600727"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.167729991554"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "10.385533802211"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q96432271"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q96432271"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "55.136944444444"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "10.727777777778"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1202078"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Italian conquest of British Somaliland",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "9.5661111111111"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "44.054722222222"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q9388647"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Mniszek killings",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "53.484444"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "18.607778"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q2070808"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Jilava Massacre",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "44.335"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "26.1075"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q696018"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Operation Compass",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "31.6108"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "25.9256"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q934266"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of Kollaa",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "62.02777778"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "32.25555556"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q3532325"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of Rotterdam",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.93083333"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "4.47916667"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q705279"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of Wuyuan",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "31.09"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "108.26611111"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q126510682"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q126510682"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-12.05141173376"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-77.033519535151"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q114074194"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q114074194"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.468603595437"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "13.333096093253"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q124632648"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Opelousas Colored School",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "30.530866666667"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-92.074733333333"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q12639564"
            },
            "eventLabel": {
                "type": "literal",
                "value": "5th conference of the Communist Party of Yugoslavia",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "45.825734"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "16.0484827"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q2444884"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Tibet",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "29.6"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "91.1"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q5562130"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Gillett's Crossing Halt railway station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "53.7623"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-3.0404"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q130435860"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Gjert Eidsvik Skibsbyggeri",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "59.985203809816"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "5.9473545739298"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q4871791"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of Morava–Ivan",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "40.5833"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "20.6667"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q610000"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of the Grebbeberg",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.954"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "5.6"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q17003995"
            },
            "eventLabel": {
                "type": "literal",
                "value": "The Oregonian Building",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "45.519992"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-122.678415"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q4354480"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Operation MB8",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "35.0"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "18.0"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q154607"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Warsaw Ghetto",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.229666"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "21.012222"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q705165"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Bombing of Chongqing",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "29.4814"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "106.9382"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q716722"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of Pindus",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "40.0889"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "20.9253"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q751002"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of Kuhmo",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "64.84805556"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "29.32638889"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q116224697"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Dihua",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "43.8225"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "87.6125"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1466024"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Siegessäule",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "53.54630556"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "9.93538889"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q7958632"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Wabash Bridge",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "40.4371"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-80.0074"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1402472"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Ollesheim Airport",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "50.8129"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "6.61628"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q3081812"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Operation Alphabet",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "68.4333"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "17.4167"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q696817"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Mediterranean and Middle East Theater of World War II",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "35.0"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "18.0"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1827527"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Lippische Staatszeitung",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.936685"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "8.873241"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q6900329"
            },
            "eventLabel": {
                "type": "literal",
                "value": "The Blitz",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.50694444"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-0.1275"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q709704"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of South Guangxi",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "23.8055"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "108.984"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q696829"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of Dakar",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "14.67862"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-17.420724"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q13021733"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Ban Pho Mun railway station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "15.204811111111"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "104.80336944444"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q6783460"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Masļenki border incident",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "56.967777777778"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "28.071944444444"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q327048"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Norwegian heavy water sabotage",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "59.871666666667"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "8.4944444444444"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1589948"
            },
            "eventLabel": {
                "type": "literal",
                "value": "House Bellevue",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.7791"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "6.13958"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q477095"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of Suomussalmi",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "64.888333333333"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "28.888888888889"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q714265"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of Gembloux",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "50.6"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "4.666"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q113485685"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Secret State Police Central Office Hannover (1938 – 1943-10)",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.364983111111"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "9.7482848333333"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q15805393"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q15805393"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.17833333"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "7.19944444"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q543255"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of Taranto",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "40.451111111111"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "17.2075"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q714207"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Siege of Lille",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "50.63333333"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "3.06666667"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q80174904"
            },
            "eventLabel": {
                "type": "literal",
                "value": "National Institute for the Jewish Deaf-Mute in Budapest",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "47.503333333333"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "19.08"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q708638"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Gurs internment camp",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "43.264722222222"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-0.73166694444444"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q714684"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of Gabon",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "0.39"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "9.45166667"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q3043087"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of Saumur",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "47.26"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "0.076944444444444"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q134301"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Katyn massacre",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "54.773333"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "31.788889"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q30006881"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Gostynin Ghetto",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.4333333333"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "19.4833333333"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q4905074"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Big Bell",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-27.3401921"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "117.6603167"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q698421"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Italian invasion of Egypt",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "26.0"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "30.0"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q714207"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Siege of Lille",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "50.631944444444"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "3.0575"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q154720"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of Britain",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "54.0"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-2.0"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q2219890"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Siege of Calais",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "50.9475"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "1.8555555555556"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q85366027"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Bombing of Turin in World War II",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "45.063041"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "7.669425"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q714288"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of Fort Eben-Emael",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "50.79722222"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "5.68083333"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q6072292"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Iron Acton railway station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.5477"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-2.469"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q105071456"
            },
            "eventLabel": {
                "type": "literal",
                "value": "ETH Lectures",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "47.376527777778"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "8.5476388888889"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q3754427"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Vellone–Campo dei Fiori funicular",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "45.860772"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "8.783634"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q2750804"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Operation Ambassador",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.4228"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-2.5307"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1615205"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Herzog-Albrechts-Schule",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "54.077375"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "21.372099"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q7624870"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Stroud Green railway station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.5731"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-0.1129"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q9388656"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Palmiry massacre",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.33"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "20.74"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q2827862"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Flood of 1940",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "42.396444444444"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "2.5986111111111"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q16303589"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q16303589"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "47.68"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "2.87361"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q18415369"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Société Anonyme des Usines Métallurgiques du Hainaut",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "50.39513"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "4.4743"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q113458901"
            },
            "eventLabel": {
                "type": "literal",
                "value": "F. H. Schmidt Briefumschlag-Papier-Ausstattungs-Fabrik AG Torgau",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.558240611111"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "12.986446805556"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1099873"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Café Japan",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "47.504295894752"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "19.062304499311"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1802929"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q1802929"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.3169"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "9.50111"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q113206337"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q113206337"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-34.596109776093"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-58.486468791962"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q6665065"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Locharbriggs railway station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "55.108"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-3.5785"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q814242"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Pacification of Manchukuo",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "43.8833"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "125.317"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q4981823"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Launch site for V-1 flying bombs at Brécourt",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.65194444"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-1.67"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q4981823"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Launch site for V-1 flying bombs at Brécourt",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.65194444"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-1.67"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1581815"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of the Lys",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.055"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "3.73416667"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q115141230"
            },
            "eventLabel": {
                "type": "literal",
                "value": "John Quincy Adams Ward papers",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "39.325434"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-82.1024125"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q115144246"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Pruden Family Papers",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "39.325434"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-82.1024125"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q2032618"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of Hannut",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "50.6667"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "5.0833"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q717963"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of Zaoyang–Yichang",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "32.1252"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "112.751"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q48833613"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Vetreria Corvaya e Bazzi",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "45.480808261801"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "9.2089338266941"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q105978768"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Assault on Saint Petersburg",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "59.95"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "30.316666666667"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q97363755"
            },
            "eventLabel": {
                "type": "literal",
                "value": "World War II bombing of Steinkjer",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "64.015587463889"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "11.495340358333"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q208529"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of Dunkirk",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.0343"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "2.3768194444444"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q2981215"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of Petsamo",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "69.25"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "30.56666667"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q3535001"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Åndalsnes landings",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "62.56345833"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "7.68321944"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q7443327"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Second Great Fire of London",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.5157"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-0.0921"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q2219890"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Siege of Calais",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "50.95614444"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "1.84136111"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q17221557"
            },
            "eventLabel": {
                "type": "literal",
                "value": "poison gas production in Ōkunoshima",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "34.305944"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "132.994111"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q7508662"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of Sidi Barrani",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "31.6108"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "25.9256"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q714979"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of the Afsluitdijk",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "53.074167"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "5.336944"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q2446643"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of Raate Road",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "64.848055555556"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "29.326388888889"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1935000"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Oedheim Airbase",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.2318"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "9.26245"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q154607"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Warsaw Ghetto",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.25"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "21.0"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q435490"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Alte Börse (Frankfurt)",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "50.1113"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "8.68153"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q7580703"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Spring Vale Cemetery",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-37.92094"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "145.40509"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q327895"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Łódź Ghetto",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.801389"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "19.441389"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1126598"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Kőbánya cellar system",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "47.485"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "19.137222"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1126598"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Kőbánya cellar system",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "47.485"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "19.137222"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1126598"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Kőbánya cellar system",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "47.485"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "19.137222"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q625798"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Western Desert campaign",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "30.833333333333"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "28.95"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q106477284"
            },
            "eventLabel": {
                "type": "literal",
                "value": "State Police Office Braunschweig",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.2592008"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "10.53320315"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q3486941"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of Summa",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "60.507342"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "29.012389"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q2890351"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of Vinjesvingen",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "59.62027778"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "7.80638889"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1433779"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Oranienburg Airbase",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.7344"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "13.2161"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q2554610"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Wehrmachtsgefängnis",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.5647"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "12.9831"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q5255067"
            },
            "eventLabel": {
                "type": "literal",
                "value": "French demarcation line",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.42736111"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "2.90641944"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q2594918"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of Honkaniemi",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "60.65"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "28.78333333"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q104884617"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Walton Park Cemetery",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "53.45518"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-2.96905"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1772340"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of Elaia–Kalamas",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "39.5867"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "20.1422"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1433564"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Dedelstorf Airbase",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.7142"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "10.5097"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q677754"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Ludendorff Bridge",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "50.579166666667"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "7.2441666666667"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q106368178"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Mina Clara",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "42.218366"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "1.696859"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q76165244"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Boskovice Judicial District",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.5272995"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "16.71159225"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q715182"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Battle of Salla",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "66.83333333"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "28.66666667"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q106477284"
            },
            "eventLabel": {
                "type": "literal",
                "value": "State Police Office Braunschweig",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.26628955"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "10.525972322047"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1361469"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Rechlin Test Site",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "53.3444"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "12.7295"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q3314824"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q3314824"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "46.1939"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "2.4724"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q101252293"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q101252293"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.837778"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "6.292167"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q2622938"
            },
            "eventLabel": {
                "type": "literal",
                "value": "July 1276 papal conclave",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "41.88590556"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "12.50615556"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q15730588"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q15730588"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.443427777778"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "5.4354361111111"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1500904"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Thunderbolt",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "40.5739"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-73.9825"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q5017115"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Idrætsparken",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "55.7025"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "12.572222"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q60853693"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q60853693"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.87216"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "6.21931"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q62020991"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Llay Main Colliery",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "53.100555555556"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-3.0051111111111"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q111705317"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Groß-Siegharts station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "48.786572"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "15.408136"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q79382868"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Hotel Cloche d'Or",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.582611111111"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "6.1145277777778"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q120693754"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Drogheda Ironworks",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "53.71392"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-6.34696"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q120693754"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Drogheda Ironworks",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "53.71392"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-6.34696"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q11615386"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q11615386"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "39.46488"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "140.99256"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q18618934"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Arthur Kill Bridge",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "40.6375"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-74.1955"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q30510159"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Heinola seminar",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "61.2056"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "26.03039"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q28842972"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Sankt Andreasberg Schwalbenherd station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.70789"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "10.51176"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q74753027"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Mairie de Mertert",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.71349"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "6.49869"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q113692415"
            },
            "eventLabel": {
                "type": "literal",
                "value": "General Nikolaevo",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "42.28816529247"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "24.967737664591"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q17358260"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Palacio del Duque de Uceda",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "40.424688888889"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-3.6913722222222"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q8342970"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q8342970"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "40.4169"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-3.7033"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q111705515"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Bahnhof Raabs",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "48.8446"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "15.49621"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q108746719"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q108746719"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.047427"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "3.756254"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q62558816"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q62558816"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "48.8919237"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "2.4125819"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q118278754"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q118278754"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "46.258967437066"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "12.042817107119"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q111241532"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Collection on the Millfield Mine Explosion",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "39.325434"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-82.1024125"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q115143263"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Victor H. Bernstein Papers",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "39.325434"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-82.1024125"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q116997763"
            },
            "eventLabel": {
                "type": "literal",
                "value": "John Owens Papers",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "39.325434"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-82.1024125"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q117007329"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Fraternal Organizations Collection",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "39.325434"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-82.1024125"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q24873238"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q24873238"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "35.71"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "139.72"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q96030829"
            },
            "eventLabel": {
                "type": "literal",
                "value": "ELFA",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "54.670206"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "25.267196"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q16268389"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Funivia di San Luca",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "44.479542"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "11.295455"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q108435014"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Baertsoen-Buysse",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.053644"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "3.743803"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1398403"
            },
            "eventLabel": {
                "type": "literal",
                "value": "FIS Nordic World Ski Championships 1938",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "60.9833"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "25.6325"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q127510238"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Sieghartsles station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "48.806388888889"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "15.425833333333"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q15614886"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Vydrica",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "48.1421091"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "17.1014932"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q7281329"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Radipole railway station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "50.629"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-2.4623"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q127510151"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Schönfeld-Kirchberg station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "48.766388888889"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "15.386666666667"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q125512387"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q125512387"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "36.68648840435"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-6.1464379714331"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q800572"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Broad Street railway station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.518888888889"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-0.083333333333333"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q16927228"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Inner Circle railway line",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-37.77958"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "144.9735"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q42773305"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Hansa Pit",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.904444"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "10.513333"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q14706295"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Grand Central Palace",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "40.7544"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-73.9743"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q7718972"
            },
            "eventLabel": {
                "type": "literal",
                "value": "The Bobs",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "41.9407"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-87.6924"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q45819176"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Malayan filariasis in Hachijo-Kojima Island",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "33.12555556"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "139.68805556"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q56300364"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Hamngatspalatset",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "59.332409668871"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "18.068909006088"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q74753027"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Mairie de Mertert",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.713472"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "6.498667"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q121365257"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Station 9 Kahleberg",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "50.751655"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "13.733531"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q100989142"
            },
            "eventLabel": {
                "type": "literal",
                "value": "De Vigne-Hart",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "50.84773"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "4.3549415"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q113411118"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q113411118"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "55.65979"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "37.60768"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q126689876"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Devons Road motive power depot",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.5198"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-0.0153"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q60853715"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q60853715"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.74487"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "6.50164"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q125934923"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q125934923"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "38.929166666667"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-0.26666666666667"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q889692"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Lake Constance train ferries",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "47.5997"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "9.4342"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q61037832"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Georgia Avenue Bridge",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "40.4144"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-79.995"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q2223402"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Church of St. Ann",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.3702"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "4.91811"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q15047489"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Cyclone (Revere Beach)",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "42.42"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-70.986"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q100258236"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Theater des Friedens",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.13186"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "11.63917"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q14682063"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Graton Rancheria",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "38.41647778"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-122.883025"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q3995600"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q3995600"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "42.38694444"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "11.16916667"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q116215894"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q116215894"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "36.01538"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "139.75373"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q66829005"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Casa Cuna de Fraisoro",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "43.1895395"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-2.0624118"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q14936690"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Corona Stage Academy",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.4939"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-0.237692"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q2855099"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Yosemite Firefall",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "37.730555"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-119.573508"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q7917372"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Vaughn Street Park",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "45.5371"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-122.701"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q2105840"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Munich Post Office Railway",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "48.14207778"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "11.55613611"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q5989523"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Idora Park",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "41.072222"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-80.685"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q14714579"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Pabst Building",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "43.0389"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-87.9094"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q2230425"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Freibad Schallacker",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.4894"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "7.49187"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q56557282"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Stadttheater Basel",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "47.55372"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "7.59069"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q18748620"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Hamburg-Hausbruch train station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "53.472483829676"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "9.8936015367508"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q109021303"
            },
            "eventLabel": {
                "type": "literal",
                "value": "École de plein air de Lille",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "50.615833333333"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "3.0727777777778"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q100937816"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Fonson",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "50.8490312"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "4.3402628"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q5856515"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Faro de San Jerónimo",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "36.805981025465"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-6.327165733991"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q28970360"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Longhirst railway station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "55.1996"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-1.6269"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1529562"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Kattersnaundorf",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.4877"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "12.2966"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q5430146"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Fairfax Airport",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "39.1482"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-94.5997"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q48815688"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Carmont railway station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "56.9387"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-2.35"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q7498528"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Shire of Yarrawonga",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-36.0167"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "146.0"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q5419465"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Excelsior Amusement Park",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "44.903333333333"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-93.5625"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q96418529"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Hardies Platform railway station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-33.819444444444"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "151.025"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q97940627"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Hrabůvka airport",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.783055555556"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "18.251388888889"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q110624040"
            },
            "eventLabel": {
                "type": "literal",
                "value": "sanatorium de Dreux",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "48.759694444444"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "1.3363055555556"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q14716576"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Krejci Dump",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "41.27"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-81.54"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q4868984"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Bathampton railway station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.3983"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-2.3208"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q108746721"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q108746721"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.061731"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "3.745358"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q108407691"
            },
            "eventLabel": {
                "type": "literal",
                "value": "ex manicomio di Volterra",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "43.400660457805"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "10.876127453948"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q73458363"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Estación de Linares-San José",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "38.096229"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-3.622704"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1450218"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Jünkerather Gewerkschaft",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "50.34"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "6.58944444"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q15697693"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Paris Theatre",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-33.8768843"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "151.2114773"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q5989523"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Idora Park",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "41.071111111111"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-80.685555555556"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q116299084"
            },
            "eventLabel": {
                "type": "literal",
                "value": "O'Loughlin Road Cemetery",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.65545"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-7.23875"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q12261683"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Gran Kursaal",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "43.32454167"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-1.97908889"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q4416001"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q4416001"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "55.7789"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "37.7178"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q4975229"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Brookwood Hospital",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.315"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-0.617"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q5646420"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Hamstead Colliery",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.5319"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-1.93336"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1431855"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Leipzig-Mockau Airport",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.3956"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "12.4097"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q30132570"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Blagojev Kamen",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "44.44"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "21.85"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q49415958"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Grand Central",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "39.936666666667"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-112.11583333333"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q111239188"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Carr Liggett papers",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "39.325434"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-82.1024125"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q111241417"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Earl C. Shively Collection",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "39.325434"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-82.1024125"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q110892070"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Sammy Kaye Collection",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "39.325434"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-82.1024125"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q111212983"
            },
            "eventLabel": {
                "type": "literal",
                "value": "James Norman papers",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "39.325434"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-82.1024125"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q110892031"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Eusebia Simpson Hunkins papers",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "39.325434"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-82.1024125"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q111213001"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Frank Buhla Collection",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "39.325434"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-82.1024125"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q111192707"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Warren G. French papers",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "39.325434"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-82.1024125"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q113127295"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Wang-An Lime Kiln",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "23.370813634977"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "119.49385670937"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q17292476"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Ceintuurtheater",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.352642"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "4.89148"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q11913831"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Cine Mistral",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "41.376556666667"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "2.1590169444444"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q49429371"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Mammoth Shaft",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "39.932222222222"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-112.11222222222"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q96418529"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Hardies Platform railway station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-33.8195103"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "151.023986"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q89776462"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Mevissen harbour",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.4335"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "6.7112"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q2672891"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Grundhof train station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.835942"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "6.329628"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q109421267"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Pechersk Hippodrome",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "50.437165906883"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "30.547250687873"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q60853696"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Reisdorf train station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.86795"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "6.26321"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q60853710"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Steinheim train station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.81935"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "6.47279"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q60853703"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Bollendorf-Pont train station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.84955"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "6.35414"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1433671"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Waldau Army Airfield",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.2808"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "9.50528"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q770094"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q770094"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "47.5254"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "19.07915"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q7207973"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Point Bridge II",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "40.4408"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-80.0145"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q24693530"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Rudolph Schaeffer School of Design",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "37.763248"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-122.40597"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q5430146"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Fairfax Airport",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "39.14806"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-94.59968"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q113130795"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Fish stoves of Yeh",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "23.370885166584"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "119.49399300073"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q60853707"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q60853707"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.8336"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "6.38333"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q105956084"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Orthodox church of St. Dimitrios in Preveza, Greece",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "38.955833333333"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "20.754166666667"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q4905578"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Big Dipper",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-33.8482"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "151.21"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q60852797"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Echternach train station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.81556"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "6.41788"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q83311"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Persian Empire",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "33.0"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "53.0"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q60853711"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Rosport train station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.80366"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "6.50736"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q15830859"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q15830859"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.446236111111"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "5.4465416666667"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q60853712"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Hinkel train station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.78322"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "6.51208"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q19195"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Ridge Route",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "34.632222"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-118.696944"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q16335776"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Central Halls Brussels",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "50.85027778"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "4.35013889"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q4882064"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Belchertown State School",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "42.275"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-72.4151"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q20128116"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Church of the Ascension, Stirchley",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.4283"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-1.92272"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q4552848"
            },
            "eventLabel": {
                "type": "literal",
                "value": "174th Street",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "40.8424"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-73.8983"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1428530"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Werl Airbase",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.5687"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "7.91613"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q27084928"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Soup Kitchen For The Jewish Poor",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.518037"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-0.075356"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q26256977"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Hässelby villastads station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "59.380246666667"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "17.810843333333"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q11757782"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Lipsk Żarski",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.6953"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "15.0208"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q478896"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Amt Angerland",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.33305556"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "6.83083333"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q20516854"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Charles Aznavour Square",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "40.1818"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "44.5172"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q4967763"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Brighton Works",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "50.8319"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-0.138611"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q20796556"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Damgarten Airport",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "54.26555556"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "12.43277778"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q60853695"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Moestroff train station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.86716"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "6.23733"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q11227486"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Stow Fair, Lincolnshire",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.902"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-0.374377"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q95403543"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q95403543"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "40.279194444444"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-4.1472777777778"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q2437258"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Tivoli",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "48.1778"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "16.3167"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q110894849"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Cornelius Ryan Collection of World War II Papers",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "39.325434"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-82.1024125"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q19871275"
            },
            "eventLabel": {
                "type": "literal",
                "value": "U.S. Route 80 in Arizona",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "33.258527777778"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-111.33638888889"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q97223527"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q97223527"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "43.054535"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "17.649045"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q5061132"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Central Goods railway station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.4765"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-1.90501"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1851838"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Mereveld",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.062775"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "5.151875"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q46082539"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Grant Hospital of Chicago",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "41.92266"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-87.644557"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q2945378"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Centre de perfectionnement aux affaires",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "48.758055555556"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "2.1702777777778"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1433537"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Brandis-Waldpolenz Airbase",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.3283"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "12.6569"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1016749"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Burnden Park",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "53.568889"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-2.416111"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q797481"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Temple of Bel",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "34.547"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "38.274"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q7555979"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Solar Saros 133",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "68.4"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-137.2"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q17041712"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Ziegler Hospital",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "46.932142"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "7.434298"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q647169"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Aarwangen District",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "47.2333"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "7.7666694444444"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q119506502"
            },
            "eventLabel": {
                "type": "literal",
                "value": "University Hotel",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-37.800479025238"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "144.96722116617"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q38174699"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q38174699"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "47.682884"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "14.118065"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q2146149"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Rethebrücke",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "53.503964"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "9.966635"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q11563974"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Gengahashi Onsen",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "34.64575"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "135.529"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q953851"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Brive – Laroche Airport",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "45.14972222"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "1.47444444"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q4997421"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Bunbury Railway Bridge",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-31.9479"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "115.883"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q19901008"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Grand Bazar de Lyon",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "45.763288888889"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "4.8361611111111"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q61959133"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Réimecher Kannerheem",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.546444444444"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "6.3721666666667"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q80584502"
            },
            "eventLabel": {
                "type": "literal",
                "value": "The Baroness, Grangetown",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.469073755054"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-3.188202381134"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q112166789"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Ho-Chi-Minh-Steg",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "47.5456604"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "9.6802623"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1035580"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Dolyna Raion",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "48.8911"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "23.8431"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1433432"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Ahlhorner Heide Airbase",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.8817"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "8.21472"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1748412"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Harrods Buenos Aires",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-34.59833333"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-58.37444444"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q895713"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Duits Lijntje",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.68719"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "6.03016"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q111703091"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Obereinöd halt",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "47.832512195164"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "14.871290238443"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q124288977"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Statue of Cecil Rhodes",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-33.957927835608"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "18.462442444301"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q14253233"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Gerechtsgebouw, Stationslaan Breda",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.5954025"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "4.7732745"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q16900415"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Christ Church Sparkbrook",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.463153"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-1.870992"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q18708240"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Ambridge station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "41.6056"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-87.3722"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q98600450"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Rappenloch bridge",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "47.38349"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "9.77931"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q15114209"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Strasse Army Ammunition Plant",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "48.417222222222"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "10.166666666667"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1433448"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Alt Daber Airport",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "53.2021"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "12.5223"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q6083213"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Island House",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.4806"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-1.8907"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q5123183"
            },
            "eventLabel": {
                "type": "literal",
                "value": "City Ground",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.21638889"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "0.1225"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q381356"
            },
            "eventLabel": {
                "type": "literal",
                "value": "HM Prison Holloway",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.554166666667"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-0.125"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q106461592"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Schön's spinning mill",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "50.29838"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "19.14357"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q67891569"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Forn de Barraca",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "39.49"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-0.3383672"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q61123299"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q61123299"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.60073"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "6.11542"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q7901312"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Ursuline High School",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "38.4942"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-122.742"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q6168"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Töysä",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "62.633333333333"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "23.816666666667"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q13422369"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Sant Andreu Comtal railway station",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "41.4361"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "2.1932"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q19329520"
            },
            "eventLabel": {
                "type": "literal",
                "value": "St Bartholomew's",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.411778"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-1.984611"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q684911"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Geneva International Motor Show",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "46.23472222"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "6.11888889"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q21638884"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Didinsky Tunnel",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "56.818733333333"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "59.696830555556"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q19717621"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Kaiserlinde",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.317235"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "7.123363"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1332461"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Villa Meißner Straße 121",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.1049"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "13.664"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q19185455"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Gevleweg",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.3924"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "4.8815"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q104640811"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Whisky War",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "80.825"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-66.45"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q123035067"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Q123035067"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "60.20333333"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "15.12944444"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q38250588"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Kenwick Pioneer Cemetery",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-32.04222"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "115.97298"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q23785309"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Velbert Hauptbahnhof",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "51.34233333"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "7.05272222"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q7990579"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Whalom Park",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "42.5756"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-71.7466"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q7244438"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Princes Bridge",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-37.817778"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "144.968889"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q60785771"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Arbutus Oak",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "39.250853"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-76.682465"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1708382"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Cherry Springs Airport",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "41.666666666667"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-77.816388888889"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q29324768"
            },
            "eventLabel": {
                "type": "literal",
                "value": "District Council of Lameroo",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-34.92094"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "140.51728029"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q692052"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Teatro Kursaal",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "46.004"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "8.955"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q34063007"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Heidelberg Rbf",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.405"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "8.6702"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q34063007"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Heidelberg Rbf",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.405"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "8.6702"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q7704536"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Terry Homestead",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "41.6682"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "-72.9236"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q509140"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Heusweiler radio transmitter",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.345"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "6.915"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1433534"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Brandenburg-Briest Airport",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.4385"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "12.4583"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q20249500"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Heinola Plywood Factory",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "61.2"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "26.06"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1813664"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Leibgrenadierdenkmal",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "49.0099"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "8.39361"
            }
        },
        {
            "event": {
                "type": "uri",
                "value": "http://www.wikidata.org/entity/Q1433432"
            },
            "eventLabel": {
                "type": "literal",
                "value": "Ahlhorner Heide Airbase",
                "xml:lang": "en"
            },
            "lat": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "52.885"
            },
            "lon": {
                "datatype": "http://www.w3.org/2001/XMLSchema#double",
                "type": "literal",
                "value": "8.2325"
            }
        }
    ]

app.run(host="localhost", port=3000)