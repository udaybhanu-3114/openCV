import cv2, numpy, os
alg = 'haarcascade_frontalface_default.xml'
haar_cascade = cv2.CascadeClassifier(alg)
dataset = 'dataset'
print('Training...')
(images,labels,names,id) = ([],[],{},0)

for(subdirs,dirs,files) in os.walk(dataset):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(dataset,subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            label = id
            images.append(cv2.imread(path,0))
            labels.append(int(label))
        id+=1

(images,labels) = [numpy.array(lis) for lis in [images,labels]]
print(images,labels)
(width,height) = (130,100)
model = cv2.face.LBPHFaceRecognizer_create()

model.train(images,labels)
cam = cv2.VideoCapture(0)
count = 0
while count < 30:
    _,img = cam.read()
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(grayImg,1.3,4)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        onlyFace = grayImg[y:y+h,x:x+w]
        resizeImg = cv2.resize(grayImg,(width,height))

        prediction = model.predict(resizeImg)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        if prediction[1]<800:
            cv2.putText(img,'%s - %.0f' %(names[prediction[0]],prediction[1]),(x-10,y-10),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255))
            print(names[prediction[0]])
            count=0
        else:
            count+=1
            cv2.putText(img,'Unknown',(x-10,y-10),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0))
            if(count>100):
                print('Unknown Person')
                cv2.waitKey(10)
                count=0
    cv2.imshow("FaceDetection",img)
    key = cv2.waitKey(10)
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()



 

        