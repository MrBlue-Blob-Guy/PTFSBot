import random as rand

commands_list = ['-ifr', '-vfr', '-push_and_start', 'cmdlist']
issued_squawks = []
#there are litterally more than 100 of these
reserved_Squawks = [7500, 7600, 7700]

#command functions


#basic help function
def help():
    for command in commands_list:
        print(command)


#Generate Squawk code
def gen_squawk():
    sqwakCode = rand.randint(1000, 7777)
    return sqwakCode


#ifr function
def issue_ifr(callsign, dep, arv , deprwy ,flinit , flfinal , plane_data):
    Squawk = gen_squawk()
    for reg in reserved_Squawks:
        if Squawk == reg:
            return
    for sqks in issued_squawks:
        if Squawk == sqks:
            return
    print(f'{callsign} cleared ifr to {arv} via gps direct departure will be with me expect {deprwy} initial flight level{flinit} expect {flfinal} {flfinal/plane_data.plane.v1}minutes after departure squawking {Squawk}')

#Command Handling
def handle_commands(command):
    if command == '-cmdlist':
        help()
    else:
        print('invalid Commands or no permission to use the command')


while True:
    user_Command = input("Command" + " ")
    handle_commands(user_Command)
