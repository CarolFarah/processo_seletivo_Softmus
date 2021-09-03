# Desafios explicados e exemplificados do processo seletivo Softmus Tecnologia - 03/09/2021
Algoritmos pertinentes a entrega do desafio sugerido pela Softmus Tecnologia para apreciação de gestores e analistas.

Desenvolvido por: Ana Carolina de Oliveira Farah / e-mail: anacarolfarah@gmail.com

# Descrição
Abaixo segue uma lista de exercícios utilizados para avaliar o conhecimento do candidato.
Alguns tópicos abordarão a base da linguagem python bem como lógica de programação e
estrutura de dados.
Caso não consiga terminar um exercício específico, a tentativa será avaliada.

# ESTRUTURA DE DADOS

## Exercício 1
Abaixo segue uma lista de exercícios utilizados para avaliar o conhecimento do candidato.
Alguns tópicos abordarão a base da linguagem python bem como lógica de programação e
estrutura de dados.
Caso não consiga terminar um exercício específico, a tentativa será avaliada.

## Regras
1. Criar código de exemplo para cada exercício que exige código separadamente;
2. Publicá-los em um repositório público e compartilhá-lo para ser avaliado.
a. Prover readme de como executar os códigos compartilhados
3. As questões que correspondem a respostas dissertativas podem ser enviadas por
e-mail junto com o link do repositório.

## ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) `RESPOSTA`
Neste exercício, opto por construir duas versões para avaliação também da lógica e seus recursos.

![#c5f015](https://via.placeholder.com/15/1589F0/000000?text=+) `VERSÃO 1`

![alt text](https://i.imgur.com/DDGKpwA.png)

![#c5f015](https://via.placeholder.com/15/1589F0/000000?text=+) `SAÍDA`

![alt text](https://i.imgur.com/X6OolPa.png)

![#1589F0](https://via.placeholder.com/15/c5f015/000000?text=+) `VERSÃO 2`

![alt text](https://i.imgur.com/IAClP7K.png)

![#1589F0](https://via.placeholder.com/15/c5f015/000000?text=+) `SAÍDA`

![alt text](https://i.imgur.com/Nvzfn8A.png)

## Exercício 2
Explique com suas palavras os conceitos FIFO (First-In First-Out) e LIFO (Last-In
First-Out).

## ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) `RESPOSTA`
- FIFO (First-In First-Out) => É o conceito de fila: o primeiro elemento a entrar em uma sequência é o primeiro a sair.

- LIFO (Last-In First-Out) => É o conceito de pilha: o primeiro elemento a entrar em uma sequência é o último a sair.

## Exercício 3
Crie um script python que mostre um array com o nome do país e sua capital. Crie
métodos que ordenem a lista pelo nome do país e pelo nome da capital. Adicione
pelo menos 8 entradas no array.

## ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) `RESPOSTA`
Optei por criar uma função contendo os métodos, pois tive dúvida no entendimento do enunciado e gostaria de atingir o objetivo esperado.

![alt text](https://i.imgur.com/PCPoCAu.gif)
![alt text](https://i.imgur.com/FCW0COc.png)

![#1589F0](https://via.placeholder.com/15/c5f015/000000?text=+) `SAÍDA`

![alt text](https://i.imgur.com/0HiFIvK.gif)
![alt text](https://i.imgur.com/daF1GQF.png)

# LÓGICA DE PROGRAMAÇÃO

## Exercício 1
Um atleta que mantém meticulosos registros de suas caminhadas. Durante sua
última caminhada de exatamente P passos, para cada passo foi anotado se ele era
subida S ou descida D. As caminhadas sempre começam e terminam no nível do
mar, e cada passo para cima ou para baixo representa 1 unidade na alteração da
altitude. Considere os seguintes termos:
a. Uma montanha é uma sequência de passos consecutivos acima do nível do
mar, começando com um passo acima do nível do mar e terminando com um
passo até o nível do mar.
b. Um vale é uma sequência de passos consecutivos abaixo do nível do mar,
começando com um passo abaixo do nível do mar e terminando com um
passo até o nível do mar.

Dada uma sequência de passos de subida ou descida durante uma caminhada,
imprima o número de vales percorridos durante a caminhada.

Exemplo:
P = 8 passos = [DDSSSSDD]
O atleta primeiro entrou em um vale 2 unidades abaixo, então ele subiu uma
montanha 2 unidades acima, chegando no nível do mar no final da caminhada.

Descrição da Função:
Complete a função contandoVales com os seguintes parâmetros:
- int passos: o número de passos na caminhada (passos=9)
- string caminho: a descrição da caminhada (caminho=“SSDDDSSSS”)

Constraints:
- 2 <= passos <= 10
- caminho[i] ∈ {SD}
Exemplo de Entrada:
passos=8
caminho=SDDDSDSS

Exemplo de Saída:
1

Explicação:
Se representarmos _ como nível do mar, um passo acima como /, um passo abaixo
como \, a caminhada do exemplo de entrada acima poderia ser desenhada da seguinte
forma:
_/\ _
\ /
\/\/

Exercício:
Crie uma função que receba como parâmetro os passos e o caminho e retorne a
quantidade de vales percorridos.
Casos de Teste:
passos=12
caminho=DDUUDDUDUUUD
retorno=2
passos=10
caminho=DUDDDUUDUU
retorno=2
passos=10
caminho=UDDDUDUDUU
retorno=1
passos=100
caminho=DUDUUUUUUUUDUDDUUDUUDDDUUDDDDDUUDUUUUDDDUUUUUUUD
DUDUDUUUDDDDUUDDDUDDDDUUDDUDDUUUDUUUDUUDUDUDDDDDDDDD

## ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) `RESPOSTA`

![#c5f015](https://via.placeholder.com/15/1589F0/000000?text=+) `VERSÃO 1`

![alt text](https://i.imgur.com/VNhjp9I.png)

![#1589F0](https://via.placeholder.com/15/c5f015/000000?text=+) `VERSÃO 2`
- Versão com uma única variável

![alt text](https://i.imgur.com/gVecnDU.png)

# INFORMAÇÕES COMPLEMENTARES 

Os códigos estão individualmente lançados em arquivos de extensão ".py", com exceção da resposta teórica do exercício 2 de Estrutura de Dados, lançado em bloco de notas. Também há um arquivo de extensão ".ipynb" que se trata da plataforma onde os algoritmos foram desenvolvidos sequencialmente.

# EXECUÇÃO DOS CÓDIGOS

- Efetue o download deste repositório
- Execute os arquivos de extensão ".py" no console do PyCharm
- Abra o arquivo bloco de notas utilizando Notepad nativo do Windows, notepad++ ou bloco de notas nativo do sistema Linux
- Execute o arquivo de extensão ".ipynb" no sistema do Google Collab

# DOWNLOADS E ACESSO

- Google Collab: https://colab.research.google.com/
- JetBrains PyCharm: https://www.jetbrains.com/pt-br/pycharm/download/
