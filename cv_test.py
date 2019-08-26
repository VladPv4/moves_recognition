# import cv2

# img=cv2.imread('galaxy.jpg',0)

# print(type(img))
# print(img)
# print(img.shape)
# print(img.ndim)

# resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
# cv2.imshow('Cool Galaxy', resized_image)
# cv2.imwrite('galaxy_resized_dark.jpg',resized_image)
# cv2.waitKey(5000)
# cv2.destroyAllWindows()

#Resize Photos in Folder#
import cv2
import os

images_list = os.listdir('sample-images')

for image in images_list:
    img=cv2.imread(str('sample-images/'+image), 1)
    resized_img=cv2.resize(img,(100,100))
    cv2.imwrite(str(str(os.path.splitext(image)[0])+'_resized.jpg'),resized_img)
    #print()
    
print('Done!')




