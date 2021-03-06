from sanic import Sanic, response
# from sanic.log import logger, LOGGING_CONFIG_DEFAULT as LOG_CONFIG
from threading import Thread
import socket
from sanic.response import json
import socketio
import time
import pdb
import sys
from sanic_cors import CORS, cross_origin
import random
import datetime


sio = socketio.Client(async_mode="sanic", cors_allowed_origins=[])
app = Sanic(name = 'ney')
CORS(app)

app.config['CORS_SUPPORTS_CREDENTIALS'] = True

@sio.on("xiaotiancai")
def on_xtc(data):
  print('my id is', sio.sid)
  print("Received message")

# L1_trades_derivatives = lis.messageStorage()
# L1_listener_derivatives = lis.TradePriceCollector("spark.casper.mds_feedos-dc", ["md.*.L1.*"], 8, L1_trades_derivatives)
# thread_L1_dc = Thread(target = L1_listener_derivatives.consume)
# thread_L1_dc.start()


def compute_index():
  data = {
    'ts': str(datetime.datetime.now()),
    'HSI': 29000 + random.uniform(-200,200),
    'HSCEI': 11000 + random.uniform(-200,200),
    'NKY': 29000 + random.uniform(-200,200),
    'HSTECH': 9000 + random.uniform(-100,100),
    'TOPIX': 1400 + random.uniform(-100,100)
  }
  return data

ns = "/derivatives_trade"
def getDerivatives(): 
    while True:
        # print(L1_trades_derivatives.message())
        # pdb.set_trace()
        data = compute_index()
        print(data)
        sio.emit('xiaotiancai', data, namespace=ns)
        time.sleep(1)

@sio.on('connect', namespace='/chat')
def on_connect():
    print("I'm connected to the /chat namespace!")

def main(args=None):
    getDerivatives()
    app.run(host='localhost', port=5050, workers=4)

if __name__=="__main__":
    main(sys.argv)