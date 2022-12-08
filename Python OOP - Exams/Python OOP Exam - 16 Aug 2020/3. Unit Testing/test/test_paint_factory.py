from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self) -> None:
        self.factory = PaintFactory("TestFactory", 2)

    def test_constructor(self):
        self.assertEqual("TestFactory", self.factory.name)
        self.assertEqual(2, self.factory.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.factory.valid_ingredients)
        self.assertEqual({}, self.factory.ingredients)
        self.assertEqual({}, self.factory.products)

    def test_unsuccessful_add_ingredient_method_invalid_ingredient(self):
        with self.assertRaises(TypeError) as er:
            self.factory.add_ingredient("black", 1)

        expected = "Ingredient of type black not allowed in PaintFactory"
        result = str(er.exception)
        self.assertEqual(expected, result)

    def test_unsuccessful_add_ingredient_method_not_enough_space(self):
        factory = PaintFactory("TestFactory", 0)
        with self.assertRaises(ValueError) as er:
            factory.add_ingredient("green", 1)

        expected = "Not enough space in factory"
        result = str(er.exception)
        self.assertEqual(expected, result)

    def test_successful_add_ingredient(self):
        factory = PaintFactory("TestFactory", 10)

        factory.ingredients = {"white": 1}
        factory.add_ingredient("yellow", 3)
        self.assertEqual({"white": 1, "yellow": 3}, factory.ingredients)

        factory.add_ingredient("white", 5)
        self.assertEqual({"white": 6, "yellow": 3}, factory.ingredients)

    def test_unsuccessful_remove_ingredient_it_doesnt_exist(self):
        factory = PaintFactory("TestFactory", 10)
        factory.ingredients = {"white": 2, "red": 3}

        with self.assertRaises(KeyError) as er:
            factory.remove_ingredient("blue", 1)

        expected = "'No such ingredient in the factory'"
        result = str(er.exception)
        self.assertEqual(expected, result)
        self.assertEqual({"white": 2, "red": 3}, factory.ingredients)

    def test_unsuccessful_remove_ingredient_cannot_be_less_than_zero(self):
        factory = PaintFactory("TestFactory", 10)
        factory.ingredients = {"white": 2, "red": 3}
        with self.assertRaises(ValueError) as er:
            factory.remove_ingredient("white", 3)

        expected = "Ingredients quantity cannot be less than zero"
        result = str(er.exception)
        self.assertEqual(expected, result)
        self.assertEqual({"white": 2, "red": 3}, factory.ingredients)

    def test_successful_remove_ingredient(self):
        factory = PaintFactory("TestFactory", 10)
        factory.ingredients = {"white": 2, "red": 3}
        factory.remove_ingredient("red", 1)
        self.assertEqual({"white": 2, "red": 2}, factory.ingredients)


if __name__ == "__main__":
    main()
