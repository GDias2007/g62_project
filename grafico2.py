"""
@author: Pessoa 2 - Gonçalo Dias (up202506658)
Gráfico 2: Volume total de transações por tipo de cartão
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

def grafico_volume_por_tipo(df, pasta):
    volume = df.groupby('type')['amount'].sum().sort_values(ascending=False)
    cores = ['#334a94', '#5b7fe6', '#8fa8f0', '#c2cff7', '#e8ecfc']
    fig, ax = plt.subplots(figsize=(7, 7))
    wedges, texts, autotexts = ax.pie(
        volume.values,
        labels=volume.index,
        autopct='%1.1f%%',
        colors=cores[:len(volume)],
        startangle=140,
        pctdistance=0.8
    )
    for text in autotexts:
        text.set_fontsize(10)
    ax.set_title('Volume Total de Transações por Tipo de Cartão (€)', fontsize=14, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(pasta, 'grafico2.png'), dpi=100)
    plt.close()
