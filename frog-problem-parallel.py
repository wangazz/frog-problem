import random
import statistics
import matplotlib.pyplot as plt
import time
from multiprocessing import Pool
# print("Number of processors: ", mp.cpu_count())

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

simulations = 10
sim_size = 10

calculated_mean = []

pool = Pool(4)

start = time.time()

answers = pool.map_async(simulate(sim_size), [i for i in range(simulations)])

end = time.time()
time_taken = end - start

pool.close()
# pool.join()

print(answers)
print(answers[0])

# print(str(simulations) + " simulations of size " + str(sim_size) + " were completed, returning " + str(answer) + ". Runtime was " + str(time_taken) + "s.")

# plt.hist(calculated_mean, bins=40, density=True)
# plt.show()