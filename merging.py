# Consider the following:
#
# A string,S, of length n where .
# An integer,k , where k is a factor of n.
# We can split s into (n/k) substrings where each substring,t , consists of a contiguous block of k characters in s .
# Then, use each t to create string u such that:
#
# The characters in u are a subsequence of the characters in t.
# Any repeat occurrence of a character is removed from the string such that each character in  occurs exactly once.
# In other words, if the character at some index j in t occurs at a previous index <j in t, then do not include the character in string u.
# Given s and k, print n/k lines where each line i denotes string u .


def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        print("".join(dict.fromkeys(string[i:i + k])))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
