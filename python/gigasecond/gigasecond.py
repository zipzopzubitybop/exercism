from datetime import timedelta as td
def add_gigasecond(birth_date):
    try:
        return birth_date+td(seconds=1e9)
    except:
        raise "Bad birth_date: %s" % birth_date 
    pass