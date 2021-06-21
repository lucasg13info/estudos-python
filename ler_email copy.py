#Libs para tratativa com e-mail
import smtplib
import time
import imaplib
import email
import traceback 

#Credenciais, porta e SMTP padrão gmail
ORG_EMAIL = "lucccasestefano1@gmail.com" 
FROM_EMAIL = "lucccasestefano1@gmail.com"
FROM_PWD = "xxxxxxxxx" 
SMTP_SERVER = "imap.gmail.com" 
SMTP_PORT = 993

#função que faz a leitura
def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')
        #Feito a conexão e selecionando a caixa de e-mail "inbox" acima

        #lê todos e-mails e adiciona um Id a cada um deles 
        data = mail.search(None, 'ALL')
        mail_ids = data[1]
        id_list = mail_ids[0].split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        #Busca um e-mail com Id específico através do rptocolo RFC822
        for i in range(latest_email_id,first_email_id, -1):
            data = mail.fetch(str(i), '(RFC822)' )
            for response_part in data:
                arr = response_part[0]
                if isinstance(arr, tuple):
                    msg = email.message_from_string(str(arr[1],'utf-8'))
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print('From : ' + email_from + '\n')
                    print('Subject : ' + email_subject + '\n')


                    

    except Exception as e:
        traceback.print_exc() 
        print(str(e))


                
#executando a função de leitura de e-mail
read_email_from_gmail()
