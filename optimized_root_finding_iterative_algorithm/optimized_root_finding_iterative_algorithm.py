import math
import random
import time

tolerance=1e-14
max_iter=1000000

def adaptive_fixed_point_sqrt(N):
    if N > 1:
        x_old = max(1, math.log2(N))  # Adaptive starting point for N > 1
    else:
        x_old = N  # Directly use N for N <= 1, considering it's close to its square root
    
    for i in range(max_iter):
        x_new = 0.5 * (x_old + N / x_old)
        
        if abs(x_new - x_old) < tolerance:
            return x_new, i
        
        x_old = x_new
    
    raise ValueError("Convergence not achieved within the maximum number of iterations.")

def newton_sqrt(N):
    if N < 0:
        raise ValueError("Cannot compute square root of a negative number.")

    def f(x):
        return x**2 - N  # Function for which we find the root

    def Df(x):
        return 2 * x  # Derivative of the function

    x = max(1, math.log2(N)) if N > 1 else N  # Adaptive starting point
    p_array = [x]

    for i in range(max_iter):
        y = f(p_array[-1])
        Dy = Df(p_array[-1])
        x_next = p_array[-1] - y / Dy

        p_array.append(x_next)
        if abs(p_array[-1] - p_array[-2]) < tolerance:
            return p_array[-1], i  # Return square root and iteration count

        if len(p_array) > max_iter:
            raise Exception("Loop ran for too many iterations")

    raise ValueError("Convergence not achieved within the maximum number of iterations.")


def monte_carlo_test(test_cases=10000):
    random_ns = [random.uniform(1, 10000) for _ in range(test_cases)]
    fixed_point_iterations = []
    newton_iterations = []
    fixed_point_errors = []
    newton_errors = []
    
    # Fixed-Point Method Testing
    start_time = time.time()
    for N in random_ns:
        sqrt_approx, iteration_count = adaptive_fixed_point_sqrt(N)
        true_sqrt = math.sqrt(N)
        error = abs(sqrt_approx - true_sqrt)
        fixed_point_iterations.append(iteration_count)
        fixed_point_errors.append(error)
    fixed_point_time = time.time() - start_time
    
    # Newton's Method Testing
    start_time = time.time()
    for N in random_ns:
        sqrt_approx, iteration_count = newton_sqrt(N)  # Implement Newton's method to return square root and iteration count
        error = abs(sqrt_approx - true_sqrt)
        newton_iterations.append(iteration_count)
        newton_errors.append(error)
    newton_time = time.time() - start_time
    
    # Analysis
    print("Fixed-Point Average Iterations:", sum(fixed_point_iterations) / test_cases)
    print("Newton's Average Iterations:", sum(newton_iterations) / test_cases)
    print("Fixed-Point Average Error:", sum(fixed_point_errors) / test_cases)
    print("Newton's Average Error:", sum(newton_errors) / test_cases)
    print("Fixed-Point Time:", fixed_point_time)
    print("Newton's Time:", newton_time)

monte_carlo_test()