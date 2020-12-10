#Please see
#https://computationalmindset.com/en/neural-networks/ordinary-differential-equation-solvers.html#sys1
#for details

import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf
from tfdiffeq import odeint

def ode_fn(t, XY):
	x=XY[0]
	y=XY[1]
	dx_dt= - x + y
	dy_dt= 4. * x - y
	return tf.stack([dx_dt, dy_dt])

an_sol_x = lambda t : np.exp(t) + np.exp(-3. * t)
an_sol_y = lambda t : 2. * np.exp(t) - 2. * np.exp(-3. * t)

t_begin=0.
t_end=5.
t_nsamples=100
t_space = np.linspace(t_begin, t_end, t_nsamples)
x_init = tf.constant([2.])
y_init = tf.constant([0.])

x_an_sol = an_sol_x(t_space)
y_an_sol = an_sol_y(t_space)

x_num_sol = odeint(ode_fn, tf.convert_to_tensor([x_init, y_init], dtype=tf.float64), tf.constant(t_space)).numpy()

plt.figure()
plt.plot(t_space, x_an_sol, label='analytical x')
plt.plot(t_space, y_an_sol, label='analytical y')
plt.plot(t_space, x_num_sol[:,0], label='numerical x')
plt.plot(t_space, x_num_sol[:,1], label='numerical y')
plt.title('System of two ODEs 1st order IVP solved by TensorFlowDiffEq')
plt.xlabel('t')
plt.legend()
plt.show()

