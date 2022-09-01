import json

from config import (
    SUBSCRIPTION_TIMEOUT,
    CURRENT_CHANNEL,
    NEXT_CHANNEL,
    NOTIFY_CHANNEL,
)

from db import redis_db

def push(data: dict, channel: str = NEXT_CHANNEL, next: bool = True, notify: bool = False) -> bool:

    # if next, push message to the next channel
    if next:
        channel = NEXT_CHANNEL

    # if notify, push message to the notify channel
    if notify:
        channel = NOTIFY_CHANNEL
    l_len = redis_db.lpush(channel, json.dumps(data))
    return bool(l_len)


def get_message():
    print("Searching/listening for messages...")
    data = redis_db.brpop(CURRENT_CHANNEL, timeout=SUBSCRIPTION_TIMEOUT)
    if not data:
        print(f"Not messages found in channel: {CURRENT_CHANNEL}")
        exit()
    try:
        # decode
        _, msg = data
        return json.loads(msg.decode("utf-8"))
    except json.JSONDecodeError as e:
        print("JSON Decode error:", str(e))
    except Exception as e:
        print("Decoding error:", str(e))

    # for any failure case, exit
    exit()
