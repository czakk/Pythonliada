from typing import List


class Member:
    def __init__(self, name: str):
        self.name = name


class Question:
    def __init__(self, id: int, question: str):
        self.id = id
        self.text = question
        self.answers:  List[tuple[str, int]] = []

    def setAnswers(self, answers: List[tuple[str, int]]):
        self.answers = answers


class Team:
    def __init__(self, name: str):
        self.name = name
        self.members: List[Member] = []
        self.score = 0

    def __str__(self):
        return self.name

    def addMember(self, member: Member):
        self.members.append(member)

    def addScore(self, score: int):
        self.score += score


class Tournament:
    def __init__(self):
        self.teams: List[Team] = []
        self.questions: List[Question] = []

    def addTeam(self, team: Team):
        self.teams.append(team)

    def setQuestions(self, questions: List[tuple[int, str]]):
        self.questions = [Question(q[0], q[1]) for q in questions]

    def getLeaderboard(self):
        return sorted(self.teams, key=lambda t: t.score, reverse=True)


if __name__ == '__main__':
    pass

