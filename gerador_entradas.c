#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/stat.h>  // Para mkdir()
#include <errno.h>     // Para tratamento de erros

#ifdef _WIN32
#include <direct.h>    // Para mkdir() no Windows
#endif

// Função para criar diretório se não existir
void criar_diretorio(const char *path) {
    #ifdef _WIN32
    if (_mkdir(path) != 0 && errno != EEXIST) {
    #else
    if (mkdir(path, 0777) != 0 && errno != EEXIST) {
    #endif
        perror("Erro ao criar diretório");
        exit(1);
    }
}

void embaralhar(int *vetor, int n) {
    for (int i = n - 1; i > 0; i--) {
        int j = rand() % (i + 1);
        int tmp = vetor[i];
        vetor[i] = vetor[j];
        vetor[j] = tmp;
    }
}

void gerar_arquivo(int n, const char *tipo) {
    int *vetor = malloc(n * sizeof(int));
    if (!vetor) {
        printf("Erro de alocação\n");
        exit(1);
    }

    // Preencher vetor
    if (strcmp(tipo, "sorted") == 0) {
        for (int i = 0; i < n; i++)
            vetor[i] = i + 1;
    } else if (strcmp(tipo, "reverse") == 0) {
        for (int i = 0; i < n; i++)
            vetor[i] = n - i;
    } else if (strcmp(tipo, "random") == 0) {
        for (int i = 0; i < n; i++)
            vetor[i] = i + 1;
        embaralhar(vetor, n);
    } else {
        printf("Tipo inválido: %s\n", tipo);
        free(vetor);
        return;
    }

    // Nome do arquivo
    char nome_arquivo[256];
    snprintf(nome_arquivo, sizeof(nome_arquivo), "entradas/entrada_%d_%s.txt", n, tipo);

    // Gravar arquivo
    FILE *fp = fopen(nome_arquivo, "w");
    if (!fp) {
        perror("Erro ao criar arquivo");
        free(vetor);
        return;
    }

    for (int i = 0; i < n; i++) {
        fprintf(fp, "%d\n", vetor[i]);
    }

    fclose(fp);
    free(vetor);
    printf("Arquivo gerado: %s\n", nome_arquivo);
}

int main() {
    srand(time(NULL));
    
    // Criar diretório se não existir
    criar_diretorio("entradas");

    int tamanhos[] = {1000000, 2000000, 3000000, 4000000, 5000000};
    const char *tipos[] = {"sorted", "random", "reverse"};
    int num_tamanhos = sizeof(tamanhos)/sizeof(tamanhos[0]);
    int num_tipos = sizeof(tipos)/sizeof(tipos[0]);

    for (int i = 0; i < num_tamanhos; i++) {
        for (int j = 0; j < num_tipos; j++) {
            gerar_arquivo(tamanhos[i], tipos[j]);
        }
    }

    return 0;
}