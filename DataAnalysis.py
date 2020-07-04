import pandas as pd
import matplotlib as plt
import altair_viewer

# Create figure and axis objects
fig, ax = plt.subplots(
    nrows=3,
    ncols=1,
    sharex=True,
    sharey=False,
    gridspec_kw={'height_ratios': [2, 1, 1]},
    figsize=(15, 5))

# Set layout for 'Confirmed' cases
ax[0].plot(full_grouped['Confirmed'], color='red')
ax[0].set_ylim(ymin=0, ymax=None)
ax[0].set_ylabel('Confirmed')
ax[0].set_xlabel('Months')
ax[0].grid(True, which='major')

# Set layout for 'Deaths' cases
ax[1].plot(full_grouped['Deaths'], color='black')
ax[1].set_ylim(ymin=0, ymax=None)
ax[1].set_ylabel('Deaths')
ax[1].set_xlabel('Months')
ax[1].grid(True, which='major')

# Set layout for 'Recovered' cases
ax[2].plot(full_grouped['Recovered'], color='green')
ax[2].set_ylim(ymin=0, ymax=None)
ax[2].set_ylabel('Recovered')
ax[2].set_xlabel('Months')
ax[2].grid(True, which='major')

# Set general layout for figure (all axis)
fig.tight_layout()
plt.setp(ax[2].get_xticklabels(), rotation=45, horizontalalignment='right')
plt.show()


plt.show('Australia')
#plot('Germany')
#plot('France')
#plot('Spain')
#plot('Italy')

