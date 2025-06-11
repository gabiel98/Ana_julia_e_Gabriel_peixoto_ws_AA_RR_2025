# Análise do Algoritmo Insertion Sort

## Objetivo
Implementar e analisar o algoritmo de ordenação Insertion Sort, avaliando-o com base em:
- Tempo de execução
- Tamanho da entrada

## Algoritmos Implementados
- Insertion Sort
- Merge Sort

## Tipos de entrada geradas

- Ordenado crescente (`sorted`)
- Ordenado decrescente (`reverse`)
- Aleatório (`random`)

## Estrutura de Diretórios

- Algoritmos :
     - insertion_sort.c
     - merge_sort.c
- Entradas : Entradas geradas como sorted, random e reverse entre 1000, 10000, 100000, 500000, 1000000, 2000000, 3000000;
- Graficos :
     - graficos_tempo: tempo_aleatório.png, tempo_decrescente.png, tempo_ordenado.png;
     - graficos_tempo_estimado : tempo_estimado_aleatório.png, tempo_estimado_decrescente.png, tempo_estimado_ordenado.png;
- Resultados:
     - resultados.csv : Resultados com entrada de até 3000000
- Utils:
     - gerar_entradas.c : Gerador de entradas
     - medir_performance.c : Medir a Performance

## Como Executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/A-juli07/Analise_Comparacao_Ordenacao_AnaliseDeAlgoritmos.git

