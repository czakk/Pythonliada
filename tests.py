import unittest
from game import *


class TeamTest(unittest.TestCase):
    def test_build(self):
        team = Team('Test1')
        self.assertEqual(team.name, 'Test1')
        self.assertEqual(team.members, [])

    def test_addMember(self):
        team = Team('Test1')
        member = Member('Test2')
        team.addMember(member)
        self.assertEqual(team.members[0].name, 'Test2')

    def test_setScore(self):
        team = Team('Test1')
        team.addScore(10)
        self.assertEqual(team.name, 'Test1')
        self.assertEqual(team.score, 10)


class QuestionTest(unittest.TestCase):
    def test_build(self):
        question = Question(1, 'Test1')
        self.assertEqual(question.id, 1)
        self.assertEqual(question.text, 'Test1')


class TournamentTest(unittest.TestCase):
    def test_build(self):
        tournament = Tournament()
        self.assertEqual(tournament.teams, [])

    def test_addTeam(self):
        tournament = Tournament()
        team = Team('Test1')
        tournament.addTeam(team)
        self.assertEqual(tournament.teams[0].name, 'Test1')

    def test_setQuestions(self):
        tournament = Tournament()
        question = [(1, 'Test1'), (2, 'Test2'), (3, 'Test3')]
        tournament.setQuestions(question)
        self.assertIsInstance(tournament.questions[1], Question)
        self.assertEqual(tournament.questions[0].id, 1)
        self.assertEqual(tournament.questions[2].text, 'Test3')

    def test_getLeaderboard(self):
        tournament = Tournament()

        team1 = Team('Test1')
        team1.score = 10
        team2 = Team('Test2')
        team2.score = 20
        team3 = Team('Test3')
        team3.score = 30

        tournament.addTeam(team1)
        tournament.addTeam(team2)
        tournament.addTeam(team3)

        self.assertEqual(tournament.getLeaderboard(), [team3, team2, team1])


class GameTest(unittest.TestCase):
    def test_displayQuestions(self):
        q1 = Question(1, 'Test1')
        q1.answers = [('Test1', 1), ('Test2', 2), ('Test3', 3)]
        q2 = Question(2, 'Test2')
        q2.answers = [('Test1', 1), ('Test2', 2), ('Test3', 3)]
        q3 = Question(3, 'Test3')
        q3.answers = [('Test1', 1), ('Test2', 2), ('Test3', 3)]
        questions = [q1, q2, q3]
        hidden = [[True, False, False], [False, True, False], [False, False, True]]
        self.assertEqual(displayQuestionsAndAnswers(questions, hidden),
                         ['1. Test1\n\t-\n\tTest2 - 2%\n\tTest3 - 3%',
                          '2. Test2\n\tTest1 - 1%\n\t-\n\tTest3 - 3%',
                          '3. Test3\n\tTest1 - 1%\n\tTest2 - 2%\n\t-'])
        hidden = [[False, False, False], [False, False, False], [False, False, False]]
        self.assertEqual(displayQuestionsAndAnswers(questions, hidden),
                         ['1. Test1\n\tTest1 - 1%\n\tTest2 - 2%\n\tTest3 - 3%',
                          '2. Test2\n\tTest1 - 1%\n\tTest2 - 2%\n\tTest3 - 3%',
                          '3. Test3\n\tTest1 - 1%\n\tTest2 - 2%\n\tTest3 - 3%'])


if __name__ == '__main__':
    unittest.main()
