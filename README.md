There are a few ways you could measure the latency of volatility index calculation in Python:

Use the time module: You can use the time module to measure the elapsed time before and after the calculation, and then calculate the latency as the difference between these two times.

Use the perf_counter function: You can use the perf_counter function from the time module to measure the elapsed time in higher precision, which may be useful if you need to measure very small latencies.

Use a profiling tool: You can use a profiling tool such as cProfile or the built-in %timeit magic function in Jupyter notebooks to measure the latency of the calculation. These tools will give you more detailed information about the performance of your code, including how long each part of the calculation takes to run.

Here is an example of how you could use the time module to measure the latency of a volatility index calculation:

