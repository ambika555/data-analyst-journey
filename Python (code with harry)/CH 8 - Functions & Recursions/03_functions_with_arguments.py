def goodDay(name):
    print('Good Day,' + name)

goodDay('akash')
goodDay('ambika')

def goodDay(name , ending ):
    print('Good Day,' + name)
    print(ending)

goodDay('divya','thank u')

def goodDay(name , ending ):
    print('Good Day,' + name)
    print(ending)
    return 'done'

a = goodDay('divya','thank u')
print(a)