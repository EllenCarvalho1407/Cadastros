#Control Model
from ModelPessoa import ModelPessoa
class ControlPessoa:
    #Método Construtor
    def __init__(self):
        self.pessoaUm= ModelPessoa#Criando uma chave para acessar métodos da classe ModelPessoa
        self.opcao = -1
        self.atu = 0
    def menu(self):
        print("\n\nEscolha uma das opções abaixo: +"
              "\n sair +"
              "\n 1. Cadastrar Pessoa +"
              "\n 2. Consultar pessoa + "
              "\n 3. Atualizar Pessoas: + "
              "\n 4. Excluir Pessoas ")
        self.opcao = int(input())

    def cadastrar (self):
        cpf = int(input("Informe seu CPF:"))
        nome = (input("Informe seu Nome:"))
        telefone = int(input("Informe seu Telefone:  "))
        endereco = (input("Informe seu Endereço: "))
        email = (input("Informe seu E-mail: "))
        self.pessoaUm.cadastrarPessoa(self, cpf,nome,telefone,endereco,email)


    def consultar(self):
        print(self.pessoaUm.consultarPessoa())

    def menuatualizar(self):
        print ("\nQual Campo você deseja Atualizar? +"
               "\n1. Nome +"
               "\n2.Telefone +"
               "\n3.Endereço +"
               "\n4. E-mail")

        self.atu = int(input())

    def atualizar (self):
         self.menuAtualizar()
         if self.atu ==1:
            nome =input("Informe o novo nome:")
            self.pessoaUm.AtualizarPessoa(self.atu,nome)
         elif self.atu ==2:
            telefone = int(input("Informe o novo Telefone: "))
            self.pessoaUm.atualizarPessoa(self.atu, telefone)
         elif self.atu == 3:
            endereco = input("Informe o novo Endereço:")
            self.pessoaUm.atualizarPessoa(self.atu,endereco)
         elif self.atu ==4:
            email = input("Informe o novo E-mail:")
            self.pessoaUm.atualizarPessoa (self.atu,email)
         else:
            print("Escolha uma opção 1 a 4")

    def exluir(self):
            self.pessoaUm.excluirPessoa()
            print("Dados Excluidos com Sucesso!")

    def operacao(self):
        while self.opcao !=0:
            self.menu()
            if self.opcao ==1:
              self.cadastrar()
            elif self.opcao == 2:
              self.consultar()
            elif self.opcao ==3:
              self.atualizar()
            elif self.opcao == 4:
              self.excluir ()
            else :
                print("Escolha uma opção entre 1 a 4")

