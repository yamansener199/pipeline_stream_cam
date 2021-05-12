import cv2
import numpy as np
from flask import Flask, render_template, Response
app = Flask(__name__)
def find_camera(id):
    cameras = [0,5]
    return cameras[int(id)]

def gen_frames(camera_id):
     
    cam = find_camera(camera_id[0])
    cap =  cv2.VideoCapture(cam)
    cam1 = find_camera(camera_id[1])
    cap1 =  cv2.VideoCapture(cam1)
    
    while True:
        # for cap in caps:
        # # Capture frame-by-frame
        success, frame = cap.read()
        success1, frame1 = cap1.read()  # read the camera frame
        both = np.concatenate((frame, frame1), axis=1)
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', both)
            both = buffer.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + both + b'\r\n')  # concat frame one by one and show 
                
@app.route('/video_feed/<string:id>/', methods=["GET"])
def video_feed(id):
   
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames(id),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='192.168.1.53', port=80)