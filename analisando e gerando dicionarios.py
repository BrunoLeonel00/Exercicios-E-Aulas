def notas(*num, sit=False):
    """
    Mostra a situação do aluno
    :param num: Notas do aluno(a)
    :param sit: Retorna se o aluno está: Aprovado, Reprovado ou em recuperação
    :return: retorna o dicionario com varias situações
    """
    alunos = dict()
    alunos['Total'] = len(num)
    alunos['maior'] = max(num)
    alunos['Menor'] = min(num)
    alunos['media'] = sum(num) / len(num)
    if sit:
        if alunos['media'] <= 6:
            alunos['Situação'] = 'RUIM'
        else:
            alunos['Situação'] = 'Boa'
    return alunos


# Programa principal
resp = notas(5.4, 3.1, 4.7, sit=True)
print(resp)
