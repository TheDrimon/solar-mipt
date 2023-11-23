import matplotlib.pyplot as plt
import numpy as np

f = np.loadtxt(open("cccccccgd.txt","r"))
#print(f)
#print(f.values)
plt.subplot(311)
plt.plot(f[:,0], f[:,1])

plt.subplot(312)
plt.plot(f[:,0], f[:,2])

plt.subplot(313)
plt.plot(f[:,1], f[:,2])

plt.show()