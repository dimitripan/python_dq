# import regex
import re

# create variable with input text
text = """homEwork:
 tHis iz your homeWork, copy these Text to variable.



 You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



 it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



 last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# split text on sentences using '.' as delimiter
sentences = text.split('.')
# create variable to store last word from every sentence
last_words = []
# initiate loop to loop through list of sentences
for s in sentences:
    # if the split sentence is not empty
    if s.split() != []:
        # append last element to list oh last words
        last_words.append(s.split()[-1].lower())

# to capitalize first word
# loop through list of sentences
for i in range(len(sentences)):
    # remove any whitespaces before and after the sentence
    sentences[i] = sentences[i].strip(' ')
    # capitalize first word
    sentences[i] = sentences[i].capitalize()


# loop through list of sentences
for i in range(len(sentences)):
    # split sentences by next line
    sentences[i] = sentences[i].split('\n')
    # loop through result of splitting sentence by next line
    for i2 in range(len(sentences[i])):
        # remove any whitespaces before and after the sentence
        sentences[i][i2] = sentences[i][i2].strip(' ')
        # capitalize first word
        sentences[i][i2] = sentences[i][i2].capitalize()

# loop through result of splitting sentence by next line
for i in range(len(sentences)):
    # join sentences back together using next line and space
    sentences[i] = '\n '.join(sentences[i])

# join sentences back together using '. '
one_sentence = '. '.join(sentences)

# fix iz to is but only where it is a mistake
one_sentence = re.sub(r'iz(?!e)', 'is', one_sentence)

# loop through all simbols
num_space = 0
for s in text:
    # if symbol is a whitespace
    if s.isspace():
        # count + 1
        num_space += 1

# add new paragraph with last words from each sentence
one_sentence = one_sentence + '\n ' + ' '.join(last_words)

print(one_sentence)
