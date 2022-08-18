import time
import random
import os

x = 0
while(True):
    print(x, flush=True)
    print(os.environ.get('ENV_VAR'), flush=True)
    x +=1
    time.sleep(random.randint(1,5))
