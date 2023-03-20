
gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
alunos = []
while True:
    respostas = []
    acertos = 0
    for i in range(10):
        resposta = input(f'Resposta {i + 1}: ').upper()
        respostas.append(resposta)
        if resposta == gabarito[i]:
            acertos += 1
    nota = acertos
    alunos.append({'nota': nota, 'acertos': nota})
    if input('Deseja Continuar? S ou N: ').upper() != 'S':
        break
maior_acerto = max(aluno['acertos'] for aluno in alunos)
menor_acerto = min(aluno['acertos'] for aluno in alunos)
media = sum(aluno['nota'] for aluno in alunos) / len(alunos)
print(f'Maior Acerto: {maior_acerto}\n'
      f'Menor Acerto: {menor_acerto}\n'
      f'Total de Alunos: {len(alunos)}\n'
      f'Média das Notas: {media:.2f}')
