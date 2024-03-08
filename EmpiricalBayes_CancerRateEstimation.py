#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy.stats import beta

# Assuming this is the complete dataset for previous experiments
# (number of rats with tumors, total number of rats)
data = [
    (0, 20), (0, 20), (1, 20), (2, 20), (3, 20), (4, 20), (6, 23),
    (0, 20), (0, 18), (2, 25), (5, 49), (9, 48), (4, 19), (6, 22),
    (0, 20), (0, 17), (2, 24), (2, 19), (10, 50), (4, 19), (6, 20),
    (0, 20), (1, 20), (2, 20), (3, 27), (4, 20), (5, 22), (6, 20),
    (0, 20), (1, 20), (2, 20), (2, 17), (4, 20), (11, 46), (16, 52),
    (0, 19), (1, 20), (2, 20), (7, 49), (4, 20), (12, 49), (15, 47),
    (0, 19), (1, 19), (2, 20), (7, 47), (4, 20), (5, 20), (15, 46),
    (0, 19), (1, 19), (2, 20), (3, 20), (4, 20), (5, 20), (9, 24)
]

# New experiment data: (number of rats with tumors, total number of rats)
new_experiment = (4, 14)

# Step 1: Compute MLEs for the previous experiments
mles = np.array([y/n for y, n in data])

# Step 2: Compute the sample mean and variance of these MLEs
m = np.mean(mles)
v = np.var(mles, ddof=1)  # ddof=1 for an unbiased estimator

# Step 3: Use method of moments to estimate alpha and beta for the Beta distribution
alpha_hat = m * ((m * (1 - m) / v) - 1)
beta_hat = (1 - m) * ((m * (1 - m) / v) - 1)

print(f"Estimated alpha: {alpha_hat:.2f}, Estimated beta: {beta_hat:.2f}")

# Step 4: Calculate the Bayes estimate for the new experiment
# Update alpha and beta based on new experiment's data
alpha_post = alpha_hat + new_experiment[0]
beta_post = beta_hat + (new_experiment[1] - new_experiment[0])

# The Bayes estimate is the mean of the posterior Beta distribution
bayes_estimate = alpha_post / (alpha_post + beta_post)

print(f"Bayes estimate for the new experiment: {bayes_estimate:.3f}")

