import tensorflow as tf
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import roc_auc_score, accuracy_score
from sklearn.metrics import ConfusionMatrixDisplay
import json
import matplotlib.pyplot as plt

#Criação de classe
class ExportMetrics:
    '''
    Exporta as métricas utilizadas no processo.
    
    '''
    def export (model, test_ds):
        '''
        Exporta as métricas de precisão, recall, f1_score e acurácia para o formato json.
        Também exporta no formato png a matriz confusão.
        
        Inputs:
            model -> modelo treinado.
            test_ds -> dataset de teste   
        '''
        #Criação de listas vazias
        test_images = []
        test_labels = []

        #Iteração para criação de listas
        for images, labels in test_ds: 
            test_images.append(images)
            test_labels.append(labels)

        #Formatação para tensorflow
        test_data = tf.concat(test_images, axis=0)
        test_labels = tf.concat(test_labels, axis=0)

        #Realização das previsões
        prediction = model.predict(test_data)
        predicted_classes = np.argmax(prediction, axis=1)

        #Calcular a matriz de confusão
        cm = confusion_matrix(test_labels, predicted_classes)
        
        #Mostrar matriz de confusão
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=np.unique(test_labels))
        
        #Plotar e salvar a figura
        disp.plot(cmap=plt.cm.Blues)
        plt.savefig('metrics/confusion_matrix.png')
        plt.close()

        class_report = classification_report(test_labels, predicted_classes, output_dict=True, digits=4)
        accuracy = accuracy_score(test_labels, predicted_classes)
        auc = roc_auc_score(test_labels, prediction, multi_class='ovr')

        #Estruturar as métricas em um dicionário
        report_dict = {
            'classification_report': class_report,
            'accuracy': accuracy,
            'AUC': auc
        }

        #Salvar em JSON
        with open('metrics/classification_report.json', 'w') as json_file:
            json.dump(report_dict, json_file, indent=4)