import subprocess
import time
import os

def tensorboard_process():
    #Diretório onde os logs do TensorBoard estão armazenados
    log_dir = './logs'

    #Verifica se o diretório de logs existe
    if not os.path.exists(log_dir):
        print(f"O diretório de logs '{log_dir}' não existe.")
        exit(1)

    #Comando para iniciar o TensorBoard
    command = ['tensorboard', '--logdir', log_dir, '--port', '6006']

    #Iniciar o TensorBoard
    process = subprocess.Popen(command)

    try:
        # Manter o script ativo para continuar monitorando o TensorBoard
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        # Se o usuário interromper o script com Ctrl+C, termine o processo do TensorBoard
        print('Interrompendo TensorBoard...')
        process.terminate()
        process.wait()