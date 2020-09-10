# Keep these 2 lines
text_to_translate = input("Text to translate: ")
VOWELS = "aeiouyAEIOUY"
translation = ''

VOW_APPEND = 'yay'
CON_APPEND = 'ay'

words = text_to_translate.split()
for n in range(0,len(words)):
    newword = ''
    storage = ''
    nth_word = words[n] 
    first_letter = nth_word[0]

    if first_letter in VOWELS:
        translation += nth_word + VOW_APPEND + ' '
    else:


        for i in range(0,len(nth_word) ):
            if nth_word[i] in VOWELS:
                break
            else:
                storage += nth_word[i]
        
        translation += newword + storage + CON_APPEND + ' '





# Keep this line
print("Translation:", translation)
