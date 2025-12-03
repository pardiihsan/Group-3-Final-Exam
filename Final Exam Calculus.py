# -*- coding: utf-8 -*-
"""
Matrix & Function Plotting Application
Python 3.12
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def matrix_operations():
    print("=== Matrix Operations ===")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("Enter elements of the matrix row by row (space separated):")
    elements = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            print("Invalid number of columns! Exiting matrix operation.")
            return
        elements.append(row)

    A = np.array(elements)
    print("\nMatrix A:")
    print(A)

    # Determinant (only for square matrices)
    if rows == cols:
        det = np.linalg.det(A)
        print(f"Determinant of A: {det}")

        try:
            inv = np.linalg.inv(A)
            print("Inverse of A:")
            print(inv)
        except np.linalg.LinAlgError:
            print("Matrix is singular; inverse does not exist.")
    else:
        print("Matrix is not square; skipping determinant and inverse.")

    print("Matrix Transpose:")
    print(A.T)

    # Optionally, matrix addition/multiplication with another matrix
    choice = input("Do you want to multiply this matrix by another matrix? (y/n): ")
    if choice.lower() == 'y':
        rows2 = int(input("Enter number of rows of second matrix: "))
        cols2 = int(input("Enter number of columns of second matrix: "))
        print("Enter elements of second matrix row by row:")
        elements2 = []
        for i in range(rows2):
            row = list(map(float, input(f"Row {i+1}: ").split()))
            elements2.append(row)
        B = np.array(elements2)

        try:
            result = np.dot(A, B)
            print("Result of A * B:")
            print(result)
        except ValueError as e:
            print(f"Error in multiplication: {e}")

def plot_function():
    print("\n=== Plot Function ===")
    x = sp.symbols('x')
    expr_input = input("Enter a function of x (e.g., sin(x), x**2 + 3*x): ")
    try:
        f_expr = sp.sympify(expr_input)
    except sp.SympifyError:
        print("Invalid function input!")
        return

    # Plot original function
    f_lambdified = sp.lambdify(x, f_expr, "numpy")
    x_vals = np.linspace(-10, 10, 400)
    y_vals = f_lambdified(x_vals)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label=f"f(x) = {f_expr}")
    plt.title("Plot of Function")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_derivative():
    print("\n=== Plot Derivative Function ===")
    x = sp.symbols('x')
    expr_input = input("Enter a function of x (e.g., sin(x), x**2 + 3*x): ")
    try:
        f_expr = sp.sympify(expr_input)
    except sp.SympifyError:
        print("Invalid function input!")
        return

    # Compute derivative
    f_prime = sp.diff(f_expr, x)
    print(f"Derivative: f'(x) = {f_prime}")

    # Plot derivative
    f_prime_lambdified = sp.lambdify(x, f_prime, "numpy")
    x_vals = np.linspace(-10, 10, 400)
    y_prime_vals = f_prime_lambdified(x_vals)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_prime_vals, label=f"f'(x) = {f_prime}", color='red')
    plt.title("Plot of Derivative Function")
    plt.xlabel("x")
    plt.ylabel("f'(x)")
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    while True:
        print("\n=== Matrix & Function Application ===")
        print("1. Matrix Operations")
        print("2. Plot Function")
        print("3. Plot Derivative Function")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            matrix_operations()
        elif choice == '2':
            plot_function()
        elif choice == '3':
            plot_derivative()
        elif choice == '4':
            print("Exiting application.")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
