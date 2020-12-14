
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt


def str_from_array(array):
    list = [i[0][0] for i in array]
    return list

simple_efm = sio.loadmat('myPremodels_simple.mat')

simple_efm = simple_efm['modeli']
mets_c = str_from_array(simple_efm[0][0][0])

mets_e = str_from_array(simple_efm[0][0][1])

rxns = str_from_array(simple_efm[0][0][2])

sc = simple_efm[0][0][3]
se = simple_efm[0][0][4]
z = simple_efm[0][0][5]
sez = simple_efm[0][0][6]



print(mets_e)
print(sez.shape)
# x = eth/biomass; y = glc/biomass

sez = sez[:,sez[6,:]>0]/sez[6,(sez[6,:]>0)]


x_glc = np.absolute(sez[0,(sez[0,:]<0)&(sez[1,:]==0)])
x_xyl = np.absolute(sez[1,(sez[0,:]==0)&(sez[1,:]<0)])
x_glc_xyl = np.absolute((sez[0,(sez[1,:]<0)&(sez[0,:]<0)] + sez[1,(sez[1,:]<0)&(sez[0,:]<0)]))


y_eth_glc = sez[2,(sez[0,:]<0)&(sez[1,:]==0)]
y_eth_xyl = sez[2,(sez[0,:]==0)&(sez[1,:]<0)]
y_eth_glc_xyl = sez[2,(sez[1,:]<0)&(sez[0,:]<0)]


fig = plt.figure()
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

ax1.plot(x_glc, y_eth_glc,'o',color = 'tab:blue',label = 'GLC',markersize=5,alpha = 0.7)
ax2.plot(x_xyl,y_eth_xyl, 'o',color = 'tab:red',label = 'XYL',markersize=5,alpha = 0.7,)
ax3.plot(x_glc_xyl,y_eth_glc_xyl, 'o',color = 'tab:orange',label = 'GLC+XYL',markersize=5,alpha = 0.7,)

ax1.set_ylabel('ETHx/Biomass',fontsize = 12)
ax1.set_xlabel('GLC/Biomass',fontsize = 12)
ax2.set_xlabel('XYL/Biomass',fontsize = 12)
ax3.set_xlabel('GLC+XYL/Biomass',fontsize = 12)
fig.show()
fig.savefig('simple.pdf')

