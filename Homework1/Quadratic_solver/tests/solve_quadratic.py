import unittest
from Homework1.Quadratic_solver.src.quadratic_solver.quadratic_solver import solve_quadratic as QuadraticS

class TestQuadraticSolver(unittest.TestCase):
    def test_positive_discriminant(self):
        self.assertEqual(QuadraticS(1, -3, 2), (2.0, 1.0))
        self.assertEqual(QuadraticS(1, -5, 6), (3.0, 2.0))
        self.assertEqual(QuadraticS())

    def test_zero_discriminant(self):
        self.assertEqual(QuadraticS(1, -2, 1), (1.0))
        self.assertEqual(QuadraticS(1, 0, 0), (0.0))

    def test_negative_discriminant(self):
        self.assertEqual(QuadraticS(1, 1, 1), "No real solutions")
        self.assertEqual(QuadraticS(1, 2, 3), "No real solutions")
        self.assertEqual(QuadraticS(1, -3, 4), "No real solutions")


if __name__ == '__main__':
    unittest.main()
