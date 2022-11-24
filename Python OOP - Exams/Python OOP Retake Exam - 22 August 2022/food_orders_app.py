from client import Client
from meals.dessert import Dessert
from meals.starter import Starter
from meals.main_dish import MainDish


class FoodOrdersApp:
    receipt_id = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def check_if_registered(self, phone_number: str):
        for client in self.clients_list:
            if client.phone_number == phone_number:
                return True

    def validate_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def find_client(self, phone_number: str):
        for client in self.clients_list:
            if client.phone_number == phone_number:
                return client

    def register_client(self, client_phone_number: str):
        if self.check_if_registered(client_phone_number):
            raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if type(meal).__name__ in ["Starter", "MainDish", "Dessert"]:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        menu_details = []
        for meal in self.menu:
            menu_details.append(meal.details())

        return "\n".join(menu_details)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self.validate_menu()
        if not self.check_if_registered(client_phone_number):
            self.register_client(client_phone_number)
        client = self.find_client(client_phone_number)
        meals_to_order = []
        current_bill = 0

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    if meal.quantity >= meal_quantity:
                        meals_to_order.append(meal)
                        current_bill += meal_quantity * meal.price
                        break
                    else:
                        raise Exception(f"Not enough quantity of {type(meal).__name__}: {meal_name}!")
            else:
                raise Exception(f"{meal_name} is not on the menu!")
        client.shopping_cart.extend(meals_to_order)
        client.bill += current_bill

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            client.ordered_meals[meal_name] = meal_quantity
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity -= meal_quantity

        return f"Client {client_phone_number} successfully ordered {', '.join(meal.name for meal in client.shopping_cart)} " \
               f"for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.find_client(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for ordered_meal, quantity in client.ordered_meals.items():
            for menu_meal in self.menu:
                if ordered_meal == menu_meal.name:
                    menu_meal.quantity += quantity

        client.shopping_cart = []
        client.bill = 0
        client.ordered_meals = {}
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number):
        client = self.find_client(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        total_paid_money = client.bill
        client.shopping_cart = []
        client.bill = 0
        client.ordered_meals = {}
        self.receipt_id += 1
        return f"Receipt #{self.receipt_id} with total amount of {total_paid_money:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."


food_orders_app = FoodOrdersApp()
print(food_orders_app.register_client("0899999999"))
french_toast = Starter("French toast", 6.50, 5)
hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
print(food_orders_app.add_meals_to_menu(
    french_toast, hummus_and_avocado_sandwich,
    tortilla_with_beef_and_pork,
    risotto_with_wild_mushrooms,
    chocolate_cake_with_mascarpone,
    chocolate_and_violets))
print(food_orders_app.show_menu())
food = {"Hummus and Avocado Sandwich": 5,
        "Risotto with Wild Mushrooms": 1,
        "Chocolate and Violets": 4}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food))
additional_food = {"Risotto with Wild Mushrooms": 2,
                   "Tortilla with Beef and Pork": 2}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **additional_food))
print(food_orders_app.finish_order("0899999999"))
print(food_orders_app)
