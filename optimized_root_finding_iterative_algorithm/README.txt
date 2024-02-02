# Combined Root Finding Method

## Overview
This project presents an innovative approach to finding square roots by combining the secant and tangent methods. Developed in Python, it aims to leverage the global approximation capabilities of the secant method and the local precision of the tangent method, offering a more efficient convergence towards the root compared to traditional methods.

## Methodology
The algorithm modifies the traditional secant method by incorporating the tangent's x-intercept at the midpoint between two consecutive approximations. By averaging the x-intercepts of the secant and tangent lines, it uses this midpoint as the next approximation point. This hybrid approach is designed to optimize the initial convergence speed towards the square root, making it particularly effective in the early stages of approximation.

## Analysis
A comprehensive Monte Carlo simulation, involving 10,000 iterations, has been conducted to compare the performance of the modified secant method against the traditional secant method. The results indicate a lower average error in the initial iterations with the combined method, suggesting an accelerated convergence process.

## Future Improvement
To further enhance the algorithm's reliability and ensure convergence, a future update will incorporate a bracketing method like bisection. This will prevent the approximations from straying too far from the actual root, especially in cases where the combined method may start to diverge.