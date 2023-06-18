
import clear_speech
import lung_detection
import hand_model

#print(clear_speech.check_clarity('/Users/vparikh/Downloads/recorded-video.webm', 'Hi Money'))
#print(lung_detection.detect_lung('/Users/vparikh/Downloads/recorded-video1.mp4'))


res = hand_model.evaluate('/Users/vparikh/Downloads/captured-image.jpg')

if res == 1:
    print('No Cancer')

elif res == 2:
    print('Cancer')

else:
    print('No Cancer')
