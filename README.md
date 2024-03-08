# Empirical Bayes Methods: A Practical Guide

Welcome to this repository, where I demystify Empirical Bayes methods and showcase their practical applications in data analysis. Dive into the intuitive and mathematical underpinnings of both parametric and non-parametric Empirical Bayes approaches, enriched with real-life examples and code samples.

## Summary

Empirical Bayes methods offer a powerful framework for statistical inference, allowing us to borrow strength from data to estimate parameter distributions. This repository covers:

- **Parametric Empirical Bayes (ParametricEB)**: Assumes that parameters $\theta_i$ are independently and identically distributed (iid) with distribution $\pi(\theta|\psi)$, where $\psi$ is a hyperparameter. By estimating $\hat{\psi}$ from the data, we avoid integrating over hyperparameters in hierarchical models, effectively pulling estimates towards a common mean and creating shrinkage estimators. However, this approach might risk overfitting due to the dual use of data.

- **Non-Parametric Empirical Bayes (NonParametricEB)**: Operates under the assumption that $\theta_i$ are iid from some distribution $\pi$, directly estimated from the data as $\hat{\pi}$. This method doesn't assume a parametric form for the prior distribution, offering flexibility in modeling complex or unknown underlying data distributions.

## Repository Contents

- **Guides**: Detailed explanations of parametric and non-parametric Empirical Bayes methods, their assumptions, and implications.
- **Examples**: Real-life applications showcasing how these methods can be applied to solve practical problems in data analysis.
- **Code Samples**: Implementations and tutorials in Python, demonstrating the step-by-step application of Empirical Bayes techniques.

## Getting Started

To explore the materials in this repository, clone it to your local machine.

![posterior_means_comparison](https://github.com/andrewrobson3000/FromTheoryToPractice_EmpiricalBayes/assets/87878168/0ecc4563-ff50-493e-a335-60d4e6eae4a7)


