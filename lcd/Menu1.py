# Affichage de la température

tree = etree.parse(configGet('tmpFileDataXml'))
msg_1='Temp'
msg_2='In:?'
msg_3='Ex:?'
msg_4='So:?'
for datas in tree.xpath("/devices/device/datas/data"):
    if datas.get("id") in configGet('lcd','dataPrint'):
        for data in datas.getchildren():
            if data.tag == "value":
                if datas.get("id") == 'THomeT':
                    msg_2='In:'+str(round(float(data.text) ,1))
                elif datas.get("id") == 'TExtT':
                    msg_3 = 'Ex:'+str(round(float(data.text), 1))
                elif datas.get("id") == 'TSolT':
                    msg_4 = 'So:'+str(round(float(data.text), 1))
# Construction de l'affichage
lcd.clear()
nb_ligne1_space=lcd_columns-len(msg_1)-len(msg_2)
ligne1_msg=msg_1
for nb_space1 in range(nb_ligne1_space):
    ligne1_msg=ligne1_msg+' '
ligne1_msg=ligne1_msg+msg_2

nb_ligne2_space=lcd_columns-len(msg_3)-len(msg_4)
ligne2_msg=msg_3
for nb_space2 in range(nb_ligne2_space):
    ligne2_msg=ligne2_msg+' '
ligne2_msg=ligne2_msg+msg_4

lcd.message = ligne1_msg+'\n'+ligne2_msg
debugTerm('Affichage\n' + ligne1_msg+'\n'+ligne2_msg)
