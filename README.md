<p align="center"><img width=60% src="https://github.com/miles-vollet8/MilesVollet/blob/main/media/logo.png"></p>

## Overview

This application implements the Black-Scholes option pricing model to compute theoretical prices for European call and put options. The model generates dynamic 3D heatmap surfaces to visualize how option prices vary with volatility and underlying asset changes as well as offer an intuitive understanding of option moneyness with colorization. By combining the mathematical pricing model with interactive visualizations, this project is a powerful tool for exploring the implications of the Black-Scholes model.

https://blackscho.streamlit.app/

## Pricing Model

The Black-Scholes model is a mathematical technique for estimating the theoretical price of European options. The model assumes no arbitrage opportunities, lognormal stock price distributions, no transaction costs, constant volatility, and a constant risk-free rate
- Calculates call and put values as well as their Greeks

- Features an interactive dashboard that prompts Asset Price, Strike Price, Time to Expiration, Volatility, and Risk-Free Rate inputs

- Dynamically recalculates prices when inputs are changed
  
## 3D Heatmap

The 3D surfaces visualize the relationship between option prices and two parametes: the underlying asset price (S) and the volatility (ν). Seperate surfaces are generated for companion call and put options for comparison. The surfaces have heatmap characteristics through colorization of option moneyness.
- Displays interactive call and put surfaces to visualize how volatility and underlying asset changes affect option prices

- Features surface colorization to see the option's moneyness

- Allows the user to choose the volatility and asset price range in the dashboard

## Libraries
- `Plotly`: 3D Surface Generation
- `NumPy`: Vectors and Math Operations
- `SciPy`: Normal Distribution Calculations