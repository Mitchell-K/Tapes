cassette = [' __________________ ',
           '|    ___     ___   |',
           '|   /   \   /   \  |',
           '|   \___/   \___/  |',
           '|  ______________  |',
           '|_/_O__________O_\_|']

while True:
    print('How many cassettes do you want?')
    num_of_cassettes = int(input())
    dummy = False
    while (num_of_cassettes**0.5)%1 != 0:
        print("Please enter a number that is a perfect square.")
        if dummy:
            print("Example of perfect square numbers: [1, 4, 9, 16, 25, 36, 49]")
        dummy = True
        num_of_cassettes = int(input())
    squared = int(num_of_cassettes**0.5)
    
    for i in range(0, squared):
        for line_chunk in cassette:
            for j in range(0, squared):
                print(" " + line_chunk + " ", end="")
            print('\r')

    print("Want more cassettes?\n 1. Yes\n 2. No")
    if int(input()) == 2:
        break