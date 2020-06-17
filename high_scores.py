def latest(scores):
    scores.sort()
    if scores[0] == 0:
        return scores[1]
    if scores[0] != 0:
        return scores[0]


def personal_best(scores):
    scores.sort()
    return scores[-1]


def personal_top_three(scores):
    scores.sort(reverse=True)
    numc = len(scores)
    if numc <= 2:
        return scores
    elif numc >= 3:
        tres=scores[:3]
        return tres
