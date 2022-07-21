#參考網址:https://blog.everlearn.tw/%E7%95%B6-python-%E9%81%87%E4%B8%8A-raspberry-pi/raspberry-pi-3-mobel-3-%E5%88%A9%E7%94%A8-pwm-%E6%8E%A7%E5%88%B6%E4%BC%BA%E6%9C%8D%E9%A6%AC%E9%81%94

from turtle import heading
import RPi.GPIO as GPIO
import time
from compass import compass

CONTROL_PIN = 27
PWM_FREQ = 50

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(CONTROL_PIN, GPIO.OUT)

pwm = GPIO.PWM(CONTROL_PIN, PWM_FREQ)
pwm.start(0)

def angle_to_duty_cycle(angle):
    '''
        Input angle this function can use pwm control the motor
        control pin is GPIO.BCM(17) 130~30
    '''
    duty_cycle = (0.05 * PWM_FREQ) + (0.19 * PWM_FREQ * angle / 180)
    pwm.ChangeDutyCycle(duty_cycle)
    print('角度={: >3}, 工作週期={:.2f}'.format(angle, duty_cycle))

if __name__ == '__main__':

    while True:
        # try:
        heading = compass()
        print ("Heading Angle = %d°" %heading, end = ', ')
        #want heading
        wh = 115
        angle_to_duty_cycle(80 + (int(heading) - wh))

        # except:
        #     print('Error, wait 5sec and continue.')
        #     time.sleep(5)
        #     continue