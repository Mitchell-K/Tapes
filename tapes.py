tape_text = {
    'Cassettes' : 
        [' __________________ ',
         '|    ___     ___   |',
         '|   /   \   /   \  |',
         '|   \___/   \___/  |',
         '|  ______________  |',
         '|_/_O__________O_\_|'],
    'VHS' :
        [' ______________________ ',
         '|                      |',
         '|     ____________     |',
         '|    /  |      |  \    |',
         '|   |   |      |   |   |',
         '|    \__|______|__/    |',
         '||____________________||',
         '|______________________|'],
    'Floppy' :
        [' ______________ ',
         '||   |    _ |  |',
         '||   |   | ||  |',
         '||   |   |_||  |',
         '||___|______|  |',
         '| ___________  |',
         '||           | |',
         '||           | |',
         '||           | |',
         '||___________|_|'],
    'SNES' :
       ['    _____________    ',
        ' __||           ||__ ',
        '|__||           ||__|',
        '|__||___________||__|',
        '|__| ___________ |__|',
        '|__||           ||__|',
        '|__||___________||__|']
}

class Tapes:
    
    def __init__(self, type, shape, size, direction='Square'):
        self.type = type
        self.shape = shape
        self.size = size
        self.direction = direction

    def __repr__(self):
        tape_info = 'Tape object with following properties:\n\tType: {type}\n\tShape: {shape}'.format(type=self.type, shape=self.shape)
        if self.shape == 'Triangle':
            tape_info+= '\n\tDirection: {direction}'.format(direction=self.direction)
        return tape_info

    def print(self):
        """Prints out the tapes with given args

        Args:
            tape_type (int): Index pointing to tape type in tapes list
            tape_length (int): Length of the side of square or right triangle
            tape_shape (str): Name of the shape to be printed out
            direction (str): Direction to print the triange, otherwise 'square'
        """
        # Print square shape
        if self.shape == 'Square' or self.direction == 'Square':
            for row_count in range(0, self.size):
                for line_chunk in tape_text[self.type]:
                    print((" " + line_chunk + " ")*self.size)
        else: 
            if self.direction == 'Top Left':
                # Print triangle in top left
                for row_count in range(0, self.size):
                    for line_chunk in tape_text[self.type]:
                        print((" " + line_chunk + " ") * (self.size - row_count))
            elif self.direction == 'Top Right':
                # Print triangle in top right
                for row_count in range(0, self.size):
                    for line_chunk in tape_text[self.type]:
                        print(' '*(len(line_chunk)+2)*row_count, end='') # Pretape buffer
                        print((' ' + line_chunk + ' ') * (self.size - row_count))
            elif self.direction == 'Bottom Left':
                # Print triangle in bottom left
                for row_count in range(0, self.size):
                    for line_chunk in tape_text[self.type]:
                        print((' ' + line_chunk + ' ') * (row_count + 1))
            elif self.direction == 'Bottom Right':
                # Print triangle in bottom right
                for row_count in range(0, self.size):
                    for line_chunk in tape_text[self.type]:
                        print(' '*(len(line_chunk)+2)*(self.size-row_count-1), end='') # Pretape buffer
                        print((" " + line_chunk + " ") * (row_count + 1))
            else:
                print('Problem with triangle direction.')

def get_info():
    """Helper function used to get tape info from user

    Returns: tape_type, tape_shape, tape_count, direction
        tape_type (str): Name of the type tape in tape list
        tape_shape (str): The name of the shape User picked
        tape_count (int): Number of sides for shape (1-7)
        direction (str): Direction of triangle; square if square
    """

    # Request tape type from user
    choices = ['Cassettes', 'VHS', 'Floppy', 'SNES']
    # Convert menu choice to tape name
    tape_type = choices[print_menu('Tape Type', choices, 'Choose a type of tape to be printed.') - 1]

    # Request tape shape from user
    choices = ['Square', 'Triangle']
    # Convert menu choice to shape name
    tape_shape = choices[print_menu('Shape', choices, 'Choose a shape for the ' + tape_type)-1]

    # Request direction from user if triangle
    # User chose Triangle
    if tape_shape == 'Triangle':
        choices = ['Top Left', 'Top Right', 'Bottom Left', 'Bottom Right']
        # Convert menu choice to shape
        direction = choices[print_menu('Triangle Position', choices, 'Choose a direction the Triangle faces.')-1]
    else:
        direction = 'Square'

    # Request number of sides for shape
    choices = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven']
    tape_count = print_menu('Side length', choices, 'Choose the side length of the ' + tape_shape)
    
    return tape_type, tape_shape, tape_count, direction

def print_menu(title, choices, prompt='Choose an option'):
    """ Prints a menu with given options
        
    Args:
        title (str): Title to menu
        choices (list): Strings of all the available choices
        prompt (str): Prompt to help user with menu

    return:
        Returns the int associated to menu choice
    """
    buffer = int((70 - len(title))/2) # Buffer for styling menu
    print(buffer * '-' , title , buffer * '-') # Title of menu
    for num, choice in enumerate(choices, start=1):
        print('{}: {}'.format(num, choice))
    print(71 * '-')
    print(prompt) # Prompt to help user choose option
    try: # Attempt to get input from user
        dummy = False
        menu_choice = int(input())
        option_count = len(choices)
        while not 0 < menu_choice <= option_count: # Make sure user inputs value associated with a choice
            print('Problem with input\nPlease choose input a number associated with a choice.')
            if dummy: # User needs help with input
                if menu_choice == 0:
                    print_menu(title, choices, prompt)
                else:
                    print('Available choices are in range (0, ' + option_count + ')')
                    print('To see the menu again, enter \'0\'')
            dummy = True
            menu_choice = int(input())
    except (ValueError, TypeError): # Error thrown
        print('Error with input')
    else:
         return menu_choice

def main():
    while True:
        tape_type, tape_shape, tape_size, direction = get_info()
        tape = Tapes(tape_type, tape_shape, tape_size, direction)
        tape.print()

        user_choice = int(input('Want more tapes?\n 1. Yes\n 2. No\n'))
        if user_choice == -1:
            print('Debug/Info option')
            print(tape)
        elif user_choice == 2:
            print("Closing application")
            break

main()