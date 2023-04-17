import pandas as pd
from twilio.rest import Client

account_sid = "Seu SID"
auth_token  = "Seu token"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:   
    
  
    tabela_vendas = pd.read_excel('{}.xlsx'.format(mes))


    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]
        message = client.messages.create(
            to="Seu número",
            from_="Seu número Twilio",
            body="No mês {} o vendedor {} teve um total de vendas de {} ultrapassando 55.000".format(mes, vendedor, vendas))
        print(message.sid)
