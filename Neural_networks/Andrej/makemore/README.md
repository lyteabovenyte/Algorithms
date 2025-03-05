#### Notes along the way of learning to implement neural-nets from scratch by The GREAT Andrej
- Why Use Normalization Layers?
    - During neural network training, the distribution of inputs to each layer can change due to weight updates—a phenomenon called *internal covariate shift*. This can slow down training and make it harder for the network to converge. Normalization layers help by:
        - Reducing the effect of internal covariate shift.
        - Enabling higher learning rates by stabilizing gradients.
        - Preventing certain neurons from dominating due to large values.
        - Acting as a form of regularization (reducing overfitting).
    - Batch-Norm technique:
        - Batch Normalization (BN): $\hat{x}_i = \frac{x_i - \mu_B}{\sigma_B}$; $y_i = \gamma \hat{x}_i + \beta$
        - What it does: Normalizes inputs across a mini-batch by subtracting the batch *mean* and dividing by the batch *standard deviation*
        - Where to use it: Typically used between a linear layer and an activation function.

- 