from parliament import Context

import logging
import random
import time

logging.basicConfig(level=logging.INFO)

 
def main(context: Context):
    """ 
    Function template
    The context parameter contains the Flask request object and any
    CloudEvent received with the request.
    """

    if context.cloud_event is not None:
        logging.info(context.cloud_event['source'])
        logging.info(context.cloud_event['type'])

    else:
        sleeptime = random.uniform(0, 2)
        time.sleep(sleeptime)
        logging.info(f"Request delay ${sleeptime}")

    return { "message": "Howdy!" }, 200
