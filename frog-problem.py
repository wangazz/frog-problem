import random
import statistics
import matplotlib.pyplot as plt
import time

def simulate(sims):
    total_pads = 10
    results = []

    for i in range(sims):
        current_pad = 0
        jumps = 0
        while current_pad < total_pads:
            jump_length = random.randint(1, total_pads - current_pad)
            current_pad = current_pad + jump_length
            jumps += 1
        results.append(jumps)
    
    return statistics.mean(results)

simulations = 1000
sim_size = 10000

calculated_mean = []

start = time.time()

for i in range(simulations):
    calculated_mean.append(simulate(sim_size))

answer = statistics.mean(calculated_mean)

end = time.time()
time_taken = end - start

print(str(simulations) + " simulations of size " + str(sim_size) + " were completed, returning " + str(answer) + ". Runtime was " + str(time_taken) + "s.")

plt.hist(calculated_mean, bins=40, density=True)
plt.show()