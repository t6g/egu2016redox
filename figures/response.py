import numpy as np
import matplotlib.pyplot as plt

pH  = np.arange(3.0, 10.1, 0.1)
fpH = 10**(-0.2235*pH*pH + 2.7727*pH - 8.6)

fig = plt.figure()

lx = 0.05
ly = 0.90

ax1 = fig.add_subplot(211)
ax1.plot(pH, fpH, 'b-', linewidth=2)
ax1.plot([4.5, 4.5], [0, 1.2], 'k:') #, [5, 5], [0, 1.2], 'k:')
ax1.plot([5.5, 5.5], [0, 1.2], 'k:') #, [6, 6], [0, 1.2], 'k:')
ax1.plot([6.5, 6.5], [0, 1.2], 'k:') #, [7, 7], [0, 1.2], 'k:')
plt.xlabel('pH')
plt.ylabel('f(pH)')
plt.ylim([0, 1.2])
plt.text(lx, ly, '(a) CLM4Me', transform=ax1.transAxes)

TC = np.arange(-20, 51, 1)
TK = TC + 273.15
ymin = 0.01
ymax = 10.0
ftclmcn = np.exp(308.56*(1/71.02-1/(TK-227.13)))
ax2 = fig.add_subplot(212)
ax2.semilogy(TC, ftclmcn, 'b-', linewidth=2)
plt.semilogy([-2, -2], [ymin, ymax], 'k:')
plt.semilogy([4, 4], [ymin, ymax], 'k:')
plt.semilogy([8, 8], [ymin, ymax], 'k:')
plt.xlabel('Temperature ($^\circ$C)')
plt.ylabel('f(T)')
plt.ylim([ymin, ymax])
plt.text(lx, ly, '(b) CLM-CN', transform=ax2.transAxes)

plt.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.08)

fig.set_size_inches(4.5, 6.75)
plt.savefig('response.png')
plt.show()
