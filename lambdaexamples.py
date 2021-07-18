from functools import reduce

def pig_latin(word):
    if word[0] in "aieou":
        return word+"way"
    else:
        return word[1:]+word[0]+"ay"

sentence = input("Enter a sentence: ").split()
largest_word = reduce(lambda x,y: x if len(x)>len(y) else y, sentence)
print(f"The largest word of the sentence is {largest_word}")
shortest_word = reduce(lambda x,y: x if len(x)<len(y) else y, sentence)
print(f"The shortest word of the sentence is {shortest_word}")
character_total = reduce(lambda x,y: x+y, list(map(lambda x:len(x), sentence)))
print(f"Total number of characters is {character_total}")
upper_case_vowels = reduce(lambda x,y: x+" "+y, list(map(lambda word: reduce(lambda x,y: x+y, (list(map(lambda letter: letter.upper() if letter in "aeiou" else letter.lower(), word)))), sentence)))
print("Sentence with only vowels capitalized:")
print(upper_case_vowels)
message = reduce(lambda x,y: x+" "+y, list(map(lambda word: pig_latin(word), sentence)))
print("Sentence in pig latin:")
print(message)
small_words = list(filter(lambda x:len(x)<=3, sentence))
print("Words in the sentence with length three or less:")
print(small_words)
reverse_a = list(map(lambda x: x[::-1], filter(lambda word:"a" in word, sentence)))
print("Words with the letter a but reversed:")
print(reverse_a)
number_of_vowels=reduce(lambda x,y: x+y, list(map(lambda word: len(list(filter(lambda letter: letter in "aeiou", word))), sentence)))
print(f"number of vowels: {number_of_vowels}")