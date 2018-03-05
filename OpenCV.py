

'''
OpenCV practice
'''

def video_to_frame(directory, video_name):

    '''
    :param directory: directory of files
    :param video_name: name of the files
    :return: null
    '''
    import cv2
    import os

    '''
    Make new directories that will hold the frames.
    
    '''

    for name in video_name:
        new_directory = os.path.join(directory, name.split('.')[0])

        if os.path.exists(new_directory) == 0:
            os.mkdir(new_directory)

        cap = cv2.VideoCapture(directory + '\\' + name)

        ret = 1
        index = 0

        new_name = '\\' + name.split('.')[0] + '_{0}.jpg'

        while (ret):
            ret, frame = cap.read()
            #            print(new_directory + new_name.format(index))
            cv2.imwrite(new_directory + new_name.format(index), frame)
            index += 1


# if cv2.waitKey(37) & 0xFF == ord('q'):
#                break

#        cap.release()
#       cv2.destroyAllWindows()

direc = r'C:\Users\name\Documents'
video_to_frame(direc, name)
name = []
name = np.append(name, 'superman.webm')