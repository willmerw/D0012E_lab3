import time
import random
import matplotlib.pyplot as plt
from BST import BST
from d import D

n = 1000000
data = random.sample(range(1, n+1), n)

bst = BST(random.randrange(1,n))
bst_insert_times = []

items = list(range(1,n+1))
for i in data:
    start_time = time.time()
    bst.insert(i)
    end_time = time.time()
    delta_time = end_time-start_time
    bst_insert_times.append(delta_time)

plt.plot(items,bst_insert_times)
plt.show()




# def plotter(k, time, name):
#     save = name + ".pdf"
#     plt.plot(time, k, label=name)
#     plt.ylabel("Time")
#     plt.xlabel("k")
#     plt.legend()
#     plt.savefig(save)
#
# def nPlotter(n_list,time):
#     plt.plot(time, n_list)
#     plt.ylabel("Time")
#     plt.xlabel("n")
#     plt.show()