import os
import time
import tensorflow as tf

class LogConsole:
    '''
    Realiza a configuração para os logs do processamento e tensorboard.
    
    '''
    def log():
        '''
        Realiza a configuração para os logs do processamento e tensorboard. 
            
        Returns:
            tensorboard_cb -> callbacks para o tensorboard.
            csv_logger -> callbacks para exportação em csv.
        '''
        #Configuração de parâmetros
        root_logdir = os.path.join(os.curdir,"logs")
        run_id = time.strftime("run_%Y_%m_%d-%H_%M_%S")
        run_logdir = os.path.join(root_logdir, run_id)

        # Define the TensorBoard callback
        tensorboard_cb = tf.keras.callbacks.TensorBoard(run_logdir)
        csv_logger = tf.keras.callbacks.CSVLogger('metrics/epoch_metrics.csv')
        
        return tensorboard_cb,csv_logger