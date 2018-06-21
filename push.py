from Adafruit_BME280 import *
from datadog import initialize as datadog_init
from datadog import api as datadog_api
from time import time
import os

datadog_options = {
  'api_key': os.environ['DATADOG_API_KEY'],
  'app_key': os.environ['DATADOG_APP_KEY']
}

datadog_init(**datadog_options)

sensor = BME280(t_mode=4, p_mode=4, h_mode=4)

degrees = sensor.read_temperature()
pascals = sensor.read_pressure()
hectopascals = pascals / 100
humidity = sensor.read_humidity()

datadog_api.Metric.send(
    metric='spacedragons.desks.temperature',
    points=(time(), degrees),
    type='gauge'
)

datadog_api.Metric.send(
    metric='spacedragons.desks.pressure',
    points=(time(), hectopascals),
    type='gauge'
)

datadog_api.Metric.send(
    metric='spacedragons.desks.humidity',
    points=(time(), humidity),
    type='gauge'
)

