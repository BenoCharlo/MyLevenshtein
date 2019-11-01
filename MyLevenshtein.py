import numpy as np


def levenshtein_operation(M, Cost):
    assert M.shape == (Cost.shape[0] + 1, Cost.shape[1] + 1)
    operations = M

    for i in range(1, M.shape[0] + 1):
        operations[i] = [
            min(M[i - 1, j] + 1, M[i, j - 1] + 1, M[i - 1, j - 1] + Cost(i - 1, j - 1))
            for j in range(1, M.shape[1] + 1)
        ]

    return operations


def Levenshtein(text1, text2):
    """Take two texts and return the levenshtein distance of the two texts"""

    levenshtein_distance = 0

    reference_text = list(text1)
    new_text = list(text2)

    if len(reference_text) == 0:
        levenshtein_distance = len(new_text)

    if len(new_text) == 0:
        levenshtein_distance = len(reference_text)

    if len(reference_text) > 0 and len(new_text) > 0:

        if reference_text == new_text:
            levenshtein_distance = 0

        else:

            operations = np.zeros((len(reference_text) + 1, len(new_text) + 1))
            operations[0] = range(len(new_text))
            operations[:, 0] = range(len(reference_text))

            Cost = np.zeros((len(reference_text), len(new_text)))

            for i, letter in enumerate(reference_text):
                Cost[i] = [
                    1 if letter != new_text[j] else 0 for j in range(1, len(new_text))
                ]

            operations = levenshtein_operation(operations, Cost)

            levenshtein_distance = operations[operations.shape[0], operations.shape[1]]

            assert levenshtein_distance >= 0

    return levenshtein_distance
