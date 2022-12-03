from ssd1306 import SSD1306_I2C
from machine import I2C,Pin
import time,machine,framebuf

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=2000000) 
display = SSD1306_I2C(128,64,i2c)

for i in range(1,122):
    dirt = 'pbm/'+ str(i) + '.pbm' #文件地址
    print(i)
    with open(dirt,'rb') as f :
        f.readline()
        data = bytearray(f.read())
        fbuf = framebuf.FrameBuffer(data,128,64,framebuf.MONO_HLSB)
        display.fill(0)
        display.blit(fbuf,0,0)#如果不居中，可以修改中间的参数
        display.show()#记得show
        del fbuf#清理内存
        time.sleep(0.2)#这个延时的长度取决于各自的帧率
