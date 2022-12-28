

from termcolor import colored

import requests

print('JANGAN DISEBAR YA ZID!')

with open ('username.txt', 'r')as f:

    r = f.read()

k = r.split('\n')

for i in range(len(k)):

    username = k[i]

    response = requests.get(f'https://api.twitter.com/i/users/username_available.json?username={username}').json()

    if response['valid']:

       with open('available.txt','a')as f:

           f.write('{0}\n'.format(username))

    if response['valid']:

        print(colored(f'NIH PAKE MBAH ! {username}','yellow'))

    else:

        print(colored(f'SABAR, NGOPI DULU ! {username}','red'))

print('Sukses! No dana ane masih sama :D')

print('Fullochz')

