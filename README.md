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

Para cada entrada é feita somente 1 repetição;

## Estrutura de Diretórios

- Algoritmos :
     - insertion_sort.c
     - merge_sort.c
- Entradas : Entradas geradas como sorted, random e reverse entre 1000, 10000, 100000, 500000, 1000000, 2000000;
- Graficos :
     - graficos_tempo: tempo_aleatório.png, tempo_decrescente.png, tempo_ordenado.png;
     - graficos_tempo_estimado : tempo_estimado_aleatório.png, tempo_estimado_decrescente.png, tempo_estimado_ordenado.png;
- Resultados:
     - resultados.csv : Resultados com entrada de até 2000000
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
Os testes foram executados em um ambiente contendo:

* **Sistema Operacional**: Windows 11 Pro 64 bits
* **Plataforma de Testes**: Notebook Lenovo Gamer 3i 82CG0005BR
* **Especificações**:

  * Processador: Intel Core i7-10750H (2.60GHz até 5.00GHz)
  * Placa de Vídeo: NVidia Geforce GTX1650 (4GB GDDR6)
  * Memória RAM: 8GB DDR4
  * SSD: 512GB

## Saída

* **Arquivo CSV com resultados**: `resultados/resultados.csv`
* **Gráficos gerados**:

  * **Pasta `graficos/graficos_tempo`**:

    * tempo\_aleatório.png
    * tempo\_decrescente.png
    * tempo\_ordenado.png
  * **Pasta `graficos/graficos_tempo_estimado`**:

    * tempo\_estimado\_aleatório.png
    * tempo\_estimado\_decrescente.png
    * tempo\_estimado\_ordenado.png

## Insights dos Resultados


### Tempo Estimado – Vetor Ordenado

<p align="center">
  <img src="https://github.com/gabiel98/Ana_julia_e_Gabriel_peixoto_ws_AA_RR_2025/blob/main/graficos/graficos_tempo_estimado/tempo_estimado_ordenado.png" alt="Gráfico 1" width="48%" style="display: inline-block;">
  <img src="https://github.com/gabiel98/Ana_julia_e_Gabriel_peixoto_ws_AA_RR_2025/blob/main/graficos/graficos_tempo/tempo_ordenado.png" alt="Gráfico 2" width="48%" style="display: inline-block;">
</p>
<p align="center">
  <span style="display: inline-block;">1 comparação é igual a 1ms(1 clock)</span>
  <span style="display: inline-block;">Tempo de clock real.</span>
</p>


* 1 comparação é igual a 1ms(1 clock). * Tempo de clock real.
* **Insertion Sort** tem desempenho muito melhor com vetores ordenados, pois realiza poucas comparações, com custo linear O(n), o que é refletido no gráfico.
* No **melhor caso**, o **Insertion Sort** aproveita a ordem do vetor e mantém o tempo de execução baixo.
* Já o **Merge Sort**, mesmo com vetor ordenado, mantém sua complexidade O(n log n) devido às chamadas recursivas e mesclagens, resultando em maior tempo de execução.
* **Conclusão:** Para vetores ordenados, **Insertion Sort** é mais eficiente em tempo e recursos.

---

### Tempo Estimado – Vetor em Ordem Decrescente

<p align="center">
  <img src="https://github.com/gabiel98/Ana_julia_e_Gabriel_peixoto_ws_AA_RR_2025/blob/main/graficos/graficos_tempo_estimado/tempo_estimado_decrescente.png" alt="Gráfico 1" width="48%" style="display: inline-block;">
  <img src="https://github.com/gabiel98/Ana_julia_e_Gabriel_peixoto_ws_AA_RR_2025/blob/main/graficos/graficos_tempo/tempo_decrescente.png" alt="Gráfico 2" width="48%" style="display: inline-block;">
</p>

* O *Insertion Sort* teve o pior desempenho possível, com tempo de execução exponencial, confirmando sua complexidade $O(n^2)$ no pior caso.
* O *Merge Sort* manteve um crescimento log-linear estável, como esperado para $O(n \log n)$, demonstrando maior robustez.
* **Resultado**: O *Merge Sort* supera completamente o *Insertion Sort* nesse cenário.

---

### Tempo Estimado – Vetor Aleatório

<p align="center">
  <img src="https://github.com/gabiel98/Ana_julia_e_Gabriel_peixoto_ws_AA_RR_2025/blob/main/graficos/graficos_tempo_estimado/tempo_estimado_aleatório.png" alt="Gráfico 1" width="48%" style="display: inline-block;">
  <img src="https://github.com/gabiel98/Ana_julia_e_Gabriel_peixoto_ws_AA_RR_2025/blob/main/graficos/graficos_tempo/tempo_aleatório.png" alt="Gráfico 2" width="48%" style="display: inline-block;">
</p>

* **Insertion Sort** apresentou novamente desempenho quadrático, refletindo o comportamento médio do algoritmo.
* **Merge Sort** teve desempenho consistente e previsível, com vantagem crescente à medida que o tamanho do vetor aumenta.
* **Conclusão**: Para **dados aleatórios**, o Merge Sort é uma escolha claramente superior.

---

### Tempo de Execução Real (Escala Logarítmica)

As imagens com escala logarítmica reforçam os resultados anteriores:

* O **tempo real de execução** para o `Insertion Sort` cresce rapidamente nos casos decrescente e aleatório.
* O **Merge Sort** cresce de forma mais controlada e consistente.
* A diferença de tempo entre os algoritmos se **acentua com vetores maiores**, demonstrando que **o Merge Sort escala melhor**.


