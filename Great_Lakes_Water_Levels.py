""""
To use this notebook for your in-class assignment, you will need these 
files, which you shoujld have downloaded:
* mhu.csv -- Lake Michigan and Lake Huron
* sup.csv -- Lake Superior
* eri.csv -- Lake Erie
* ont.csv -- Lake Ontario

As instructed in the in-class activity notebook for today, you are 
only expected to complete one PART below. Do not worry if your group 
is not big enough to finish all parts below, but if you have extra 
time, you're welcome to do so.
""""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# PART 1
# Using the Michigan/Huron Dataset, plot the Water Level, the second 
# column, as a function of time years

mhu = pd.read_csv('mhu.csv')
plt.plot(mhu.loc[:,"time"],mhu.loc[:,"lake average"])
plt.show()

# PART 2
# Using the Superior Dataset, plot the Water Level, the second column, 
# as a function of time years

sup = pd.read_csv('sup.csv')
plt.plot(sup.loc[:,"year"],sup.loc[:,"lake levels"])
plt.show()

# PART 3
# Using the Erie Dataset, plot the Water Level, the second column, 
# as a function of time years

eri = pd.read_csv('eri.csv')
plt.plot(eri.loc[:,"time"],eri.loc[:,"water level"])
plt.show()

# PART 4
# Using the Ontario Dataset, plot the Water Level, the second column, 
# as a function of time years

ont = pd.read_csv('ont.csv')
plt.plot(ont.loc[:,"year"],ont.loc[:,"Lake Ontario annual averages"])
plt.show()

# PART 5
# Using the Michigan/Huron and Superior Datasets, plot the 
# Michigan/Hurion Water Level vs Superior Water Level to see if there 
# is any correlation between the water levels.

plt.scatter(mhu.loc[:,"lake average"],sup.loc[:,"lake levels"])
plt.show()


# PART 6
# Using the Michigan/Hurion and Erie Datasets, plot the 
# Michigan/Huron Water Level vs Erie Water Level to see if there is 
# any correlation between the water levels.

plt.scatter(mhu.loc[:,"lake average"],eri.loc[:,"water level"])
plt.show()


# PART 7
#Using the Superior and Ontario Datasets, plot the Superior Water 
# Level vs Ontario Water Level to see if there is any correlation 
# between the water levels.

plt.scatter(sup.loc[:,"lake levels"],ont.loc[:,"Lake Ontario annual averages"])
plt.show()
