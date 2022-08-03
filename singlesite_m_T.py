import numpy as np
import matplotlib.pyplot as plt
T =np.linspace (0,6)
beta = 1/T
mu=0
U = 4

# Partition function for single site Hubbard Model 
def partition_function ( beta, mu, U):
    return np.exp (-beta*U/4) + 2* np.exp (beta * (U/4 + mu)) + np.exp (- beta * (U/4 - (2*mu)))

# n = n_up + n_down 
def number_density (beta , mu , U ):
    Z = partition_function (beta , mu , U )
    return (2/Z) * (np.exp (beta*(U/4 + mu)) + np.exp (-beta * (U/4 - (2*mu)) ))

# Double occupancy
def double_occupancy (beta, mu, U):
	Z= partition_function (beta, mu, U)
	return (1/Z) * (np.exp (2*beta*mu - beta*(U/4)))

#Local Moment
def local_moment (beta, mu, U):
    rho = number_density (beta, mu, U)
    D=double_occupancy(beta, mu, U)
    return rho-2*D

for j in T:
    m_square = local_moment(beta, 0, 4)
    plt.plot (T, m_square)

plt.xlabel (r'$T$')
plt.ylabel (r'$m_square$')
plt.grid()
plt.show()
