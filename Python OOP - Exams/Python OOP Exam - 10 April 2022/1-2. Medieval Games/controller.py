from project.player import Player


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        added_players = []
        for player in players:
            if player in self.players:
                continue
            self.players.append(player)
            added_players.append(player.name)

        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_player_name(player_name)
        if player is None:
            return

        if sustenance_type != "Food" and sustenance_type != "Drink":
            return

        supply = self.__find_supply_by_type(sustenance_type)
        if supply is None:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        player.stamina = min(player.stamina + supply.energy, Player.MAX_STAMINA)
        self.supplies.pop(self.supplies.index(supply))  # error maybe

        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__find_player_name(first_player_name)
        second_player = self.__find_player_name(second_player_name)

        error_message = self.__get_error_message(first_player, second_player)
        if error_message:
            return error_message

        if second_player.stamina < first_player.stamina:
            first_player, second_player = second_player, first_player

        first_player_win = self.__attack(first_player, second_player)
        if first_player_win:
            return f"Winner: {first_player.name}"

        second_player_win = self.__attack(second_player, first_player)
        if second_player_win:
            return f"Winner: {second_player.name}"

        winner = first_player if first_player.stamina > second_player.stamina else second_player
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - player.age * 2, Player.MIN_STAMINA)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = ''
        for player in self.players:
            result += str(player) + '\n'
        for supply in self.supplies:
            result += supply.details() + '\n'

        return result.strip()

    def __find_player_name(self, player_name: str):
        for player in self.players:
            if player.name == player_name:
                return player

    def __find_supply_by_type(self, sustenance_type: str):
        for idx in range(len(self.supplies) - 1, -1, -1):
            supply = self.supplies[idx]
            if supply.__class__.__name__ == sustenance_type:
                return supply

    def __get_error_message(self, first_player, second_player):
        error_message = ""
        if first_player.stamina == 0:
            error_message += f"Player {first_player.name} does not have enough stamina."
        elif second_player.stamina == 0:
            error_message += f"Player {second_player.name} does not have enough stamina."

        return error_message.strip()

    def __attack(self, attacker, defender):
        attacker_damage = attacker.stamina / 2
        defender.stamina = max(defender.stamina - attacker_damage, Player.MIN_STAMINA)
        return defender.stamina == 0