2. **Gerar arquivos de entrada**
   ```bash
   gcc utils/gerar_entradas.c -o gerar_entradas
   ./gerar_entradas

3. **Executar os algoritmos e salvar os dados**
   ```bash
   gcc utils/medir_performance.c algoritmos/*.c -o medir
   ./medir

4. **Gerar os gráficos (requer Python)**
   ```bash
   pip install pandas matplotlib
   python graficos/graficos.py

## Ambiente de Execução
Os testes foram executados em um ambiente contendo Sistema Operacional Windows 11 Pro 64 bits. Nossa plataforma de testes foi um Notebook Lenovo Gamer 3i 82CG0005BR, processador de 7º geração Intel Core i7-10750H de 2.60GHz até 5.00GHz, placa de vídeo NVidia Geforce GTX1650 de 4GB GDDR6, memória RAM de 8GB DDR4, SSD de 512GB, tela de 15.6 polegadas.

## Saída

Arquivo CSV com resultados: resultados/resultados.csv

Gráficos gerados na pasta graficos/graficos_tempo:

- tempo_aleatório.png
- tempo_decrescente.png
- tempo_ordenado.png

Gráficos gerados na pasta graficos/graficos_tempo_estimado:

- tempo_estimado_aleatório.png
- tempo_estimado_decrescente.png
- tempo_estimado_ordenado.png

## Insights dos Resultados


### Tempo Estimado – Vetor Ordenado

* **Insertion Sort** apresentou desempenho significativamente melhor nesse cenário.
* Como esperado, no **melhor caso**, o `Insertion Sort` executa apenas comparações mínimas, com custo linear $O(n)$.
* Já o **Merge Sort**, mesmo com o vetor ordenado, mantém sua complexidade $O(n \log n)$, já que realiza chamadas recursivas e mesclagens de qualquer forma.
* Portanto, **para vetores ordenados**, o `Insertion Sort` é mais eficiente em tempo e recurso.

---

### Tempo Estimado – Vetor em Ordem Decrescente

* **Insertion Sort** teve o pior desempenho possível, com crescimento exponencial de tempo. Isso confirma sua complexidade $O(n^2)$ no pior caso.
* Já o **Merge Sort** manteve um crescimento log-linear estável, como esperado para $O(n \log n)$, demonstrando maior robustez.
* Resultado: **Merge Sort supera completamente o Insertion Sort** nesse cenário.

---

### Tempo Estimado – Vetor Aleatório

* **Insertion Sort** apresentou novamente desempenho quadrático, refletindo o comportamento médio do algoritmo.
* **Merge Sort** teve desempenho consistente e previsível, com vantagem crescente à medida que o tamanho do vetor aumenta.
* **Conclusão**: Para **dados aleatórios**, o Merge Sort é uma escolha claramente superior.

---

### Tempo de Execução Real (Escala Logarítmica)

As imagens com escala logarítmica reforçam os resultados anteriores:

* O **tempo real de execução** para o `Insertion Sort` cresce rapidamente nos casos decrescente e aleatório.
* O **Merge Sort** cresce de forma mais controlada e consistente.
* A diferença de tempo entre os algoritmos se **acentua com vetores maiores**, demonstrando que **o Merge Sort escala melhor**.

---

## Análise Iterativa da Complexidade

### Merge Sort

#### Pseudocódigo simplificado:

```c
Função MERGE_SORT(arr, l, r, comparacoes):
    Se l < r:
        m ← l + (r - l) / 2
        MERGE_SORT(arr, l, m, comparacoes)
        MERGE_SORT(arr, m + 1, r, comparacoes)
        MERGE(arr, l, m, r, comparacoes)

Função MERGE(arr, l, m, r, comparacoes):
    n1 ← m - l + 1
    n2 ← r - m

    Criar vetores L[0...n1-1] e R[0...n2-1]

    Para i de 0 até n1 - 1:
        L[i] ← arr[l + i]

    Para j de 0 até n2 - 1:
        R[j] ← arr[m + 1 + j]

    i ← 0, j ← 0, k ← l

    Enquanto i < n1 e j < n2:
        comparacoes ← comparacoes + 1
        Se L[i] ≤ R[j]:
            arr[k] ← L[i]
            i ← i + 1
        Senão:
            arr[k] ← R[j]
            j ← j + 1
        k ← k + 1

    Enquanto i < n1:
        arr[k] ← L[i]
        i ← i + 1
        k ← k + 1

    Enquanto j < n2:
        arr[k] ← R[j]
        j ← j + 1
        k ← k + 1
```
---

#### Recorrência:

$$
T(n) = 2T\left(\frac{n}{2}\right) + cn
$$


### Iterando a Recorrência:

***Não esta responsivo no celular***

1. **1ª iteração:**

$$
T(n) = 2T\left(\frac{n}{2}\right) + cn
$$

2. **2ª iteração:**

$$
\begin{aligned}
T(n) &= 2\left[2T\left(\frac{n}{4}\right) + c \cdot \frac{n}{2}\right] + cn \\
     &= 4T\left(\frac{n}{4}\right) + 2c \cdot \frac{n}{2} + cn \\
     &= 4T\left(\frac{n}{4}\right) + 2cn
\end{aligned}
$$

3. **kª iteração:**

$$
T(n) = 2^k T\left(\frac{n}{2^k}\right) + kcn
$$

4. **Parar quando** $\frac{n}{2^k} = 1 \Rightarrow k = \log_2 n$

5. **Substituindo:**

$$
T(n) = n \cdot T(1) + cn \cdot \log_2 n
$$



### Conclusão:

* **Melhor caso:** $O(n \log n)$
* **Pior caso:** $O(n \log n)$
  *(igual, pois o algoritmo sempre executa o mesmo número de divisões e mesclagens)*

---

### Insertion Sort

#### Pseudocódigo simplificado:

```c
for (int i = 1; i < n; i++) {
    int chave = arr[i];
    int j = i - 1;
    while (j >= 0 && arr[j] > chave) {
        arr[j + 1] = arr[j];
        j--;
    }
    arr[j + 1] = chave;
}
```


### Pior Caso (vetor decrescente)

Cada elemento precisa ser comparado e movido por todo o subvetor anterior:

1. Iteração 1: 1 comparação
2. Iteração 2: 2 comparações
3. ...
4. Iteração $i$: $i$ comparações

$$
T(n) = 1 + 2 + 3 + \dots + (n - 1) = \sum_{i=1}^{n-1} i = \frac{n(n - 1)}{2}
$$


### Melhor Caso (vetor ordenado)

O `while (arr[j] > chave)` nunca entra, então só há uma comparação por iteração:

$$
T(n) = n - 1
$$


### Conclusão:

* **Melhor caso:** $O(n)$
* **Pior caso:** $O(n^2)$


## Tabela Comparativa

* **Insertion Sort** é preferível apenas para vetores pequenos ou já ordenados.
* **Merge Sort** é mais eficiente e confiável para grandes volumes de dados e cenários onde a ordem dos dados é imprevisível.
* A análise confirma as complexidades teóricas:

| Algoritmo          | Melhor Caso   | Caso Médio    | Pior Caso     |
| ------------------ | ------------- | ------------- | ------------- |
| **Insertion Sort** | $O(n)$        | $O(n^2)$      | $O(n^2)$      |
| **Merge Sort**     | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ |


| Algoritmo      | Melhor Caso | Pior Caso          | Comparações   | Complexidade                             |
| -------------- | ----------- | ------------------ | ------------- | ---------------------------------------- |
| **Insertion**  | $n - 1$     | $\frac{n(n-1)}{2}$ | $O(n^2)$      | Melhor: $O(n)$ <br> Pior/Médio: $O(n^2)$ |
| **Merge Sort** | $n\log n$ | $n\log n$        | $O(n \log n)$ | Sempre $O(n \log n)$                     |


## Slide


## Autores

Ana Julia Vieira P.A. Costa e
Gabriel Menezes
