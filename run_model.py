import tensorflow as tf
from metrics import f1_m, precision_m, recall_m

def evaluate(test_ds):
    '''
    Realiza a avaliação do modelo.
    
    '''
    #Carregamento do modelo com suas métricas
    model = tf.keras.models.load_model('defect_model.keras', custom_objects={
        'recall_m': recall_m,
        'precision_m': precision_m,
        'f1_m': f1_m
    })

    #Print do processo à executar
    print("Testando o modelo...")

    #Avaliação do modelo no dataset de teste
    model.evaluate(test_ds, return_dict=True)