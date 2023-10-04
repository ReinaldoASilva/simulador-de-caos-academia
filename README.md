# README - Simulação de Academia

Este código em Python é uma simulação básica de uma academia com usuários que pegam e devolvem halteres de forma aleatória. O objetivo é demonstrar o conceito de caos na academia, ou seja, a proporção de halteres que não estão no local correto.

## Funcionalidades do Código

- Classe Academia: representa a academia e possui os seguintes métodos:
  - `__init__()`: inicializa a academia com a criação dos halteres e porta halteres.
  - `reiniciar_o_dia()`: reinicia o dia na academia, colocando todos os halteres de volta nos seus respectivos lugares.
  - `listar_halteres()`: retorna uma lista dos halteres disponíveis para uso.
  - `listar_espacos()`: retorna uma lista dos espaços vazios nos porta halteres.
  - `pegar_haltere(peso)`: pega um halter de determinado peso da academia.
  - `devolver_halter(pos, peso)`: devolve um halter de determinado peso para a academia.
  - `calcular_caos()`: calcula a proporção de halteres fora do lugar na academia.

- Classe Usuário: representa um usuário da academia e possui os seguintes métodos:
  - `__init__(tipo, academia)`: inicializa o usuário com um tipo (normal ou bagunçeiro) e a academia em que ele treina.
  - `iniciar_treino()`: inicia o treino do usuário, escolhendo um halter de forma aleatória da academia.
  - `finalizar_treino()`: finaliza o treino do usuário, devolvendo o halter para a academia de forma aleatória.

- Simulação:
  - Criação da academia e inicialização dos usuários.
  - Execução de 50 iterações, em cada uma reiniciando o dia na academia e realizando o treino dos usuários.
  - Cálculo da proporção de halteres fora do lugar em cada iteração.
  - Visualização da distribuição da proporção de caos em um gráfico utilizando a biblioteca seaborn.

## Execução do Código

Para executar o código, basta copiá-lo para um ambiente Python e rodar. Certifique-se de ter a biblioteca seaborn instalada para a visualização do gráfico. Caso não a tenha instalada, utilize o seguinte comando para instalar:

```
pip install seaborn
```

## Resultados

O código irá simular o treino dos usuários na academia e calcular a proporção de halteres fora do lugar em cada iteração. Ao final, será exibido um gráfico com a distribuição da proporção de caos ao longo das iterações.

O gráfico gerado permite visualizar a variação do caos na academia ao longo das iterações, fornecendo uma ideia da estabilidade do ambiente. Quanto menor a proporção de halteres fora do lugar, mais organizada está a academia.

## Nota

Este código é apenas uma simulação básica, com fins didáticos, e não representa necessariamente a realidade de uma academia. É importante adaptar e ajustar o código de acordo com suas necessidades e requisitos específicos.