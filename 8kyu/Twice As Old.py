#Twice As Old
def twice_as_old(dad_years_old, son_years_old):
    birth=dad_years_old-son_years_old
    twice_as_old=birth*2
    if dad_years_old >=twice_as_old:
        return dad_years_old - twice_as_old
    else:
        return twice_as_old-dad_years_old 