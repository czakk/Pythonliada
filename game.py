from typing import List
from tournament import *


def displayQuestionsAndAnswers(questions: List[Question], hidden: List[List[bool]]) -> str:
    return ['\n'.join([f'{i + 1}. {q.text}', '\n'.join([f'\t{a[0]} - {int(a[1])}%'
                                                        if hidden[i][j] is False else '\t-'
                                                        for j, a in enumerate(q.answers)])])
            for i, q in enumerate(questions)]
