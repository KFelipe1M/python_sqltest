#teste de conexão do python com o mysql.
#feito para estudos, entender as funcionalidades do python e sua conexão com o mysql.

import random
import mysql.connector

conect = mysql.connector.connect(
   host ='localhost',
   user ='root',
   password ='',
   database ='pysql',
)

cursor = conect.cursor()
id_s = set()

while True:
    print("gerador de informações automático")
    print("Aperte G ou g para gerar >> ")
    op = input("")
    if op.lower() == 'g':
        print("gerando informações aleatórias")

        for i in range(50):
         
         id = random.randint(1000,9000)


         cpf1 = random.randint(100,500)
         cpf2 = random.randint(100,500)
         cpf3 = random.randint(100,5000)
         cpf4 = random.randint(1,9) or random.randint(10,99)

         nome = f'nome {i+1}'
         cpf = f'{cpf1}.{cpf2}.{cpf3}-0{cpf4}'

         sql = "insert into info (id, nome, cpf) values (%s,%s,%s)"
         values = (id,nome,cpf)

         cursor.execute(sql, values)
        
        conect.commit()

        print("Os dados já foram inseridos!")
        break
        
        


    else:
       print("erro digite apenas letra g") 

cursor.close
conect.close
