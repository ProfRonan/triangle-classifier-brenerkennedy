a = int(input("digite um valor inteiro "))
b = int(input("digite um segundo valor inteiro "))
c = int(input ("digite um terceiro valor inteiro "))
if((a+b)> c and (a+c)> b and (b+c)>a):
    if(a==b and b==c):
        print("os valores formam um triângulo equilátero ")
    elif(a==b or b==c):
        print("os valores formam um triângulo isóceles")
    else:
        print("os valores formam um triângulo esqualeno")
else:
    print("os valores não formam um triângulo ") 
