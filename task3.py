import numpy as np
from root_numpy import root2array
import matplotlib
import matplotlib.pyplot as plt
import cPickle as pickle
import deepdish.io as io

ttbar = root2array('ttbar.root')
qcd = root2array('qcd.root')
wjets = root2array('wjets.root')

matplotlib.rcParams.update({'font.size': 16})
fig = plt.figure(figsize=(11.69, 8.27), dpi=100)

bins = np.linspace(min(min(ttbar['NMuon']), min(qcd['NMuon']), min(wjets['NMuon'])), max(max(ttbar['NMuon']), max(qcd['NMuon']), max(wjets['NMuon'])), 10)

_ = plt.hist([ttbar['NMuon'], qcd['NMuon'], wjets['NMuon']], stacked=True, label=[r'$t\overline{t}$', 'QCD', 'wjets'], alpha = 0.5, histtype='stepfilled', normed=False, bins=bins, weights=[ttbar['EventWeight'], qcd['EventWeight'], wjets['EventWeight']])

plt.xlabel('NMuon')
plt.ylabel('Number of Events')
plt.yscale('log')
plt.legend()
plt.plot()
plt.savefig('task3.pdf')

io.save('wj_nmuons.h5', wjets['NMuon'])
#new_df = io.load('wj_nmuons.h5')
#print new_df

pickle.dump(wjets['NMuon'], open('wj_nmuons.pkl', 'wb'))
#test = pickle.load(open('wj_nmuons.pkl', 'rb'))
#print test
