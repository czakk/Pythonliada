from game import *
from database import Database


def main():
    db = Database('familiada.db')
    db.setQuestionsNotUsed()
    tournament = Tournament()

    def displayLeaderboard():
        print('Leaderboard:\n' + '\n'.join([f'{x.name}[{x.members[0].name} {x.members[1].name}]: {x.score}'
                                            for x in tournament.getLeaderboard()]))

    while True:
        for _ in range(2):
            tournament.addTeam(Team(input('Enter team name: ')))
        teams = tournament.teams[-2:]
        for i in range(2):
            teams[i].addMember(Member(input(f'{teams[i].name}: Enter player name: ')))
            teams[i].addMember(Member(input(f'{teams[i].name}: Enter player name: ')))
        tournament.setQuestions(db.getFiveRandomNotUsedQuestions())

        for i in tournament.questions:
            db.setQuestionUsed(i.id)

        for x in tournament.questions:
            x.setAnswers(db.getAnswersWithPercent(x.id))

        hidden = [[True for _ in q.answers] for q in tournament.questions]

        for x in range(len(displayQuestionsAndAnswers(tournament.questions, hidden))):
            teamsMistakes = [0, 0]
            print(displayQuestionsAndAnswers(tournament.questions, hidden)[x])
            team = int(input(f'{teams[0].name} or {teams[1].name}?: ')) - 1
            scores = 0

            while any(hidden[x]) is not False:
                if teamsMistakes == [3, 3]:
                    hidden[x] = list(map(lambda j: False, hidden[x]))
                    print(displayQuestionsAndAnswers(tournament.questions, hidden)[x])
                    scores = 0
                    break
                print(f'Mistakes:\n\t{teams[0].name} {"X" * teamsMistakes[0]}\n\t{teams[1].name} {"X" * teamsMistakes[1]}')
                print(displayQuestionsAndAnswers(tournament.questions, hidden)[x])

                choice = input(f'{teams[team].name} answers: ')
                if choice.lower() != 'x':
                    scores += tournament.questions[x].answers[int(choice) - 1][1]
                    hidden[x][int(choice) - 1] = False
                else:
                    teamsMistakes[team] += 1
                    if teamsMistakes[team] == 3:
                        team = 1 if team == 0 else 0

                if any(hidden[x]) is False:
                    print(displayQuestionsAndAnswers(tournament.questions, hidden)[x])
            teams[team].score += scores
            print(f'{teams[0].name} score: {teams[0].score}\n{teams[1].name} score: {teams[1].score}')

        if teams[0].score == teams[1].score:
            print('Draw')
        else:
            winner = sorted(teams, key=lambda x: x.score, reverse=True)[0]
            print(f'{winner.name} wins with {winner.score} points!')
        displayLeaderboard()

        if input('Continue? (y/n)') == 'n':
            print('Tournament ended! And The Winner is: ' + tournament.getLeaderboard()[0].name)
            displayLeaderboard()
            db.setQuestionsNotUsed()
            break


if __name__ == '__main__':
    main()
