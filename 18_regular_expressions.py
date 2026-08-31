'''
Project: 30 Days Of Python challenge
Author (Original): Asabeneh Yetayeh (https://github.com/Asabeneh/30-Days-Of-Python)
Day: 18 - Regular Expressions (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/18_Day_Regular_expressions/18_regular_expressions.md)
Challenger: KataTNT
'''

import re
import string
from collections import Counter
import pprint

## Exercises: Level 1
# 1. What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
words_counts = Counter(paragraph.split())
res = [(count, word) for word, count in words_counts.most_common()]
pprint.pprint(res)

## Exercises: Level 2
# 1. Write a pattern which identifies if a string is a valid python variable
valid_pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
var_names = '''total_count
_private_var_2
UserAge2026
3rd_time
'''

matches = re.findall(valid_pattern, var_names, re.MULTILINE)
print(matches)

## Exercises: Level 3
# 1. Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(text: str):
    special_chars = r'[!@#$%&.,;?]'
    return re.sub(special_chars, '', text)
    
def clean_text_punc(text: str):
    return text.translate(str.maketrans('', '', string.punctuation))

def most_frequent_words(text: str):
    words_counts = Counter(text.split())
    result = [(count, word) for word, count in words_counts.most_common()]
    return result[:3]

print(clean_text(sentence))
print(clean_text_punc(sentence))
cleaned_text = clean_text(sentence)
(most_frequent_words(cleaned_text))