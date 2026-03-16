Monte Carlo Simulation for Autocallable Structured Product
Description

This project implements a Monte Carlo simulation in Python to model the evolution of an underlying asset price under the Black–Scholes framework and estimate the payoff of an autocallable structured product.

The simulation generates multiple price paths of the underlying asset using a geometric Brownian motion and evaluates the payoff depending on whether the autocall barrier is reached during the observation dates.

Model

The underlying price dynamics follow the Black–Scholes model:

𝑑
𝑆
𝑡
=
𝑟
𝑆
𝑡
𝑑
𝑡
+
𝜎
𝑆
𝑡
𝑑
𝑊
𝑡
dS
t
	​

=rS
t
	​

dt+σS
t
	​

dW
t
	​


where:

𝑆
𝑡
S
t
	​

 : underlying price

𝑟
r : risk-free interest rate

𝜎
σ : volatility

𝑊
𝑡
W
t
	​

 : Brownian motion

Product Structure

The structured product is an autocallable note with:

Annual observation dates

Autocall barrier at 100% of the initial price

Annual coupon of 8%

Maturity of 5 years

If the underlying price is above the barrier at an observation date, the product is automatically redeemed and the investor receives the nominal plus the accumulated coupon.

Methodology

Simulate price paths using geometric Brownian motion.

Check the autocall condition at each observation date.

Compute the payoff for each simulation.

Discount the expected payoff to obtain the estimated price.

Technologies Used

Python

NumPy

Matplotlib

Monte Carlo simulation

Output

The model produces:

Simulated price paths of the underlying asset

Distribution of final prices

Estimated price of the autocallable product
