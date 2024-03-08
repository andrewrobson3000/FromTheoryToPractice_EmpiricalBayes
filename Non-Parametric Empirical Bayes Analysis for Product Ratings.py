#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd

# Step 1: Generate synthetic data
np.random.seed(42)
num_products = 1000
true_5_star_probs = np.random.beta(2, 5, size=num_products)
ratings_count = np.random.poisson(20, size=num_products) + 1  # Ensure at least one rating
five_star_counts = np.random.binomial(ratings_count, true_5_star_probs)

# Step 2: Non-parametric empirical Bayes estimation
# Estimating the distribution of 5-star rating proportions
rating_proportions = five_star_counts / ratings_count
mean_prop = np.mean(rating_proportions)
var_prop = np.var(rating_proportions)

# Assuming a Beta distribution for the underlying true proportions
from scipy.stats import beta
a, b = mean_prop * ((mean_prop * (1 - mean_prop) / var_prop) - 1), (1 - mean_prop) * ((mean_prop * (1 - mean_prop) / var_prop) - 1)

# Estimating true rating proportions using Robbins' method
estimated_props = (five_star_counts + a) / (ratings_count + a + b)

# Step 3: Comparing original and adjusted estimates
products = pd.DataFrame({
    'Product': np.arange(num_products),
    'Original_Proportion': rating_proportions,
    'Estimated_Proportion': estimated_props
})

print(products.head())

