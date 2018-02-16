import json

from .const import DATA_PATH


def _get_data():
    try:
        with open(DATA_PATH) as f:
            return json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return dict(queue=[])


def _set_data_val(key, value):
    data = _get_data()
    data[key] = value
    with open(DATA_PATH, 'w') as f:
        json.dump(data, f)


def get_listener_id():
    return _get_data().get('listener_id')


def get_listener_name():
    return _get_data().get('listener_name', 'your friend')


def get_queue():
    return _get_data()['queue']


def get_key():
    return _get_data().get('api_key', '')


def get_channel():
    return _get_data()['channel']


def set_listener_id(id_):
    _set_data_val('listener_id', id_)


def set_listener_name(name):
    _set_data_val('listener_name', name)


def set_queue(queue):
    _set_data_val('queue', queue)


def set_key(api_key):
    _set_data_val('api_key', api_key)


def set_channel(channel):
    _set_data_val('channel', channel)
