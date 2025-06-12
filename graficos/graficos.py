import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np
from matplotlib.ticker import ScalarFormatter

# Configurações de estilo
sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 72
plt.rcParams['font.size'] = 9

# Unidade de tempo por comparação (1 = 1 ms ou 1 clock)
UNIT_TIME = 1

def carregar_dados(caminho_arquivo):
    """Carrega dados, normaliza nomes de algoritmos e calcula comparações teóricas."""
    df = pd.read_csv(caminho_arquivo)

    # Remove extensão .txt de 'tipo' e traduz
    df['tipo'] = (df['tipo']
                  .str.replace(r'\.txt$', '', regex=True)
                  .map({'sorted': 'Ordenado',
                        'random': 'Aleatório',
                        'reverse': 'Decrescente'}))

    # Normaliza nome dos algoritmos de forma robusta
    def _normaliza_alg(x):
        x = x.lower()
        if 'inser' in x:
            return 'Insertion Sort'
        elif 'merge' in x:
            return 'Merge Sort'
        else:
            # se houver outro, mantém título + Sort
            return x.title().replace(' Sortsort', '') + ' Sort'
    df['algoritmo'] = df['algoritmo'].apply(_normaliza_alg)

    # Verifica quais algoritmos temos
    print("Algoritmos encontrados:", df['algoritmo'].unique())

    # Tamanho como inteiro
    df['tamanho_int'] = df['tamanho'].astype(int)

    # Prepara coluna de comparações teóricas
    n = df['tamanho_int']
    df['comparacoes'] = 0.0

    # Insertion Sort
    mask_ins = df['algoritmo'] == 'Insertion Sort'
    df.loc[mask_ins & (df['tipo']=='Ordenado'),    'comparacoes'] = n - 1
    df.loc[mask_ins & (df['tipo']=='Decrescente'), 'comparacoes'] = n * (n - 1) / 2
    df.loc[mask_ins & (df['tipo']=='Aleatório'),   'comparacoes'] = n * (n - 1) / 4

    # Merge Sort (comparações ≈ n · log2(n) em todos os casos)
    mask_mer = df['algoritmo'] == 'Merge Sort'
    df.loc[mask_mer, 'comparacoes'] = n * np.log2(n)

    # Converte comparações em tempo teórico
    df['tempo_teorico'] = df['comparacoes'] * UNIT_TIME

    return df

def gerar_graficos_teorico(df, output_dir):
    """Gera gráficos log–log de tamanho × tempo_teorico para ambos os algoritmos."""
    os.makedirs(output_dir, exist_ok=True)

    for tipo in df['tipo'].dropna().unique():
        dados = df[df['tipo'] == tipo]
        fig, ax = plt.subplots(figsize=(8, 5))

        sns.lineplot(
            data=dados,
            x='tamanho_int',
            y='tempo_teorico',
            hue='algoritmo',
            style='algoritmo',
            markers=True,
            dashes=False,
            linewidth=1.5,
            markersize=6,
            errorbar=None,
            ax=ax
        )

        # Escalas log–log
        ax.set_xscale('log')
        ax.set_yscale('log')

        # Formatter para ticks do eixo X
        ax.xaxis.set_major_formatter(ScalarFormatter())
        ax.xaxis.set_minor_formatter(ScalarFormatter())
        ax.xaxis.set_tick_params(which='minor', labelsize=0)

        ax.set_xlabel('Tamanho do Vetor (log scale)')
        ax.set_ylabel(f'Tempo Teórico (unidades ×{UNIT_TIME}) (log scale)')
        ax.set_title(f'Tempo Teórico de Comparações (log–log) – {tipo}')

        # Legenda
        ax.legend(title='Algoritmo', bbox_to_anchor=(1.05, 1), loc='upper left')

        plt.tight_layout()
        filename = os.path.join(output_dir, f"comparacoes_{tipo.lower()}.png")
        plt.savefig(filename, bbox_inches='tight')
        plt.close(fig)
        print(f"Salvo: {filename}")

def main():
    caminho = os.path.join(os.path.dirname(__file__),
                           '../resultados/resultados.csv')
    df = carregar_dados(caminho)
    gerar_graficos_teorico(df, os.path.join(os.path.dirname(__file__), 'graficos_tempo_comparacao'))

if __name__ == "__main__":
    main()
