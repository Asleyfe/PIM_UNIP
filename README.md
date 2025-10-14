# PIM_UNIP

Este repositório contém o projeto em grupo do 2º período de Análise e Desenvolvimento de Sistemas, focado na análise PIM (RF, RNF, RS, RU).

## Equipe

*   **Lucas:** Macro do trabalho (ABNT, delegação de tarefas, descrição do que foi feito), quebra-galho.
*   **Carlos:** GitHub, Diagramação, Redes de Computadores, Código.
*   **Melo:** Ambiental, Quebra-galho, Pontual, amigo de todos.
*   **Pedro:** Pesquisa Tecnológica, Comunicativo.
*   **Rafaela:** Organização, Engenharia Ágil (software).
*   **Rodrigo:** Código, Organização, Foco, Diagramação, Planejamento Estruturado, Bancos de Dados, GitHub, IA.

## Requisitos Funcionais (RF)

### Cadastro de Turma
*   **Descrição:** Professor pode cadastrar turmas com Matéria, Curso, Vagas e RegistroTurma.
*   **Critérios de Aceitação:**
    *   Gera ID único.
    *   Campos obrigatórios validados.
    *   Não permite duplicidades.
    *   Confirma criação no terminal.

### Cadastro de Aluno/Professor
*   **Descrição:** Aluno pode se cadastrar no sistema com Nome, Matrícula e Função.
*   **Critérios de Aceitação:**
    *   Matrícula única.
    *   Valida campos obrigatórios.
    *   Não permite duplicatas.
    *   Confirma criação no terminal.

### Cadastro de Aluno em Turma
*   **Descrição:** Aluno pode se cadastrar em uma turma de seu curso.
*   **Critérios de Aceitação:**
    *   Verifica vagas disponíveis.
    *   Verifica curso.
    *   Decrementa vaga.
    *   Registra nome e matrícula na vaga ocupada.

### Registro de Aula
*   **Descrição:** Professor registra aula (turma, tema) e resumo (2000 caracteres).
*   **Critérios de Aceitação:**
    *   Armazena registro com timestamp e autor.
    *   Permite listar por turma.

### Registro de Diário Eletrônico (Resumo da Aula)
*   **Descrição:** Professor registra (turma, data, curso) e resumo (2000 caracteres), marca alunos presentes, inclui notas de cada aluno e anexo da aula.
*   **Critérios de Aceitação:**
    *   Armazena registro.
    *   Salva aula como concluída.
    *   Salva anexo junto à aula com turma, data e resumo.

### Upload de Atividades
*   **Descrição:** Professor publica atividade com Nome, Matéria, Data, Anexo e Turma.
*   **Critérios de Aceitação:**
    *   Anexo em PDF.
    *   Tamanho máximo de 20MB.
    *   Visível apenas para os alunos da turma.

### Consulta de Atividades
*   **Descrição:** Lista atividades da turma para alunos por matéria; busca por matéria.
*   **Critérios de Aceitação:**
    *   Paginação funcional.
    *   Filtros aplicáveis.
    *   Tempo de resposta aceitável (ver RNF).

### Consulta Geral
*   **Descrição:** Lista turmas, alunos, aulas e atividades via comandos no terminal.
*   **Critérios de Aceitação:**
    *   Filtros básicos (por turma, abertas/fechadas, vagas, pertence à turma).

## Requisitos Não Funcionais (RNF)

### Rede Local (LAN)
*   **Descrição:** Suportar operação local, cliente-servidor.
*   **Critérios:**
    *   4 usuários simultâneos no laboratório.
    *   Listagem < 500 ms em condições normais.

## Requisitos de Sistema (RS)

### Tecnologias
*   **Descrição:** Deve utilizar por padrão C para servidor local e Python para funcionalidades.
*   **Critérios:** Documento arquitetural descrevendo responsabilidades claras entre C e Python.

### Python
*   **Descrição:** A UI do CLI deve ser em Python.
*   **Critérios:** Interface do terminal aprimorada e amigável.

### C
*   **Descrição:** O servidor deve ser feito em C, pequeno e local.
*   **Critérios:** Aceitar JSON-lines via TCP.

### Impacto Ambiental
*   **Descrição:** Destacar o impacto ambiental do sistema (não desperdício de papel - relatório). Mostrar sempre a quantidade de papel não gasto e quanto isso é benéfico para a vida na terra.
*   **Critérios:** Função em Python para calcular o impacto de uma folha de papel no meio ambiente.

## Requisitos de Usuário (RU)

*   Cadastrar turmas e alunos.
*   Registro de aulas.
*   Diário eletrônico.
*   Upload de atividades.
*   Consulta de atividades.
