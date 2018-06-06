def word_count(phrase):
    import re
    from collections import Counter
    print(Counter(re.findall("([a-z0-9]+(?:'[a-z])?)", phrase.lower())))
    #return Counter(re.findall("([a-z0-9]+(?:'[a-z])?)", phrase.lower()))
 
word_count("test")