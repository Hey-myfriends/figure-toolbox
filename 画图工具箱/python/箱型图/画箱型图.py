#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.io import loadmat


# In[73]:


metrics = loadmat('E:\Desktop\PD多模态数据处理（宣武）\交叉验证\intra-subject result5\lstm模型\PM结果\paperResults.mat')
# metrics = loadmat(r'E:\Desktop\PD多模态数据处理（宣武）\交叉验证\统一架构实验结果\input=24，output=12\lstm_net19.mat')
p = metrics['p']
r = metrics['r']
print(r.shape)
listName = [chr(946),chr(945),chr(952),chr(948)]
rFz = r[:,:4]
rCz = r[:,4:8]
rO1 = r[:,8:]

#rrFz = pd.DataFrame(r[:,:4], columns = listName)
#rrCz = pd.DataFrame(r[:,4:8], columns = listName)
#rrO1 = pd.DataFrame(r[:,8:], columns = listName)


# In[83]:


#df = pd.DataFrame(rr, columns = ['Fz','Cz','O1'])
#df['label'] = [listName[int(i / length)] for i in range(df.shape[0])]


# In[86]:

fig, ax = plt.subplots(3,1, figsize=(6.3, 4.2))
boxprops = {'color':'k', 'linewidth':1.5}
medianprops = {'linestyle':'-','color':'black','linewidth':1.5}
whiskerprop = {'color':'black','linewidth':1.5}
capprop = {'color':'black','linewidth':1.5}
ax[0].boxplot(rFz, vert = True, sym = '.', labels = [''] * 4, boxprops = boxprops, medianprops = medianprops,
              whiskerprops = whiskerprop, capprops = capprop)
ax[1].boxplot(rCz, vert = True, sym = '.', labels = [''] * 4, boxprops = boxprops, medianprops = medianprops,
              whiskerprops = whiskerprop, capprops = capprop)
ax[2].boxplot(rO1, vert = True, sym = '.', labels = listName, boxprops = boxprops, medianprops = medianprops,
              whiskerprops = whiskerprop, capprops = capprop)
plt.tick_params(labelsize = 17, axis = 'x')
labels = ax[2].get_xticklabels()
for label in labels:
    label.set_fontname('Times New Roman')

name = ['Corr(Fz)', 'Corr(Cz)', 'Corr(O1)']
for axis, t in zip(ax, name):
    axis.yaxis.grid(True)
    axis.set_yticks(np.arange(0,1.1,0.5))
    axis.set_ylabel(t)
    axis.set_ylim([-0.35, 1.1])
    axis.grid(axis='y', c='k', alpha=0.3)
    # axis.spines['right'].set_visible(False)
    # axis.spines['left'].set_visible(False)
    # axis.spines['top'].set_visible(False)
    labels = axis.get_yticklabels()
    #for label in labels:
     #   label.set_fontname('Times New Roman')
plt.subplots_adjust(left=0, right=1, top=1, bottom=0, wspace=0, hspace=0.05)
plt.savefig('boxplot.tiff', format='tiff', bbox_inches='tight', dpi=300,  pad_inches=0)
# plt.show()



# In[ ]:




