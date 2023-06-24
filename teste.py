from comu.ser import se
from time import sleep

s = se(net={'SSID':'Nao_Tem_Wifi','PASSWORD':'miqueias'},conecao=True,Host='127.3.0.1')

x=0
while True:
    data = s.send(x)
    print(x)
    sleep(1)
    x+=1