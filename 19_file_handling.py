"""
Project: 30 Days Of Python challenge
Author (Original): Asabeneh Yetayeh (https://github.com/Asabeneh/30-Days-Of-Python)
Day: 19 - File Handling (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/19_Day_File_handling/19_file_handling.md)
Challenger: KataTNT
"""

## Exercises: Level 1
# 1. Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
def text_count(file_name: str):
    print('Counting lines and words of file:', file_name)
    with open(file=file_name, mode='r', encoding='utf-8') as file:
        lines = file.readlines()
        line_count = len(lines)
        text = "".join(lines)
        word_count = len(text.split())
        print('Number of lines:', line_count)
        print('Number of words:', word_count)

# i. Read obama_speech.txt file and count number of lines and words
text_count('./data/obama_speech.txt')

# ii. Read michelle_obama_speech.txt file and count number of lines and words
text_count('./data/michelle_obama_speech.txt')

# iii. Read donald_speech.txt file and count number of lines and words
text_count('./data/donald_speech.txt')

# iv. Read melina_trump_speech.txt file and count number of lines and words
text_count('./data/melina_trump_speech.txt')
