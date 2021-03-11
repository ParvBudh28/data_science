#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[2]:


X = pd.read_csv("./Training Data/Linear_X_Train.csv").values
Y = pd.read_csv("./Training Data/Linear_Y_Train.csv").values


# ## Steps
# 1. Save Numpy theat_list in a numpy file using np.save()
# 2. create interactive_plot.py

# In[7]:


theta_list = np.load('theta_list.npy')
T0 = theta_list[:,0]
T1 = theta_list[:,1]


# In[8]:


plt.ion()
# to use interactive mode


# In[9]:


for i in range(50):
    y_ = T1[i]*X + T0
    plt.scatter(X,Y)
    plt.plot(X,y_,color='red')
    plt.draw()
    plt.pause(0.01)
    plt.clf() # destroys previous object


# In[ ]:




