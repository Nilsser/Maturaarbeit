
from gc import callbacks
import tensorflow as tf
import json
import keras
from time import sleep


class Model():

    def __init__(
        
        self,
       
        path,
        img_size,
        batch_size,
        callback,
        model,
       
        ):

        self.train_set = create_tf_dataSet(
            path=path+"/train",
            img_size=img_size,
            batch_size=batch_size
            )

        self.validation_set = create_tf_dataSet(
            path=path+"/validation",
            img_size=img_size,
            batch_size=batch_size,
            )

        self.callback=callback  
        self.model=model
        



    def compile(self,lr):
        self.model.compile(
            loss='binary_crossentropy',#focal_loss(),
              
            
            optimizer=tf.keras.optimizers.Adam(learning_rate=lr),
            metrics=[tf.keras.metrics.Recall(),tf.keras.metrics.Precision()]
        ) 

    def train(self,epochs=10):
        print(self.model.layers[-1].weights)
        self.history=self.model.fit(
                    self.train_set,
                    epochs=epochs,
                    steps_per_epoch=len(self.train_set),
                    validation_data=self.validation_set,
                    validation_steps=int(len(self.validation_set)), 
                    
                    callbacks=callbacks 
                    )
        print(self.model.layers[-1].weights)
                            
    def save_histroy(self,history_path):
        
        history_dict = self.history.history
        
        json.dump(history_dict, open(history_path, 'w'))



def create_tf_dataSet(path,img_size,batch_size=32,):
    """Gibt ein TF DataSet zurück.
    Bilder müssed dazu der Klasse nach in Ordner Sortiert sein.\n \n params: \n    -img_size -batch_size"""
  
    return tf.keras.preprocessing.image_dataset_from_directory(
    path,
    image_size=img_size,
    batch_size=batch_size,
    label_mode= 'binary',
    #color_mode='grayscale'
)

def upload_tensorboard(path,name):
    
    callback = tf.keras.callbacks.TensorBoard(
        log_dir=path+name
    )

    return callback



