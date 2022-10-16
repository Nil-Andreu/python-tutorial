# Benchmarking & Profiling

We can develop a simulation of the evolution of the particle depending on its initial position.

Then, we can develop a tests and run it with *pytest* to make sure that we have written it correctly.

Once we have the test, we can use it as a **benchmark** with the tool of *pytest-benchmark*. So we can include in the code the following:
```
    def test_evolve(benchmark):
        ...

        benchmark(simulator.evolve(0.1))
```

