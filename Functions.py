def cap(match):
    """
    Return capitalized matched word
    :param match: re.Match object
    :return: return capitalized matched word
    """
    return match.group().capitalize()


def capitalise_text(i_text):
    """
    Capitalise first word in a sentence
    :param i_text: string with text
    :return: inputted text where first word in each sentence is capitalised
    """
    # import regex
    import re
    # create pattern to find first word in sentence or first word in text
    p = re.compile(r'(?<=[\.\?!]\s|\s{2})(\w+)|(^\s?\w+)')
    # lower all characters in a string
    r_text = i_text.lower()
    # capitalize all matched words
    r_text = p.sub(cap, r_text)
    return r_text


def attach_last_words(i_text):
    """
    Attaches last words from sentences as new line at the end
    :param i_text: string with text
    :return: string with text with added line with last words
    """
    # split text on sentences using '.' as delimiter
    sentences = i_text.split('.')
    # create variable to store last word from every sentence
    last_words = []
    # initiate loop to loop through list of sentences
    for s in sentences:
        # if the split sentence is not empty
        if s.split():
            # append last element to list oh last words
            last_words.append(s.split()[-1].lower())
    # join sentences back together and last words in new line
    return '.'.join(sentences) + '\n ' + ' '.join(last_words)


def count_whitespaces(i_text: str):
    """
    function returns number of whitespaces in a string
    :param i_text: str
    :return: number of whitespaces
    """
    # loop through all simbols
    num_space = 0
    for s in i_text:
        # if symbol is a whitespace
        if s.isspace():
            # count + 1
            num_space += 1
    return num_space


def fix_iz(i_text: str):
    """
    Fixes iz to is in a string where iz is not followed with `e`
    :param i_text: string from homework task
    :return: string
    """
    import re
    return re.sub(r'iz(?!e)', 'is', i_text, flags=re.IGNORECASE)


text1 = """homEwork:
 tHis iz your homeWork, copy these Text to variable.



 You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



 it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



 last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

print(attach_last_words(capitalise_text(fix_iz(text1))))
print(count_whitespaces(text1))
