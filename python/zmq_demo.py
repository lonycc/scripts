#-*- coding=utf-8 -*-

# 发布 - 订阅 模式
# 客户端
import sys
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)

print("从服务端获取更新...")
socket.connect("tcp://localhost:5556")

# Subscribe to zipcode, default is NYC, 10001
zip_filter = sys.argv[1] if len(sys.argv) > 1 else "10001"

# Python 2 - ascii bytes to unicode str
if isinstance(zip_filter, bytes):
    zip_filter = zip_filter.decode('ascii')
socket.setsockopt_string(zmq.SUBSCRIBE, zip_filter)

# Process 5 updates
total_temp = 0
for update_nbr in range(5):
    string = socket.recv_string()
    zipcode, temperature, relhumidity = string.split()
    total_temp += int(temperature)

print("Average temperature for zipcode '%s' was %dF" % (
      zip_filter, total_temp / update_nbr)
)

# 服务端
import zmq
from random import randrange

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

while True:
	zipcode = randrange(1, 100000)
	temperature = randrange(-80, 135)
	relhumidity = randrange(10, 60)

	socket.send_string("%i %i %i" % (zipcode, temperature, relhumidity))
##################################################################################

# 请求 - 应答 模式
# 客户端
import zmq

context = zmq.Context()
print("Connecting to hello world server")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
print("发送请求")
socket.send(b"Hello")
message = socket.recv()
print("获得应答 [ %s ]" % message)
socket.close()


# 服务端
import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
message = socket.recv()
print("接收到请求: %s" % message)
time.sleep(1)
socket.send(b"got it")
socket.close()
##################################################################################

# 生产者 - 消费者模式
# 客户端
import sys
import time
import zmq

context = zmq.Context()
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:5557")
sender = context.socket(zmq.PUSH)
sender.connect("tcp://localhost:5558")

while True:
    s = receiver.recv()
    sys.stdout.write('.')
    sys.stdout.flush()
    time.sleep(int(s)*0.001)
    sender.send(b'')
    
# 服务端
import zmq
import random
import time

try:
    raw_input
except NameError:
    # Python 3
    raw_input = input

context = zmq.Context()
sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:5557")

sink = context.socket(zmq.PUSH)
sink.connect("tcp://localhost:5558")

print("Press Enter when the workers are ready: ")
_ = raw_input()
print("Sending tasks to workers…")

sink.send(b'0')
random.seed()
total_msec = 0
for task_nbr in range(100):
    workload = random.randint(1, 100)
    total_msec += workload
    sender.send_string(u'%i' % workload)

print("Total expected cost: %s msec" % total_msec)
time.sleep(1)
