"""json reader"""
import json
from urllib.error import HTTPError
import twitter2
# import urllib
# import twitter1


def account():
    """
    Gets and reads a json file using twitter API
    """
    acc = input('Please enter a twitter account ')
    while True:
        try:
            data = twitter2.data_return(acc)
            break
        except HTTPError:
            acc = input('Please enter an existing twitter account ')
    with open('data.json', 'w')as file:
        json.dump(data, file, indent=4)
    with open('data.json', 'r')as file:
        dicti = json.load(file)
    return dicti


def walking(cur):
    """
    Walks through the dictionary until a non dict or list object is found
    """
    while True:
        if isinstance(cur, dict):
            keys = list(cur.keys())
            print('there is a dictionary')
            print(*keys, sep='\n')
            key = input('Please insert a key: ')
            while True:
                try:
                    cur = cur[key]
                    break
                except KeyError:
                    key = input('Please insert a *valid* key: ')
        elif isinstance(cur, list):
            print(len(cur))
            index = input(
                f'there is a list out here. there in a {len(cur)} elements in it')
            while True:
                if (int(index)-1) <= len(cur) and int(index) >= 1:
                    cur = cur[int(index)-1]
                    break
                else:
                    index = input(
                        f'there is a list out here. there in a {len(cur)} \
                        elements in it, choose the number wisely.')
        else:
            print(cur)
            print('Good luck!')
            break


if __name__ == '__main__':
    walking(account())
