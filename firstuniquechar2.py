
def solution(inp):

    for idx, i in enumerate(inp):
        if inp.count(i) == 1:
           return idx
    return -1

solution('mauro moreira')