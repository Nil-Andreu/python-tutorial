# Benchmarking & Profiling

We can develop a simulation of the evolution of the particle depending on its initial position.

Then, we can develop a tests and run it with *pytest* to make sure that we have written it correctly.

## Benchmarking
We will create a benchmark, in *benchmark.py*, where we will create 100 random particles.
Then, we can track how much time it  takes for us to run this program, with: *time python3 benchmark.py*. Where *time* is a command in the Unix system that keeps track of how much time it takes to run this command.
It gives you the following information:
- **real**: actual time spent running the process. Includes CPUs processes + waiting for input/output operations.
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
So when running pytest, it will run the benchmark function several times and provide an statistic summary.

So this way, we can keep track of how much time our code is in each version.


## Bottlenecks
After we know how much time it takes for the execution of the pgoram, we can identify then which parts of the code will need to be tuned for performance.

We aim to identify the parts of the code that are small compared to the program.

There are two **profiling** modules in Python:
- *profile*: it adds significant overhead to the program execution.
- *cProfile*: also written in C, and adds small overhead and is more suitable.

We can use this module in different ways:
- As command python module: *python3 -m cProfile main.py*:
```
    python3 -m cProfile -s tottime main.py    # sort by a metric value
    python3 -m cProfile -o prof.out main.py     # save the output into the prof.out file
```

- As program python module:
```
    import cProfile
    cProfile.run("function()")
```

You could also warap a section of code:
```
    import cProfile
    pr = cProfile.Profile()
    pr.enable()     # start the profiling
    function()
    pr.disable()    # stop the profiling
    pr.print_stats()    # print the stats of profiling
```

- Interactively in IPython (notebook):
```
    %prun function()
```

