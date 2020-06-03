# Nomes de classes comecao com letra maiúscula.
# Nomes compostos devem ser escritos DessaManeira (igual no java)
class Conta:

    # Atributo estático
    # Ex.: Conta.pais
    pais = "BRASIL"

    # __init__ = é o construtor (função construtora).
    # self = é a referência que sabe encontrar o objeto construído em memória (equivalente ao this no Java).
    # Utilizaremos self para acessar o objeto e definir seus atributos e características.

    # Em self.numero, o caractere "ponto" (.) é um comando de ida ao objeto e numero, titular, saldo e limite são atributos.

    # O valor do self é passado pelo Python, responsável pela criação final do objeto em memória. No entanto, os valores
    # dos parâmetros como numero deverão ser definidos usando a aplicação.

    # Obs¹.: sempre precisaremos do self como parâmetro no __init__
    # Obs².: parâmetro limite por padrão será de mil reais e não é obrigatório (lembrar do curso anterior)

    # Exemplo de criação de uma conta:
    # conta = Conta(321, "Marco", 100.0, 3000.0)
    # conta = Conta(321, "Marco", 100.0)
    def __init__(self, numero, titular, saldo, limite=1000.0):
        print("Construindo objeto...{}".format(self))

        # Atributos públicos. Podem ser acessados diretamente
        #   self.numero = numero
        #   self.titular = titular
        #   self.saldo = saldo
        #   self.limite = limite

        # Atributos privados. Atributos privados começam com "__".
        # O Python não proibe acessá-los diretamente, mas não proíbe de alterá-los
        # O Python avisa que o atributo foi criado para ser usado dentro da classe por meio dos métodos.
        # Ex.: conta._Conta__numero (fazer isso é válido, mas não é recomendado)
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    # Atribuindo valor ao saldo
    def deposita(self, valor):
        self.__saldo += valor

    # Subtraindo valor do saldo
    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Limite ultrapassado")

    # Definindo um método privado com __ antes do nome do método
    # Assim como os atributos, o Python não proíbe de acessar esse método diretamente,
    # apesar de não ser recomendado
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_sacar = (self.__saldo + self.__limite)
        return valor_a_sacar <= valor_disponivel_sacar

    # Realiza uma transferência da conta atual (self), para a conta dentino
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    # GETTERS
    def get_numero(self):
        return self.__numero

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    # SETTERS
    # Acessar a classe Cliente para consultar outra forma de fazer GETTER e SETTER
    def set_limite(self, limite):
        self.__limite = limite

    # Criando método estático (similar ao static do Java)
    # Dessa forma, conseguimos chamar esse método sem precisar criar uma instância de conta.
    # Ex.: Conta.codigo_banco()
    @staticmethod
    def codigo_banco():
        return "001"

    # Mais um exemplo de uso de método estático
    # Retornando um dicionário de dados (similar ao HashMap no Java)
    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}