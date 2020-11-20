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
	
	dNdt = P*N - U*N + N
	
	diff = np.empty(len(yvec))
	diff = [dNdt]
	
	return diff

# b = 2/3 # prey population increase rate
# a = 4/3 # predation coeff
# b = 1   # postproduction rate per 1 prey eaten
# c = 1   # predator mortality rate


# pocatek   = 1990
# prirustek = 1
# rok = []

# for i in range(30):
	# rok.append(pocatek + i)

# print(rok)

# porodnost = [12.6, 12.5, 11.8, 11.7, 10.3, 9.3, 8.8, 8.8, 8.8, 8.7, 8.8, 8.9,
              # 9.1,  9.2,  9.6, 10, 10.3, 11.1, 11.5, 11.3, 11.1, 10.4, 10.3,
			 # 10.2, 10.4, 10.5, 10.7, 10.8, 10.7, 10.5]

# coeff_porodnost = np.polyfit(rok, porodnost, 6)

# porod_calc = []
# for item in rok:
	# porod_calc.append(coeff_porodnost[5]*pow(item, 6) + coeff_porodnost[4]*pow(item, 5) + coeff_porodnost[3]*pow(item, 4) + coeff_porodnost[2]*pow(item, 3) + coeff_porodnost[1]*pow(item, 2) + \
				 # coeff_porodnost[0]*pow(item, 1))

# print(coeff_porodnost)
# print(porod_calc)

# plt.figure("porodnost")
# plt.plot(rok, porodnost, "o", rok, porod_calc)
# plt.show()

yini = [1000]
ts = np.linspace(0, 2E-13, 1*1000)

result = sc.odeint(lambda y, t: fun(y, t), yini, ts)
# print(result)
prey     = result[:, 0]

plt.figure("Jedna")
plt.plot(ts, prey)
plt.legend(["prey", "predator"])

plt.show()





