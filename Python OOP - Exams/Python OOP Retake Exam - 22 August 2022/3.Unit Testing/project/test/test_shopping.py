from project.shopping_cart import ShoppingCart

from unittest import TestCase, main


class ShoppingCartTest(TestCase):
    def setUp(self):
        self.shopping_cart = ShoppingCart("BimBim", 200)

    def test_if_constructor_is_correct(self):
        self.assertEqual("BimBim", self.shopping_cart.shop_name)
        self.assertEqual(200, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)

    def test_if_shop_name_first_digit_is_upper_and_value_is_letters_only_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            ShoppingCart("bimbim1", 100)

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_add_to_cart_fail_expect_value_error(self):
        shop = self.shopping_cart
        with self.assertRaises(ValueError) as ve:
            shop.add_to_cart("test", 100)

        self.assertEqual("Product test cost too much!", str(ve.exception))

    def test_add_to_cart_valid_run(self):
        shop = self.shopping_cart
        shop.add_to_cart("test_product", 10)
        actual = shop.add_to_cart("test_product2", 10)
        expected = "test_product2 product was successfully added to the cart!"
        self.assertEqual(expected, actual)
        self.assertEqual({"test_product": 10, "test_product2": 10}, shop.products)

    def test_remove_from_cart_raise_value_error(self):
        shop = self.shopping_cart
        with self.assertRaises(ValueError) as vr:
            shop.remove_from_cart("test_product")

        self.assertEqual("No product with name test_product in the cart!", str(vr.exception))

    def test_remove_from_cart_valid_run(self):
        shop = self.shopping_cart
        shop.add_to_cart('test_product', 10)
        shop.add_to_cart('test_product2', 10)
        result = shop.remove_from_cart("test_product2")
        self.assertEqual("Product test_product2 was successfully removed from the cart!", result)
        self.assertEqual(shop.products, {"test_product": 10})

    def test_add_method(self):
        shop1 = self.shopping_cart
        shop1.add_to_cart("test_product1", 10)
        shop2 = ShoppingCart("TestShop", 200)
        shop2.add_to_cart("test_product2", 10)
        merged = shop1.__add__(shop2)
        self.assertEqual("BimBimTestShop", merged.shop_name)
        self.assertEqual(400, merged.budget)
        self.assertEqual({"test_product1": 10, "test_product2": 10}, merged.products)

    def test_buy_products_expect_value_error(self):
        shop = ShoppingCart("TestShop", 20)
        shop.add_to_cart("test_product1", 30)
        with self.assertRaises(ValueError) as ve:
            shop.buy_products()

        expected = "Not enough money to buy the products! Over budget with 10.00lv!"
        self.assertEqual(expected, str(ve.exception))

    def test_buy_products_valid_run(self):
        shop = ShoppingCart("TestShop", 100)
        shop.add_to_cart("test_product1", 10)
        shop.add_to_cart("test_product2", 10)

        self.assertEqual("Products were successfully bought! Total cost: 20.00lv.", shop.buy_products())


if __name__ == "__main__":
    main()
