import cProfile

from benchmark import benchmark

pr = cProfile.Profile()
pr.enable()
benchmark()
pr.disable()
pr.print_stats()


"""
The output of this is the following:
- ncalls: number of times the function is called
- tottime: total time spent in the function without considering calls to the other functions. The most important metric --> time spent in the function excluding the subcalls --> tells where the bottleneck is.
- cumtime: total time spent in the function + considering calls to the other functions
- percall: time spent for a single call of the function: (tottime or cumtime) / ncalls
- filename:lineno: the filename and corresponding line numbers
"""