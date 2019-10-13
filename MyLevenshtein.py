def substitution(text1, text2):
    """The two texts have same lengths"""

    reference_text = list(text1)
    new_text = list(text2)

    assert reference_text == new_text
    levenshtein_distance = 0

    for i, letter in enumerate(reference_text):
        if new_text[i] != letter:
            levenshtein_distance += 1

    return levenshtein_distance


def deletion(text1, text2):
    """Length of text1 is greater than length of text2"""

    reference_text = list(text1)
    new_text = list(text2)

    assert reference_text > new_text
    levenshtein_distance = len(reference_text) - len(new_text)
    reference_text = reference_text[: len(new_text)]

    for i, letter in enumerate(reference_text):
        if new_text[i] != letter:
            levenshtein_distance += 1

    return levenshtein_distance


def insertion(text1, text2):
    """Length of text2 is greater than length of text1"""

    reference_text = list(text1)
    new_text = list(text2)

    assert reference_text < new_text
    levenshtein_distance = len(new_text) - len(reference_text)
    new_text = new_text[: len(reference_text)]

    for i, letter in enumerate(reference_text):
        if new_text[i] != letter:
            levenshtein_distance += 1

    return levenshtein_distance


def Levenshtein(text1, text2):
    """Take two texts and return the levenshtein distance of the two texts"""

    levenshtein_distance = 0

    if len(text1) == len(text2):
        levenshtein_distance = substitution(text1, text2)

    if len(text1) > len(text2):
        levenshtein_distance = insertion(text1, text2)

    if len(text1) < len(text2):
        levenshtein_distance = deletion(text1, text2)

    assert levenshtein_distance >= 0
    return levenshtein_distance
