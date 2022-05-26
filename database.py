import sqlite3


class Database:
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def getQuestions(self):
        self.cursor.execute('SELECT question_id, text FROM questions ORDER BY random()')
        return self.cursor.fetchall()

    def getAnswersForId(self, question_id: int):
        self.cursor.execute('SELECT * FROM answers WHERE question = ?', (question_id,))
        return self.cursor.fetchall()

    def addAnswer(self, question_id: int, text: str):
        self.cursor.execute('INSERT INTO answers VALUES (NULL, ?, ?)', (text, question_id))
        self.connection.commit()

    def getLastAnswerId(self):
        self.cursor.execute('SELECT max(answer_id) from answers')
        return self.cursor.fetchone()[0]

    def setVotesForAnswer(self, answer_id: int, votes: list):
        self.cursor.execute('UPDATE voting SET vote1 = vote1 + ?, vote2 = vote2 +  ?, vote3 = vote3 + ? WHERE answer_id = ?',
                            (votes[0], votes[1], votes[2], answer_id))
        self.connection.commit()

    def getFiveRandomNotUsedQuestions(self):
        self.cursor.execute('SELECT question_id, text FROM questions WHERE used = FALSE ORDER BY random() LIMIT 5')
        return self.cursor.fetchall()

    def setQuestionUsed(self, question_id: int):
        self.cursor.execute('UPDATE questions SET used = TRUE WHERE question_id = ?', (question_id,))
        self.connection.commit()

    def setQuestionsNotUsed(self):
        self.cursor.execute('UPDATE questions SET used = FALSE')
        self.connection.commit()

    def getAnswersWithPercent(self, question_id: int):
        self.cursor.execute('select text, perct from answers_percent WHERE question = ? ORDER BY perct DESC LIMIT 5',
                            (question_id,))
        return self.cursor.fetchall()
