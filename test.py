import time
import random
import matplotlib.pyplot as plt
from BST import BST
from d import D
import sys

n = 10000
sys.setrecursionlimit(10**6)
#data = random.sample(range(1, n+1), n)

data = list(range(2, n+2))


# d = D(0.8,1)
# d_insert_times = []
# for i in data:
#     print(i)
#     start_time = time.time()
#     d.insert(i)
#     end_time = time.time()
#     delta_time = end_time-start_time
#     print(delta_time)
#     d_insert_times.append(delta_time)

bst = BST(1)
bst_insert_times = []
bsts = []
for i in range(10):
    bsts.append(BST(1))
items = list(range(1,n+1))
avg_time = 0
total_time = 0
for i in data:
    print(i)
    for b in bsts:
        start_time = time.time()
        b.insert(i)
        end_time = time.time()
        delta_time = end_time-start_time
        total_time = total_time + delta_time
    avg_time = total_time / len(bsts)
    bst_insert_times.append(avg_time)
    total_time = 0
plt.plot(items,bst_insert_times)
#plt.plot(items,d_insert_times)
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