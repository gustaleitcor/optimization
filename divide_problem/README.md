# Optimization Problem

## Variáveis:

- Seja \( x_{ij} \) a variável de decisão para os índices \( i \) e \( j \).

## Parâmetros:

- \( N \): Limite superior para o índice \( i \).
- \( n \): Limite superior para o índice \( j \).
- \( W_t \): Peso total.
- \( i_0 \): Limite inferior para o índice \( i \) na segunda restrição.
- \( j_0 \): Parâmetro que define o intervalo para \( j \) na segunda restrição.
- \( n_0 \): Parâmetro que define o intervalo para \( j \) na segunda restrição.

## Modelagem Matemática

### Objetivo

Minimizar a soma das variáveis de decisão:

$$
\text{Minimizar} \quad \sum_{i=0}^{N} \sum_{j=0}^{n} x_{ij}
$$

### Sujeito a

1. A soma das variáveis ponderadas é igual a \( W_t \):

$$
\sum_{i=0}^{N} \sum_{j=0}^{n} \left( \frac{W_t}{2^i} \right) x_{ij} = W_t
$$

2. Para cada \( j \) no intervalo \([2 \cdot j_0, 2^{n_0-n})\), a soma de \( x_{ij} \) de \( i = i_0 + 1 \) a \( N \) é igual a 0:

$$
\sum_{i=i_0+1}^{N} x_{ij} = 0
$$

3. As variáveis \( x_{ij} \) estão limitadas entre 0 e 1:

$$
0 \leq x_{ij} \leq 1
$$

## Resumo do Problema

Este problema de otimização visa minimizar a soma das variáveis de decisão \( x_{ij} \) sob duas restrições. A primeira restrição garante que a soma ponderada de \( x_{ij} \) seja igual a um peso total \( W_t \). A segunda restrição garante que, para um intervalo específico de \( j \), a soma de \( x_{ij} \) de \( i = i_0 + 1 \) a \( N \) seja zero. Todas as variáveis de decisão estão limitadas entre 0 e 1.

## Exemplo

Um exemplo será fornecido aqui, demonstrando a configuração e a solução deste problema usando um solucionador de otimização específico.

