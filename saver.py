import numpy as np
import cv2
from mss import mss
import keypresses
import h5py
import time
import os


class Saver:
    def __init__(self):
        self.bbox = {'top': 120, 'left': 3, 'width': 500, 'height': 90}
        self.sct = mss()
        self.img = None

        if not os.path.isfile("data.hdf5"):
            self.file = h5py.File("data.hdf5", "a")
            self.images = self.file.create_group("images")
            self.keys = self.file.create_group("keys")
        else:
            self.file = h5py.File("data.hdf5", "a")
            self.images = self.file.get("images")
            self.keys = self.file.get("keys")

    def record(self, save, kp):
        screen = np.array(self.sct.grab(self.bbox))

        self.img = cv2.resize(cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY), (20, 20), interpolation=cv2.INTER_LINEAR)

        cv2.imshow('emulator', cv2.resize(self.img, (250, 250), interpolation=cv2.INTER_NEAREST))

        k = np.array(kp, dtype='i8')

        current_time = str(time.time())

        if save:
            self.images.create_dataset(current_time, data=self.img)
            self.keys.create_dataset(current_time, data=k)

    def get_current_img(self):
        return np.array(self.img).flatten()

    def close(self):
        self.file.close()
        cv2.destroyAllWindows()


