#screen recording

import cv2 as c
import pyautogui as p
import numpy as np

#create resolution (capture resolution)
rs=p.size()

#filename in which we store recording
fn=input("Please enter any file name and path:")

fps=15.0

#for saving video
fourcc =c.VideoWriter_fourcc(*"XVID")
output=c.VideoWriter(fn,fourcc,fps,rs)#fn,fps,rs is defined early
#setting window name
c.namedWindow("LIVE RECORDING",c.WINDOW_NORMAL)
#c.resize("LIVE RECORDING", (600,400))

while True:  #infinite loop
    img=p.screenshot() #captures images
    f=np.array(img)  #array is required to store images
    f=c.cvtColor(f, c.COLOR_BGR2RGB) #setting color format
    output.write(f)
    c.imshow("LIVE RECORDING", f)
    if c.waitKey(1) & 0xFF == ord('q'): #exit the code
        break
    
    
output.release()
c.destroyAllWindows()


