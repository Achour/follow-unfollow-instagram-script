from instagram_private_api import Client, ClientCompatPatch
from time import sleep
import functools
import socket


def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False




print = functools.partial(print, flush=True)




user_name = 'yourusername'
password = 'password'




while is_connected() == False:
        print("no internet connecton ")
        print("rechecking ...")
        sleep(1)


api = Client(user_name, password)


celebrities = {
        'instagram': '25025320',
        'cristiano': '173560420',
        'selenagomez': '460563723',
        'arianagrande': '7719696',
        'taylorswift': '11830955',
        'beyonce': '247944034',
        'therock':'232192182',
        'kimkardashian':'18428658',
        'kyliejenner':'12281817',
        'kendalljenner':'6380930',
        'nickiminaj':'451573056',
        'natgeo':'787132',
        'neymarjr':'26669533',
        'nike':'13460080',
        'leomessi':'427553890',
        'khloekardashian':'208560325',
        'mileycyrus':'325734299',
        'katyperry':'407964088',
        'jlo':'305701719',
        'ddlovato':'189393625',
        'kourtneykardash':'145821237',
        'victoriassecret':'3416684',
        'badgalriri':'25945306',
        'kevinhart4real':'6590609',
        'fcbarcelona':'260375673',
        'realmadrid':'290023231',
        'theellenshow':'18918467',
        'justintimberlake':'303054725',
        'zendaya':'9777455'
}


for i in range(1000):


        for key,value in celebrities.items():
                while is_connected() == False:
                        print("no internet connecton ")
                        print("rechecking ...")
                        sleep(1)


                api.friendships_create(value)
                print("{0} : Followed successfully".format(key))
                sleep(5)


        print('')
        print('relaxing ..')
        print('')


        for key,value in celebrities.items():        
                while is_connected() == False:
                        print("no internet connecton ")
                        print("rechecking ...")
                        sleep(1)


                api.friendships_destroy(value)
                print("{0} : Unfollowed successfully".format(key))
                sleep(5)


        print('')
        print ("######################################")
        print('')
