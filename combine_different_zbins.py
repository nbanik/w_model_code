from Cosmo import distance

d = distance(.25,.75)



print d.Dgn(0.65), d.Dgn(0.75), d.Dgn(0.85), d.Dgn(0.95)


 ## bias_bf is the bias parameter of the sample, for dark matter, you use bias_bf = 1 
## w_full is the final w you want   

import numpy as np

dir = '/home/nil/Dropbox/w_model_code/'

full_fname=dir + 'outbin_1.txt'
amean=0.75
bias=1.8
beta=0.4


#f = Omegam_a( amean )**0.55
ff = d.omz(amean)**.557
betad = ff/bias
betaf = betad/beta

theta, w0, w2, w4  = np.loadtxt( full_fname, usecols=( 0, 1,2,3 ), unpack=True )


b2_term = w0
bf_term = ff * ( 2/3.*w0 + 4/3.*w2 )
f2_term = ff**2 * ( 1/5.*w0 + 4/7.*w2 + 8/35.*w4)


w_full = betaf**2 * b2_term  +  betaf * bf_term  +  f2_term

import matplotlib.pyplot as plt

plt.figure()
plt.plot(theta,100.*(theta)*w_full)
plt.xlim(0.6,5.2)
plt.savefig('wtheta_1.pdf')
plt.show()

