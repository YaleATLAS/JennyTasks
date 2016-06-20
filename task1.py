import numpy as np
from root_numpy import root2array, root2rec
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from rootpy.vector import LorentzVector

ttbar = root2array('ttbar.root')

#open ttbar.root
print ttbar

#print how many events and how many jets are present
df = pd.DataFrame(ttbar)
jet_df = df[[key for key in df.keys() if key.startswith('Jet')]]
print jet_df.shape

#print the average number of jets per event using 2 decimal places
def flatten(column):
	try:
	        return np.array([v for e in column for v in e])
	except (TypeError, ValueError):
        	return column
df_flat = pd.DataFrame({k: flatten(c) for k, c in jet_df.iteritems()})
print ("{:.2f}".format(float(len(df_flat))/len(jet_df)))

#print the number of events that do not pass the muon trigger (triggerIsoMu24 branch = False)
muont_df = df[[key for key in df.keys() if key.startswith('trigger')]]
count = 0
for bool in muont_df.values:
	if bool==False:
		count+=1
print count

#construct the four-vector of all jets
df['Jet_4V'] = [map(lambda args: LorentzVector(*args), zip(px, py, pz, e)) for (_, (px, py, pz, e)) in df[['Jet_Px', 'Jet_Py', 'Jet_Pz', 'Jet_E']].iterrows()]

#use the four-vectors to get the jet etas
Jet_Eta = np.array(float)
for jt in df['Jet_4V']:
	for n in range (0,len(jt)-1):
		Jet_Eta = np.append(Jet_Eta, jt[n].eta())


