# Kevin and Stuart want to play the 'The Minion Game'.
#
# Game Rules
#
# Both players are given the same string,S .
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
#
# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.


def minion_game(string):
    vowels = ['A', 'I', 'E', 'O', 'U']
    KEVIN = 0
    STUART = 0


    for i in range(len(string)):
        if string[i] in vowels:
            KEVIN += (len(string) - i)
        else:
            STUART += (len(string) - i)

    if KEVIN > STUART:
        print("Kevin " + str(KEVIN))
    elif KEVIN < STUART:
        print("Stuart " + str(STUART))

if __name__ == '__main__':
    s = input()
    print(s.swapcase())
    minion_game(s)