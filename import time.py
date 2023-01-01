import time
import random
t = time.time()
print(f"{t=}")

#measure computational latency

for _ in range(10000000):
    random.random()**random.random()

t1 = time.time()
print(f"{t1=}")
delta_t = t1-t
print(f"\nLatency: {delta_t:.2f}s")