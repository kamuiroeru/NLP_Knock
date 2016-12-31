from nltk import stem, re

with open('nlp51.out') as f:
    st = stem.PorterStemmer()
    for word in f:
        word = word.rstrip()
        if word:
            # word_for_stem = re.sub('[^a-z]', '', word.lower())
            print(word + '\t' + st.stem(word))
