import numpy as np
import cv2
from mss import mss
import keypresses
import h5py
import time
import os

if __name__ == '__main__':
    bbox = {'top': 120, 'left': 3, 'width': 500, 'height': 90}
    sct = mss()

    if not os.path.isfile("data.hdf5"):
        file = h5py.File("data.hdf5", "a")
        images = file.create_group("images")
        keys = file.create_group("keys")
    else:
        file = h5py.File("data.hdf5", "a")
        images = file.get("images")
        keys = file.get("keys")

    running = True

    while running:
        screen = np.array(sct.grab(bbox))

        img = cv2.resize(cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY), (25, 25), interpolation=cv2.INTER_LINEAR)

        cv2.imshow('emulator', cv2.resize(img, (250, 250), interpolation=cv2.INTER_NEAREST))

        k = np.array(keypresses.get_bits(), dtype='i8')

        current_time = str(time.time())

        images.create_dataset(current_time, data=img)
        keys.create_dataset(current_time, data=k)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

    file.close()
