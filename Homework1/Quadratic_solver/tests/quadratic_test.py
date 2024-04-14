import unittest
from quadratic_solver_tanpaa.quadratic_solver import solve_quadratic

class TestSolveQuadratic(unittest.TestCase):
    def test_solve_quadratic_positive_discriminant(self):
        result = solve_quadratic(1, -3, 2)
        self.assertEqual(result, (2.0, 1.0))

    def test_solve_quadratic_zero_discriminant(self):
        result = solve_quadratic(1, -2, 1)
        self.assertEqual(result, 1.0)

    def test_solve_quadratic_negative_discriminant(self):
        result = solve_quadratic(1, 1, 1)
        self.assertEqual(result, "No real solutions")

if __name__ == '__main__':
    unittest.main()