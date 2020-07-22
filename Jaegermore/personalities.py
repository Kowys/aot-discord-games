import discord
import random

def eren(player):
    writeup = 'Determined. Courageous. Resolute. These are your defining attributes. \
You are the type of person whom, once set on a goal, will do whatever it takes to achieve success against all odds. \
Some may see you as headstrong and impulsive, but many respect you for your unwavering spirit and dedication to your goals.'
    result = discord.Embed(title= 'You are **Eren**!', description = writeup, colour=0x5CFFE9)
    username, user_url = player.name, player.avatar_url
    result.set_author(name = username, icon_url = user_url)
    
    urls = ['https://i.imgur.com/9rG4HHC.gif',
            'https://i.imgur.com/fzmZ3hk.gif',
            'https://i.imgur.com/Yf5wjZe.gif',
            'https://i.imgur.com/XbkOPQ8.gif',
            'https://i.imgur.com/Xntn7eK.gif']
    result.set_image(url = urls[random.randint(0, len(urls) - 1)])
    return result

def mikasa(player):
    writeup = 'On the outside, you are the strong and fearless person whom everyone looks up to. \
However, what many do not know is that you have a soft side, especially towards the important people in your life. \
Once someone has earned your trust, you are exceptionally loyal to them and will stand by their side no matter what.'
    result = discord.Embed(title= 'You are **Mikasa**!', description = writeup, colour=0x5CFFE9)
    username, user_url = player.name, player.avatar_url
    result.set_author(name = username, icon_url = user_url)
    
    urls = ['https://i.imgur.com/dLofDNA.gif',
            'https://i.imgur.com/7TwlowP.gif',
            'https://i.imgur.com/sl8ywCC.gif',
            'https://i.imgur.com/bH4ObXP.gif',
            'https://i.imgur.com/turkkTg.gif',
            'https://i.imgur.com/I0h1XD0.gif',
            'https://i.imgur.com/chUtCJx.gif',
            'https://i.imgur.com/gu0sjBQ.gif',
            'https://i.imgur.com/oj2hhTa.gif',
            'https://i.imgur.com/Rm6Aa9t.gif',
            'https://i.imgur.com/OBEimH5.gif']

    result.set_image(url = urls[random.randint(0, len(urls) - 1)])
    return result

def armin(player):
    writeup = '"Nothing ventured, nothing gained." To a large degree, you apply this motto to all aspects of your life. \
Ever hungry for knowledge, your insatiable curiosity and your logical mind have given you a deep and intricate understanding of the world you live in. \
With the gifts you possess, you have the potential to change the world.'
    result = discord.Embed(title= 'You are **Armin**!', description = writeup, colour=0x5CFFE9)
    username, user_url = player.name, player.avatar_url
    result.set_author(name = username, icon_url = user_url)
    
    urls = ['https://i.imgur.com/YXDh10y.gif',
            'https://i.imgur.com/Nzs0UB6.gif',
            'https://i.imgur.com/BUksr18.gif',
            'https://i.imgur.com/yuhlJ1I.gif',
            'https://i.imgur.com/WUwlkZs.gif',
            'https://i.imgur.com/psVtT97.gif',
            'https://i.imgur.com/uUwi9JR.gif',
            'https://i.imgur.com/TccLtEU.gif']
    result.set_image(url = urls[random.randint(0, len(urls) - 1)])
    return result

def jean(player):
    writeup = 'To most people, you appear to be an uncaring person who always puts themselves first. \
However, deep down, you are really a kind person who values friendships and always has your buddies\' back. You may not be the smartest or the toughest  \
person around, but it is precisely because of it that you are able to emphasize with others, which is what makes you a great leader.'
    result = discord.Embed(title= 'You are **Jean**!', description = writeup, colour=0x5CFFE9)
    username, user_url = player.name, player.avatar_url
    result.set_author(name = username, icon_url = user_url)
    
    urls = ['https://i.imgur.com/sBJikp9.gif',
            'https://i.imgur.com/TICMwVd.gif',
            'https://i.imgur.com/5kVgkNt.gif',
            'https://i.imgur.com/il3RzJw.gif',
            'https://i.imgur.com/D6S9PXi.gif',
            'https://i.imgur.com/abeA0WW.gif']
    result.set_image(url = urls[random.randint(0, len(urls) - 1)])
    return result

def krista(player):
    writeup = 'You are a kind and caring person who always tries to see the good in everyone, earning the love and adoration of those around you. \
However, your external personality is not really your true self, but to an extent a facade that you put up to escape from a troubled past. \
Deep inside your soul, you yearn to be free from pretending to be someone that you are not, to be able to come to terms with who you really are.'
    result = discord.Embed(title= 'You are **Krista**!', description = writeup, colour=0x5CFFE9)
    username, user_url = player.name, player.avatar_url
    result.set_author(name = username, icon_url = user_url)
    
    urls = ['https://i.imgur.com/DsQvCy7.gif',
            'https://i.imgur.com/Ha5yUI2.gif',
            'https://i.imgur.com/a0CRAQj.gif',
            'https://i.imgur.com/gWn3l5r.gif',
            'https://i.imgur.com/Sy2Q02o.gif',
            'https://i.imgur.com/SfBJdMB.gif',
            'https://i.imgur.com/BcTzTmh.gif']
    result.set_image(url = urls[random.randint(0, len(urls) - 1)])
    return result

