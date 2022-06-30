import json, pprint
f = open('message_1.json')
data = json.load(f)
participants = []
messages = data['messages']
board  = {}
print('the participants of this game are:')
for i in data['participants']: # creates a list of dictionarys containing the name  of  the participants and prints the names
   #prints name
    n = i['name']
    print(n)

    #appends dict entry to  participants list
    participants.append(i)

    board[i['name']]={'Average score': 0, 'Games played' : 0, 'Total guesses' : 0 }
# print(board)

for i in messages:
    name =  i["sender_name"]
    # print(name)
    try:
        # if messages
        g = i['content'][11]
        # print(g)
    except:
        continue
    if g.isdigit():
        # print(g)
        board[name]['Games played'] += 1
        board[name]['Total guesses'] += int(g)
        board[name]['Average score'] = board[name]['Total guesses'] / board[name]['Games played']
    elif g == 'X':
        board[name]['Games played'] += 1
        board[name]['Average score'] = board[name]['Total guesses'] / board[name]['Games played']

pprint.pprint(board)
