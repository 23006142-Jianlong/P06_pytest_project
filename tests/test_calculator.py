from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

class TestCalculator:
    def test_multiplication(self):
        # arrange
        a = 5
        b = 2
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 10
        assert result == expected

class TestCalculator:
    def test_subtraction(self):
        # arrange
        a = 5
        b = 2
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 3
        assert result == expected
        
class TestCalculator:
    def test_division(self):
        # arrange
        a = 6
        b = 2
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 3
        assert result == expected