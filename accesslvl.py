import sys

lvl = 0 # access level
guess = 0 # number of tries
lim = 3 # tries limit

login = ''
while not login and guess < lim:
    login = input ("Login: ")
    guess += 1
if guess == lim:
    sys.exit()
else:
    guess = 0

pwd = ''
while not pwd and guess < lim:
    pwd = input ("Password: ")
    guess += 1
if guess == lim:
    sys.exit()
else:
    guess = 0

if login == "root" and pwd == "rootpwd":
    lvl = 2
elif login == "user" and pwd == "123":
    lvl = 1

if lvl:
    print (f"Hello, {login}, your access level is {lvl}.")
else:
    print ("Access denied.")