import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from root_numpy import root2array

ttbar = root2array('ttbar.root')
qcd = root2array('qcd.root')

matplotlib.rcParams.update({'font.size': 16})
fig = plt.figure(figsize=(11.69, 8.27), dpi=100)
bins = np.linspace(0, 10, num=11)
_ = plt.hist([ttbar['NJet'], qcd['NJet']], stacked=True, normed=False, color = ['green','red'], bins=bins, histtype='stepfilled', weights=[ttbar['EventWeight'], qcd['EventWeight']], alpha=0.5, label=[r'$t\overline{t}$', 'QCD'], linewidth=2)
plt.xlabel('NJet')
plt.yscale('log')
plt.ylabel('Number of Events')
plt.legend()
plt.plot()
plt.show()
plt.savefig('task2.pdf')
