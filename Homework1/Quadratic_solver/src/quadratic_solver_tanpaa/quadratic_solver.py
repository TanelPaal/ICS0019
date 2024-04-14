def solve_quadratic(a, b, c):
    """Solve a quadratic equation ax^2 + bx + c = 0.

    Args:
        a: Coefficient of x^2.
        b: Coefficient of x.
        c: Constant term.

    Returns:
        A tuple of two solutions or a single solution or a message indicating no real solutions.
    """
    # Calculate the discriminant.
    d = b**2 - 4*a*c

    # Calculate the solutions.
    if d > 0:
        x1 = (-b + d**0.5) / (2*a)
        x2 = (-b - d**0.5) / (2*a)
        return x1, x2
    elif d == 0:
        x = -b / (2*a)
        return x
    else:
        return "No real solutions"
