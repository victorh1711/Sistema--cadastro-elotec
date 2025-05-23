#função para cadastar uma missão
def casdastrarmissao(lista):
      nave=input("Digite o nome da nave: ")
      destino=input("Digite o destino da nave: ")
      tripulaçao=int(input("Digite o número de tripulantes: "))
      #combusdtivel em litros
      combustivel=float(input("Digite a quantidade de combustível disponivel: "))
      duração=int(input("Duraçaõ em dias:"))
     
      missão={
     "nave": nave,
      "destino": destino,
     "tripulação": tripulaçao,
     "combustível": combustivel,
     "duração": duração
      }
      lista.append(missão);
   
      print("missão cadastrada com sucesso!")
    
    

   
