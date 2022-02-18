import json
import twitter2
# import twitter1

acc=input()
data=twitter2.data_return(acc)
with open('data.json', 'w')as file:
    json.dump(data, file, indent=4)
with open('data.json', 'r')as file:
    dicti=json.load(file)
cur=dicti
while True:
    if isinstance(cur, dict):
        keys = list(cur.keys())
        print('there is a dictionary')
        print(*keys, sep ='\n')
        key=input('Please insert a key: ')
        while True:
            try:
                cur=cur[key]
                break
            except KeyError:
                key=input('Please insert a *valid* key: ')
    elif isinstance(cur,list):
        print(len(cur))
        index=input()
        cur=cur[int(index)]
    else:
        print(cur)
        break
