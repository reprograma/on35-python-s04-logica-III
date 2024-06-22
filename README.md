<h1 align="center">
  <img src="assets/reprograma-fundos-claros.png" alt="logo reprograma" width="500">
</h1>

# Lógica III

On35 | Semana 4 | 2024 | Agnes Ignácio

![enter image description here](https://64.media.tumblr.com/49add96a62291bec5e33f2078be50d39/tumblr_p5a7qhj1IP1ut0jmvo7_400.gifv)

### Instruções
Antes de começar, vamos organizar nosso setup.
* Fork esse repositório 
* Clone o fork na sua máquina (Para isso basta abrir o seu terminal e digitar `git clone url-do-seu-repositorio-forkado`)
* Entre na pasta do seu repositório (Para isso basta abrir o seu terminal e digitar `cd nome-do-seu-repositorio-forkado`)

### Resumo
O que veremos na aula de hoje?
* Loops
* While
* For
* range()
* break, continue, else
* \+ funções

### Loops
Na programação, um loop é uma estrutura de controle que executa repetidamente um bloco de código, desde que uma condição especificada seja verdadeira. Essa execução repetida continua até que a condição se torne falsa, momento em que o loop termina e o controle passa para a próxima seção do código.

O uso de loops permite que as programadoras automatizem com eficiência tarefas repetitivas, como processar itens em uma coleção ou gerar sequências de números. Essencialmente, os loops facilitam o tratamento de tarefas que exigem ações repetidas, sem a necessidade da programadora escrever cada operação individualmente. Os loops tornam o código mais curto, mais fácil de entender e mais simples de manter, reduzindo assim a redundância na programação e permitindo uma programação mais dinâmica e responsiva.

#### While
O comando while faz com que um conjunto de instruções seja executado enquanto uma condição é atendida. Quando o resultado dessa condição passa a ser falso, a execução do loop é interrompida, como mostra o exemplo a seguir:

```
contador = 0
while (contador < 5):
       print(contador)
       contador   = contador + 1
```
Neste código, enquanto a variável contador, inicializada com 0, for menor do que 5, as instruções das linhas 3 e 4 serão executadas.

Observe que na linha 4 incrementamos o valor da variável contador, de forma que em algum momento seu valor igualará o número 5. Quando isso for verificado na linha 2, o laço será interrompido. Sem esse código, a condição de parada não será atingida, gerando o que é chamado de loop infinito. Evite que isso aconteça, pois leva ao congelamento e finalização da aplicação.

#### While-else
Ao final do while podemos utilizar a instrução else. O propósito disso é executar alguma instrução ou bloco de código ao final do loop, como podemos ver no exemplo a seguir:
```
contador = 0
while (contador < 5):
      print(contador)
      contador = contador + 1
else:
      print("O loop while foi encerrado com sucesso!")
```
Assim como acontece com for/else, declarando o else ao final do while é possível executar um código ao final do loop. Neste caso será impressa a mensagem: “O loop while foi encerrado com sucesso!”.

#### For
O loop for em Python é uma estrutura de controle que permite iterar sobre uma sequência (como uma lista, uma string ou uma faixa de números), executando um bloco de código repetidamente para cada item da sequência. A beleza do loop for está em sua simplicidade e flexibilidade, permitindo ao programador executar tarefas repetitivas com poucas linhas de código.

A sintaxe básica do loop for em Python é direta e consiste na palavra-chave for, seguida de uma variável que representa o item atual da sequência, a palavra-chave in, a sequência sobre a qual iterar, seguida de dois pontos (:). Abaixo disso, o bloco de código indentado será executado para cada item da sequência.

Vamos ver um exemplo simples de como usar o loop for para imprimir todos os números de 0 a 4:
```
for i in range(5):
 print(i)
 ```
 Uma das aplicações mais comuns para o loop for em Python é iterar através dos elementos de uma lista. Isso permite que você manipule ou processe cada elemento individualmente de maneira simples e eficiente. Por exemplo:

```
frutas = ['maçã', 'banana', 'cereja', 'kiwi', 'manga']

for fruta in frutas:
 print(fruta)
```
As strings em Python são sequências imutáveis de caracteres. Utilizando o loop for, podemos percorrer cada caractere de uma string de forma simples e intuitiva. Vejamos um exemplo prático:
```
for char in "Python":
 print(char)
```

### range()
Uma das funções mais poderosas para controlar o loop for é o range(). Com ele, podemos definir exatamente quantas vezes o loop deve executar, fornecendo um controle preciso sobre as nossas iterações.

Por exemplo, se quisermos imprimir os números de 0 a 9, podemos fazer da seguinte forma:
```
for i in range(10):
 print(i)
 ```
 
O range() é extremamente flexível, permitindo definir não só o ponto de partida e de término das iterações, mas também o passo entre elas. Por exemplo, range(1, 10, 2) irá gerar os números 1, 3, 5, 7, 9.

### break, continue, else
Para ter um controle ainda maior sobre a execução dos loops, Python nos oferece as palavras-chave break, continue e else. Cada uma dessas palavras-chave tem um propósito específico que pode enriquecer a lógica dos nossos programas.

* Break: Utilizado para interromper imediatamente o loop, independentemente de sua condição de término.
* Continue: Pula a iteração atual e continua com a próxima iteração do loop.
* Else: Executado somente quando o loop for concluído sem interrupções pelo break.

Veja como podemos utilizar o break e o else em um exemplo prático:
```
for num in range(1, 11):
 print(num)
 if num == 5:
  break
else:
 print("Loop concluído com sucesso!")
 ```
Neste exemplo, o loop será interrompido quando o num for igual a 5, e a mensagem do else não será exibida, pois o loop não concluiu todos os passos previstos inicialmente.

### + Funções
* len(): retorna um int do tamanho de um objeto iterável (list, tuple, string, dictionary...)

* .append(): adiciona um item ao final da lista.
 
* .update(): adiciona uma nova chave-valor ao dicionário.

* .values(): retorna uma lista apenas com os valores de um dicionário.


### Links úteis
* [while](https://www.devmedia.com.br/python-estrutura-de-repeticao-while/38546)
* [for + range + break, continue, else](https://didatica.tech/loop-for-em-python-aprenda-a-dominar-com-exemplos-praticos/)
* [len()](https://didatica.tech/loop-for-em-python-aprenda-a-dominar-com-exemplos-praticos/)
* [.append()](https://www.w3schools.com/python/ref_list_append.asp)
* [.update()](https://www.w3schools.com/python/ref_dictionary_update.asp)
* [.values()](https://www.w3schools.com/python/ref_dictionary_values.asp)
