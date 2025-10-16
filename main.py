usuarios = []
professores = [] 
alunos = []


def validacaoMatricula():
    matriculas = {usuario[1] for usuario in usuarios}

    while True:
        matricula = input("Qual a sua matricula:")

        if matricula in matriculas:
            print(f"O usuario e invalido Matricula existente")

        else:
            print(f"Matricula Valida")
            break
    return matricula


def validacaoFuncao():

    while True:
        funcao = input("Qual sua funcao (professor ou aluno):").lower()

        if funcao == "professor" or funcao == "aluno":
            break
        else:
            print("Digite uma função valida")
    return funcao


def createUser():
    """ usuario = ["nome"[0], "matricula"[1], "funcao"[2]] """
    global usuarios
    nome = input("Qual seu nome:")
    matricula = validacaoMatricula()
    funcao = validacaoFuncao()

    novo_usuario = [nome, matricula, funcao]

    usuarios.append(novo_usuario)

    print(f"Novo usuario adicionado{usuarios}")
    return usuarios

def ListarProfessores():
    global professores
    for usuario in usuarios:
        if usuario[2] == "professor":
            professores.append(usuario)
    return print(f"Os Professores cadastrados sao:{professores}")

def ListarAlunos():
    global alunos
    for usuario in usuarios:
        if usuario[2] == "aluno":
            alunos.append(usuario)
    return print(f"Os Professores cadastrados sao:{alunos}")
createUser()
