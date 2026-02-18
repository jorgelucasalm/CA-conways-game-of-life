# Simulação do Canhão de Planadores – Jogo da Vida

Este projeto implementa uma simulação do Jogo da Vida de Conway, com
foco no Canhão de Planadores de Gosper.

A aplicação foi desenvolvida em Python, utilizando as bibliotecas NumPy
e Matplotlib para cálculo e visualização gráfica.

## Sobre o Projeto

O Jogo da Vida é um autômato celular bidimensional onde cada célula pode
estar viva ou morta. A evolução do sistema ocorre a partir de regras
simples aplicadas aos oito vizinhos de cada célula:

-   Uma célula viva morre se tiver menos de 2 ou mais de 3 vizinhos.
-   Uma célula viva sobrevive com 2 ou 3 vizinhos.
-   Uma célula morta nasce se tiver exatamente 3 vizinhos.

## Neste projeto:

-   O grid é inicializado com quatro Canhões de Planadores.
-   Eles são posicionados simetricamente nos quatro quadrantes.
-   Os planadores gerados se movem em direção ao centro.
-   A simulação é exibida como uma animação.

## Conceitos Envolvidos

-   Autômatos Celulares
-   Emergência de comportamento complexo
-   Periodicidade
-   Colisão de padrões
-   Computação baseada em colisões

O Canhão de Gosper demonstra que o Jogo da Vida pode gerar crescimento
infinito a partir de uma configuração finita.

## Tecnologias Utilizadas

-   Python 3
-   NumPy
-   Matplotlib

## Como Executar

1.  Instale as dependências:

```
pip install numpy matplotlib
```

2.  Execute o arquivo:

```
python index.py
```

Uma janela será aberta mostrando a animação da simulação.

## Estrutura

-   index.py → Código principal da simulação
-   Artigo em PDF → Documento explicando a fundamentação teórica e
    análise do experimento

## Referência Teórica

O projeto é baseado no Jogo da Vida, criado por John Conway, e utiliza o
padrão conhecido como Canhão de Planadores de Gosper, descoberto por
Bill Gosper.
