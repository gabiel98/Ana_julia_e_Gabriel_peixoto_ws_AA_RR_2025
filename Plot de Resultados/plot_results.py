import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path
import os
import sys

# Configurar estilo
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

# 1. Localizar o arquivo CSV - CORREÇÃO PARA PASTA SEMINARIO_1
script_dir = Path(__file__).parent
csv_path = script_dir.parent / "resultados.csv"  # Subir um nível para seminario_1

if not csv_path.exists():
    print(f"Erro: Arquivo não encontrado em {csv_path}")
    sys.exit(1)
    
print(f"CSV encontrado em: {csv_path}")

# 2. Carregar dados
try:
    df = pd.read_csv(csv_path)
    print("\nPrimeiras 5 linhas do CSV:")
    print(df.head())
    
    # Verificar se temos dados de insertion sort
    if df[df['algoritmo'] == 'insertion'].empty:
        print("\nAVISO: Não há dados de Insertion Sort no CSV")
    
except Exception as e:
    print(f"\nERRO ao carregar CSV: {str(e)}")
    sys.exit(1)

# 3. Verificar colunas necessárias
cols_necessarias = {'algoritmo', 'n', 'tipo_array', 'tempo'}
if not cols_necessarias.issubset(df.columns):
    print("\nERRO: Colunas faltando no CSV")
    print("Necessárias:", cols_necessarias)
    print("Encontradas:", df.columns.tolist())
    sys.exit(1)

# 4. Corrigir tipos de array
mapeamento_tipos = {
    'ran': 'random',
    'rev': 'reverse',
    'sor': 'sorted',
    'rand': 'random',
    'rever': 'reverse',
    'sorte': 'sorted'
}

if any(tipo in mapeamento_tipos for tipo in df['tipo_array'].unique()):
    print("\nCorrigindo nomes de tipos de array...")
    df['tipo_array'] = df['tipo_array'].map(mapeamento_tipos).fillna(df['tipo_array'])

# 5. Preparar dados
df = df.sort_values(by=['n', 'tipo_array'])
df['n'] = df['n'].astype(int)

# 6. Criar diretório para gráficos
output_dir = script_dir / "graficos"
os.makedirs(output_dir, exist_ok=True)
print(f"Os gráficos serão salvos em: {output_dir}")

# 7. Gerar gráficos para cada tipo de array
tipos_validos = ['random', 'reverse', 'sorted']
tipos_csv = df['tipo_array'].unique()

for tipo in tipos_csv:
    # Pular tipos desconhecidos
    if tipo not in tipos_validos:
        print(f"\nAVISO: Tipo desconhecido '{tipo}' - pulando gráfico")
        continue
        
    try:
        plt.figure(figsize=(10, 6))
        df_tipo = df[df['tipo_array'] == tipo]
        
        # Insertion Sort
        insertion = df_tipo[df_tipo['algoritmo'] == 'insertion']
        if not insertion.empty:
            plt.plot(insertion['n'], insertion['tempo'], 'o-', label='Insertion Sort')
        else:
            print(f"AVISO: Sem dados de Insertion Sort para {tipo}")
        
        # Merge Sort
        merge = df_tipo[df_tipo['algoritmo'] == 'merge']
        plt.plot(merge['n'], merge['tempo'], 's-', label='Merge Sort')
        
        plt.title(f'Desempenho: Array {tipo.capitalize()}')
        plt.xlabel('Tamanho da Entrada (n)')
        plt.ylabel('Tempo (segundos)')
        plt.yscale('log')
        plt.xscale('log')
        plt.legend()
        plt.grid(True)
        
        plt.savefig(output_dir / f"comparacao_{tipo}.png", dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Gráfico gerado: comparacao_{tipo}.png")
        
    except Exception as e:
        print(f"Erro ao gerar gráfico para {tipo}: {str(e)}")

# 8. Gráfico combinado
try:
    plt.figure(figsize=(14, 8))
    
    # Para cada combinação algoritmo-tipo
    for (algo, tipo), group in df.groupby(['algoritmo', 'tipo_array']):
        if tipo not in tipos_validos:
            continue
            
        if algo == 'insertion':
            marcador = 'o-'
        else:
            marcador = 's-'
            
        plt.plot(group['n'], group['tempo'], marcador, label=f"{algo.capitalize()} ({tipo})")
    
    plt.title('Comparação Completa de Desempenho')
    plt.xlabel('Tamanho da Entrada (n)')
    plt.ylabel('Tempo (segundos)')
    plt.yscale('log')
    plt.xscale('log')
    plt.legend(ncol=2)
    plt.grid(True)
    
    plt.savefig(output_dir / "comparacao_completa.png", dpi=300, bbox_inches='tight')
    plt.close()
    print("Gráfico completo gerado: comparacao_completa.png")
    
except Exception as e:
    print(f"Erro ao gerar gráfico completo: {str(e)}")

print("\nProcesso concluído com sucesso!")