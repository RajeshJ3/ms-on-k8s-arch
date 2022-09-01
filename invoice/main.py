from connection import get_message

from service import run

if __name__ == "__main__":
    # get message from the channel, if any
    data = get_message()

    # calling the service
    run(data=data)
