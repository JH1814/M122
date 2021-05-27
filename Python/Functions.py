def how_should_i_get_there(miles):
  if(miles > 120.0):
    print("Take a plane")
  elif(miles >= 2.0):
    print("Take a Car")
  else:
    print("Walk")


how_should_i_get_there(2.0)
how_should_i_get_there(.5)
how_should_i_get_there(800.3)

def mit_zwei_multiplizieren(eingabe):
    eingabe = 2*eingabe
    print("Verdopple ich diese Zahl, so erhalte ich ",eingabe)
zahl = int(input("Gib eine ganze Zahl ein: "))
mit_zwei_multiplizieren(zahl)
zahl = int(input("Gib eine weitere ganze Zahl ein: "))
mit_zwei_multiplizieren(zahl)
print("Danke für die Eingabe.")