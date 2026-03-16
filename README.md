Monte Carlo Simulation for Autocallable Structured Product
Description

This project implements a Monte Carlo simulation in Python to model the evolution of an underlying asset price under the Black-Scholes framework and estimate the payoff of an autocallable structured product.

The simulation generates multiple price paths of the underlying asset using geometric Brownian motion and evaluates the payoff depending on whether the autocall barrier is reached during the observation dates.

This type of simulation is commonly used in derivatives pricing and structured products analysis.

Model

The underlying asset price follows the Black-Scholes dynamics:
dS = r * S * dt + sigma * S * dW
where:

S : underlying asset price

r : risk-free interest rate

sigma : volatility

dW : Brownian motion

In discrete time, the simulated price evolves as:
S(t+dt) = S(t) * exp((r - 0.5 * sigma^2) * dt + sigma * sqrt(dt) * Z)
where Z ~ N(0,1).
Product Structure

The structured product simulated in this project is an autocallable note with the following features:

Annual observation dates

Autocall barrier at 100% of the initial price

Annual coupon of 8%

Maturity of 5 years

If the underlying price is above the autocall barrier at an observation date:

the product is automatically redeemed

the investor receives the nominal plus the accumulated coupon

If the barrier is never reached, the investor receives the nominal at maturity.

Methodology

The pricing approach follows these steps:

Simulate price paths using geometric Brownian motion

Check the autocall condition at each observation date

Compute the payoff for each simulation

Discount the expected payoff to obtain the estimated product price

The price is obtained using Monte Carlo averaging of discounted payoffs.

Technologies Used

Python

NumPy

Matplotlib

Monte Carlo simulation

Output

The model produces:

Simulated price paths of the underlying asset

Distribution of simulated payoffs

Estimated price of the autocallable product

Example outputs include:

Monte Carlo simulated trajectories

Histogram of simulated payoffs

Estimated price of the structured product
