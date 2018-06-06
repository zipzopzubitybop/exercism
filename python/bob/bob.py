def hey(phrase):
    phrase = phrase.strip()
    
    if not phrase:
        return("Fine. Be that way!")
        
    yelling = phrase.isupper()
    question = phrase[-1]=='?'
    
    if question:
        if yelling:
            return("Calm down, I know what I'm doing!")
        else:
            return("Sure.")
    if yelling:
        return("Whoa, chill out!")
    return("Whatever.")
    pass
