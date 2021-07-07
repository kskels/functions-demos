from parliament import Context

import logging

logging.basicConfig(level=logging.INFO)

 
def main(context: Context):
    """ 
    Function template
    The context parameter contains the Flask request object and any
    CloudEvent received with the request.
    """

    logging.info(context.cloud_event['source'])
    logging.info(context.cloud_event['type'])

    return { "message": "Howdy!" }, 200
