import math
import random

num_iter=100


def weighted_newton_sqrt_with_intervals(N, intervals):
    def f(x): return x**2 - N
    def Df(x): return 2 * x
    x = N / 2  # Improved starting point based on the magnitude of N
    approximations = {}
    
    for i in range(num_iter):
        y = f(x)
        Dy = Df(x)
        # Dynamic adjustment based on the magnitude of y relative to N
        x_next = x - y / Dy
        magnitude_adjustment =(x_next-x)/(2*x)
        adjusted_Dy = Dy * (1 + magnitude_adjustment)
        
        x_next = x - y / adjusted_Dy
        
        if i in intervals:
            approximations[i] = x_next  # Store approximation at this interval
        
        x = x_next
    
    return approximations

def newton_sqrt_with_intervals(N, intervals):
    def f(x): return x**2 - N
    def Df(x): return 2 * x
    x = N/2  # Non-adaptive starting point
    approximations = {}
    for i in range(num_iter):
        y, Dy = f(x), Df(x)
        x_next = x - y / Dy
        if i in intervals:
            approximations[i] = x_next  # Store approximation at this interval
        x = x_next
    return approximations

def monte_carlo_test(test_cases=1000, specific_iters=[2, 3, 4, 5, 6, 7, 8, 9, 10, 50, 100]):
    all_intervals = specific_iters
    
    # Adjust the range for N values to be more manageable
    random_ns = [2**(random.uniform(0, 100)) for _ in range(test_cases)]
    errors_at_intervals = {interval: {'weighted_newton': [], 'newton': []} for interval in all_intervals}
    
    for N in random_ns:
        true_sqrt = math.sqrt(N)

        # Testing Weighted Newton's method
        sqrt_approximations_weighted_newton = weighted_newton_sqrt_with_intervals(N, all_intervals)
        for interval in all_intervals:
            approx_sqrt = sqrt_approximations_weighted_newton.get(interval, true_sqrt)
            error = abs(1 - approx_sqrt * (approx_sqrt / N))  # Adjusted error calculation
            errors_at_intervals[interval]['weighted_newton'].append(error)

        # Testing Newton's method
        sqrt_approximations_newton = newton_sqrt_with_intervals(N, all_intervals)
        for interval in all_intervals:
            approx_sqrt = sqrt_approximations_newton.get(interval, true_sqrt)
            error = abs(1 - approx_sqrt * (approx_sqrt / N))  # Adjusted error calculation
            errors_at_intervals[interval]['newton'].append(error)

    # Analysis: Calculate average errors at each interval
    for interval in all_intervals:
        avg_error_weighted_newton = sum(errors_at_intervals[interval]['weighted_newton']) / test_cases
        avg_error_newton = sum(errors_at_intervals[interval]['newton']) / test_cases
        print(f"Interval {interval}:")
        print(f"  Weighted Newton's Average Error: {avg_error_weighted_newton}")
        print(f"  Newton's Average Error: {avg_error_newton}")

monte_carlo_test()
