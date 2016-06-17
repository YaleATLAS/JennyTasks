import numpy as np
from root_numpy import root2array
import pandas as pd

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
muon_df = df[[key for key in df.keys() if key.startswith('trigger')]]
count = 0
for bool in muon_df.values:
	if bool==False:
		count+=1
print count

#construct the four-vector of all jets
