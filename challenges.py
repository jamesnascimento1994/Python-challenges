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

# # TESTS
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

# Challenge Six: Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World! if name is not given (or passed as an empty String). Assuming that name is a String and it checks for user typos to return a name with a first capital letter(Xxxx).
# Challenge Source: https://www.codewars.com/kata/57e3f79c9cb119374600046b/python

# def hello(name=""):
#     if name:
#         return 'Hello, ' + name[0:1].upper() + name[1:].lower() + '!'
#     else:
#         return "Hello, World!"
    
# # TESTS
# print(hello("jameS"))
# print(hello())
# print(hello(""))

# Challenge Seven: Enough is enough!
# Alice and Bob were on a holiday. Both of them took many pictures of the places they've been, and now they want to show Charlie their entire collection. However, Charlie doesn't like these sessions, since the motive usually repeats. He isn't fond of seeing the Eiffel tower 40 times. He tells them that he will only sit during the session if they show the same motive at most N times. Luckily, Alice and Bob are able to encode the motive as a number. Can you help them to remove numbers such that their list contains each number only up to N times, without changing the order?

# Task
# Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering. For example if N = 2, and the input is [1, 2, 3, 1, 2, 1, 2, 3], you take[1, 2, 3, 1, 2], drop the next[1, 2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to[1, 2, 3, 1, 2, 3].
# Challenge Source: https://www.codewars.com/kata/554ca54ffa7d91b236000023/python

# def delete_nth(order, max_e):
#     result = []
#     occurrences = {}
#     for n in order:
#         count = occurrences.setdefault(n, 0)
#         if count >= max_e:
#            continue
#         result.append(n)
#         occurrences[n] += 1
#     return result

# # TESTS
# print(delete_nth([1, 1, 1, 1], 2))
# print(delete_nth([20, 37, 20, 21], 1))

# Challenge Eight: You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.
# Challenge Source: https://www.codewars.com/kata/54da539698b8a2ad76000228/python

# def is_valid_walk(walk):
#     ns = 0
#     we = 0
#     for dir in walk:
#         if dir == 'n':
#             ns += 1
#         if dir == 's':
#             ns -= 1
#         if dir == 'w':
#             we += 1
#         if dir == 'e':
#             we -= 1
#     if ns == 0 and we == 0 and len(walk) == 10:
#         return True
#     else:
#         return False

# # TESTS
# print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))
# print(is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']))
# print(is_valid_walk('w'))
# print(is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))

# Challenge Nine: Return the number (count) of vowels in the given string. We will consider a, e, i, o, u as vowels for this Kata(but not y). The input string will only consist of lower case letters and / or spaces.
# Challenge Source: https://www.codewars.com/kata/54ff3102c1bad923760001f3/python

# def get_count(input_str):
#     num_vowels = 0
#     for char in input_str:
#         if char in "aeiouAEIOU":
#             num_vowels += 1
#     return num_vowels

# # TESTS
# print(get_count("vowel"));
# print(get_count('cover'));
# print(get_count('cranium'));

# Challenge Ten: Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it. Your task is to write a function maskify, which changes all but the last four characters into '#'.
# Challenge Source: https://www.codewars.com/kata/5412509bd436bd33920011bc

# return masked string
# def maskify(cc):
#     if len(cc) > 4:
#         reversedCC = cc[::-1]
#         newString = ''
#         for i in range(0, len(reversedCC)):
#             if i < 4:
#                 newString += reversedCC[i]
#             else:
#                 newString += '#'
#         return newString[::-1]
#     else:
#         return cc;

# # TESTS
# print(maskify("4556364607935616"))
# print(maskify("64607935616"))
# print(maskify("1"))
# print(maskify(""))
# print(maskify("Skippy"))
# print(maskify("Nananananananananananananananana Batman!"))

# Challenge Eleven: Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
# Challenge Source: https://www.codewars.com/kata/5467e4d82edf8bbf40000155

# def descending_order(num):
#     # Bust a move right here
#     return int("".join(map(str, sorted([i for i in str(num)], reverse=True))));

# # TESTS
# print(descending_order(0));
# print(descending_order(15));
# print(descending_order(123456789));

# Challenge Twelve: In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
# Challenge Source: https://www.codewars.com/kata/53dbd5315a3c69eed20002dd

# def filter_list(l):
#     new_list = []
#     for x in l:
#         if type(x) == int:
#             new_list.append(x)
    
#     return new_list

# # TESTS
# print(filter_list([1,2,'a','b']))
# print(filter_list([1,'a','b',0,15]))
# print(filter_list([1,2,'aasf','1','123',123]))

# Challenge Thirteen: In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superseded by voice and digital data communication channels, it still has its use in some applications around the world. The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·. NOTE: Extra spaces before or after the code have no meaning and should be ignored. In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal SOS (that was first issued by Titanic), that is coded as ···−−−···. These special codes are treated as single special characters, and usually are transmitted as separate words. Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.
# Challenge Source: https://www.codewars.com/kata/54b724efac3d5402db00065e
# NOTE: MORSE_CODE on line 224 is exclusive to codewars. I'm not sure how to fix the error on VS code without having to create a giant array of every letter with its morse code.

