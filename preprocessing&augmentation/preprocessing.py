import os
import numpy as np
import cv2
import random
class ImageEditor():

    
    def __init__(self,imgPath):
        self.imgName = imgPath.split('/')[-1]
        self.img = cv2.imread(imgPath)

  
   
    def cut2square(self):
        """Schneidet mitig ein Quadrat aus dem Bild und belässst Auflösung."""
        height = self.img.shape[0]
        width = self.img.shape[1]

        if height>width: #hochformat
            y= round((height-width)/2)
            self.img = self.img[y:y+width, 0:width]
        else:
            x= round((width-height)/2)
            self.img = self.img[0:height, x:x+height]
    
    def contrastEnhancementCLAHE(self):
        clahe = cv2.createCLAHE(clipLimit = 5)
        self.img = clahe.apply(self.img)

    def rescale(self,res):
        self.img = cv2.resize(self.img, (res,res), interpolation = cv2.INTER_AREA)


   

    def write(self,path,):
        """Speichert das Bild an gegebenem Ortab. Prefixe bitte im Pfad einbetten."""
        cv2.imwrite(path+self.imgName,self.img)
        

    def zoom(self,factor):
        """Zoomt im Bild um den gegtebenen Faktor, bitte nur mit Quadratiscfhen Bildern verwenden."""
        length = self.img.shape[0]
        newLength = round(length/factor)

        x = round((length-newLength)/2)

        self.img = self.img[x:newLength+x,x:newLength+x]    




    def randomFlip(self):
        """Spiegelt das Bild, um eine Zufällige Achse"""
        axs= random.randint(0,1)

        self.img =  cv2.flip(self.img,axs)

    def flip(self,axs):

        """Spiegelt das Bild, axs=0 für horizontale Achse."""
        self.img =  cv2.flip(self.img,axs)



    def randomZoom(self):
        """Zufäliger Zoom zwischen 1 und 1.5. Bitte Original Bild ImageEditor geben, ansonsten zu hoher Datenverlust."""
        length = self.img.shape[0]
        zoom=1+random.randint(0,50)/100
        newLength = round(length/zoom)

        x = round((length-newLength)/2)

        self.img = self.img[x:newLength+x,x:newLength+x]   

       

    





def pickRandom(origin_path,count,save_path):
    assert save_path[-1]=='/'
    origin_dir= os.listdir(origin_path)
    
    for i in range(0,count):

        x= random.randint(0,len(origin_dir)-1)
        img_path=origin_path+str(origin_dir[x])
        img=cv2.imread(img_path)
        cv2.imwrite(save_path+origin_dir[x],img)

        origin_dir.remove(origin_dir[x])
