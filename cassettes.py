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
        tape_count = int(input('How many tapes wide should the shape be?\n'))
        if 0 < tape_count < 8:
            return tape_count
    except (ValueError, TypeError):
        print('Error with input')
    except:
        print('Please enter a valid number')
        print('Available input is in range (1-7)')
        get_tape_count()

def get_tape_shape():
    try:
        dummy = False
        tape_shape = int(input('What shape would you like the tapes printed in?\n1. Square\n2. Triangle\n'))
        while (tape_shape != 1 and tape_shape != 2):
            print('Please enter a valid choice')
            if dummy:
                print('Available options are: 1 or 2')
            dummy = True
            tape_count = int(input())
    except (ValueError, TypeError):
        print('Error with input')
    else:
        return tape_shape

def get_shape_direction():
    return 1

def print_tapes(tape_type, tape_length, tape_shape):
    """Prints out the tapes with given args

    Args:
        tape_type (str): Type of tape to be printed out
        tape_length (int): Length of the side of square or right triangle
        tape_shape (int): 1 = Square, 2 = Triangle
    """
    # Print square shape
    if tape_shape == 1:
        for i in range(0, tape_length):
            for line_chunk in tape_type[1]:
                for j in range(0, tape_length):
                    print(" " + line_chunk + " ", end="")
                print('\r')
    else: # Print triangle in top left
        col_count = tape_length
        for row_count in range(0, tape_length):
            for line_chunk in tape_type[1]:
                print((" " + line_chunk + " ") * col_count)
            col_count-=1
    

while True:
    print_menu()
    tape_type = get_tape_type()
    tape_count = get_tape_count()
    tape_shape = get_tape_shape()
    print_tapes(tape_type, tape_count, tape_shape)

    print('Want more tapes?\n 1. Yes\n 2. No')
    if int(input()) == 2:
        break