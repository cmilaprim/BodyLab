from Exception.NumeroTelefoneInvalidoException import NumeroTelefoneInvalido
from Exception.NomeNaoehAlfa import NomeNaoehAlfa
from telas.telaAluno import TelaAluno
from modelos.aluno import Aluno
from modelos.endereco import Endereco
class ControladorAluno():
    def __init__(self, controlador_sistema):
        self.__tela_aluno = TelaAluno()
        self.__controlador_sistema = controlador_sistema
        self.__alunos = []
        self.__matricula = None


    def cadastrar_aluno(self):
        dados_aluno = self.__tela_aluno.pega_dados_aluno()
        nome = dados_aluno['nome']
        if dados_aluno['nome'] not alfa:

        nome_aluno = self.buscar_aluno_por_nome(nome)
        if nome_aluno:
            self.__tela_aluno.mostra_mensagem("Aluno já cadastrado")
            return
        if len(dados_aluno['numero_telefone']) != 11 or not dados_aluno['numero_telefone'].isnumeric:
           raise NumeroTelefoneInvalido()
        endereco = Endereco(dados_aluno['rua'], dados_aluno['complemento'], dados_aluno['bairro'], dados_aluno['cidade'], dados_aluno['cep'])
        aluno = Aluno(dados_aluno['nome'], dados_aluno['numero_telefone'], dados_aluno['email'], matricula = None, endereco = endereco)
        self.__alunos.append(aluno)
        self.__tela_aluno.mostra_mensagem("Aluno cadastrado com sucesso")
        return aluno


    def remover_aluno(self):
        aluno = self.__tela_aluno.seleciona_aluno()
        if aluno in self.__alunos:
            self.__alunos.remove(aluno)
            self.__tela_aluno.mostra_mensagem("Aluno removido com sucesso")

        else:
            self.__tela_aluno.mostra_mensagem("Aluno não encontrado")

    def buscar_aluno_por_nome(self, nome_aluno):
        for aluno in self.__alunos:
            if aluno.nome == nome_aluno:
                return aluno
        return None

    def listar_alunos(self):
        if not self.__alunos:
            self.__tela_aluno.mostra_mensagem("Nenhum aluno cadastrado")
        else:
            for aluno in self.__alunos:
                dados_aluno = {
                    'nome': aluno.nome,
                    'numero_telefone': aluno.numero_telefone,
                    'email': aluno.email,
                    'endereco': aluno.endereco
                }
                self.__tela_aluno.mostra_aluno(dados_aluno)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_aluno, 2: self.remover_aluno, 3: self.listar_alunos, 4: self.buscar_aluno_por_nome, 0: self.retornar}

        while True:
            try:
                opcao_escolhida = self.__tela_aluno.tela_opcoes()
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
            except NumeroTelefoneInvalido:
                self.__tela_aluno.mostra_mensagem("Número de telefone inválido")

    def retornar(self):
        self.__controlador_sistema.abre_tela()