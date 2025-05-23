
from function import *
def menu():
    while True:
     print("Olá, seja bem-vindo ao nosso sistema:");
     print('escolha algum das opções abaixo:');
     print("1.Cadastrar missão.");
     print('2.Listar as missões.');
     print('3.Simular lançamento.');
     print('4.Sair.');

     opcao=int(input('Digite sua escolha:'))
     if opcao==1:
        return cadastrarmissão();
        break;
     elif opcao==2:
        return listarmissão();
        break;
     elif opcao==3:
        return simularlançamento();
        break;
     elif opcao==4:
        print('Saindo do sistema...');
        break;
     else:
            print('Opção inválida, tente novamente.');


menu()
        
    