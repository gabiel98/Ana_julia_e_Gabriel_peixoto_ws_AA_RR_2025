# Análise do Algoritmo Insertion Sort

## Objetivo

Implementar e analisar o algoritmo de ordenação **Insertion Sort**, avaliando-o com base em:

* **Tempo de execução**
* **Tamanho da entrada**

## Algoritmos Implementados

* **Insertion Sort**
* **Merge Sort**

## Tipos de Entrada Geradas

* **Ordenado crescente** (`sorted`)
* **Ordenado decrescente** (`reverse`)
* **Aleatório** (`random`)

## Estrutura de Diretórios

```bash
Algoritmos :
     - insertion_sort.c
     - merge_sort.c
Entradas :
     - Entradas geradas como sorted, random e reverse entre 1000, 10000, 100000, 500000, 1000000, 2000000, 3000000;
Graficos :
     - graficos_tempo: tempo_aleatório.png, tempo_decrescente.png, tempo_ordenado.png;
     - graficos_tempo_estimado: tempo_estimado_aleatório.png, tempo_estimado_decrescente.png, tempo_estimado_ordenado.png;
Resultados:
     - resultados.csv : Resultados com entrada de até 3000000
Utils:
     - gerar_entradas.c : Gerador de entradas
     - medir_performance.c : Medir a Performance
```

## Como Executar

### 1. **Clone o repositório:**

```bash
git clone https://github.com/A-juli07/Analise_Comparacao_Ordenacao_AnaliseDeAlgoritmos.git
```

### 2. **Gerar arquivos de entrada**

```bash
gcc utils/gerar_entradas.c -o gerar_entradas
./gerar_entradas
```

### 3. **Executar os algoritmos e salvar os dados**

```bash
gcc utils/medir_performance.c algoritmos/*.c -o medir
./medir
```

### 4. **Gerar os gráficos (requer Python)**

```bash
pip install pandas matplotlib
python graficos/graficos.py
```

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

* **Insertion Sort** tem desempenho muito melhor com vetores ordenados, pois realiza poucas comparações, com custo linear **O(n)**.
* **Merge Sort** mantém sua complexidade **O(n log n)**, mesmo para vetores já ordenados, devido às chamadas recursivas.
* **Conclusão**: Para vetores ordenados, **Insertion Sort** é mais eficiente.

---

### Tempo Estimado – Vetor em Ordem Decrescente

<p align="center">
  <img src="https://github.com/gabiel98/Ana_julia_e_Gabriel_peixoto_ws_AA_RR_2025/blob/main/graficos/graficos_tempo_estimado/tempo_estimado_decrescente.png" alt="Gráfico 1" width="48%" style="display: inline-block;">
  <img src="https://github.com/gabiel98/Ana_julia_e_Gabriel_peixoto_ws_AA_RR_2025/blob/main/graficos/graficos_tempo/tempo_decrescente.png" alt="Gráfico 2" width="48%" style="display: inline-block;">
</p>

* **Insertion Sort** apresentou desempenho quadrático **O(n^2)** no pior caso.
* **Merge Sort** se manteve estável com **O(n log n)**, mostrando maior robustez.
* **Conclusão**: **Merge Sort** é muito superior em vetores decrescentes.

---

### Tempo Estimado – Vetor Aleatório

<p align="center">
  <img src="https://github.com/gabiel98/Ana_julia_e_Gabriel_peixoto_ws_AA_RR_2025/blob/main/graficos/graficos_tempo_estimado/tempo_estimado_aleatório.png" alt="Gráfico 1" width="48%" style="display: inline-block;">
  <img src="https://github.com/gabiel98/Ana_julia_e_Gabriel_peixoto_ws_AA_RR_2025/blob/main/graficos/graficos_tempo/tempo_aleatório.png" alt="Gráfico 2" width="48%" style="display: inline-block;">
</p>

* **Insertion Sort** apresentou desempenho quadrático, refletindo seu comportamento médio.
* **Merge Sort** teve desempenho mais previsível, com vantagem crescente conforme o tamanho do vetor aumenta.
* **Conclusão**: Para **dados aleatórios**, **Merge Sort** é a melhor escolha.

---

### Tempo de Execução Real (Escala Logarítmica)

