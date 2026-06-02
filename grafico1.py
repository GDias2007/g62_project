import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

def grafico_transacoes_por_tipo(df, pasta):
    contagem = df.groupby('type')['id_tx'].count().sort_values(ascending=False)
    cores = ['#334a94', '#5b7fe6', '#8fa8f0', '#c2cff7', '#e8ecfc']
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(contagem.index, contagem.values, color=cores[:len(contagem)])
    ax.set_title('Número de Transações por Tipo de Cartão', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel('Tipo de Cartão')
    ax.set_ylabel('Número de Transações')
    ax.set_xticks(range(len(contagem)))
    ax.set_xticklabels(contagem.index, rotation=20, ha='right')
    for bar, val in zip(bars, contagem.values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 20,
                str(val), ha='center', va='bottom', fontsize=10)
    plt.tight_layout()
    plt.savefig(os.path.join(pasta, 'grafico1.png'), dpi=100)
    plt.close()
