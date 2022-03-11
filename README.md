# ALGORÍTMO GENÉTICO

## Thomaz Flanklin de Souza Jorge
> Disciplina GCC128-2021/1

> Professor: AHMED ALI ABDALLA ESMIN

### Algorítmo Genético implementado em python para maximização de função *x²-3x+4*

#### Descrição do trabalho
- Encontrar de x para o qual a função f(x) = x*x - 3x + 4, encontre o valor máximo .
- Assumir que x [-10, +10]
- Codificar X como vetor binário
- Criar uma população inicial com 4  indivíduos  (pode usar mais para testar até 30) 
- Aplicar Mutação com taxa de 1%
- Aplicar Crossover com taxa de 70%
- Usar seleção por torneio.
- Usar 5  gerações. ( pode usar mais para testar até 20) 

#### Requisitos
1. Biblioteca random
2. execute o arquivo main.py
```python
python main.py
```
  2.1 Caso deseje a saída em um arquivo de log
  `python main.py > log.txt`

  * Saída terminal
    
    
```
    **********************ALGORÍTMO GENÉTICO*************************
    -----------------------------------------------------------------
     Execução do algorítmo genético para maximizar a função 'x²-3x+4'
     com as seguintes definições:

     limite inferior .............................-10 
     limite superior ..............................10
     população inicial .............................4
     taxa de mutacao .............................1.0%
     taxa de crossOver ..........................70.0%
     quant. gerações ...............................5

    
     Deseja alterar algum valor? (S/N):
```
    
3. Altere os valores default selecionando 's' e dando enter, ou pressione ENTER para executar com os valores pré-definidos
4. Caso opte por alterar algum valor, basta seguir o menu:

```
Entre com o novo limite inferior ou ENTER para continuar com -10:
Entre com o novo limite superior ou ENTER para continuar com 10:
Entre com o nova população inicial ou ENTER para continuar com 4:
Entre com a nova taxa de mutação ou ENTER para continuar com 1.0%:
Entre com a nova taxa de crossover ou ENTER para continuar com 70.0%:
Entre com a nova quantidade de gerações ou ENTER para continuar com 5 gerações:
```
  * Caso não deseje alterar algum valor basta apertar enter
  
5. O programa inicia com uma população inicial
```
População inicial com 5 indivíduos
----------------------------------
| -3  |  -00011  |
|  8  |  +01000  |
| -11 |  -01011  |
| -2  |  -00010  |
| 15  |  +01111  |
```
6. E já resolve a função com os valores da população inicial selecionando o melhor resultado
```
resolvendo f(-3 ) = 22
resolvendo f( 8 ) = 44
resolvendo f(-11) = 158
resolvendo f(15 ) = 184

para a 1ª geração, o indivíduo mais apto é 15, pois seu resultado é 184
Logo 15 passa a ser o novo melhor valor
```
7. Encontra os pais através de torneio realizado entre 2 indivíduos da população
  * O torneio pega 2 indivíduos de forma aleatória, retornando o melhor entre eles
```
Os pais selecionados foram
  8  |     ['+', '0', '1', '0', '0', '0']     
 15  |     ['+', '0', '1', '1', '1', '1']
```
8. Sorteia um número, se estiver dentro da taxa de crossover para cada um dos pais, o crossover é realizado
  - Ex: taxa de crossover é 70% e o número sorteado foi 53
  - Então define o ponto de corte de forma aleatória entre 0 e o tamanho em bits do indivíduo:
  - É gerado dois filhos, trocando os bits após o ponto de corte
```
-----------------------------
          crossover
-----------------------------
Ponto do corte definido em  2
pai ..............8|['+', '0', '1', '0', '0', '0']
mae .............15|['+', '0', '1', '1', '1', '1']
primeiro filho ..15|['+', '0', '1', '1', '1', '1']
segundo filho ....8|['+', '0', '1', '0', '0', '0']
```
  - Caso o valor do filho seja maior que os limites, os filhos são os próprios limites
  ```
  -----------------------------
          crossover
-----------------------------
Ponto do corte definido em  4
**Estourou o limite, ajustando para o máximo**
pai .............15|['+', '0', '1', '1', '1', '1']
mae .............20|['+', '1', '0', '1', '0', '0']
primeiro filho ..12|['+', '0', '1', '1', '0', '0']
segundo filho ...20|['+', '1', '0', '1', '0', '0']
  ```
  - Se o número sorteado for maior que 70% não é realizado o crossover e os filhos são identicos aos pais
  
  `Não ocorreu crossover`

9. É realizado um novo sorteio, dessa vêz para causar alguma mutação:
  * Se ocorrer a mutação em algum indivíduo, é selecionado algum bit aleatório, e seu valor é invertido
```
-----------------------------
            mutação
-----------------------------
Trocando o 2º BIT do 1º filho
['+', '0', '0', '0', '1']
trocando 0 por 1
['+', '1', '0', '0', '1']
```
  * Caso estoure o limite, o próprio limite é retornado
10. É criada uma nova população com os novos indivíduos
11. Essa tarefa é repetida de acordo com o número de gerações
```
para a 5ª geração, o indivíduo mais apto é -10, pois seu resultado é 134

Logo o melhor valor continua sendo -10

================================================
O resultado final é -10, pois seu retorno é 134
```