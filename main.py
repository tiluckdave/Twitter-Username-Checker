import tweepy
import os
from dotenv import load_dotenv
from itertools import product
load_dotenv()

client = tweepy.Client(os.getenv('BEARER_TOKEN'), os.getenv('API_KEY'), os.getenv('API_SECRET'))

hint = str(input("Enter 5 letter word with letters and underscores: (e.g. k_v_a) "))
if (len(hint) != 5):
    print("Invalid input. Please try again.")
    exit()
if not (hint.isalpha() or '_' in hint):
    print("Invalid input. Please try again.")
    exit()

allowed_symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# , 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'

_count = hint.count('_')
keywords = [''.join(i) for i in product(allowed_symbols, repeat = _count)]


generated_names = []

hint = list(hint)
temp = hint.copy()

for keyword in keywords:
    count = 0
    for i, j in enumerate(temp):
        if temp[i] == '_':
            # print(temp)
            # print(keyword[count])
            temp[i] = keyword[count]
            count = count + 1
    generated_names.append("".join(temp))
    temp = hint.copy()


            
count = 0

for i in generated_names[:300]:
    data = client.get_user(username=i)
    if (data.errors == []):
        continue
    elif (data.errors[0]['detail'] == f'User has been suspended: [{data.errors[0]["resource_id"]}].'):
        continue
    print(data.errors[0]['value'])
    count = count + 1

print("Total number of username available: " + str(count))