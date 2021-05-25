import string
print('Hello World')

a = 4
b = 5
print(a+b)

 #Kommentar

print(1+1)
print(1-1)
print(1*1)
print(1/1)

print(4*(1+2))
print(a*(a+b))
print('''Hallo 
"ich" 
 bin zuhause''') 



print('Hello ' + 'World') 

print('1' + '3')

        #0,  1,  2,  3,  4
list = ['1','2','3','4','5']# String beginnt immer mit 0
list.insert(3, '6')
print(list)

#liste aus vielen listen
              #array    #list
mixed_list = [{1, 2}, [5, 6, 7]]
#tupel erstellen
number_tuple = (3, 4)
# tupel einfügen
mixed_list.insert(1, number_tuple)
print(mixed_list)

'''Mehrzeiliger 
Kommentar'''

age = 17
print(age)
age = 18
print(age)
name = 'Jonas'
print(name, age)
#Bezeichner beginnt immer mit einem Buchstaben oder einem _ (keine Sonderzeichen möglich)

_8jsdaöf = 'Hallo'

print(_8jsdaöf)

print('''h
e
l
p''')


print('Hallo ' *3)

# int = integer (Ganzzahl)

# float = Gleitkommazahl

# String = 'Text'  

print('''Mir "geht" es gut''')

vorname1 = 'Axel'
vorname2 = 'Elke'
vorname3 = 'Martin'

vornamen = ['Axel', 'Elke', 'Martin']

print(vornamen)

print(vornamen[1])
print(vornamen[-1])

vornamen += ['Heike', 'Sabine']
print(vornamen)

del(vornamen)

vornamen = ['x','y']
print(vornamen)

vornamen.insert(3, 'z')
vornamen.remove('x')
print(vornamen)
print(vornamen.index('y'))

#array gibt das letzte Element im String aus
variableA = 'Ich bin eine Variable'
print(variableA[-1])

#Array gibt position 1 vom String aus 
print(variableA[1])

variableA = 'Ich bin eine Variable'
print(len(variableA))

deutschenglisch = {}
deutschenglisch['null'] = 'zero'
deutschenglisch['eins'] = 'one'
deutschenglisch['zwei'] = 'two'
deutschenglisch['drei'] = 'three'


deutschitalienisch = {'eins': 'uno', 'zwei': 'due', 'drei': 'tre'}

print(deutschitalienisch)

Vorname = input("Ihr Vorname: ")
Nachname = input("Ihr Nachname: ")
Vorname = Vorname[::-1]
Nachname = Nachname[::-1]
print(Vorname, Nachname)

list = input("Enter numbers to list: ")
tuple = input("Enter numbers to list: ")

print(list, tuple)

list = input("Enter numbers to list: ")
tuple = input("Enter numbers to list: ")

print("[", list, "]", "(", tuple, ")")
