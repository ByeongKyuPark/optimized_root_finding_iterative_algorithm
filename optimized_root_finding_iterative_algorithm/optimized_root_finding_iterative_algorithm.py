import math
import random

num_iter = 5  # Number of iterations
initial_x0 = 4
initial_x1 = 32

def combined_root_finding(N, intervals):
    def f(x): return x**2 - N
    def df(x): return 2*x  # Derivative of f(x)

    x0, x1 = initial_x0, initial_x1  # Initial guesses
    approximations = {}

    for i in range(num_iter):
        # Calculate the secant line's x-intercept
        y0, y1 = f(x0), f(x1)
        x_secant = x0 - y0 * (x1 - x0) / (y1 - y0)

        # Calculate the midpoint and its tangent line's x-intercept
        midpoint = (x0 + x1) / 2
        x_tangent = midpoint - f(midpoint) / df(midpoint)

        # Combine the two x-intercepts for the next approximation
        # Strategy: Use the average of x_secant and x_tangent
        x_new = (x_secant + x_tangent) / 2

        if i in intervals:
            approximations[i] = x_new  # Store the new approximation

        # Update x0 and x1 for the next iteration
        # Strategy: Choose x_new and the closer of x0 or x1 to x_new
        x0, x1 = sorted([x_new, x0, x1], key=lambda x: abs(x - x_new))[:2]

    return approximations


def original_secant_sqrt(N, intervals):
    def f(x): return x**2 - N
    x0, x1 = initial_x0, initial_x1
    approximations = {}

    for i in range(num_iter):
        y0, y1 = f(x0), f(x1)
        x = (y1 * x0 - y0 * x1) / (y1 - y0)

        if i in intervals:
            approximations[i] = x

        x0, x1 = x1, x
    return approximations

# Monte Carlo test to compare methods
def monte_carlo_test(test_cases=100000, specific_iters=[2, 3, 4, 5,10]):
    all_intervals = specific_iters
    random_ns = [2**(random.uniform(-2, 30)) for _ in range(test_cases)]
    errors_at_intervals = {interval: {'modified_secant': [], 'secant': []} for interval in all_intervals}

    for N in random_ns:
        true_sqrt = math.sqrt(N)

        sqrt_approximations_modified_secant = combined_root_finding(N, all_intervals)
        for interval in all_intervals:
            approx_sqrt = sqrt_approximations_modified_secant.get(interval, true_sqrt)
            error = abs(1 - approx_sqrt / true_sqrt)
            errors_at_intervals[interval]['modified_secant'].append(error)

        sqrt_approximations_secant = original_secant_sqrt(N, all_intervals)
        for interval in all_intervals:
            approx_sqrt = sqrt_approximations_secant.get(interval, true_sqrt)
            error = abs(1 - approx_sqrt / true_sqrt)
            errors_at_intervals[interval]['secant'].append(error)

    for interval in all_intervals:
        avg_error_modified_secant = sum(errors_at_intervals[interval]['modified_secant']) / test_cases
        avg_error_secant = sum(errors_at_intervals[interval]['secant']) / test_cases
        print(f"Interval {interval}:")
        print(f"  Modified Secant's Average Error: {avg_error_modified_secant}")
        print(f"  Secant's Average Error: {avg_error_secant}")

monte_carlo_test()
