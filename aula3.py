import pandas as pd
import openpyxl
import plotly.express as px
from pathlib import Path

pasta = Path(__file__).parent
dados = pd.read_excel(str(pasta / "vendas.xlsx"))
grafico = px.histogram(dados, x="loja",
                              y="preco",
                              color="forma_pagamento",
                              text_auto=True,
                              title="Faturamento por loja")
grafico2 = px.pie(dados, "loja",
                         "preco",
                         title="OI")
grafico2.write_html("Faturamento.html")