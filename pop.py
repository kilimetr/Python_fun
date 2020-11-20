# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr



import scipy.integrate   as sc
import numpy             as np
import matplotlib.pyplot as plt
	


def fun(yvec, t):
	N = yvec[0] # prey

	P = 10.8
	U = 10.5
	
	dNdt = P*N - U*N
	
	diff = np.empty(len(yvec))
	diff = [dNdt]
	
	return diff


P = 10.8
U = 10.5
cas = []
for i in range(1, 11, 1):
	cas.append(i)

N = []
N.append(P*1000 - U*1000)
for i in range(len(cas)):
	if i >= 1:
		N.append(P*N[-1] - U*N[-1] + N[-1])
		print(N)
	else:
		print("i = 1")

# b = 2/3 # prey population increase rate
# a = 4/3 # predation coeff
# b = 1   # postproduction rate per 1 prey eaten
# c = 1   # predator mortality rate

# yini = [1000]
# ts = np.linspace(0, 10, 1*1000)

# result = sc.odeint(lambda y, t: fun(y, t), yini, ts)
# # print(result)
# prey     = result[:, 0]

plt.figure("Jedna")
plt.plot(cas, N)
plt.legend(["cas", "N"])

plt.show()





