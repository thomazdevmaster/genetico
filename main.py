from random import randint, random, sample

# Valores globais
limites = [-10,10]
qtdInicial = 4
taxaMutacao = 0.01
taxaCrossOver = 0.7
qtdGeracoes = 5
_tamanhoVetor = 0
_melhorValor = 0
equacao = 'x²-3x+4'

# Realiza a resolução da função objetivo com f(x)
def funcaoObjetivo (x):
    resultado = x*x - 3*x + 4
    print(f'resolvendo f({x:^3}) = {resultado}')
    return resultado

# Converte array de bytes em inteiro
def binToInt(arr):
    return int(''.join(arr),2)

# Converte inteiro em array de bytes
def intToBin(num):
    return bin(num).replace('0b','' if num < 0 else '+').zfill(_tamanhoVetor)

# Retorna a quantidade de bits necessária de acordo com o limite
def qtdBits(limites):
    maior = max(abs(limites[0]),abs(limites[1]))
    return len(bin(maior))

# Cria a população com indivíduos array de bytes
def gerarPopulacao(quantidade):

    # Cria lista de lista vazia
    populacao = [[] for i in range(quantidade)]
    global _tamanhoVetor
    _tamanhoVetor = qtdBits(limites) - 1

    # Define cada indivíduo de forma aleatória
    for individuo in populacao:
        indivAtual = randint(limites[0], limites[1])
        binIndivAtual = intToBin(indivAtual)
        print(f'|{indivAtual:^5}|{binIndivAtual:^10}|')
        for bit in binIndivAtual:
            individuo.append(bit)

    return populacao

# Retorna lista com resultado de cada indivíduo sobre a função objetivo
def avaliar(populacao):
    avaliados = []
    for individuo in populacao:
        indivInt = binToInt(individuo)
        avaliados.append(funcaoObjetivo(indivInt))
    return avaliados

# Seleção por torneio
def selecionarPorTorneio(populacao, resultados):
    # Seleciona dois indivíduos aleatórios e retorna o que leva a um resultado melhor
    indices = sample(range(0, len(populacao)), 2)    
    return populacao[indices[0]] if resultados[indices[0]] > resultados[indices[1]] else populacao[indices[1]]

# Retorna o indivíduo com melhor resultado entre a população
def retornaMelhor (populacao, resultados):
    candidatos = zip(populacao, resultados)
    return max(candidatos, key=lambda elemento: elemento[1])

# Realiza crossover entre pais
def crossover(pai,mae,taxaCrossOver):
    
    # Sorteio de valor aleatório para testar a taxa de crossover
    if random() <= taxaCrossOver:
        print('\n-----------------------------')
        print('          crossover')
        print('-----------------------------')

        # Define o bit que será cortado de forma aleatória
        pontoCorte = randint(0, len(pai)-1)
        print('Ponto do corte definido em ', pontoCorte)

        # troca a calda do pai com a mãe, a partir do ponto de corte
        filho1 = pai[:pontoCorte] + mae[pontoCorte:]
        filho2 = mae[:pontoCorte] + pai[pontoCorte:]

        # Verifica se os novos indivíduos extrapolam os valores limite
        filho1 = verificaLimites(filho1)
        filho2 = verificaLimites(filho2)

        print(f'pai {binToInt(pai):.>15}|{pai}')
        print(f'mae {binToInt(mae):.>15}|{mae}')
        print(f'primeiro filho {binToInt(filho1):.>4}|{filho1}')
        print(f'segundo filho {binToInt(filho2):.>5}|{filho2}')

        return filho1, filho2
    else:
        print('Não ocorreu crossover')
        return pai, mae

# Verifica se o indivíduo extrapola algum limite
def verificaLimites(individuo):
    # Converte valores em int
    indivInt = binToInt(individuo)
    limMin = intToBin(limites[0])
    limMax = intToBin(limites[1])

    # Se estourar o limite retorna o próprio limite estourado
    if indivInt < limites[0]:
        print('**Estourou o limite, ajustando para o mínimo**')
        for indice, bit in enumerate(limMin):
            individuo[indice] = bit

    elif indivInt > limites[1]:
        print('**Estourou o limite, ajustando para o máximo**')
        for indice, bit in enumerate(limMax):
            individuo[indice] = bit
    
    return individuo

# Realiza mutação de gene
def mutacao(individuo, qualFilho):
    # Auxiliar para efetuar a troca
    possiveis = ['0','1','+','-']
    trocaPor = ['1','0','-','+']

    # Verifica a probabilidade de mutação
    if random() <= taxaMutacao:
        print('\n-----------------------------')
        print('            mutação')
        print('-----------------------------')

        # Escolhe algum bit para ser invertido
        trocarBit = randint(1,_tamanhoVetor)
        print(f'Trocando o {trocarBit}º BIT do {qualFilho}º filho')
        print(individuo)
        bit = individuo[trocarBit -1]
        indice = possiveis.index(bit)
        novoBit = trocaPor[indice]
        print(f'trocando {bit} por {novoBit}')
        individuo[trocarBit -1] = novoBit
        individuo = verificaLimites(individuo)
        print(individuo)
    else:
        print(f'Não ocorreu mutação! para o {qualFilho}º filho')
    return individuo

