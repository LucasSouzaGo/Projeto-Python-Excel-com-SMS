import pandas as pd
from twilio.rest import Client

account_sid = "AC79f4918c6e3dfdf366db1adb05ff64c9"
auth_token  = "c028f3a87610e1235501ed4842a55e9b"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:   
    
  
    tabela_vendas = pd.read_excel('{}.xlsx'.format(mes))


    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]
        message = client.messages.create(
            to="+5512981459787",
            from_="+16202998929",
            body="No mês {} o vendedor {} teve um total de vendas de {} ultrapassando 55.000".format(mes, vendedor, vendas))
        print(message.sid)


