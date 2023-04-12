# Fat Tree Algorithm 2: Generating core switch routing tables

k = 4 # int(sys.argv[1])

def addPrefix(prefix):
    print(prefix)

def addSuffix(suffix):
    print(suffix)

for j in range(1, k//2):
    for i in range(1, k//2):
        for destinationPod in range(0, k//2):
            addPrefix("10.{k}.{j}.{i}, 10.{destinationPod}.0.0/16, {destinationPod}".format(k = k, i = i, j = j, destinationPod = destinationPod))