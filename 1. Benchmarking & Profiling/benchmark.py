from random import uniform
from main import Particle, ParticleSimulator

# We can create a representative process called benchmark
def benchmark():
    particles = [
        Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-1.0, 1.0))
        for i in range(100)
    ]

    simulator = ParticleSimulator(particles)
    simulator.evolve(0.1)


if __name__ == '__main__':
    benchmark()
