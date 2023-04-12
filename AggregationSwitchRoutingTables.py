# Fat Tree Algorithm 1: Generating aggregation switch routing tables

import sys

k = 4 # int(sys.argv[1])

def addPrefix(prefix):
    print(prefix)

def addSuffix(suffix):
    print(suffix)  

for pod in range(0, k):
    for switch in range(k//2, k):
        for subnet in range(0, k//2):
            addPrefix("10.{pod}.{switch}.1, 10.{pod}.{subnet}.0/24".format(pod = pod, switch = switch, subnet = subnet))
        addPrefix("10.{pod}.{switch}.0".format(pod = pod, switch = switch))
        for host in range(2, (k//2)+2):
            addSuffix("10.{pod}.{switch}.1 , 0.0.0.{host}/8, ({calc})".format(pod = pod, switch = switch, host = host, calc = int(((host - 2 + switch) % (k/2) + (k/2)))))

      