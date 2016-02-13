"""
CityOfBoston.gov API query functions

"""
import json
from mjclawar_rarshad import reference
import urllib.request


def api_query(base_url, limit=100, order=None, select=None, where=None):
    query_url = get_query_url(base_url, limit, order, select, where)
    response = urllib.request.urlopen(query_url).read().decode('utf-8')
    r = json.loads(response)
    s = json.dumps(r, sort_keys=True, indent=2)
    return s


def get_query_url(base_url, limit, order, select, where):
    # TODO make me in auth.json
    query_url = base_url + '$$app_token=%s&' % reference.api_token + '$limit=%s' % limit

    if order is not None:
        assert isinstance(order, str)
        query_url += '&$order=%s' % order + '%20DESC'

    if select is not None:
        assert isinstance(select, list)

    if where is not None:
        assert isinstance(where, str)

    return query_url
