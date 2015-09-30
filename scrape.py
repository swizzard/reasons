import re

import requests


def get_reasons(req):
    params = {'search': 'reasons',
            'page': idx}

    posts = requests.get(url, params=params).json()['posts']

    bodies = [post['post_content'] for post in posts]

    p = re.compile(r'^(?:<h2>)?\d+\.(?P<reason>.+?)(?:(\<\/h2\>)?\r)?$', re.M)
    for body in bodies:
        for m in re.finditer(p, body):
            yield m.group('reason')


 def get_all_reasons(): 
    idx = 0
    saw_stopiteration = False
    url = 'http://elitedaily.com/api/get_search_results'
    while True:
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



