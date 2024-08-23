#Importação de bibliotecas necessárias (terceiros)
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0' #Desativação de avisos
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0' #Desativação de avisos
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.applications import InceptionV3
import argparse
import subprocess

#Importação das bibliotecas necessárias (funções próprias)
from unzip_file import UnzipFile
from data_treat import Data_Tensorflow
from metrics import f1_m, precision_m, recall_m
from export_metrics import ExportMetrics
from log_cons import LogConsole
from run_model import evaluate
from tensorboard_run import tensorboard_process

#Título do processo
print("\nTreinamento de modelo para detecção de defeitos em superfícies")

#Definição do número de épocas pelo usuário
epochs = int(input('\nInsira o número de épocas: '))

#Criação do parser
parser = argparse.ArgumentParser(description='Training model for defect detect')

#Adição de argumentos
parser.add_argument('-e', type=str, help='Avaliar modelo')
parser.add_argument('-t', type=str, help='Ativar o Tensorboard')

#Argumentos parse
args = parser.parse_args()

#Criação do diretório para salvar as métricas
os.mkdir("metrics")

#Caminho do arquivo zipado
zipfilepath = "dataset/archive.zip"

#Caminho de destino
zipfilepathdest = "dataset/"

#Caminho da pasta dos arquivos de treino
data_train_dir = "dataset/NEU-DET/train/"

#Caminho da pasta dos arquivos de treino
data_val_dir = "dataset/NEU-DET/validation/"

#Função para processar o arquivo zipado
UnzipFile.unzip_file(zipfilepath, zipfilepathdest)

#Parâmetros para os processos
batch_size = 32
img_height = 200
img_width = 200

#Geração dos datasets de treino, validação e teste nos padrões do TensorFlow
train_ds, val_ds, test_ds = Data_Tensorflow.data_prep(data_train_dir,data_val_dir,batch_size,img_height,img_width)

#Aumento de dados para generalização de modelo
data_augmentation = tf.keras.Sequential(
  [
    layers.RandomFlip("horizontal",
                      input_shape=(img_height,
                                  img_width,
                                  1)),
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.1),
  ]
)

# Carregar o modelo pré-treinado InceptionV3 sem as camadas densas
base_model = InceptionV3(input_shape=(200, 200, 3),include_top=False, weights='imagenet')

# Congelar as camadas convolucionais pré-treinadas
base_model.trainable = False

# Adaptar o modelo para processar as imagens
model = Sequential([
    layers.Rescaling(1./255, input_shape=(img_height, img_width, 1)),
    data_augmentation,
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(6, activation='softmax') 
])

#Criação do diretório de log para registro de informações
tensorboard_cb, csv_logger = LogConsole.log()

#Compilação do modelo, com o dataset de treino e validação
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['acc', f1_m, precision_m, recall_m])

#Print do processo à executar
print("\nTreinando o modelo...")

model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=epochs,
    callbacks=[tensorboard_cb,csv_logger]
)

#Print do processo à executar
print("\nSalvando o modelo...")

#Salvamento do modelo
model.save('defect_model.keras')  # The file needs to end with the .keras extension

#Print do processo à executar
print("\nExportando métricas...")

#Exportação das métricas utilizadas
ExportMetrics.export(model,test_ds)

# Caminho para o ambiente virtual
#env_dir = os.path.join(os.curdir, "env_detect", "Scripts", "activate.bat")

#Condições para o argparse
if args.e:
    # Comando para ativar o ambiente virtual e executar o script Python
    evaluate(test_ds)

if args.t:
    # Comando para ativar o ambiente virtual e executar o script Python
    #command = f'{env_dir} && python tensorboard_run.py'
    tensorboard_process()
    




