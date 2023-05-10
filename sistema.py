#CADASTRO DE PRODUTOS
itens_cadastrados = []
def cadastro():
  itens_cadastrados.append(input("Digite o nome do produto para cadastrar : "))

#EXIBIR PRODUTOS CADASTRADOS

def exibir():
  global contador
  contador =0
  while(contador<len(itens_cadastrados)):
   print(f'{contador} - {itens_cadastrados[contador]}')
   contador+=1
   
#EDITAR PRODUTOS CADASTRADOS
 
def editar_items():
  global indice_item
  exibir()
  indice_item = int(input("Qual dos itens acima deseja editar ? : ")) 
  itens_cadastrados[indice_item] = input("Digite o valor correto : ")
  print("Lista Atualizada : ")
  exibir()
  
#EXCLUIR PRODUTO

def excluir_item():
 global excluir
 excluir = int(input("Qual dos itens abaixo deseja excluir ? : ")) 
 exibir()
 del itens_cadastrados[excluir]
 exibir()
 
#MENU SECUNDÁRIO

def menu_secundario(): 
  global escolha 
  escolha = 0
  while(escolha!=5):
      escolha = int(input("1-CADASTRAR PRODUTO 2-EXIBIR 3-EDITAR  4-EXCLUIR   5-SAIR\n"))
      match escolha:
          case 1:cadastro()  
          case 2:print("Itens cadastrados : "),exibir()
          case 3:editar_items()
          case 4:excluir_item()
          case 5: print("Até a próxima !")
          case _:print("Inválido")  
               
#CADASTRO 

logins = []
senhas = []
def cadastro_entrada():
    global logins
    global senhas
    logins.append(input("Digite o emaill para cadastro : "))
    senhas.append(input("Digite a senha de sua preferência : "))

#VALIDAÇÃO DE LOGIN

def validacao_login():
    global indice
    global login_teste
    global senha_teste
    login_teste= input("Digite seu email : ")
    senha_teste = input("Digite sua senha : ")
    indice =0
    
    while(True):
        if len(logins) > indice and login_teste == logins[indice]:
            if senha_teste == senhas[indice]:
                print("Logado com sucesso")
                menu_secundario() 
                break  
        elif len(logins)<indice:
          print("Não Encontrado")
          if(login_teste[i]>len[logins]):
            break
        indice+=1
                          

#MENU PRINCIPAL
escolha_principal = 0
while(escolha_principal!=3):
  escolha_principal = int(input("*SEJA BEM VINDO AO SISTEMA DE ESTOQUE DO SUPERMERCADO REIS* \n1-PARA ENTRAR NO SISTEMA 2-CRIAR CADASTRO 3-SAIR\n")) 
  match escolha_principal:
    case 1: validacao_login()
    case 2 : cadastro_entrada()
    case 3 : break
    case _ : print("Inválido")

      
