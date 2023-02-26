#Century From Year
def century(year):
    if year%100 != 0:
        return (int(year/100)+1)
    else:
        return year/100