## Análise Iterativa da Complexidade

### Insertion Sort

#### Pseudocódigo:

```c
Algoritmo InsertionSort(A):
    Para i de 1 até tamanho(A) - 1 faça:
        chave ← A[i]                   
        j ← i - 1                       
        Enquanto j ≥ 0 e A[j] > chave faça:
            A[j + 1] ← A[j]            
            j ← j - 1                  
        FimEnquanto
        A[j + 1] ← chave               
FimAlgoritmo
```


### Pior Caso (vetor decrescente)

Cada elemento precisa ser comparado e movido por todo o subvetor anterior:

1. Iteração 1: 1 comparação
2. Iteração 2: 2 comparações
3. ...
4. Iteração $i$: $i$ comparações

$$
T(n) = 1 + 2 + 3 + \dots + (n - 1) = \sum_{i=1}^{n-1} i
$$

Agora, vamos resolver essa soma. A soma dos primeiros $n-1$ números inteiros é uma soma aritmética e tem a fórmula:

$$
S = \frac{n(n - 1)}{2}
$$

Portanto, o tempo total de execução no **pior caso** será:

$$
T(n) = \frac{n(n - 1)}{2}
$$

$$
T(n)= \frac{n^2 - n}{2}
$$

### Melhor Caso (vetor ordenado)

O `while (arr[j] > chave)` nunca entra, então só há uma comparação por iteração:

$$
T(n) = n - 1
$$


### Conclusão:

* **Melhor caso:** $O(n)$
* **Pior caso:** $O(n^2)$

---

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

Claro! Aqui estão mais iterações da resolução da recorrência $T(n) = 2T\left(\frac{n}{2}\right) + cn$, para que você possa visualizar o padrão que surge a cada iteração.

### Iterações Adicionais

#### 1ª Iteração:

$$
T(n) = 2T\left(\frac{n}{2}\right) + cn
$$

#### 2ª Iteração:

Substituímos $T\left(\frac{n}{2}\right)$ por $2T\left(\frac{n}{4}\right) + c\frac{n}{2}$:

$$
T(n) = 2\left[2T\left(\frac{n}{4}\right) + c \cdot \frac{n}{2}\right] + cn
$$

$$
T(n) = 4T\left(\frac{n}{4}\right) + 2c \cdot \frac{n}{2} + cn
$$

$$
T(n) = 4T\left(\frac{n}{4}\right) + 2cn
$$

#### 3ª Iteração:

Agora, substituímos $T\left(\frac{n}{4}\right)$ por $2T\left(\frac{n}{8}\right) + c \cdot \frac{n}{4}$:

$$
T(n) = 4\left[2T\left(\frac{n}{8}\right) + c \cdot \frac{n}{4}\right] + 2cn
$$

$$
T(n) = 8T\left(\frac{n}{8}\right) + 4c \cdot \frac{n}{4} + 2cn
$$

$$
T(n) = 8T\left(\frac{n}{8}\right) + cn + 2cn
$$

$$
T(n) = 8T\left(\frac{n}{8}\right) + 3cn
$$

#### 4ª Iteração:

Substituímos $T\left(\frac{n}{8}\right)$ por $2T\left(\frac{n}{16}\right) + c \cdot \frac{n}{8}$:

$$
T(n) = 8\left[2T\left(\frac{n}{16}\right) + c \cdot \frac{n}{8}\right] + 3cn
$$

$$
T(n) = 16T\left(\frac{n}{16}\right) + 8c \cdot \frac{n}{8} + 3cn
$$

$$
T(n) = 16T\left(\frac{n}{16}\right) + cn + 3cn
$$

$$
T(n) = 16T\left(\frac{n}{16}\right) + 4cn
$$

#### 5ª Iteração:

Substituímos $T\left(\frac{n}{16}\right)$ por $2T\left(\frac{n}{32}\right) + c \cdot \frac{n}{16}$:

$$
T(n) = 16\left[2T\left(\frac{n}{32}\right) + c \cdot \frac{n}{16}\right] + 4cn
$$

$$
T(n) = 32T\left(\frac{n}{32}\right) + 16c \cdot \frac{n}{16} + 4cn
$$

$$
T(n) = 32T\left(\frac{n}{32}\right) + cn + 4cn
$$

$$
T(n) = 32T\left(\frac{n}{32}\right) + 5cn
$$

### Geralizando o Padrão

Após $k$ iterações, temos a forma geral da recorrência:

$$
T(n) = 2^k T\left(\frac{n}{2^k}\right) + k \cdot cn
$$

### Parando a Recursão

A recursão para quando $\frac{n}{2^k} = 1$, ou seja, $k = \log_2 n$. Substituindo $k = \log_2 n$:

$$
T(n) = 2^{\log_2 n} T(1) + \log_2 n \cdot cn
$$

$$
T(n) = n T(1) + cn \log_2 n
$$

### Passo 2: Conclusão

Sabemos que $T(1)$ é uma constante, então a solução para $T(n)$ será:

$$
T(n) = O(n) + O(n \log n)
$$

Portanto, a **complexidade assintótica** de $T(n)$ é:

$$
T(n) = O(n \log n)
$$


### Conclusão:

* **Melhor caso:** $O(n \log n)$
* **Pior caso:** $O(n \log n)$
  *(igual, pois o algoritmo sempre executa o mesmo número de divisões e mesclagens)*

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
