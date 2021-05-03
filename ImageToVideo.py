'''                                             The Effort from M.Shaheryar Haider
                                                           Jr. GIS Analyst
                                                                ECIL
'''
import os 
import cv2  
from PIL import Image, ImageFile 
import glob 
import arcpy
Image.MAX_IMAGE_PIXELS = 2475030272



input_folder = arcpy.GetParameterAsText(0)
input_folder.replace("\\\\","\\")
sub_folder = arcpy.GetParameterAsText(1)
frame_speed = arcpy.GetParameterAsText(2)

main_dir = input_folder+"\\"
sub_fol = sub_folder  
speed = int(frame_speed)

directories = glob.glob(main_dir+"*/")



for directorie in directories:
    a = os.path.basename(os.path.normpath(directorie))
    #print(a)
    os.chdir(main_dir+a+"\\"+sub_fol)   
    path = main_dir+a+"\\"+sub_fol


    mean_height = 0
    mean_width = 0

    num_of_images = len(os.listdir('.')) 
    # print(num_of_images) 

    for file in os.listdir('.'): 
        im = Image.open(os.path.join(path, file)) 
        width, height = im.size 
        mean_width += width 
        mean_height += height 
       

    
    mean_width = int(mean_width / num_of_images) 
    mean_height = int(mean_height / num_of_images) 

    # print(mean_height) 
    # print(mean_width) 

  
    for file in os.listdir('.'): 
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"): 
           
            im = Image.open(os.path.join(path, file))  

            
            width, height = im.size    
           
            imResize = im.resize((900,550), Image.ANTIALIAS)  
            imResize.save( file, 'JPEG', quality = 75) # setting quality 
            


  
    def generate_video(sub_fol): 
        image_folder = '.' 
        video_name = a+'.avi'
       
        
        os.chdir(main_dir+a+"\\"+sub_fol)
        
        images = [img for img in os.listdir(image_folder) 
                  if img.endswith(".jpg") or
                     img.endswith(".jpeg") or
                     img.endswith("png")] 

       
        frame = cv2.imread(os.path.join(image_folder, images[0])) 

        height, width, layers = frame.shape
        

        video = cv2.VideoWriter(video_name,0, speed, (900,550))  

        for image in images:  
            video.write(cv2.imread(os.path.join(image_folder, image)))  

       
        cv2.destroyAllWindows()  
        video.release()  

   
    generate_video(sub_fol) 

    