* O **tempo real de execução** do **Insertion Sort** cresce rapidamente em vetores maiores e desordenados.
* O **Merge Sort** tem um crescimento mais controlado.
* A diferença de tempo entre os algoritmos aumenta conforme o vetor cresce, mostrando que **Merge Sort** escala melhor.

## Análise Iterativa da Complexidade

### Complexidade Assintótica

#### Merge Sort

##### Pseudocódigo Simplificado:

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

##### Recorrência:

$$
T(n) = 2T\left(\frac{n}{2}\right) + cn
$$

##### Resolução da Recorrência por Substituição:

Para resolver a recorrência $T(n) = 2T\left(\frac{n}{2}\right) + cn$, vamos expandir a recorrência passo a passo:

1. **Primeira Substituição** (para $T(n)$):

$$
T(n) = 2T\left(\frac{n}{2}\right) + cn
$$

2. **Segunda Substituição** (para $T\left(\frac{n}{2}\right)$):

$$
T\left(\frac{n}{2}\right) = 2T\left(\frac{n}{4}\right) + c\left(\frac{n}{2}\right)
$$

Substituindo na equação original:

$$
T(n) = 2\left[2T\left(\frac{n}{4}\right) + c\left(\frac{n}{2}\right)\right] + cn
$$

$$
T(n) = 4T\left(\frac{n}{4}\right) + 2c\left(\frac{n}{2}\right) + cn
$$

$$
T(n) = 4T\left(\frac{n}{4}\right) + cn + cn
$$

3. **Geralmente, após $k$ substituições**:

$$
T(n) = 2^k T\left(\frac{n}{2^k}\right) + k \cdot cn
$$

5. **Parar a Recursão**:

A recursão para quando $\frac{n}{2^k} = 1$, ou seja, $k = \log_2 n$. Substituindo $k = \log_2 n$ na equação:

$$
T(n) = 2^{\log_2 n} T(1) + \log_2 n \cdot cn
$$

$$
T(n) = n T(1) + cn \log_2 n
$$

### Passo 2: Conclusão

Agora, sabemos que $T(1)$ é uma constante, então a solução para $T(n)$ será:

$$
T(n) = O(n) + O(n \log n)
$$

Aqui, $O(n)$ vem de $n T(1)$, e $O(n \log n)$ é o termo dominante. Portanto, podemos concluir que a **complexidade assintótica** de $T(n)$ é:

$$
T(n) = O(n \log n)
$$

---

#### Insertion Sort

##### Pseudocódigo Simplificado:

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

##### Pior Caso (Vetor Decrescente):

No pior caso, cada elemento precisa ser comparado e movido por todo o subvetor anterior:

$$
T(n) = 1 + 2 + 3 + \dots + (n - 1) = \frac{n(n - 1)}{2}
$$

##### Melhor Caso (Vetor Ordenado):

No melhor caso, **Insertion Sort** realiza uma única comparação por iteração:

$$
T(n) = n - 1
$$

##### Complexidade Assintótica:

* **Melhor caso**: **O(n)** (vetor ordenado)
* **Pior caso**: **O(n^2)** (vetor decrescente)
* **Caso médio**: **O(n^2)**

---

## Tabela Comparativa

| Algoritmo          | Melhor Caso     | Caso Médio      | Pior Caso       |
| ------------------ | --------------- | --------------- | --------------- |
| **Insertion Sort** | \$O(n)\$        | \$O(n^2)\$      | \$O(n^2)\$      |
| **Merge Sort**     | \$O(n \log n)\$ | \$O(n \log n)\$ | \$O(n \log n)\$ |

| Algoritmo      | Melhor Caso  | Pior Caso            | Comparações     | Complexidade                                 |
| -------------- | ------------ | -------------------- | --------------- | -------------------------------------------- |
| **Insertion**  | \$n - 1\$    | \$\frac{n(n-1)}{2}\$ | \$O(n^2)\$      | Melhor: \$O(n)\$ <br> Pior/Médio: \$O(n^2)\$ |
| **Merge Sort** | \$n \log n\$ | \$n \log n\$         | \$O(n \log n)\$ | Sempre \$O(n \log n)\$                       |

---

## Autores

Ana Julia Vieira P.A. Costa e Gabriel Menezes
