import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

SOME_BUCKET = os.getenv('SOME_BUCKET')

def handler(event, context):
  logger.info("Incoming event: {}".format(event))
  logger.info("Environment variables: {}".format(SOME_BUCKET))

  return {
    "statusCode": 200,
    "body": "Goodbye from another lambda!"
  }