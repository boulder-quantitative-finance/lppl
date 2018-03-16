'''
Help from https://www.ricequant.com/community/topic/427/
Thanks ricequant!
Updated implementation of the LPPL model running on the s&p 500
'''
import lib.lppl as lppl
from matplotlib import pyplot as plt
import datetime
import numpy as np
import pandas as pd
import seaborn as sns

sns.set_style('white')

# respective minimum and maximum values ​​of the seven parameters fitting process
limits = (
    [8.4, 8.8],     # A :
    [-1, -0.1],     # B :
    [350, 400],     # Critical Time :
    [.1, .9],       # m :
    [-1, 1],        # c :
    [12, 18],       # omega
    [0, 2 * np.pi]  # phi :
)
x = lppl.Population(limits, 20, 0.3, 1.5, .05, 4)
for i in range(2):
    x.Fitness()
    x.Eliminate()
    x.Mate()
    x.Mutate()

x.Fitness()
values = x.BestSolutions(3)
for x in values:
    print(x.PrintIndividual())

data = pd.DataFrame({'Date':values[0].getDataSeries()[0],'Index':values[0].getDataSeries()[1],'Fit1':values[0].getExpData(),'Fit2':values[1].getExpData(),'Fit3':values[2].getExpData()})
data = data.set_index('Date')
data.plot(figsize=(14,8))
plt.show(block=True)