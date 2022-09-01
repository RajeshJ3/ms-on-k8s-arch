from db import redis_db

import json

def publish(data, channel) -> None:
    '''
    Publish message to a particular channel
    '''
    resp = redis_db.publish(channel, json.dumps(data))
    print(f"Published to {channel}, now #{resp} message(s) pending.")

def subscribe(channel, handler_function, *args, **kwargs):
    '''
    Scuscribe to a channel to get messages.
    '''
    pubsub = redis_db.pubsub()
    pubsub.subscribe(channel)

    for index, message in enumerate(pubsub.listen()):
        if not index: continue

        data = message["data"]
        try: handler_function(json.loads(data), *args, **kwargs)
        except json.JSONDecodeError as e: print("[JSONDecodeError]", str(e))
        except Exception as e: print("[Exception]", str(e))
