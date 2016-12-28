# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 23:10:19 2016

@author: vance
"""

from scipy import stats
import numpy as np
import  matplotlib.pyplot as plt
mu = 208.673314627
sigma = 47554.6326596

x = np.arange(-5,5,0.1)
print(x)
y = stats.norm.pdf(x,0,1)

plt.plot(x,y)
