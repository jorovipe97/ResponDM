#Importando librerias
from time import sleep
import random
import tweepy
from credenciales import *

## Instrucciones de uso
# Cree un archivo llamado credenciales y dentro defina y asignele el valor correspondiente a las siguientes variables:
# USER_SCREEN_NAME
# CONSUMER_KEY
# CONSUMER_SECRET
# ACCESS_TOKEN
# ACCESS_TOKEN_SECRET

# Configurando credenciales del bot
print ("Identificando app")
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
print ("Dando pemriso")
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
print ("Secure == true")
auth.secure = True;
print ("Configurando auth en la api")
api = tweepy.API(auth)
user = api.get_user(USER_SCREEN_NAME)
print ("%s, description: %s" % (user.screen_name, user.description))

agradecimientos =  [
    "I appreciate it :D",
    "Thanks, I wish you well :D",
    "That would be nice, thanks :D",
    "It would be nice!!",
    "Thanks a lot!",
    "Thanks a million",
    "Thank you for your time and effort in this matter :D"
]

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            sleep(15 * 60)
        except StopIteration:
        	break


api.get_direct_message()
"""
for friend in limit_handled( tweepy.Cursor(api.friends).items() ):
    print ("Buscando...")    
    try:
        if friend.id not in followers:
            luckNumber = random.randint(0, 9)
            print ("2 < %s = %s" % (luckNumber, 1 < luckNumber))
            if 2 < luckNumber:                
                api.destroy_friendship(friend.id)
                print ("\nSe dejo de seguir a: %s, description: %s " % (friend.screen_name, friend.description))
            else:
                print ("\n%s no me esta siguiendo pero lo seguire un rato mas" % friend.screen_name)
    except tweepy.RateLimitError:
        print ("\nRate Limit Error, esperar 15 minutos")
        sleep(15*60)
    except tweepy.error.TweepError:
        print ("\nTweepy error, continuar al siguiente")
        continue
    except StopIteration:
        print ("StopIteration exception.... Bot finalizado")
        break
"""