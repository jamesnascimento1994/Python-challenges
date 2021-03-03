# Challenge One: This code does not execute properly. Try to figure out why.
# Challenge Source: https://www.codewars.com/kata/50654ddff44f800200000004/python

# Starter Code
# def multiply(a, b):
#     a * b

# Solution
# def multiply(a, b):
#     return a * b

# # TESTS
# print(multiply(7, 8));
# print(multiply(4, 3));
# print(multiply(10, 5));

# Challenge Two: We want an array, but not just any old array, an array with contents! Write a function that produces an array with the numbers 0 to N-1 in it.
# Challenge Source: https://www.codewars.com/kata/571d42206414b103dc0006a1/python

# def arr(n=None): 
#     new_array = []
#     if n == None:
#         return []
#     for x in range(n):
#         new_array.append(x)
#     return new_array

# # TESTS
# print(arr(5));
# print(arr(7));
# print(arr(8));

# Challenge Three: Polycarpus works as a DJ in the best Berland nightclub, and he often uses dubstep music in his performance. Recently, he has decided to take a couple of old songs and make dubstep remixes from them. Let's assume that a song consists of some number of words (that don't contain WUB). To make the dubstep remix of this song, Polycarpus inserts a certain number of words "WUB" before the first word of the song (the number may be zero), after the last word (the number may be zero), and between words (at least one between any pair of neighbouring words), and then the boy glues together all the words, including "WUB", in one string and plays the song at the club. For example, a song with words "I AM X" can transform into a dubstep remix as "WUBWUBIWUBAMWUBWUBX" and cannot transform into "WUBWUBIAMWUBX".Recently, Jonny has heard Polycarpus's new dubstep track, but since he isn't into modern music, he decided to find out what was the initial song that Polycarpus remixed. Help Jonny restore the original song.
# Challenge Source: https://www.codewars.com/kata/551dc350bf4e526099000ae5/python

# import re;

# def song_decoder(song):
#     fstr = re.sub('WUB', ' ', song)
#     return ' '.join((fstr.strip()).split());

# print(song_decoder('WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB'))
# print(song_decoder("WUBFORGIVEWUBMEWUBFATHERWUB"))
# print(song_decoder("WUBJESSEWUBBADWUBBOYWUBJUSTWUBCOMEWUBLOOKWUBATWUBWHATWUBYOURWUBBROTHERWUBDIDWUB"))

# Challenge Four: Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.
# Challenge Source: https://www.codewars.com/kata/52fba66badcd10859f00097e/python

# def disemvowel(string):
#     output = []
#     for char in string:
#         if char not in "aeiouAEIOU":
#             output.extend(char)
#     return "".join(output)

# # TESTS
# print(disemvowel("This website is for losers! LOL"))
# print(disemvowel("Do you like biscuits?"))

# Challenge Five: When it's spring Japanese cherries blossom, it's called "sakura" and it's admired a lot. The petals start to fall in late April. Suppose that the falling speed of a petal is 5 centimeters per second (5 cm/s), and it takes 80 seconds for the petal to reach the ground from a certain branch. Write a function that receives the speed (in cm/s) of a petal as input, and returns the time it takes for that petal to reach the ground from the same branch.
# Challenge Source: https://www.codewars.com/kata/5a0be7ea8ba914fc9c00006b/python

# def sakura_fall(v):
#     distance_fell = 400
#     if v > 0:
#         how_many_seconds = distance_fell / v
#         return how_many_seconds
#     else:
#         return 0

# # TESTS
# print(sakura_fall(5))
# print(sakura_fall(8))
# print(sakura_fall(-7))