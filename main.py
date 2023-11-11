from datetime import datetime
import time
from json import dumps
import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

KAFKA_TOPIC_NAME = "random_numbers"
KAFKA_BOOTSTRAP_SERVERS = '127.0.0.1:9093'
RANDOM_NUMBER_RANGE = (1, 10000)
NUMBER_OF_MESSAGES = 3

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    for i in range(NUMBER_OF_MESSAGES):
        try:
            message = {}
            message_timestamp = datetime.now()
            print("Printing message id: " + str(NUMBER_OF_MESSAGES - i))
            message["id"] = str(NUMBER_OF_MESSAGES - i)
            #message["timestamp"] = message_timestamp.strftime("%Y-%m-%d %H:%M:%S")
            random.seed(datetime.now().second)
            #message['value'] = random.randint(*RANDOM_NUMBER_RANGE)

            #print("Show message topic: " + KAFKA_TOPIC_NAME)
            print("Message: ", message)

        except Exception as ex:
            print("Event Failed. ")
            print(ex)

        time.sleep(1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
