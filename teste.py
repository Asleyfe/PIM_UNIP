usuarios = {}
professores = {} 
alunos = {}
usuario = {}

def criarturma():
    print('turma criada')

def inseriraula():
    print('Aula')

def inseriratividade():
    print('atividade inserida')


def acoesProfessor():
    global usuario
    global professores
    if usuario in professores:
        acoes = {
        1: ("Criar Turma", criarturma),
        2: ("Inserir Aula", inseriraula),
        3: ("Inserir Atividade", inseriratividade)
        }
        for chave,(rotulo,funcao) in acoes.items():
            print(f'{chave}: {rotulo}')
        
        print('exemplo:(1,2 ou 3)\n')
        escolha = int(input('Escolha uma opção:\n'))

            
        while True:
            if escolha == 1:
                criarturma()
            elif escolha == 2:
                inseriraula()
            elif escolha == 3:
                inseriratividade()
            else:
                print("Opção invalida")
    else:
        print(f'{usuario} não esta cadastrado como Professor')


def menu():
    opcao = 0

    print('menu inicial')


def validacaoMatricula():
    global usuarios
    while True:
        matricula = input("Qual a sua matricula:").strip()

        if matricula in usuarios:
            print(f"O usuario e invalido Matricula existente")

        else:
            print(f"Matricula Valida")
            break
    return matricula

def validacaoFuncao():

    while True:
        funcao = input("Qual sua funcao (professor ou aluno):").lower().strip()

        if funcao == "professor" or funcao == "aluno":
            break
        else:
            print("Digite uma função valida")
    return funcao

def createUser():
    """ usuario = ["nome"[0], "matricula"[1], "funcao"[2]] """
    global usuarios
    nome = input("Qual seu nome:").strip()
    matricula = validacaoMatricula()
    funcao = input('Qual sua função(professor(a)/aluno(a)):')

    usuarios[matricula]=[nome, funcao]

    print(f"Novo usuario adicionado{usuarios}")
    return usuarios

def ListarProfessores():
    global professores, usuarios
    
    for matricula, dados in usuarios.items():
        if dados[1] == "professor":
            professores[matricula] = dados
    return print(f"Os Professores cadastrados sao:{professores}")

def ListarAlunos():
    global alunos, usuarios
    for matricula, dados in usuarios.items():
        if dados[1] == "aluno":
            alunos[matricula] = dados
    return print(f"Os Alunos cadastrados sao:{alunos}")

createUser()
ListarProfessores()
ListarAlunos()

