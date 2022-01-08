import math
import matplotlib.pyplot as plt
from barplot_annotate_brackets import barplot_annotate_brackets
Failures =  [91, 71, 46];
Spaces = [1, 3, 5];
NTrials = 200;
zeta = 1.96;

Failures_Error = [ ((zeta/(NTrials*math.sqrt(NTrials)))*math.sqrt(x*(NTrials-x))) for x in Failures ];

SuccessPercentage = [ (NTrials-x)/NTrials for x in Failures ];
FailurePercentage = [ x/NTrials for x in Failures ];

print(SuccessPercentage)
print(FailurePercentage)
print(Failures_Error)
plt.bar(Spaces,FailurePercentage, width=1.0,align = 'center', edgecolor = 'black', alpha =.9, tick_label = ['0.8 micron', '1.0 micron', '1.2 micron'],capsize = 5, yerr=Failures_Error,color=['#1f77b4', 'C4', 'C1'])
#plt.xlabel("Nuclear Diameter")
plt.ylabel("Fraction of simulations with interlocks remaining")
plt.xlabel("Nuclear radius")
plt.ylim(0,1)
#barplot_annotate_brackets(0, 1, .1, Spaces, FailurePercentage, dh=.25, barh=.01)

plt.show()

#color=['Grey', 'Blue', 'C1']

#colors for nuc diam =['#1f77b4', 'C4', 'C1']

#colors for strains =['#545454', '#7d097d', '#0c7b0c']




