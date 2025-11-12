#Clear the Screen
import os
os.system("cls")


# funtion to count words in sentence
def count_words(sentence):
    #split sentence into a list
    words = sentence.split()
    # John Elder is cool
    # words = ['john', 'edler', 'is', 'cool]

    #get length of list with len
    return len(words)

#function to count characters including spaces
def count_char_with_spaces(sentence):
    #use len fo characters
    return len(sentence)

#funtion to count characters excluding spaces
def count_char_without_spaces(sentence):
    #remove spaces from sentence
    return len(sentence.replace(" ", "")) #.replace('thing to replace', 'thing to replace it with')
    
def word_count_program():
    #prompt the user
    sentence = input('Enter a sentence: ')

    #get word adn character counts
    if sentence:
        word_count = count_words(sentence)
        char_count_with_spaces = count_char_with_spaces(sentence)
        char_count_without_spaces = count_char_without_spaces(sentence)

    else:
        print('That is not a sentence!')

    #print the results
    print(f'Word count: {word_count}')
    print(f'Character count (with spaces): {char_count_with_spaces} ')
    print(f'Character count (without spaces): {char_count_without_spaces}')
    
                           
word_count_program()




