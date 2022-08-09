from matplotlib import pyplot as plt
import numpy as np

x,y = [x for x in range(10)] , np.random.randint(0,10,size=10)
print("x : {}".format(x))
print("y : {}".format(y))

fig = plt.figure(figsize=(10,5))

ax_line = fig.add_subplot(2,3,1)
ax_line.plot(x,y)

ax_scatter = fig.add_subplot(2,3,2)
ax_scatter.scatter(x,y)

print(fig.show())