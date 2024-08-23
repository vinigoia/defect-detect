from tensorflow.keras import backend as K
import tensorflow as tf
from tensorflow.keras.utils import get_custom_objects

@tf.keras.utils.register_keras_serializable()
def recall_m(y_true, y_pred):
    '''
    Calcula o recall.
    
    Inputs:
        y_true -> labels reais.
        y_pred -> labels previstas.  
        
    Returns:
        recall -> valor do recall
    '''
    y_true = tf.one_hot(tf.cast(y_true, tf.int32), depth=y_pred.shape[-1]) # Convert to one-hot encoding
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (possible_positives + K.epsilon())
    return recall

@tf.keras.utils.register_keras_serializable()
def precision_m(y_true, y_pred):
    '''
    Calcula a precisão.
    
    Inputs:
        y_true -> labels reais.
        y_pred -> labels previstas.  
        
    Returns:
        precision -> valor do precisão.
    '''
    y_true = tf.one_hot(tf.cast(y_true, tf.int32), depth=y_pred.shape[-1]) # Convert to one-hot encoding
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    return precision

@tf.keras.utils.register_keras_serializable()
def f1_m(y_true, y_pred):
    '''
    Calcula a f1_score.
    
    Inputs:
        y_true -> labels reais.
        y_pred -> labels previstas.  
        
    Returns:
        f1 -> valor do f1_score.
    '''
    precision = precision_m(y_true, y_pred)
    recall = recall_m(y_true, y_pred)
    f1 = 2*((precision*recall)/(precision+recall+K.epsilon()))
    return f1