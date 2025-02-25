#delisgar o pc pelo python
import os

def progShutdown(time):
    os.system(f'shutdown /s /t {time}')
    print('Shutdown agendado em {time} segundos...')

def cancelShutdown():
    os.system('shutdown -a')
    print ('agendamento cancelado')



#progShutdown(1500)
cancelShutdown()