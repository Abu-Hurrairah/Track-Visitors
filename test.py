import os
import queue
import threading
import time
import cv2
import requests
from visitorsInFrame import *


has_started = False
frame_queue = queue.Queue()

def process_stream(camera_id, camera_name):
    print("Thread Started of Camera", camera_id, camera_name)

    videoPath = f"CamerasVideo/{camera_id}.webm"
    if not os.path.exists(videoPath):
        return

    cap = cv2.VideoCapture(videoPath)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frameCounter = 1

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frameCounter += 1
            if frameCounter % int(fps) == 0:
                frame_queue.put((camera_id,camera_name, frame,frameCounter))
                time.sleep(1)
    cap.release()



def start_threads_for_camera():
    try:
        frame_queue.queue.clear()
        print(frame_queue)
        #response = requests.get('http://127.0.0.1:5000/GetAllCameras')
        cameras_data = [{'id':'29','name':'C5'}]

        threads = []
        for camera_data in cameras_data:
            thread = threading.Thread(target=process_stream, args=(camera_data['id'], camera_data['name'],))
            threads.append(thread)
            thread.start()

        while True:
            print(frame_queue)

            camera_id,camera_name, frame,frameCounter = frame_queue.get()

            print(f"Processing frame from Camera {camera_id}")

            visitors_in_one_frame = returnVisitorsInFrame(frame)
            print(f"Visitors Detected from Camera{camera_name} in frame {frameCounter} is :",visitors_in_one_frame)

            current_visitors = [{'id':52}]

            current_visitor_ids = [visitor['id'] for visitor in current_visitors]
            print(f"Current Visitors :",current_visitor_ids)

            current_visitors_detected_in_frame = [visitor for visitor in visitors_in_one_frame if int(visitor) in current_visitor_ids]
            print(f"Current Visitors detected in Camera{camera_name} is :", current_visitors_detected_in_frame)

            time.sleep(2)
            frame_queue.task_done()

    except Exception as e:
        print(e)
        print("An error occurred..")


def on_startup():
    global has_started
    print("Executing on_startup function")
    if not has_started:
        thread = threading.Thread(target=start_threads_for_camera)
        thread.start()
        has_started = True


on_startup()