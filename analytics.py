"""
@author: Grupo 62 (2025)
Análise de dados bancários com Pandas
"""
import sqlite3
import pandas as pd
import os
from datafile import filename
from grafico1 import grafico_transacoes_por_tipo
from grafico2 import grafico_volume_por_tipo
from grafico3 import grafico_media_por_tipo
from grafico4 import grafico_distribuicao_montantes

def gerar_graficos():
    # Ligação à base de dados
    conn = sqlite3.connect(filename + 'Bancos.db')

    # Leitura dos dados com Pandas
    df_tx = pd.read_sql_query('SELECT * FROM "Transaction"', conn)
    df_card = pd.read_sql_query('SELECT * FROM Card', conn)
    df_bank = pd.read_sql_query('SELECT * FROM Bank', conn)
    df_branch = pd.read_sql_query('SELECT * FROM Branch', conn)
    conn.close()

    # Juntar transações com cartões
    df = df_tx.merge(df_card, left_on='card_id', right_on='id', suffixes=('_tx', '_card'))

    # Pasta para guardar os gráficos
    pasta = os.path.join('static', 'graficos')
    os.makedirs(pasta, exist_ok=True)

    # Gerar os 4 gráficos
    grafico_transacoes_por_tipo(df, pasta)
    grafico_volume_por_tipo(df, pasta)
    grafico_media_por_tipo(df, pasta)
    grafico_distribuicao_montantes(df_tx, pasta)

    # Estatísticas com Pandas
    estatisticas = {
        'total_transacoes': len(df_tx),
        'volume_total': round(df_tx['amount'].sum(), 2),
        'valor_medio': round(df_tx['amount'].mean(), 2),
        'valor_maximo': round(df_tx['amount'].max(), 2),
        'valor_minimo': round(df_tx['amount'].min(), 2),
        'total_bancos': len(df_bank),
        'total_agencias': len(df_branch),
        'total_cartoes': len(df_card),
    }

    return estatisticas
