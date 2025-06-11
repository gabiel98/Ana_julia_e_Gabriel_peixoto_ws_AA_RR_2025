# Análise do Algoritmo Insertion Sort

## Objetivo
Implementar e analisar o algoritmo de ordenação Insertion Sort, avaliando-o com base em:
- Tempo de execução
- 

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
- Entradas : Entradas geradas como sorted, random e reverse entre 1000, 10000, 100000, 500000, 1000000;
- Graficos :
     - graficos.py : Codigo para criação dos graficos.
     - resultados_graficos : Primeiro arquivo de teste
- Resultados:
     - resultados.csv : Rewsultados
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
Os testes foram executados em um ambiente contendo Sistema Operacional
Windows 11 Home 64 bits. Nossa plataforma de testes foi um computador com processador Processador AMD Ryzen 5 5600, 3.5GHz (4.4GHz Turbo), 6-Cores 12-Threads,
Memória DDR4, 16GB, 3733Mhz, SSD 500GB Leitura 4800MBs e Gravação 2700MBs e Placa de Vídeo MSI NVIDIA GeForce RTX 3060 VENTUS 2X OC, LHR, 12GB GDDR6, DLSS, Ray Tracing.

## Saída

Arquivo CSV com resultados: resultados/resultados.csv

Gráficos gerados na pasta graficos/:

- comparacoes_random.png
- comparacoes_sorted.png
- comparacoes_reverse.png

## Insights dos Resultados


Claro! Abaixo está o **cálculo completo da função de custo por iteração**, para **Merge Sort** e **Insertion Sort**, incluindo **melhor e pior caso**, escrito em Markdown, pronto para o `README.md`.

---

## 📊 Análise Iterativa da Complexidade


### 🔹 Merge Sort

#### Recorrência:

$$
T(n) = 2T\left(\frac{n}{2}\right) + cn
$$

---

Claro! O erro está na formatação do LaTeX no Markdown — ele deve ser feito com crases triplas para blocos de código ou com `\(` e `\)` para inline, e `\[...\]` para blocos.

Aqui está a correção ideal para o seu README.md, com a iteração da recorrência formatada corretamente:

---

### ✅ Iterando a Recorrência:

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



### 📌 Conclusão:

* **Melhor caso:** $O(n \log n)$
* **Pior caso:** $O(n \log n)$
  *(igual, pois o algoritmo sempre executa o mesmo número de divisões e mesclagens)*


### 🔸 Insertion Sort

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


### ✅ Pior Caso (vetor decrescente)

Cada elemento precisa ser comparado e movido por todo o subvetor anterior:

1. Iteração 1: 1 comparação
2. Iteração 2: 2 comparações
3. ...
4. Iteração $i$: $i$ comparações

$$
T(n) = 1 + 2 + 3 + \dots + (n - 1) = \sum_{i=1}^{n-1} i = \frac{n(n - 1)}{2}
$$


### ✅ Melhor Caso (vetor ordenado)

O `while (arr[j] > chave)` nunca entra, então só há uma comparação por iteração:

$$
T(n) = n - 1
$$


### 📌 Conclusão:

* **Melhor caso:** $O(n)$
* **Pior caso:** $O(n^2)$


### 📊 Tabela Comparativa

| Algoritmo          | Melhor Caso   | Caso Médio    | Pior Caso     |
| ------------------ | ------------- | ------------- | ------------- |
| **Insertion Sort** | $O(n)$        | $O(n^2)$      | $O(n^2)$      |
| **Merge Sort**     | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ |

---


| Algoritmo      | Melhor Caso | Pior Caso          | Comparações   | Complexidade                             |
| -------------- | ----------- | ------------------ | ------------- | ---------------------------------------- |
| **Insertion**  | $n - 1$     | $\frac{n(n-1)}{2}$ | $O(n^2)$      | Melhor: $O(n)$ <br> Pior/Médio: $O(n^2)$ |
| **Merge Sort** | $n\log n$ | $n\log n$        | $O(n \log n)$ | Sempre $O(n \log n)$                     |



## Autores

Ana Julia Vieira P.A. Costa e
Gabriel Menezes
