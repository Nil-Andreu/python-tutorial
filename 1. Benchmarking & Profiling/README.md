# Benchmarking & Profiling

We can develop a simulation of the evolution of the particle depending on its initial position.

Then, we can develop a tests and run it with *pytest* to make sure that we have written it correctly.

## Benchmarking
We will create a benchmark, in *benchmark.py*, where we will create 100 random particles.
Then, we can track how much time it  takes for us to run this program, with: *time python3 benchmark.py*. Where *time* is a command in the Unix system that keeps track of how much time it takes to run this command.
It gives you the following information:
- **real**: actual time spent running the process
- **user**: cumulative time spent by all the CPUs during computation
- **sys**: cumulative time spent by all the CPUs during system-related tasks (memory allocation, ...)


Once we have the test, we can use it as a **benchmark** with the tool of *pytest-benchmark*. So we can include in the code the following:
```
    def test_evolve(benchmark):
        ...

        benchmark(simulator.evolve(0.1))
```
So we are passing this **benchmark** resource as an argument of the function (this is called a fixture).
This way, we can keep track of how much time it takes to run an application.

So this way, we can keep track of how much time our code is in each version.
