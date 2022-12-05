from project.plantation import Plantation
from unittest import TestCase, main


class PlantationTest(TestCase):

    def test_init_constructor(self):
        plantation = Plantation(4)
        self.assertEqual(4, plantation.size)
        self.assertEqual({}, plantation.plants)
        self.assertEqual([], plantation.workers)

    def test_size_setter(self):
        with self.assertRaises(ValueError) as er:
            Plantation(-1)

        expected = "Size must be positive number!"
        actual = str(er.exception)

        self.assertEqual(expected, actual)

    def test_hire_worker_raise_value_error(self):
        plantation = Plantation(4)
        plantation.workers = ["Yavor"]

        with self.assertRaises(ValueError) as er:
            plantation.hire_worker("Yavor")

        expected = "Worker already hired!"
        actual = str(er.exception)

        self.assertEqual(expected, actual)

    def test_hire_worker_valid_data(self):
        plantation = Plantation(4)
        result = plantation.hire_worker("Yavor")
        expected = "Yavor successfully hired."

        self.assertEqual(expected, result)
        self.assertEqual(["Yavor"], plantation.workers)


    def test_len_method(self):
        plantation = Plantation(10)
        plantation.plants = {"Yavor": ["Tulip", "Arabic Rose", "OtherRose"], "Tea": ["Rose"],
                             "Adrean": ["Chinese Rose"]}

        self.assertEqual(5, len(plantation))

    def test_planting_method_raise_value_error_worker_doesnt_exist(self):
        with self.assertRaises(ValueError) as er:
            plantation = Plantation(4)
            plantation.planting("Yavor", "Rose")

        expected = "Worker with name Yavor is not hired!"
        actual = str(er.exception)

        self.assertEqual(expected, actual)

    def test_planting_method_plantation_is_full(self):
        plantation = Plantation(1)
        plantation.hire_worker("Yavor")
        plantation.hire_worker("Tea")
        with self.assertRaises(ValueError) as er:
            plantation.planting("Yavor", "Tulip")
            plantation.planting("Tea", "Rose")

        expected = "The plantation is full!"
        actual = str(er.exception)

        self.assertEqual(expected, actual)

    def test_planting_method_valid_data(self):
        plantation = Plantation(20)
        plantation.hire_worker("Yavor")
        plantation.hire_worker("Tea")
        plantation.hire_worker("Adrean")
        plantation.plants = {"Yavor": ["Rose", "Tulip"], "Tea": ["Arabic Rose", "Arabic Tulip"]}

        result1 = plantation.planting("Yavor", "White Rose")
        result2 = plantation.planting("Tea", "Black Rose")

        expected1 = "Yavor planted White Rose."
        expected2 = "Tea planted Black Rose."

        self.assertEqual(expected1, result1)
        self.assertEqual(expected2, result2)
        self.assertEqual(
            {"Yavor": ["Rose", "Tulip", "White Rose"], "Tea": ["Arabic Rose", "Arabic Tulip", "Black Rose"]},
            plantation.plants)
        self.assertEqual(6, len(plantation))

        result3 = plantation.planting("Adrean", "GayRose")

        self.assertEqual(
            {"Yavor": ["Rose", "Tulip", "White Rose"], "Tea": ["Arabic Rose", "Arabic Tulip", "Black Rose"],
             "Adrean": ["GayRose"]}, plantation.plants)

        expected = "Adrean planted it's first GayRose."

        self.assertEqual(expected, result3)

    def test_str_method(self):
        plantation = Plantation(20)
        plantation.hire_worker("Yavor")
        plantation.hire_worker("Tea")
        plantation.hire_worker("Adrean")
        plantation.plants = {"Yavor": ["Rose", "Tulip", "White Rose"],
                             "Tea": ["Arabic Rose", "Arabic Tulip", "Black Rose"],
                             "Adrean": ["GayRose"]}

        result = f"Plantation size: 20\n" \
                 f"Yavor, Tea, Adrean\n" \
                 f"Yavor planted: Rose, Tulip, White Rose\n" \
                 f"Tea planted: Arabic Rose, Arabic Tulip, Black Rose\n" \
                 f"Adrean planted: GayRose"

        self.assertEqual(result, str(plantation))

    def test_repr_method(self):
        plantation = Plantation(20)
        plantation.hire_worker("Yavor")
        plantation.hire_worker("Tea")
        plantation.hire_worker("Adrean")

        result = f"Size: 20\n" \
                 f"Workers: Yavor, Tea, Adrean"

        self.assertEqual(result, repr(plantation))



if __name__ == "__main__":
    main()
