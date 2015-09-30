import re

import requests


def get_reasons(req):
    posts = req.json()['posts']

    bodies = [post['post_content'] for post in posts]

    p = re.compile(r'^(?:<h2>)?\d+\.(?P<reason>.+?)(?:(\<\/h2\>)?\r)?$', re.M)
    for body in bodies:
        for m in re.finditer(p, body):
            yield m.group('reason').strip()


def get_all_reasons(): 
    idx = 1
    url = 'http://elitedaily.com/api/get_search_results'
    req = requests.get(url, params={'search': 'reasons', 'page': 1})
    page_count = req.json()['pages']
    reasons = get_reasons(req)
    for reason in reasons:
        yield reason
    while idx < pages:
        req = requests.get(url, params={'search': 'reasons', 'page': idx})
        reasons = get_reasons(req)
        while True:
            try:
                yield next(reasons)
            except StopIteration:
                if second_empty:
                    raise
                else:
                    saw_stopiteration = True
                    idx += 1
                    continue
            else:
                saw_stopiteration = False



