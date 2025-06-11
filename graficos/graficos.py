import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configurações de estilo
sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 72
plt.rcParams['font.size'] = 9

def carregar_dados(caminho_arquivo):
    """Carrega dados e prepara colunas essenciais."""
    df = pd.read_csv(caminho_arquivo)

    # Remove extensão .txt de 'tipo'
    df['tipo'] = df['tipo'].str.replace(r'\.txt$', '', regex=True)

    # Verifica colunas
    required = ['algoritmo', 'tipo', 'tamanho', 'tempo']
    if not all(col in df.columns for col in required):
        raise ValueError("Faltam colunas necessárias no CSV")

    # Traduz e ajusta categorias de 'tipo'
    trad = {'sorted': 'Ordenado', 'random': 'Aleatório', 'reverse': 'Decrescente'}
    df['tipo'] = df['tipo'].map(trad)

    # Ajuste de algoritmo
    df['algoritmo'] = df['algoritmo'].str.title() + ' Sort'

    # pega valores únicos de tamanho como ints, ordena e converte em str
    unique_sizes = sorted(df['tamanho'].astype(int).unique())
    size_labels  = [str(s) for s in unique_sizes]
    df['tamanho_cat'] = pd.Categorical(
        df['tamanho'].astype(str),
        categories=size_labels,
        ordered=True
    )

    return df

def gerar_graficos_tempo(df, output_dir):
    """Gera gráficos tamanho × tempo (todas em escala log)."""
    os.makedirs(output_dir, exist_ok=True)
    for tipo in df['tipo'].dropna().unique():
        dados = df[df['tipo'] == tipo]
        fig, ax = plt.subplots(figsize=(8, 5))

        sns.lineplot(
            data=dados, x='tamanho_cat', y='tempo',
            hue='algoritmo', style='algoritmo',
            markers=True, dashes=False,
            linewidth=1.5, markersize=6,
            errorbar=None,
            ax=ax
        )

        # Define escala log para TODOS os tipos
        ax.set_yscale('log')
        ax.set_xlabel('Tamanho do Vetor')
        ax.set_ylabel('Tempo (s) – Escala Log')
        ax.set_title(f'Tempo de Execução (log) – {tipo}')

        # Legenda lateral, se houver
        handles, labels = ax.get_legend_handles_labels()
        if labels:
            ax.legend(title='Algoritmo', bbox_to_anchor=(1.05, 1), loc='upper left')

        plt.tight_layout()

        tipo_str = tipo.lower().replace(" ", "_")
        filename = os.path.join(output_dir, f"tempo_{tipo_str}.png")
        plt.savefig(filename, bbox_inches='tight')
        plt.close(fig)
        print(f"Salvo: {filename}")

def main():
    caminho = os.path.join(os.path.dirname(__file__),
                           '../resultados/resultados.csv')
    df = carregar_dados(caminho)
    gerar_graficos_tempo(df, os.path.join(os.path.dirname(__file__), 'graficos_tempo'))

if __name__ == "__main__":
    main()
