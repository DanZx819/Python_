frase = input("Digite uma algo: ")


s = frase.isspace()
N = frase.isnumeric()
n = frase.isalnum()
M = frase.isupper()
m = frase.islower()
afb = frase.isalpha()
c = frase.capitalize()
print (type(frase))
print ("É feito de espaços ? =", s)
print ("É numero ? =", N)
print ("É alfanumérico ? =", n)
print ("É maiusculo ? =", M)
print ("É minusculo ? =", m)
print ("É alfabético ? =", afb)
print ("Capitalização:", c)