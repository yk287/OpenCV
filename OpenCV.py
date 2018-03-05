

'''
OpenCV practice
'''

def video_to_frame(directory, video_name, file_extension):

    '''
    :param directory: directory of files
    :param video_name: name of the files
    :param file_extension: file extension the output should be
    :return: null
    '''

    '''
    A function that takes in a list of names of files and the directory those files are in
    and saves every frame in the source file as a jpg file into their own folder.
    
    Name of the folder is the name of the file name without the file extension. 
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

        new_name = '\\' + name.split('.')[0] + '_{0}.' + '{0}'.format(file_extension)

        while (ret):
            ret, frame = cap.read()
            #            print(new_directory + new_name.format(index))
            cv2.imwrite(new_directory + new_name.format(index), frame)
            index += 1


# if cv2.waitKey(37) & 0xFF == ord('q'):
#                break

#        cap.release()
#       cv2.destroyAllWindows()

direc = r'C:\Users\Youngwook\Documents'
name = []
name = np.append(name, 'superman.webm')
name = np.append(name, 'JMdN6AB.mp4')

video_to_frame(direc, name, 'jpg')