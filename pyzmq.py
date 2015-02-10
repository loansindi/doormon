import zmq
from subprocess import call
 
context = zmq.Context.instance()
socket = context.socket(zmq.SUB)
socket.connect("tcp://frontdoor.pumpingstationone.org:5556")
socket.connect("tcp://backdoor.pumpingstationone.org:5556")
socket.connect("tcp://bob.ad.pumpingstationone.org:5556")
socket.connect("tcp://10.100.203.10:5556")
socket.setsockopt(zmq.SUBSCRIBE, b"door")
 
print("waiting")
while True:
    topic, message = socket.recv_multipart()
    if topic == "b'door.bell'":
        call(["echo 'Ding Dong' > /srv/doormon/irc/chat.freenode.org/#pumpingstationone/in"])
        print("ding dong")