def main():
    menu()
    print(f'População inicial com {qtdInicial} indivíduos')
    print('----------------------------------')

    # Gerar população inicial
    populacao = gerarPopulacao(qtdInicial)

    # resolve a equação com todos indivíduos da população
    avaliados = avaliar(populacao)
    print()

    # repete a quantidade de gerações escolhida
    for i in range(qtdGeracoes):
        # retorna o melhor valor dentre a população
        melhorNum, resultado = retornaMelhor(populacao,avaliados)
        global _melhorValor

        # Converte o melhor valor atual para decimal
        valorAtual = binToInt(melhorNum)
        print(f'\npara a {i + 1}ª geração, o indivíduo mais apto é {valorAtual}, pois seu resultado é {resultado}\n')

        # Verifica se o valor atual é melhor que o valor alcançado anteriormente
        if(funcaoObjetivo(valorAtual) < funcaoObjetivo(_melhorValor)):
            print(f'Porém o melhor valor ainda é {_melhorValor}')
        elif funcaoObjetivo(valorAtual) == funcaoObjetivo(_melhorValor):
            print(f'Logo o melhor valor continua sendo {_melhorValor}')
        else:
            _melhorValor = valorAtual
            print(f'Logo {valorAtual} passa a ser o novo melhor valor')

        # Vetor para nova população que será gerada por crossover ou mutação
        novaPopulacao = []

        while len(novaPopulacao) < len(populacao):
            # Seleciona os pais diferentes, selecionados por torneio
            paiBin = selecionarPorTorneio(populacao, avaliados) 
            maeBin = selecionarPorTorneio(populacao, avaliados)
            while maeBin == paiBin:
                maeBin = selecionarPorTorneio(populacao, avaliados)
            pai = int(''.join(paiBin),2)
            mae = int(''.join(maeBin),2)
            print('Os pais selecionados foram')
            print(f'{pai:^5}|{str(paiBin):^40}')
            print(f'{mae:^5}|{str(maeBin):^40}')

            # Realiza crossover dos pais e gera 2 filhos
            filho1, filho2 = crossover(paiBin,maeBin,taxaCrossOver)   

            # Mutação de gene
            filho1 = mutacao(filho1, 1)
            filho2 = mutacao(filho2, 2)

            # Adiciona novos indivíduos na população
            novaPopulacao.append(filho1)
            novaPopulacao.append(filho2)
            print('-------população atual----------')
            for i in populacao:
                print(f'{binToInt(i)} | {i}')
            print('--------------------------------')

        # Atualiza a população
        populacao = novaPopulacao
        print('=======================================')

        # Realiza a avalização da nova população
        avaliados = avaliar(populacao)
    print('================================================================')
    print(f'O resultado final é {_melhorValor}, pois seu retorno é {funcaoObjetivo(_melhorValor)}')


def menu():
    
    print(f"""
    **********************ALGORÍTMO GENÉTICO*************************
    -----------------------------------------------------------------
     Execução do algorítmo genético para maximizar a função '{equacao}'
     com as seguintes definições:

     limite inferior {limites[0]:.>32} 
     limite superior {limites[1]:.>32}
     população inicial {qtdInicial:.>30}
     taxa de mutacao {taxaMutacao*100:.>32}%
     taxa de crossOver {taxaCrossOver*100:.>30}%
     quant. gerações {qtdGeracoes:.>32}

    """)
    alterar = input('Deseja alterar algum valor? (S/N): ')
    if alterar == 's' or alterar == 'S':
        alterarValores()
        menu()
        

def alterarValores():
    global limites, qtdInicial, taxaMutacao,taxaCrossOver, qtdGeracoes

    limInf = input(f'Entre com o novo limite inferior ou ENTER para continuar com {limites[0]}: ')
    if validarEntrada(limInf):
        limites[0] = int(limInf)

    limSup = input(f'Entre com o novo limite superior ou ENTER para continuar com {limites[1]}: ')
    if validarEntrada(limSup):
        while int(limSup) <= limites[0]:
            limSup = input(f'O valor digitado deve ser maior que o limite inferior({limites[0]}), digite novamente ')
        limites[1] = int(limSup)
    
    op = input(f'Entre com o nova população inicial ou ENTER para continuar com {qtdInicial}: ')
    if validarEntrada(op):
        qtdInicial = int(op)

    op = input(f'Entre com a nova taxa de mutação ou ENTER para continuar com {taxaMutacao*100}%: ')
    if validarEntrada(op):
        taxaMutacao = float(op) / 100
    
    op = input(f'Entre com a nova taxa de crossover ou ENTER para continuar com {taxaCrossOver*100}%: ')
    if validarEntrada(op):
        taxaCrossOver = float(op) / 100

    op = input(f'Entre com a nova quantidade de gerações ou ENTER para continuar com {qtdGeracoes} gerações: ')
    if validarEntrada(op):
        taxaMutacao = int(op)
    

def validarEntrada(entrada):
    try:
        if isinstance(int(entrada), int):
            return True
    except:
        return False

# inicia o programa
main()