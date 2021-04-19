import pandas as pd
d = pd.read_csv("therms.csv")
d.columns


from statsmodels.graphics.factorplots import interaction_plot
from matplotlib import pyplot as plt

fig = interaction_plot(d['number'],d['status'],d['time'])
plt.xticks([])
plt.xlabel("")
plt.savefig("congruent-incongruent.png")


from statsmodels.formula.api import ols
ols_d = ols(formula = "time ~ number * status",data = d)
myfits = ols_d.fit()
plt.clf()
f = plt.figure()
a = f.gca()

ip1 = interaction_plot(d['number'], d['status'], myfits.fittedvalues, plottype="line",ax = a,)

ip2 = interaction_plot(d['number'], d['status'], d['time'], plottype='scatter',ax = a,)
lines, labels = f.axes[0].get_legend_handles_labels()
a.legend_ = None

f.legend(lines[0:2], labels[0:2], loc = 'upper left', bbox_to_anchor=(0.15,0.85))
plt.xticks([])
plt.xlabel("")
plt.savefig("congruent-incongruent-line.png")
