from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import time


def abrir_pagina():

    global navegador
    link = "https://painel.autentique.com.br/entrar"
    #iniciar
    navegador = webdriver.Chrome(ChromeDriverManager().install())
    navegador.get(link)

    #espera usuário se logar
    #elemento = WebDriverWait(navegador, 300).until(EC.presence_of_element_located((By.XPATH, )))
    time.sleep(20)

#Procurar quantidade de Documentos

def procurar_por_usuario(nome):
    """
    Procura por um nome que o usuario deseja
    """

    elemento_de_procura = navegador.find_element(By.XPATH,"/html/body/app-root/app-documents-home/app-documents-group-list/div[2]/div/div/app-search/div/label/input")
    elemento_de_procura.send_keys(nome)

    elemento_de_ok = navegador.find_element(By.XPATH,"/html/body/app-root/app-documents-home/app-documents-list/div/div/app-search/div/label/div/i")
    elemento_de_ok.click()
    time.sleep(15)

def verificar_assinaturas(nome):

    documentos = []
    assinaturas = []
    datas = []

    for i in range(1,300):
        print(i)
        main_documentos = f"/html/body/app-root/app-documents-home/app-documents-list/div/app-documents-list-boxes/div/div/div[{i}]/a/p[1]"
        assinatura = f"/html/body/app-root/app-documents-home/app-documents-list/div/app-documents-list-boxes/div/div/div[{i}]/a/div[2]/p"
        data = f"/html/body/app-root/app-documents-home/app-documents-list/div/app-documents-list-boxes/div/div/div[{i}]/a/p[2]"
        try:
            temp_doc = navegador.find_element(By.XPATH,main_documentos)
            temp_ass = navegador.find_element(By.XPATH,assinatura).get_attribute("class")
            if temp_ass == "document-subscriber checked":
                temp_ass = "Assinado"
                temp_temp = navegador.find_element(By.XPATH,data)
                datas.append(temp_temp.text)
            else:
                temp_ass = "Pendente"
                temp_temp = '-'
                datas.append(temp_temp)
            documentos.append(temp_doc.text)
            assinaturas.append(temp_ass)

        except:
            print("ERRO")
            k = i
            break

    return documentos,assinaturas,datas,[nome]*(k+1)

def excel(doc,ass,data,nome):
    def descompac(base):
        temp = []
        for array in base:
            for item in array:
                temp.append(item)
        return temp
    try:
        d = pd.DataFrame({"Nomes":descompac(nome),"Documentos":descompac(doc),"Assinatura":descompac(ass),"Data":descompac(data)})
    except:
        d = pd.DataFrame({"Nomes":nome,"Documentos":doc,"Assinatura":ass,"Data":data})
        
    writer = pd.ExcelWriter('Renatinha.xlsx',engine="xlsxwriter")
    d.to_excel(writer)
    writer.save()


"""
procurar_por_usuario("Renata")

documentos, assinaturas ,datas ,nomes= verificar_assinaturas()


excel(d)

"""
'se estiver minimizado ele nao reconhece com o msm xpath'
