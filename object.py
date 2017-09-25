import httplib, urllib, base64, json
import cv2, time, thread

# https://southcentralus.api.cognitive.microsoft.com/customvision/v1.0/Prediction/image?iterationId=0601e978-1575-4410-bf4d-31f27fa0de26
cap = cv2.VideoCapture(1)




font = cv2.FONT_HERSHEY_SIMPLEX

###############################################
#### Update or verify the following values. ###
###############################################

# Replace the subscription_key string value with your valid subscription key.


# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace 
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.
text = 'Unknown'
headers = {
    # Request headers
    'Content-Type': 'multipart/form-data',
    'Prediction-key': 'yourpredictionkey',
}
params = urllib.urlencode({
    # Request parameters
    'application': 'OverWatch',
})

def calling_api(img):
    global text
    conn = httplib.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/customvision/v1.0/Prediction/c6da9a55-b5f4-40e2-b2e2-7bb1d21e5309/image?%s" % params, img.read(), headers)
    response = conn.getresponse()
    data = response.read()
    #print(data)
    parsed = json.loads(data)
    #print(parsed)
    conn.close()
    texted = parsed['Predictions']
    for texts in texted:
        print(texts['Tag'],float(texts['Probability']))
    
    
# The URL of a JPEG image to analyze.
i=0
while True:
    ret, img = cap.read()
    print(ret)
    cv2.imwrite('xx.jpeg', img)
    # cv2.waitKey(0)
    img1 = open('xx.jpeg','rb')

    
        #if w*h > 6500:
        
        
        
    if i%50 == 0:
        thread.start_new_thread(calling_api, (img1,) )
    cv2.putText(img, text ,(10, 20), font, .5,(255,255,255),2,cv2.CV_AA)
    if i>100:
        i = i%50

    
    
    

    
    
    
        #print(parsed)
        # text = parsed['categories']
        # print(text[0])
        # if text ==[]:
        #     text = 'Unknown'
        # else:
        #     text = text[0]['name']
        # # print(text)
        # conn.close()
    
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
    i+=1
    
    # time.sleep(2)vb
cap.release()
cv2.destroyAllWindows()
    
