from tkinter import *
import ctypes, os
from PIL import ImageTk, Image
import tkinter.messagebox as tkMessageBox
from tkinter.filedialog import askopenfilename

import cv2
from ultralytics import YOLO
import supervision as sv

model = YOLO("best_5cls.pt")
box_annotator = sv.BoxAnnotator(thickness=2, text_scale=0)
from tkinter import filedialog

home = Tk()
home.title("Garbage Detection and Recognition")

img = Image.open("images/home.jpg")
img = ImageTk.PhotoImage(img)
panel = Label(home, image=img)
panel.pack(side="top", fill="both", expand="yes")
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
lt = [w, h]
a = str(lt[0] // 2 - 450)
b = str(lt[1] // 2 - 320)
home.geometry("900x653+" + a + "+" + b)
home.resizable(0, 0)
file = ''


def Exit():
    global home
    result = tkMessageBox.askquestion(
        "Garbage Detection and Recognition", 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        home.destroy()
        exit()
    else:
        tkMessageBox.showinfo(
            'Return', 'You will now return to the main screen')


def video():
    global file, l1
    try:
        l1.destroy()
    except:
        pass
    # file = askopenfilename(initialdir=os.getcwd(), title="Select Video File", filetypes=( ("Video files", ".mp4")))
    file = filedialog.askopenfilename(
        title="Select Video File",
        filetypes=[("Video files", "*.mp4"), ("All files", "*.*")]
    )
    print(file)
    vid = cv2.VideoCapture(file)

    while (True):
        ret, frame = vid.read()

        res = model(frame)[0]
        detection = sv.Detections.from_ultralytics(res)
        idx = len(detection)

        if (idx > 0):
            image = box_annotator.annotate(scene=frame, detections=detection)
            x1, y1, x2, y2 = detection.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            cls_ = model.names[detection.class_id[0]]
            cv2.putText(frame, cls_, (x1 + 10, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 255, 0),
                        thickness=2)

            # Display the resulting frame
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


def live():
    vid = cv2.VideoCapture(0)

    while (True):
        ret, frame = vid.read()

        res = model(frame)[0]
        detection = sv.Detections.from_ultralytics(res)
        idx = len(detection)

        if (idx > 0):
            image = box_annotator.annotate(scene=frame, detections=detection)
            x1, y1, x2, y2 = detection.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            cls_ = model.names[detection.class_id[0]]
            cv2.putText(frame, cls_, (x1 + 10, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 255, 0),
                        thickness=2)

            # Display the resulting frame
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


def about():
    about = Toplevel()
    about.title("Garbage Detection and Recognition")
    img = Image.open("images/about.jpg")
    img = ImageTk.PhotoImage(img)
    panel = Label(about, image=img)
    panel.pack(side="top", fill="both", expand="yes")
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    lt = [w, h]
    a = str(lt[0] // 2 - 450)
    b = str(lt[1] // 2 - 320)
    about.geometry("900x653+" + a + "+" + b)
    about.resizable(0, 0)
    about.mainloop()


photo = Image.open("images/1.png")
img2 = ImageTk.PhotoImage(photo)
b1 = Button(home, highlightthickness=0, bd=0, activebackground="#2b4b47", image=img2, command=live)
b1.place(x=0, y=209)

photo = Image.open("images/2.png")
img3 = ImageTk.PhotoImage(photo)
b2 = Button(home, highlightthickness=0, bd=0, activebackground="#2b4b47", image=img3, command=video)
b2.place(x=200, y=282)

photo = Image.open("images/3.png")
img4 = ImageTk.PhotoImage(photo)
b3 = Button(home, highlightthickness=0, bd=0, activebackground="#2b4b47", image=img4, command=about)
b3.place(x=0, y=354)

photo = Image.open("images/4.png")
img5 = ImageTk.PhotoImage(photo)
b4 = Button(home, highlightthickness=0, bd=0, activebackground="#2b4b47", image=img5, command=Exit)
b4.place(x=200, y=426)

home.mainloop()
