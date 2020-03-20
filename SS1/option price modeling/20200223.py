from IPython.display import HTML

table = """<table>
<tr>
<th>Greek</th>
<th>Call</th>
<th>Put</th>
</tr>
<tr>
<td>Delta $\Delta$</td>
<td>$N(d_1)$</td>
<td>$-N(-d_1)$</td>
</tr>
<tr>
<td>Theta $\Theta$</td>
<td>$\\frac{\sigma SN'(d_1)}{2\sqrt{T-t}} - rKe^{-r(T-t)} N(d_2)$</td>
<td>$\\frac{-\sigma SN'(d_1)}{2\sqrt{T-t}} + rKe^{-r(T-t)} N(d_2)$</td>
</tr>
<tr>
<td>Gamma $\Gamma$</td>
<td>$\\frac{N'(d_1)}{S\sigma \sqrt{T}}$</td>
<td>$\\frac{N'(d_1)}{S\sigma \sqrt{T}}$</td>
</tr>
<tr>
<td>Vega $v$</td>
<td>$S_0 N'(d_1)\sqrt{T}$</td>
<td>$S_0 N'(d_1)\sqrt{T}$</td>
</tr>
<tr>
<td>Rho $\\rho$</td>
<td>$TKe^{-r(T)} N(d_2)$</td>
<td>$-TKe^{-r(T)} N(-d_2)$</td>
</tr>
</table>"""

import numpy as np
import scipy.stats as si
import sympy as sy
# import sympy.statistics as systats


def delta_call(S, K, T, r, sigma):

    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    delta_call = si.norm.cdf(d1, 0.0, 1.0)

    return delta_call


def delta_put(S, K, T, r, sigma):

    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    delta_put = si.norm.cdf(-d1, 0.0, 1.0)

    return -delta_put


def delta(S, K, T, r, sigma, option='call'):

    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    if option == 'call':
        result = si.norm.cdf(d1, 0.0, 1.0)
    if option == 'put':
        result = -si.norm.cdf(-d1, 0.0, 1.0)

    return result


print("delta: " + str(delta(100, 50, 1, 0.05, 0.25, option='put')))


def theta_call(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    prob_density = 1 / np.sqrt(2 * np.pi) * np.exp(-d1 ** 2 * 0.5)

    theta = (-sigma * S * prob_density) / (2 * np.sqrt(T)) - r * K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0)

    return theta


def theta_put(S, K, T, r, sigma):

    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    prob_density = 1 / np.sqrt(2 * np.pi) * np.exp(-d1 ** 2 * 0.5)

    theta = (-sigma * S * prob_density) / (2 * np.sqrt(T)) + r * K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0)

    return theta


def theta(S, K, T, r, sigma, option='call'):

    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    prob_density = 1 / np.sqrt(2 * np.pi) * np.exp(-d1 ** 2 * 0.5)

    if option == 'call':
        theta = (-sigma * S * prob_density) / (2 * np.sqrt(T)) - r * K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0)
    if option == 'put':
        theta = (-sigma * S * prob_density) / (2 * np.sqrt(T)) + r * K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0)

    return theta


print("theta: " + str(theta(110, 100, 2, 0.05, 0.25, option='put')))


def gamma(S, K, T, r, sigma):

    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    prob_density = 1 / np.sqrt(2 * np.pi) * np.exp(-d1 ** 2 * 0.5)

    gamma = prob_density / (S * sigma * np.sqrt(T))

    return gamma


print("gamma: " + str(gamma(110, 100, 1, 0.05, 0.25)))


def vega(S, S0, K, T, r, sigma):

    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    prob_density = 1 / np.sqrt(2 * np.pi) * np.exp(-d1 ** 2 * 0.5)

    vega = S0 * prob_density * np.sqrt(T)

    return vega


print("vega: " + str(vega(110, 105, 100, 1, 0.05, 0.25)))


def rho_call(S, K, T, r, sigma):

    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    rho = T * K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0)

    return rho


def rho_put(S, K, T, r, sigma):

    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    rho = -T * K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0)

    return rho


def rho(S, K, T, r, sigma, option='call'):

    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    if option == 'call':
        rho = T * K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0)
    if option == 'put':
        rho = -T * K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0)

    return rho


def all(S, K, T, r, sigma, option):
    print("delta: " + str(delta(100, 50, 1, 0.05, 0.25, option='put')))
    print("theta: " + str(theta(110, 100, 2, 0.05, 0.25, option='put')))
    print("gamma: " + str(gamma(110, 100, 1, 0.05, 0.25)))
    print("vega: " + str(vega(110, 105, 100, 1, 0.05, 0.25)))


def all2(S, S0, K, T, r, sigma, option):
    # S = 0
    # S0 =
    # K = 0
    # T = 0
    # r = 0
    # sigma = 0
    # option = "call"

    print("S: " + (str(S)))
    print("K: " + (str(K)))
    print("T: " + (str(T)))
    print("r: " + (str(r)))
    print("sigma: " + (str(sigma)))
    print("option: " + (str(option)))

    print("delta: " + str(delta(S, K, T, r, sigma, option)))
    print("theta: " + str(theta(S, K, T, r, sigma, option)))
    print("gamma: " + str(gamma(S, K, T, r, sigma)))
    print("vega: " + str(vega(S, S0, K, T, r, sigma)))


all2(75, 70, 60, 4, 1, 0.25, "call")
