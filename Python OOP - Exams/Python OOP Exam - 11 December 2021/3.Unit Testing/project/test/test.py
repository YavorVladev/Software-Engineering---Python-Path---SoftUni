from unittest import TestCase, main
from project.team import Team


class TestGunitSquad(TestCase):

    def setUp(self) -> None:
        self.team = Team("WinnerTeam")

    def test_constructor(self):
        self.assertEqual("WinnerTeam", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_setter(self):
        with self.assertRaises(ValueError) as er:
            Team("456")
            Team("Winner36")
            Team("Win ner")

        expected = "Team Name can contain only letters!"
        actual = str(er.exception)

        self.assertEqual(expected, actual)

    def test_add_member(self):
        team = Team("TestTeam")
        team.members = {"Yavor": 22}
        result = team.add_member(Adrean=21, Tea=23)
        expected = "Successfully added: Adrean, Tea"
        self.assertEqual(expected, result)
        self.assertEqual({"Yavor": 22, "Adrean": 21, "Tea": 23}, team.members)

    def test_remove_member(self):
        team = Team("TestTeam")
        team.add_member(Yavor=21)
        result = team.remove_member("Yavor")
        expected = "Member Yavor removed"
        self.assertEqual({}, team.members)
        self.assertEqual(expected, result)
        result1 = team.remove_member("Tea")
        expected1 = "Member with name Tea does not exist"
        self.assertEqual(result1, expected1)
        self.assertEqual({}, team.members)

    def test_gt_method(self):
        team1 = Team("TestTeaOne")
        team1.add_member(Yavor=21)
        team2 = Team("TestTeamTwo")
        team2.add_member(Tea=23, Adrean=21)
        result = team1 > team2
        self.assertEqual(False, result)
        self.assertTrue(len(team1.members) <= len(team2.members))

    def test_len_method(self):
        team = Team("TestTeam")
        team.members = {"Yavor": 23, "Adrean": 21, "Tea": 24}
        self.assertEqual(3, len(team))
        self.assertEqual({"Yavor": 23, "Adrean": 21, "Tea": 24}, team.members)

    def test_add_method(self):
        team1 = Team("TestTeamOne")
        team1.add_member(Yavor=21, Tea=23, Adrean=21)
        team2 = Team("TestTeamTwo")
        team2.add_member(Dimitar=23, Ivan=45, Kiko=31)
        merged_team = team1 + team2

        self.assertEqual("TestTeamOneTestTeamTwo", merged_team.name)
        self.assertEqual({"Yavor": 21, "Tea": 23, "Adrean": 21, "Dimitar": 23, "Ivan": 45, "Kiko": 31},
                         merged_team.members)

    def test_str_method(self):
        team = Team("TestTeam")
        team.add_member(Yavor=21, Tea=23, Adrean=21)
        result = f"Team name: TestTeam\n" \
                 f"Member: Tea - 23-years old\n" \
                 f"Member: Adrean - 21-years old\n" \
                 f"Member: Yavor - 21-years old"

        self.assertEqual(result, team.__str__())

    if __name__ == "__main__":
        main()
