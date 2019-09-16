import random
import statistics
import matplotlib.pyplot as plt
import time

def simulate(sims):
    total_pads = 10
    sim = 0
    results = []

    while sim < sims:
        current_pad = 0
        jumps = 0
        while current_pad < total_pads:
            jump_length = random.randint(1, total_pads - current_pad)
            current_pad = current_pad + jump_length
            jumps += 1
        results.append(jumps)
        sim += 1
    
    return statistics.mean(results)

simulations = 10000
sim_size = 10000

counter = 0
calculated_mean = []

start = time.time()

while counter < simulations:
    calculated_mean.append(simulate(sim_size))
    counter += 1

answer = statistics.mean(calculated_mean)

end = time.time()
time_taken = end - start

print(str(simulations) + " simulations of size " + str(sim_size) + " were completed, returning " + str(answer) + ". Runtime was " + str(time_taken) + "s.")

plt.hist(calculated_mean, bins=40, density=True)
plt.show()