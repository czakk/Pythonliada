from database import Database


class Vote:
    def __init__(self):
        self.db = Database('familiada.db')
        self.questions = {}
        self.results = {}

    def __del__(self):
        for x in self.results:
            self.db.setVotesForAnswer(x, list(self.results[x]))

    def setQuestionsInObject(self):
        self.questions = {
            question[1]: {
                'id': question[0],
                'answers': {
                    answer[1]: {
                        'id': answer[0],
                    } for answer in self.db.getAnswersForId(question[0])
                }, } for question in self.db.getQuestions()
        }
        return self.questions


def main():
    vote = Vote()
    for x in vote.setQuestionsInObject().items():
        print(f'Q: {x[0]}')
        answers = x[1]['answers'].items()
        for index, key in enumerate(answers):
            print(f'{index + 1}. {key[0]}')
        for i in range(3):
            votes = [1 if x == i else 0 for x in range(3)]
            chosenAnswer = input('A: ')
            if chosenAnswer == 'skip':
                break
            elif chosenAnswer[0] == '.':
                vote.db.addAnswer(x[1]['id'], chosenAnswer[1:])
                vote.results[vote.db.getLastAnswerId()] = votes
            else:
                vote.results[list(answers)[int(chosenAnswer) - 1][1]['id']] = votes
        print()


if __name__ == '__main__':
    main()
