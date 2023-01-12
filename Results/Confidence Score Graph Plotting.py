#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

fig, ax = plt.subplots()

y = [0.9721, 0.9745, 0.9746, 0.9749, 0.9750]
x = ['AVG 4v5', 'AVG 5v4', 'AVG 6v3', 'AVG 7v2', 'AVG 8v1']

plt.ylim(0.97, 0.9755)
plt.bar(x, y, color ='blue', width = 0.4)
ax.plot(x,y)

plt.xlabel('Train:Test Dataset')
plt.ylabel('Confidence Score')
plt.title('Confidence Score Graph')

plt.show()

