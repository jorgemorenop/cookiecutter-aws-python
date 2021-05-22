# Python internal libraries
import json

# Project libraries
from . import config as cfg


def dummy_function(a, b):
    return a+b


def main(event):
    """Sample pure Lambda function

    :type event: dict
    :param event: Event received by the lambda function.
    :type context: dict or None
    :param event: Lambda Context runtime methods and attributes
    :rtype: dict
    :return: Lambda API response
    """

    print(f"[START] Starting execution. Environment: {cfg.ENV_ENVIRONMENT}")
    print(json.dumps(event))
    print(f"2 + 2 = {dummy_function(2, 2)}")
    print("[END] Execution finished.")
    return {"statusCode": 200, "body": json.dumps({"message": "Process finished"})}
