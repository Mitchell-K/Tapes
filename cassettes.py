tapes = [
['Cassettes',
[' __________________ ',
 '|    ___     ___   |',
 '|   /   \   /   \  |',
 '|   \___/   \___/  |',
 '|  ______________  |',
 '|_/_O__________O_\_|']],
['VHS',
[' ______________________ ',
 '|                      |',
 '|     ____________     |',
 '|    /  |      |  \    |',
 '|   |   |      |   |   |',
 '|    \__|______|__/    |',
 '||____________________||',
 '|______________________|']],
['Floppy',
[' ______________ ',
 '||   |    _ |  |',
 '||   |   | ||  |',
 '||   |   |_||  |',
 '||___|______|  |',
 '| ___________  |',
 '||           | |',
 '||           | |',
 '||           | |',
 '||___________|_|']],
['SNES',
['    _____________    ',
 ' __||           ||__ ',
 '|__||           ||__|',
 '|__||___________||__|',
 '|__| ___________ |__|',
 '|__||           ||__|',
 '|__||___________||__|']]]

def print_menu():
    print(30 * '-' , 'MENU' , 30 * '-')
    print('1. Cassettes')
    print('2. VHS')
    print('3. Floppy Disk')
    print('4. SNES')
    print(67 * '-')

def get_tape_type():
    try:
        dummy = False
        tape_choice = int(input())
        while not 0 < tape_choice < 5:
            print('Please enter a valid choice')
            if dummy:
                if tape_choice == 0:
                    print_menu()
                else:
                    print('Available options are: [1, 2, 3, 4]')
                    print('To see the menu again, enter \'0\'')
            dummy = True
            tape_choice = int(input())
    except (ValueError, TypeError):
        print('Error with input')
    else:
         return tapes[tape_choice - 1]

def get_tape_count():
    try:
        dummy = False
        tape_count = int(input('How many tapes do you want?\n'))
        while (tape_count**0.5)%1 != 0:
            print("Please enter a number that is a perfect square.")
            if dummy:
                print('Examples of perfect square numbers: [1, 4, 9, 16, 25, 36]')
            dummy = True
            tape_count = int(input())
    except (ValueError, TypeError):
        print('Error with input')
    else:
        return tape_count

def print_tapes(tape_type, tape_count):
    side_length = int(tape_count**0.5)
    for i in range(0, side_length):
        for line_chunk in tape_type[1]:
            for j in range(0, side_length):
                print(" " + line_chunk + " ", end="")
            print('\r')
    

while True:
    print_menu()
    tape_type = get_tape_type()
    tape_count = get_tape_count()
    print_tapes(tape_type, tape_count)

    print("Want more tapes?\n 1. Yes\n 2. No")
    if int(input()) == 2:
        break