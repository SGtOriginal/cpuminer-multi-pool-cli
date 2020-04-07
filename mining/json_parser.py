import json
from collections import namedtuple


def _json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())


def json2obj(data: str):
    return json.loads(data, object_hook=_json_object_hook) if len(data.strip()) > 0 else None
