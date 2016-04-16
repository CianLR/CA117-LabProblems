import sys, string

def pluralise(singular):
    es = ['ch','sh','x','s','z','o']
    ves = ['fe','f']
    constonants = [c+'y' for c in string.ascii_lowercase if c not in ['a','e','i','o','u']]

    for ending in es:
        if singular[-len(ending):] == ending:
            return singular+'es'
            
    for ending in ves:
        if singular[-len(ending):] == ending:
            return singular[:-1]+'ves'
        
    for ending in constonants:
        if singular[-len(ending):] == ending:
            return singular[:-1]+'ies'
    
    return singular+'s'

if __name__ == '__main__':
    print(pluralise(sys.argv[1]))
