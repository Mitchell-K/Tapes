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


def print_menu2(title, choices, prompt='Choose an option'):
    """ Prints a menu
        
    Args:
        title (str): Title to menu
        choices (list): Strings of all the available choices
        prompt (str): Prompt for to help user with menu
    """
    buffer = int((70 - len(title))/2) # Buffer for styling menu
    print(buffer * '-' , title , buffer * '-')
    option_count = 1
    for option in choices:
        print(str(option_count) + ". " + option)
        option_count+=1
    print(71 * '-')
    print(prompt)
    try: # Attempt to get input from user
        dummy = False
        menu_choice = int(input())
        while not 0 < menu_choice < option_count: # Make sure user inputs value associated with a choice
            print('Please choose a value associated with a choice.')
            if dummy: # User needs help with input
                if menu_choice == 0:
                    print_menu2(title, choices, prompt)
                else:
                    print('Available choices are in range (0, ' + str(option_count) + ')')
                    print('To see the menu again, enter \'0\'')
            dummy = True
            menu_choice = int(input())
    except (ValueError, TypeError): # Error thrown
        print('Error with input')
    else:
         return menu_choice # Return the int associated to menu choice

    
def get_info():
    choices = ['Cassettes', 'VHS', 'Floppy', 'SNES']
    # Convert menu choice index to tapes index
    tape_type = print_menu2('Tape Type', choices, 'Choose a type of tape to be printed.') - 1

    choices = ['Square', 'Triangle']
    tape_shape = choices[print_menu2('Shape', choices, 'Choose a shape for the ' + tapes[tape_type][0])-1]

    # User chose Triangle
    if tape_shape == 'Triangle':
        choices = ['Top Left', 'Top Right', 'Bottom Left', 'Bottom Right']
        direction = print_menu2('Triangle Position', choices, 'Choose a direction the Triangle faces.')
    else: 
        direction = 0 # Default the direction
    
    choices = ['1', '2', '3', '4', '5', '6', '7']
    tape_count = print_menu2('Side length', choices, 'Choose the side length of the ' + tape_shape)
    
    return tape_type, tape_shape, tape_count, direction
    

def print_tapes(tape_type, tape_shape, tape_length, direction):
    """Prints out the tapes with given args

    Args:
        tape_type (str): Type of tape to be printed out
        tape_length (int): Length of the side of square or right triangle
        tape_shape (int): 1 = Square, 2 = Triangle
    """
    # Print square shape
    if tape_shape == 'Square' or direction == 0:
        for i in range(0, tape_length):
            for line_chunk in tapes[tape_type][1]:
                for j in range(0, tape_length):
                    print(" " + line_chunk + " ", end="")
                print('\r')
    else: 
        if direction == 1:
            # Print triangle in top left
            col_count = tape_length
            for row_count in range(0, tape_length):
                for line_chunk in tapes[tape_type][1]:
                    print((" " + line_chunk + " ") * col_count)
                col_count-=1
        elif direction == 2:
            # Print triangle in top right
            for row_count in range(0, tape_length):
                for line_chunk in tapes[tape_type][1]:
                    print(' '*(len(line_chunk)+2)*row_count, end='')
                    print((' ' + line_chunk + ' ') * (tape_length - row_count))
        elif direction == 3:
            # Print triangle in bottom left
            for row_count in range(0, tape_length):
                for line_chunk in tapes[tape_type][1]:
                    print((' ' + line_chunk + ' ') * (row_count + 1))
        elif direction == 4:
            # Print triangle in bottom right
            for row_count in range(0, tape_length):
                for line_chunk in tapes[tape_type][1]:
                    print(' '*(len(line_chunk)+2)*(tape_length-row_count-1), end='')
                    print((" " + line_chunk + " ") * (row_count + 1))
        else:
            print('Problem with triangle direction.')
        
    

while True:
    tape_type, tape_shape, tape_count, direction = get_info()
    print_tapes(tape_type, tape_shape, tape_count, direction)

    print('Want more tapes?\n 1. Yes\n 2. No')
    if int(input()) == 2:
        break