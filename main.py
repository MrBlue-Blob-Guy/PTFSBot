import random as rand

commands_list = ['-ifr', '-vfr', '-push_and_start', 'cmdlist']
issued_squawks = []
reserved_Squawks = [7500, 7600, 7700]

#command functions


#basic help function
def help():
    for command in commands_list:
        print(command)


#Generate Squawck code
def gen_squawk():
    sqwakCode = rand.randint(1000, 7777)
    return sqwakCode


#ifr function
def issue_ifr(callsign, dep, arv):
    Squawk = gen_squawk()
    for reg in reserved_Squawks:
        if Squawk == reg:
            return
    for sqks in issued_squawks:
        if Squawk == sqks:
            return


#Command Handling
def handle_commands(command):
    if command == '-cmdlist':
        help()
    else:
        print('invalid Commands or no permission to use the command')


while True:
    user_Command = input("Command" + " ")
    handle_commands(user_Command)
