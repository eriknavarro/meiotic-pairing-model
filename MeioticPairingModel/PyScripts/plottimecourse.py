import subprocess
import matplotlib.pyplot as plt
import os
import random
import shutil
import time
import fileinput
import glob
import math
import matplotlib.pyplot as plt
from statistics import mean
from statistics import stdev
from scipy.stats import sem
# define empty list
WT = [];
CSM4 = [];
NDJ1 = [];
Timesteps = []
Bouquet = [];

# open file and read the content in a list
with open('WT.txt', 'r') as filehandle:
    WT = [current_place.rstrip() for current_place in filehandle.readlines()]
filehandle.close()
WT = [float(item) for item in WT]
# open file and read the content in a list
with open('CSM4.txt', 'r') as filehandle:
    CSM4 = [current_place.rstrip() for current_place in filehandle.readlines()]
filehandle.close()
CSM4 = [float(item) for item in CSM4]
# open file and read the content in a list
with open('NDJ1.txt', 'r') as filehandle:
    NDJ1 = [current_place.rstrip() for current_place in filehandle.readlines()]
filehandle.close()
with open('CSM4STD.txt', 'r') as filehandle:
    CSM4STD = [current_place.rstrip() for current_place in filehandle.readlines()]
CSM4STD = [float(item) for item in CSM4STD]
CSM4STD = [(1.96*number / math.sqrt(100)) for number in CSM4STD]
filehandle.close()
NDJ1 = [float(item) for item in NDJ1]
# open file and read the content in a list
with open('Timesteps.txt', 'r') as filehandle:
    Timesteps = [current_place.rstrip() for current_place in filehandle.readlines()]
Timesteps = [float(item) for item in Timesteps]
filehandle.close()
with open('Bouquet.txt', 'r') as filehandle:
    Bouquet = [current_place.rstrip() for current_place in filehandle.readlines()]
Bouquet = [float(item) for item in Bouquet]
filehandle.close()
with open('WTSTD.txt', 'r') as filehandle:
    WTSTD = [current_place.rstrip() for current_place in filehandle.readlines()]
WTSTD = [float(item) for item in WTSTD]
WTSTD = [(1.96*number / math.sqrt(100)) for number in WTSTD]
filehandle.close()
with open('NDJ1STD.txt', 'r') as filehandle:
    NDJ1STD = [current_place.rstrip() for current_place in filehandle.readlines()]
NDJ1STD = [float(item) for item in NDJ1STD]
NDJ1STD = [(1.96*number / math.sqrt(100)) for number in NDJ1STD]
filehandle.close()

plt.errorbar(Timesteps,WT, WTSTD, errorevery=50, label = 'WT',color = 'Black')
plt.errorbar(Timesteps,NDJ1,NDJ1STD, errorevery=51, label='$\it{ndj1Δ}$',color = 'Purple')
plt.errorbar(Timesteps,CSM4,CSM4STD, errorevery=52, label='$\it{csm4Δ}$',color = 'Green')
plt.xlabel('Time(seconds)')
plt.ylabel('Percent Of Paired Nodes')
plt.legend()

plt.ylim(0,100)
plt.show()
   