# def decode_morse(morse_code):
#     # ToDo: Accept dots, dashes and spaces, return human-readable message
#     word = morse_code.strip().split('   ')
#     result_char = []
    
#     for i in word:
#         character = i.split(' ')
        
#         for j in character:
#             result_char.append(MORSE_CODE[j])
            
#         result_char.append(' ')
        
    
#     result_word = ''.join(result_char).strip()
#     return result_word

#     # TESTS
# print(decode_morse('.... . -.--   .--- ..- -.. .'))

# Challenge Thirteen: Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
# Challenge Source: https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

# def duplicate_count(text):
#     # Your code goes here
#     lowercase_text = text.lower()
#     count = 0
#     dictionary = {}
    
#     for i in range(0, len(lowercase_text)):
#         dictionary[lowercase_text[i]] = 0
    
#     for key in dictionary:
#         for i in range(0, len(lowercase_text)):
#             if key == lowercase_text[i]:
#                 dictionary[key] += 1
    
#     for key in dictionary:
#         if dictionary[key] > 1:
#             count += 1
    
#     return count

# # TESTS
# print(duplicate_count("abcde"))
# print(duplicate_count("aabbcde"))
# print(duplicate_count("aabBcde"))
# print(duplicate_count("indivisibility"))
# print(duplicate_count("Indivisibilities"))
# print(duplicate_count("aA11"))
# print(duplicate_count("ABBA"))

# Challenge Fourteen: Define a function that takes one integer argument and returns logical value true or false depending on if the integer is a prime. Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

# Challenge Source: https://www.codewars.com/kata/5262119038c0985a5b00029f

# def is_prime(num):
#     if num <= 0 or num == 1:
#         return False
#     i = 2
#     while i <= num ** 0.5:
#         if num % i == 0:
#             return False
#         i += 1
#     return True

# # TESTS
# print(is_prime(1))
# print(is_prime(2))
# print(is_prime(-1))

# Challenge Fifteen: Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below. Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

# Challenge Source: https://www.codewars.com/kata/5390bac347d09b7da40006f6

# def to_jaden_case(string):
#     return ' '.join([word.capitalize() for word in string.split()])

# # TESTS
# print(to_jaden_case("How can mirrors be real if our eyes aren't real"))

# Challenge Sixteen: Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Challenge Source: https://www.codewars.com/kata/520b9d2ad5c005041100000f

# def pig_it(text):
#     #your code here
#     words = text.split(' ')
#     pig_sentence = ' '
    
#     for word in words:
#         if word in '!.%&?':
#             pig_sentence += word
#         else:
#             pig_word = word[1:] + word[0] + 'ay'
#             pig_sentence += pig_word + ' '
#     return pig_sentence.strip()

# # TESTS
# print(pig_it('Pig latin is cool'))
# print(pig_it('Hello world !'))

# Challenge Seventeen: For this exercise you will be strengthening your page-fu mastery. You will complete the PaginationHelper class, which is a utility class helpful for querying paging information related to an array. The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page. The types of values contained within the collection/array are not relevant.

# Challenge Source: https://www.codewars.com/kata/515bb423de843ea99400000a

# import math
# class PaginationHelper:

#   # The constructor takes in an array of items and a integer indicating
#   # how many items fit within a single page
#     def __init__(self, collection, items_per_page):
#         self.collection = collection
#         self.items_per_page = items_per_page
      
  
#   # returns the number of items within the entire collection
#     def item_count(self):
#         return len(self.collection)
     
#   # returns the number of pages
#     def page_count(self):
#         return int(math.ceil(1.0 * self.item_count() / self.items_per_page))
      
    
#   # returns the number of items on the current page. page_index is zero based
#   # this method should return -1 for page_index values that are out of range
#     def page_item_count(self,page_index):
#         items_per_page = self.items_per_page
#         if page_index >= self.page_count():
#             return -1
#         elif page_index == self.page_count() - 1:
#             return self.item_count() - self.items_per_page*page_index
#         else:
#             return self.items_per_page
      
  
#   # determines what page an item is on. Zero based indexes.
#   # this method should return -1 for item_index values that are out of range
#     def page_index(self,item_index):
#         if item_index in range(self.item_count()):
#             return item_index//self.items_per_page
        
#         return -1

# # TESTS
# collection = range(1, 25)
# collection = ['a','b','c','d','e','f']
# helper = PaginationHelper(collection, 4)
# print(helper.page_count())
# print(helper.item_count())
# print(helper.page_item_count(0))
# print(helper.page_item_count(1))
# print(helper.page_item_count(2))
# print(helper.page_index(5))
# print(helper.page_index(2))
# print(helper.page_index(20))
# print(helper.page_index(-1))

# Challenge Eighteen: Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes? Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

# Challenge Source: https://www.codewars.com/kata/525c65e51bf619685c000059

def cakes(recipe, available):
    count = 0
    l = [0]*len(recipe)
    for required in recipe:
        for avail_ing in available:
            if required == avail_ing:
                l[count]=available[required]//recipe[avail_ing]
                count+=1
    return min(l)

# TESTS
print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))
print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000}))