def sasha(player):
    writeup = 'With your easy-going and cheerful personality, you are the life of parties and the light of people\'s lives. Despite having an odd \
quirk or two (perhaps an unusually voracious appetite), your friends love you for who you are and can\'t wait to have you join in the fun!'
    result = discord.Embed(title= 'You are **Sasha**!', description = writeup, colour=0x5CFFE9)
    username, user_url = player.name, player.avatar_url
    result.set_author(name = username, icon_url = user_url)
    
    urls = ['https://i.imgur.com/4y1Xq3J.gif',
            'https://i.imgur.com/2g0ExGW.gif',
            'https://i.imgur.com/24x7nI5.gif',
            'https://i.imgur.com/KOFLBS6.gif',
            'https://i.imgur.com/iqi9JxT.gif',
            'https://i.imgur.com/x2f9qLR.gif',
            'https://i.imgur.com/WBQc2dX.gif',
            'https://i.imgur.com/LKbm7hI.gif']
    result.set_image(url = urls[random.randint(0, len(urls) - 1)])
    return result

def levi(player):
    writeup = 'You are the strong but silent type. You are usually very direct with your words and speak no more than necessary. \
This may make you seem unwelcoming and unfriendly to strangers, but those close to you know that you have a noble spirit and would \
go to great lengths to fight for the causes you believe in and protect those you love.'
    result = discord.Embed(title= 'You are **Levi**!', description = writeup, colour=0x5CFFE9)
    username, user_url = player.name, player.avatar_url
    result.set_author(name = username, icon_url = user_url)

    urls = ['https://i.imgur.com/91iptWG.gif',
            'https://i.imgur.com/AXmAAxI.gif',
            'https://i.imgur.com/gwxny7f.gif',
            'https://i.imgur.com/aWSLhVj.gif',
            'https://i.imgur.com/j5Se7nc.gif',
            'https://i.imgur.com/jxaGxcz.gif',
            'https://i.imgur.com/D5gg2aA.gif',
            'https://i.imgur.com/jJ8lXIF.gif',
            'https://i.imgur.com/n6QWsz1.gif']
    result.set_image(url = urls[random.randint(0, len(urls) - 1)])
    return result

def annie(player):
    writeup = 'You possess a strong and independent personality. You tend to rely on yourself most of the time, rarely interacting or seeking \
help from others, preferring to do things your own way. To those around you, this behaviour may make you seem aloof and anti-social, but it also \
commands respect from others who recognize the value of not following others blindly and choosing to forge your own path.'
    result = discord.Embed(title= 'You are **Annie**!', description = writeup, colour=0x5CFFE9)
    username, user_url = player.name, player.avatar_url
    result.set_author(name = username, icon_url = user_url)
    
    urls = ['https://i.imgur.com/sJOiA5i.gif',
            'https://i.imgur.com/QZIitrE.gif',
            'https://i.imgur.com/SAmdd0E.gif',
            'https://i.imgur.com/Mx6c6nk.gif',
            'https://i.imgur.com/KuBjxcj.gif',
            'https://i.imgur.com/EvtarEj.gif',
            'https://i.imgur.com/Oxpb0Xi.gif',
            'https://i.imgur.com/uBAzkoH.gif']
    result.set_image(url = urls[random.randint(0, len(urls) - 1)])
    return result

def erwin(player):
    writeup = 'You are a naturally charismatic person, and are able to inspire those around you to greater heights. \
Even so, you rarely allow your emotions to overtake you, giving you the ability to see the big picture even in stressful situations. \
Like all great leaders, you are prepared to make sacrifices and make the hard choices necessary to achieve success.'
    result = discord.Embed(title= 'You are **Erwin**!', description = writeup, colour=0x5CFFE9)
    username, user_url = player.name, player.avatar_url
    result.set_author(name = username, icon_url = user_url)
    
    urls = ['https://i.imgur.com/ClsRTrq.gif',
            'https://i.imgur.com/BJZu8Py.gif',
            'https://i.imgur.com/Y7GUL09.gif',
            'https://i.imgur.com/eRxfRKH.gif',
            'https://i.imgur.com/wC87INm.gif',
            'https://i.imgur.com/w4zmGaw.gif']
    result.set_image(url = urls[random.randint(0, len(urls) - 1)])
    return result

all_results = {'mikasa':mikasa, 'eren':eren, 'armin':armin, 'jean':jean, 'krista':krista, 'sasha':sasha, 
'levi':levi, 'annie':annie, 'erwin':erwin}