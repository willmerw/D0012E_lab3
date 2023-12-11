import time
import random
import matplotlib.pyplot as plt
from BST import BST
from d import D
import sys

n = 30000
sys.setrecursionlimit(10**6)
#data = random.sample(range(1, n+1), n)


bst_insert_times = []
d_insert_times = []
items = []
steps = list(range(1,n+1,100))
avg_time = 0
total_time = 0

c_steps = []
c = 0.6

# while c < 1:
#     d = D(c,random.randint(1,n))
#     data = random.sample(range(1, n+1), n)
#     start_time = time.time()
#     for i in data:
#         print(i)
#         d.insert(i)
#     end_time = time.time()
#     delta_time = end_time - start_time
#     d_insert_times.append(delta_time)
#     c_steps.append(c)
#     c = c + 0.01
#
# plt.plot(c_steps,d_insert_times, label = "D")
# plt.legend()
# plt.show()



for step in steps:
    items.append(step)
    bst = BST(random.randint(1,step))
    data = random.sample(range(1, step), step-1)
    start_time = time.time()
    for i in data:
        print(i)
        bst.insert(i)
    end_time = time.time()
    delta_time = end_time-start_time
    bst_insert_times.append(delta_time)

    d = D(0.9,random.randint(1,n))
    start_time = time.time()
    for i in data:
        print(i)
        d.insert(i)
    end_time = time.time()
    delta_time = end_time - start_time
    d_insert_times.append(delta_time)


plt.plot(items,bst_insert_times, label = "BST")
plt.plot(items,d_insert_times, label = "D")
plt.legend()
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