import re
import time
import wda
from skimage.measure import compare_ssim
import numpy as np
import cv2
import uiautomator2 as u2

### automation iOS on Windows:
# must install iTunes
# pip3 install -U tidevice -i https://mirrors.aliyun.com/pypi/simple
### install uiautomator2 facebook-wda:
# pip3 install uiautomator2 -i https://mirrors.aliyun.com/pypi/simple
# pip3 install -U facebook-wda -i https://mirrors.aliyun.com/pypi/simple
# xcode need compile WebDriverAgent.xcodeproj to iOS device under developer signature
### find the UI element via web:
# pip3 install -U weditor -i https://mirrors.aliyun.com/pypi/simple
# python -m weditor
# tidevice wdaproxy --port 8100

c = wda.USBClient()
c.session().app_start("puzzle.game.find.differences")
time.sleep(2)
# c.swipe(0.5, 0.5, 0.5, 1.0)  # swipe middle to bottom
# time.sleep(1)
print(c.info)


def initCheat():
    c.click(0.207, 0.948)
    time.sleep(1)
    c.click(0.35, 0.029)
    time.sleep(1)
    c.screenshot('ScreenShot/Cheat.png')


def showBanner():
    c.click(0.374, 0.428)
    time.sleep(1)
    c.click(0.526, 0.418)


def destoryBanner():
    c.click(0.896, 0.432)
    time.sleep(1)


def requestInt():
    c.click(0.929, 0.486)
    time.sleep(1)


def showInt():
    c.click(0.601, 0.548)
    time.sleep(1)
    c.screenshot('ScreenShot/Int.png')
    if SSIM(cv2.imread('ScreenShot/Int.png'), cv2.imread('ScreenShot/Cheat.png')) < 0.9:
        print('Show Int Success.')
        return True
    else:
        print('Show Int Fail!')
        return False


def skipInt():
    c.click(0.929, 0.067)
    time.sleep(8)


def closeInt():
    c.click(0.925, 0.036)
    time.sleep(3)
    c.screenshot('ScreenShot/Int.png')
    if SSIM(cv2.imread('ScreenShot/Int.png'), cv2.imread('ScreenShot/Cheat.png')) < 0.9:
        try:
            c.xpath('//*[@label="完成"]').click()
        except:
            pass
        c.click(0.072, 0.078)
        time.sleep(1)
        c.screenshot('ScreenShot/Int.png')
        if SSIM(cv2.imread('ScreenShot/Int.png'), cv2.imread('ScreenShot/Cheat.png')) < 0.9:
            print('Close Int Fail!')
        else:
            print('Close Int Success.')
    else:
        print('Close Int Success.')


def testInt():
    requestInt()
    if isInitReady():
        if showInt():
            time.sleep(40)
            closeInt()
            return True
        else:
            return False


def SSIM(img1, img2):
    img2 = np.resize(img2, (img1.shape[0], img1.shape[1], img1.shape[2]))
    ssim = compare_ssim(img1, img2, multichannel=True)
    return ssim


def isInitReady():
    c.screenshot('ScreenShot/isInitReady.png')
    image = cv2.imread('ScreenShot/isInitReady.png')
    image = image[int(image.shape[0] * 0.475): int(image.shape[0] * 0.50),
            int(image.shape[1] * 0.699): int(image.shape[1] * 0.8)]
    image_true = cv2.imread('ScreenShot/True.png')
    image_false = cv2.imread('ScreenShot/False.png')
    print('SSIM - True : ' + str(SSIM(image, image_true)))
    print('SSIM - False : ' + str(SSIM(image, image_false)))
    if SSIM(image, image_true) > 0.98:
        return True
    else:
        return False

# c.screenshot('ScreenShot/temp.png')
# image = cv2.imread('ScreenShot/temp.png')
# image = image[int(image.shape[0] * 0.475): int(image.shape[0] * 0.50),
#         int(image.shape[1] * 0.699): int(image.shape[1] * 0.8)]
# cv2.imshow('temp',image)
# cv2.imwrite('ScreenShot/False.png', image)
# cv2.waitKey()
# exit(1)
i=0
initCheat()
showBanner()
while True:
    if testInt():
        i += 1
        print('Show Ads Num Success : '+str(i))
        time.sleep(20)
