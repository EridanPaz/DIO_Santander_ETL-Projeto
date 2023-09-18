import csv

'''--------------------------------------------------
|E-xtract: ler o arquivo com extensão .csv, extrair |
|as informações e colocá-las em reader (lista).     |
--------------------------------------------------'''

with open('ClientePerfilCobranca.csv', 'r') as file: 
     reader = csv.reader(file)
                       

     ''' ------------------------------------------------------------------------------
     |T-ransform: Verificar o segmento do cliente e definir a cobrança:               |
     |1 - Entrada Normal: multa de 2% + juros de 230% a.a.                            |
     |2 - Van Gogh: multa de 2% + juros anuais com 30% de desconto.                   |
     |3 - Select: dispensar a multa de 2% aplicar 45% de desconto nos juros anuais.   |
     |                                                                                |
     |  criar um novo item ('ação') na primeira lista (cabeçalho) para guardar        |
     |  as orientações                                                                |
     |                                                                                |
     |  criar uma lista (tabela) para guardar as listas tratadas (matriz)             |
     -------------------------------------------------------------------------------''' 

     table = list()                       

     for data in reader:
          if data[2] == '1':
               data.append('multa de 2% + juros de 230%" a.a.')               
          
          elif data[2] == '2':
               if float(data[3]) < 15.000:
                    data.append('multa de 2% + juros anuais com 15% de desconto.')
               elif float(data[3]) >= 15.000 and float(data[3]) < 40.000:
                    data.append('multa de 2% + juros anuais com 20% de desconto.')
               elif float(data[3]) >= 40 and float(data[3]) < 100.000:
                    data.append('multa de 2% + juros anuais com 45% de desconto.')

          elif data[2] == '3':
               if float(data[3]) >= 100.000 and float(data[3]) < 600.000:
                    data.append('dispensar a multa de 2% aplicar 45% de desconto nos juros anuais.')
               else:
                   data.append('dispensar a multa de 2% aplicar 85% de desconto nos juros anuais.') 
               
          else:
               data.append('Cobrança')
          
          table.append(data)


     
     '''---------------------------------------------------------------------------
     | L-oad: Cria um arquivo com as informações para cada segmento de cliente.   |
     ---------------------------------------------------------------------------''' 
                
     with open('ClienteCobrancaPerfilDefinido.csv','w', newline='') as newFile:
          definition = csv.writer(newFile, delimiter=',')        
          definition.writerows(table)

     file.close
     newFile.close
          
