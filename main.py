def verificar_par_ou_impar (numero) :
   if numero % 2 == 0:
        return "Numero par"
   else:
       return "Numero ímpar"

resposta = int(input("Verifique se seu número é par ou ímpar: "))

print(verificar_par_ou_impar(resposta))