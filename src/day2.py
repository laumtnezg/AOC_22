import sys
#1st part function
def game(opponent, me):
    me_score = guide_game[me][0]
    if opponent == me:
        r_score = 3
    elif guide_game[opponent][1] == me:
        r_score = 6
    elif guide_game[opponent][2] == me:
        r_score = 0    
    return me_score + r_score
#2nd part function
def new_game(opponent, result):
    r_score = result
    if result == 0:
        me = guide_game[opponent][2]
        me_score = guide_game[me][0]
    elif result == 3:
        me_score = guide_game[opponent][0]
    elif result == 6:
        me = guide_game[opponent][1]
        me_score = guide_game[me][0]
    return r_score + me_score


# guide_game[opponent] = [points, beaten_by, beats]
guide_game = {"A" : [1, "B", "C"],
              "B": [2, "C", "A"],
              "C": [3, "A", "B"]}

guide_me = {"X": "A", "Y": "B", "Z": "C"} 

whole_score = []
fname = sys.argv[1]
with open(fname, 'r') as fhandle:
    for line in fhandle:
        line = line.replace("\n", "")
        whole_score.append(game(line.split(" ")[0], guide_me[line.split(" ")[1]]))
print(sum(whole_score))

## 2nd part
guide_me = {"X": 0, "Y": 3, "Z": 6} 
new_score = []
with open(fname, 'r') as fhandle:
    for line in fhandle:
        line = line.replace("\n", "")
        new_score.append(new_game(line.split(" ")[0], guide_me[line.split(" ")[1]]))
print(sum(new_score))

