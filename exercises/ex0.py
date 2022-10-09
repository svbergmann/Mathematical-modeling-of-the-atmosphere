import numpy as np

rt_srf = 10


def r_t0(z):
    if z > 1:
        return 1
    elif z > 0.5:
        return -r_t0(z - 0.5) + rt_srf
    else:
        return 1


def k(z):
    if z > 1:
        return 1
    elif z > 0.5:
        return z + 0.5
    else:
        return 1


def alpha_delta_t_div_delta_x_square(z):
    return k(z)


u_start = np.linspace(0, 10, 100)
for i in range(0, 100):
    u_start[i] = r_t0(u_start[i])

print(u_start)
