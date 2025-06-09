#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <dirent.h>
#include <sys/types.h>
#include <errno.h>

// Insertion Sort
void insertion_sort(int arr[], int n) {
    int i, j, key;
    for (j = 1; j < n; j++) {
        key = arr[j];
        i = j - 1;
        while (i >= 0 && arr[i] > key) {
            arr[i + 1] = arr[i];
            i--;
        }
        arr[i + 1] = key;
    }
}

// Merge Sort
void merge(int arr[], int l, int m, int r) {
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;

    int *L = malloc(n1 * sizeof(int));
    int *R = malloc(n2 * sizeof(int));

    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];

    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }

    free(L);
    free(R);
}

void merge_sort_recursive(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        merge_sort_recursive(arr, l, m);
        merge_sort_recursive(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

void merge_sort(int arr[], int n) {
    merge_sort_recursive(arr, 0, n - 1);
}

// Função para ler array de arquivo TXT
int *ler_array_do_arquivo(const char *filename, int *n) {
    FILE *fp = fopen(filename, "r");
    if (!fp) {
        fprintf(stderr, "Erro ao abrir %s: %s\n", filename, strerror(errno));
        return NULL;
    }

    // Contar número de elementos
    int count = 0;
    int temp;
    while (fscanf(fp, "%d", &temp) == 1) {
        count++;
    }
    rewind(fp);

    // Alocar memória
    int *arr = malloc(count * sizeof(int));
    if (!arr) {
        fclose(fp);
        return NULL;
    }

    // Ler elementos
    for (int i = 0; i < count; i++) {
        if (fscanf(fp, "%d", &arr[i]) != 1) {
            fprintf(stderr, "Erro de leitura em %s\n", filename);
            free(arr);
            fclose(fp);
            return NULL;
        }
    }

    fclose(fp);
    *n = count;
    return arr;
}

// Função para extrair informações do nome do arquivo
int extrair_info_do_nome(const char *filename, int *n, char *tipo) {
    // Formato: entrada_<n>_<tipo>.txt
    char ext[5];
    int result = sscanf(filename, "entrada_%d_%[^.].%4s", n, tipo, ext);
    
    // Verificar se capturou todos os elementos e se a extensão é txt
    if (result == 3 && strcmp(ext, "txt") == 0) {
        return 1;
    }
    return 0;
}

// Função de comparação para ordenação de arquivos
int comparar_arquivos(const void *a, const void *b) {
    const char *nome_a = *(const char **)a;
    const char *nome_b = *(const char **)b;
    
    int n_a, n_b;
    char tipo_a[20], tipo_b[20];
    
    if (!extrair_info_do_nome(nome_a, &n_a, tipo_a)) return 0;
    if (!extrair_info_do_nome(nome_b, &n_b, tipo_b)) return 0;
    
    // Ordenar primeiro por tamanho (n), depois por tipo
    if (n_a != n_b) return n_a - n_b;
    return strcmp(tipo_a, tipo_b);
}

int main() {
    // Abrir diretório de entradas
    DIR *d = opendir("entradas");
    if (!d) {
        fprintf(stderr, "Erro ao abrir diretório: %s\n", strerror(errno));
        return 1;
    }

    // Listar e armazenar nomes dos arquivos
    struct dirent *dir;
    char **arquivos = NULL;
    int num_arquivos = 0;
    
    while ((dir = readdir(d)) != NULL) {
        if (dir->d_type == DT_REG && strncmp(dir->d_name, "entrada_", 8) == 0) {
            // Ignorar arquivos que não terminam com .txt
            if (strstr(dir->d_name, ".txt") == NULL) continue;
            
            arquivos = realloc(arquivos, (num_arquivos + 1) * sizeof(char *));
            arquivos[num_arquivos] = strdup(dir->d_name);
            num_arquivos++;
        }
    }
    closedir(d);
    
    if (num_arquivos == 0) {
        printf("Nenhum arquivo de entrada encontrado!\n");
        return 1;
    }
    
    // Ordenar arquivos pelo tamanho e tipo
    qsort(arquivos, num_arquivos, sizeof(char *), comparar_arquivos);

    // Arquivo de saída CSV
    FILE *fp_csv = fopen("resultados.csv", "w");
    if (!fp_csv) {
        perror("Erro ao criar CSV");
        for (int i = 0; i < num_arquivos; i++) free(arquivos[i]);
        free(arquivos);
        return 1;
    }
    fprintf(fp_csv, "algoritmo,n,tipo_array,tempo\n");

    // Processar cada arquivo em ordem
    for (int i = 0; i < num_arquivos; i++) {
        char caminho[256];
        snprintf(caminho, sizeof(caminho), "entradas/%s", arquivos[i]);

        int n;
        char tipo[20] = "";  // Inicializar como string vazia
        
        if (!extrair_info_do_nome(arquivos[i], &n, tipo)) {
            printf("Formato inválido: %s\n", arquivos[i]);
            free(arquivos[i]);
            continue;
        }

        int *arr = ler_array_do_arquivo(caminho, &n);
        if (!arr) {
            printf("Erro ao ler %s\n", caminho);
            free(arquivos[i]);
            continue;
        }

        // Testar Insertion Sort para TODOS os tamanhos
        printf("Processando Insertion Sort para %s (n=%d)\n", arquivos[i], n);
        int *copia_insertion = malloc(n * sizeof(int));
        if (copia_insertion) {
            memcpy(copia_insertion, arr, n * sizeof(int));
            
            clock_t inicio = clock();
            insertion_sort(copia_insertion, n);
            clock_t fim = clock();
            
            double tempo = (double)(fim - inicio) / CLOCKS_PER_SEC;
            fprintf(fp_csv, "insertion,%d,%s,%.6f\n", n, tipo, tempo);
            free(copia_insertion);
        } else {
            printf("Falha na alocação para Insertion Sort em %s\n", caminho);
        }

        // Testar Merge Sort
        printf("Processando Merge Sort para %s (n=%d)\n", arquivos[i], n);
        int *copia_merge = malloc(n * sizeof(int));
        if (copia_merge) {
            memcpy(copia_merge, arr, n * sizeof(int));
            
            clock_t inicio = clock();
            merge_sort(copia_merge, n);
            clock_t fim = clock();
            
            double tempo = (double)(fim - inicio) / CLOCKS_PER_SEC;
            fprintf(fp_csv, "merge,%d,%s,%.6f\n", n, tipo, tempo);
            free(copia_merge);
        } else {
            printf("Falha na alocação para Merge Sort em %s\n", caminho);
        }

        free(arr);
        free(arquivos[i]);
    }

    fclose(fp_csv);
    free(arquivos);
    
    printf("Resultados salvos em resultados.csv\n");
    return 0;
}