from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):

    def test_constructor(self):
        test_store = ToyStore()
        self.assertEqual({"A": None,
                          "B": None,
                          "C": None,
                          "D": None,
                          "E": None,
                          "F": None,
                          "G": None, }, test_store.toy_shelf)

    def test_add_toy_shelf_doesnt_exist_raise_exception(self):
        test_store = ToyStore()
        with self.assertRaises(Exception) as er:
            test_store.add_toy("Z", "Invalid")

        expected = "Shelf doesn't exist!"
        result = str(er.exception)
        self.assertEqual(expected, result)

    def test_add_toy_toy_already_exist_raise_exception(self):
        test_store = ToyStore()
        test_store.toy_shelf = {
            "A": "HotWheels",
            "B": None,
            "C": None,
            "D": "WaterGun",
            "E": None,
            "F": None,
            "G": "TeddyBear",
        }

        with self.assertRaises(Exception) as er:
            test_store.add_toy("A", "HotWheels")
            test_store.add_toy("D", "WaterGun")
            test_store.add_toy("G", "TeddyBear")

        expected = "Toy is already in shelf!"
        result = str(er.exception)
        self.assertEqual(expected, result)
        self.assertEqual({
            "A": "HotWheels",
            "B": None,
            "C": None,
            "D": "WaterGun",
            "E": None,
            "F": None,
            "G": "TeddyBear",
        }, test_store.toy_shelf)

    def test_add_toy_shelf_is_already_taken_raise_exception(self):
        test_store = ToyStore()
        test_store.toy_shelf = {
            "A": "HotWheels",
            "B": None,
            "C": None,
            "D": "WaterGun",
            "E": None,
            "F": None,
            "G": "TeddyBear",
        }

        with self.assertRaises(Exception) as er:
            test_store.add_toy("A", "MagicWand")
            test_store.add_toy("D", "WaterGun")

        expected = "Shelf is already taken!"
        result = str(er.exception)
        self.assertEqual(expected, result)
        self.assertEqual({
            "A": "HotWheels",
            "B": None,
            "C": None,
            "D": "WaterGun",
            "E": None,
            "F": None,
            "G": "TeddyBear",
        }, test_store.toy_shelf)

    def test_add_toy_successfully_added_toy(self):
        test_store = ToyStore()
        test_store.toy_shelf = {
            "A": "HotWheels",
            "B": None,
            "C": None,
            "D": "TeddyBear",
            "E": None,
            "F": None,
            "G": "WaterGun",
        }

        result = test_store.add_toy("B", "RubberDucky")
        self.assertEqual(f"Toy:RubberDucky placed successfully!", result)

        self.assertEqual({
            "A": "HotWheels",
            "B": "RubberDucky",
            "C": None,
            "D": "TeddyBear",
            "E": None,
            "F": None,
            "G": "WaterGun",
        }, test_store.toy_shelf)

    def test_remove_toy_shelf_doesnt_exist_raise_exception(self):
        test_store = ToyStore()
        with self.assertRaises(Exception) as er:
            test_store.remove_toy("Z", "Invalid")

        expected = "Shelf doesn't exist!"
        result = str(er.exception)
        self.assertEqual(expected, result)

    def test_remove_toy_toy_is_not_on_that_shelf_raise_exception(self):
        test_store = ToyStore()
        test_store.toy_shelf = {
            "A": "HotWheels",
            "B": None,
            "C": None,
            "D": "WaterGun",
            "E": None,
            "F": None,
            "G": "TeddyBear",
        }

        with self.assertRaises(Exception) as er:
            test_store.remove_toy("D", "HotWheels")

        expected = "Toy in that shelf doesn't exists!"
        result = str(er.exception)
        self.assertEqual(expected, result)

    def test_remove_toy_successfully_removed_toy(self):
        test_store = ToyStore()
        test_store.toy_shelf = {
            "A": "HotWheels",
            "B": None,
            "C": None,
            "D": "WaterGun",
            "E": None,
            "F": None,
            "G": "TeddyBear",
        }

        result = test_store.remove_toy("D", "WaterGun")
        self.assertEqual("Remove toy:WaterGun successfully!", result)
        self.assertEqual({
            "A": "HotWheels",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": "TeddyBear",
        }, test_store.toy_shelf)




if __name__ == "__main__":
    main()
