def word_count(phrase):
    import re
    phrase = [s.translate(str.maketrans("", "", ",.!&@:%^$")) for s in re.split(',|, | |\t|_|\n|  '," ".join(phrase.split()))]
    phrase = [re.sub("^'|'$", '', x ).lower() for x in phrase if x != '']
    return (dict((x,phrase.count(x)) for x in set(phrase)))