class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    '''
    Na linguagem Python, os métodos que dão acesso são nomeados como properties. 
    Desta forma, indicaremos para o Python nossa intenção de ter acesso ao objeto.
    
    Com isto, indicamos que este método representa uma propriedade — um termo já 
    recorrente em outras linguagens, como Delphi e C#. Com @property, 
    indicamos que estamos trabalhando com uma propriedade.
    
    Agora, quando digitarmos no console cliente.nome, sem a adição dos parênteses, 
    conseguiremos que o método seja executado como antes (como se o atributo fosse público).
    
    A maneira como escrevemos no console, parece que estamos acessando diretamente o atributo, 
    porém o método nome() foi chamado.
    
    Obs.: o atributo precisa ser sempre privado!!!
    '''
    @property
    def nome(self):
        print("Realizando GETTER em atributo privado usando @property")
        return self.__nome.title()

    '''
    Criamos um setter sem a adicionação do set antes do nome do método. Mas para que ele 
    funcione, teremos que adicionar também uma configuração: @nome.setter.
    
    Somente precisamos especificar: @meu_atributo.setter
    
    E dessa maneira, conseguiremos executar: cliente.nome = "Algum Nome"
    '''
    @nome.setter
    def nome(self, nome):
        print("Realizando SETTER em atributo privado usando @nome.setter")
        self.__nome = nome