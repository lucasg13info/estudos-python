#Leia o nome da cidade e fale se começa com 'Santo'

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
