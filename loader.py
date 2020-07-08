import h5py
import numpy as np
from collections import deque

TIMESTEP = 5


def generate():
    file = h5py.File("data.hdf5", "r")
    images = file.get("images")
    keys = file.get("keys")

    outimages = []
    outkeys = []

    stack_img = deque()

    print(f"Saving with timestep {TIMESTEP}\n")

    i = 0

    for img, key in zip(images.values(), keys.values()):
        if i == TIMESTEP:
            outimages.append(np.array(stack_img))

            outkeys.append(np.array(key))
            stack_img.popleft()
            stack_img.append(np.array(img).flatten())

        else:
            i += 1
            stack_img.append(np.array(img).flatten())

    file.close()

    np.save("images.npy", np.array(outimages))
    np.save("keys.npy", np.array(outkeys))


def load():
    return np.load("images.npy"), np.load("keys.npy")


def load_from(time):
    file = h5py.File("data.hdf5", "r")
    images = file.get("images")
    keys = file.get("keys")

    outimages = []
    outkeys = []

    stack_img = deque()
    i = 0

    for img, key in zip(images.items(), keys.items()):
        if float(img[0]) > time:
            if i == TIMESTEP:
                outimages.append(np.array(stack_img))
                outkeys.append(np.array(key[1]))
                stack_img.popleft()
                stack_img.append(np.array(img[1]).flatten())

            else:
                i += 1
                stack_img.append(np.array(img[1]).flatten())

    file.close()

    return np.array(outimages), np.array(outkeys)


def get_last_time():
    file = h5py.File("data.hdf5", "r")
    images = file.get("images")

    last = 0

    for k in images.keys():
        last = float(k)

    file.close()

    return last


def save_last_time():
    file = open("last_time.txt", mode="w")
    file.write(str(get_last_time()))
    file.close()

def load_last_time():
    file = open("last_time.txt", mode="r")
    val = file.readline()
    file.close()

    return float(val)
