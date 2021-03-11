#!/usr/bin/env python
# coding: utf-8

# # Surface Plots | Data Visualisation

# ## Surface Plots are used to 
# - Visualise Loss Functions in Machine Learning and Deep Learning
# - Visualise State or State Value Functions in Reinforcement Learning

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


a = np.array([1,2,3])
b = np.array([4,5,6,7])

a,b = np.meshgrid(a,b)
print(a)
print(b)


# In[3]:


fig = plt.figure()
axes = fig.gca(projection='3d')
plt.show()


# In[4]:


fig = plt.figure()
axes = fig.gca(projection='3d')
axes.plot_surface(a,b,a+b)
plt.show()


# In[5]:


fig = plt.figure()
axes = fig.gca(projection='3d')
axes.plot_surface(a,b,a**2+b**2,cmap='rainbow')
plt.show()


# In[6]:


a = np.arange(-1,1,0.02)
b = a

a,b = np.meshgrid(a,b)


# In[7]:


fig = plt.figure()
axes = fig.gca(projection='3d')
axes.plot_surface(a,b,a**2+b**2,cmap='rainbow')
plt.show()


# ## Contours
# - cut this surface plot by parallel planes

# In[9]:


fig = plt.figure()
axes = fig.gca(projection='3d')
axes.contour(a,b,a**2+b**2,cmap='rainbow')
plt.show()


# ## We can run this as a python script in terminal and there we can also rotate surfaces and see a 360 degree view
# **use**
# `from mpl_toolkits.mplot3d import Axes3d` 

# In[ ]:




