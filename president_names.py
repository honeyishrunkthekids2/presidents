import requests

def test_pres():
    url = "https://api.duckduckgo.com/?q=presidents of the united states&format=json"
    response = requests.get(url)
    my_json = response.json()
    rt = my_json["RelatedTopics"]
    pln = ["Adams",
    "Arthur",
    "Biden",
    "Buchanan",
    "Bush",
    "Carter",
    "Cleveland",
    "Clinton",
    "Coolidge",
    "Eisenhower",
    "Fillmore",
    "Ford",
    "Garfield",
    "Grant",
    "Harding",
    "Harrison",
    "Hayes",
    "Hoover",
    "Jackson",
    "Jefferson",
    "Johnson",
    "Kennedy",
    "Lincoln",
    "Madison",
    "McKinley",
    "Monroe",
    "Nixon",
    "Obama",
    "Pierce",
    "Polk",
    "Reagan",
    "Roosevelt",
    "Taft",
    "Taylor",
    "Truman",
    "Trump",
    "Tyler",
    "Van Buren",
    "Washington",
    "Wilson"]

    for item in rt:
        for pres in pln:
            if item["Text"].find(pres) != -1:
                pln.remove(pres)

    assert(len(pln) == 0)
