#!/usr/bin/python3
def multiple_returns(sentence):
    t = len(sentence)
    le = ""
    if t == 0:
        le = "None"
    else:
        le = sentence[0]
    return t, le
