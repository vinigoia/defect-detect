#Bibliotecas para manipulação de arquivos
import zipfile
import shutil
import os

class UnzipFile:
    '''
    Realiza a descompactação e configuração dos arquivos do dataset.
    
    '''
    def unzip_file(zipfilepath,zipfilepathdest):
        '''
        Através do arquivo compactado são geradas as pastas de treino e validação.
        
        Inputs:
            zipfilepath -> caminho do arquivo zipado.
            zipfilepathdest -> caminho destino.        
        '''
        #Descopacta o arquivo
        with zipfile.ZipFile(zipfilepath, 'r') as zip_ref:
            zip_ref.extractall(zipfilepathdest)
        
        #Remove as pastas pertinentes
        shutil.rmtree(zipfilepathdest + "NEU-DET/train/annotations")
        shutil.rmtree(zipfilepathdest + "NEU-DET/validation/annotations")
        
        #Move os arquivos para as pastas pertinentes
        for i in os.listdir(zipfilepathdest + "NEU-DET/train/images"):
            shutil.move(zipfilepathdest + "NEU-DET/train/images/"+ i, zipfilepathdest + "NEU-DET/train/"+ i)

        #Move os arquivos para as pastas pertinentes
        for i in os.listdir(zipfilepathdest + "NEU-DET/validation/images"):
            shutil.move(zipfilepathdest + "NEU-DET/validation/images/"+ i, zipfilepathdest + "NEU-DET/validation/"+ i)
         
        #Remove as pastas vazias   
        shutil.rmtree(zipfilepathdest + "NEU-DET/train/images")
        shutil.rmtree(zipfilepathdest + "NEU-DET/validation/images")
        
        print("\nProcesso de desconpactação finalizado\n")