def hey(phrase):
    if (re.search('.*[A-Z][A-Z][A-Z].*[?]$'," ".join(phrase.split()))):
        return("Calm down, I know what I'm doing!")
    elif (re.search('.[?]$'," ".join(phrase.split()))):
        return("Sure.")
    elif (re.search('.*[A-Z].*[A-Z].*',phrase)) and not (re.search('[a-z]',phrase)):
        return("Whoa, chill out!")
    elif (re.search('.[A-Za-z0-9]+'," ".join(phrase.split()))):
        return("Whatever.")
    else:
        return("Fine. Be that way!")
    pass
