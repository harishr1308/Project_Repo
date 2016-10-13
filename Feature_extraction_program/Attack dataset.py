#!/usr/bin/python
import time
import random

IPs = ['199.72.81.55','unicomp6.unicomp.net','199.120.110.21','129.94.144.152','205.189.154.54','205.212.115.106','199.58.68.55','129.96.165.32','206.190.155.55','198.59.69.56']
Urls = ['"GET /history/apollo/ HTTP/1.0"','"GET /shuttle/countdown/ HTTP/1.0"','"GET /shuttle/missions/sts-73/mission-sts-73.html HTTP/1.0"','"GET /shuttle/countdown/liftoff.html HTTP/1.0"','"GET /images/KSC-logosmall.gif HTTP/1.0"']
resp_code = [200,302,404]
size = [6254,4569,4562,4587,362]
for i in range(0,100):
    print (IPs[random.randrange(10)], '- -',time.strftime('[%d/%m/%Y:%I:%M:%S +5.30]'), Urls[random.randrange(5)], resp_code[random.randrange(3)], size[random.randrange(5)],'\n')
    time.sleep(random.randrange(1,5))
