

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

def grafico_distribuicao_montantes(df_tx, pasta):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df_tx['amount'], bins=40, color='#334a94', edgecolor='white', alpha=0.85)
    ax.set_title('Distribuição dos Montantes das Transações', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel('Montante (€)')
    ax.set_ylabel('Número de Transações')
    plt.tight_layout()
    plt.savefig(os.path.join(pasta, 'grafico4.png'), dpi=100)
    plt.close()
