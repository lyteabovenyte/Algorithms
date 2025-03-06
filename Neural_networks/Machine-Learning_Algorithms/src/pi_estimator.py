import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

def pi_estimator(radius=1, num_iter=int(1e4)):
    X = np.random.uniform(-radius, +radius, num_iter)
    Y = np.random.uniform(-radius, +radius, num_iter)

    R2 = X**2 + Y**2
    inside = R2 < radius**2
    outside = ~inside

    samples = (2*radius)*(2*radius)*inside
    
    