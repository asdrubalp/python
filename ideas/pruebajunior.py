"""la prueba de el mumber """
print("hola consola")
for i in range( 1, 101):
    print(i)
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")