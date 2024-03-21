import matplotlib.pyplot as plt
import numpy as np

xpoints=np.array([1,2,3,4,5,6,7])
ypoints=np.array([34,45,40,32,40,42,36])

plt.xlabel("Days")
plt.ylabel("Temperature")

plt.plot(xpoints,ypoints,linestyle="dotted",marker='o')
plt.show()