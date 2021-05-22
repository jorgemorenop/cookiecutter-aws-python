import os
import json


def load_sample(function_name, event_name):
    return json.load(open(os.path.join(
        '..', '..', 'events', function_name, event_name+'.json'
    )))
