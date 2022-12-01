from PIL import Image
import time

for i in range(1,2):
    print(i)
    file=str(i)+'.bmp'
    im=Image.open(file)
    im=im.convert('1')
    im.save(str(i)+'.pbm')
    time.sleep(0.1)