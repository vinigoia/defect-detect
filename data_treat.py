#Importação do TensorFlow
import tensorflow as tf

#Criação de classe
class Data_Tensorflow:
    '''
    Realiza a preparação do dataset nos padrões do TensorFlow.
    
    '''
    def data_prep(data_train_dir,data_val_dir,batch_size,img_height,img_width):
        
        '''
        Cria os datasets de treino, validação e teste nos padrões do TensorFlow.
        
        Inputs:
            data_train_dir -> caminho da pasta dos arquivos de treino.
            data_val_dir -> caminho da pasta dos arquivos de validação.   
            
        Returns:
            train_ds -> dataset de treino nos padrões corretos.
            val_ds -> dataset de validação nos padrões corretos.
            test_ds -> dataset de treino nos padrões corretos.
        '''        
        #Criação do dataset de treino
        train_ds = tf.keras.utils.image_dataset_from_directory(
            data_train_dir,
            seed=123,
            image_size=(img_height, img_width),
            batch_size=batch_size)

        #Criação do dataset de validação
        val_ds = tf.keras.utils.image_dataset_from_directory(
            data_val_dir,
            validation_split=0.2,
            subset="training",
            seed=123,
            image_size=(img_height, img_width),
            batch_size=batch_size)

        #Criação do dataset de teste
        test_ds = tf.keras.utils.image_dataset_from_directory(
            data_val_dir,
            validation_split=0.2,
            subset="validation",
            seed=123,
            image_size=(img_height, img_width),
            batch_size=batch_size)

        #Parâmetros para sobrepor o pré-processamento de dados e a execução do modelo durante o treinamento.
        AUTOTUNE = tf.data.AUTOTUNE
        train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
        val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
        test_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
        
        return train_ds, val_ds, test_ds

