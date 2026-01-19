from database import criar_tabela
from crud import(
    criar_usuario,
    listar_usuario,
    atualizar_usuario,
    deletar_usuario
)

def menu():
     print("\n--- CRUD Usuários ---")
     print("1-Criar Usuario")
     print("2-Listar Usuario")
     print("3-Atualizar Usuario")
     print("4-Deletar Usuario")
     print("0-Sair")

def main():
     criar_tabela()
     while True:
          menu()
          opcao = input("Escolha: ")
          if opcao == "1":
            nome = input("Nome: ")
            email= input("Email: ")
            criar_usuario(nome, email)
            print("Usuário criado!")
          elif opcao == "2":
            usuarios = listar_usuario()
            for u in usuarios:
                print(u)
          elif opcao == "3":
            id = input("Novo id do usuario: ")
            nome = input("Novo nome do usuario: ")
            email= input("Novo email do usuario: ")
            atualizar_usuario(id,nome,email)
            print("Usuário atualizado!")
          elif opcao == "4":
            id = input("Id do usuario: ")
            deletar_usuario(id)
            print("Usuario removido!")
          elif opcao == "0":
            print("Saindo...")
            break

          else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()

