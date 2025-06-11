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

| Algoritmo      | Melhor Caso | Pior Caso  | Espaço | Estável |
| -------------- | ----------- | ---------- | ------ | ------- |
| Insertion Sort | O(n)        | O(n²)      | O(1)   | Sim     |
| Merge Sort     | O(n log n)  | O(n log n) | O(n)   | Sim     |

| Algoritmo      | Melhor Caso | Pior Caso          | Comparações   | Complexidade                             |
| -------------- | ----------- | ------------------ | ------------- | ---------------------------------------- |
| **Insertion**  | $n - 1$     | $\frac{n(n-1)}{2}$ | $O(n^2)$      | Melhor: $O(n)$ <br> Pior/Médio: $O(n^2)$ |
| **Merge Sort** | $n\log_2 n$ | $n\log_2 n$        | $O(n \log n)$ | Sempre $O(n \log n)$                     |



## Autores

Ana Julia Vieira P.A. Costa e
Gabriel Menezes
