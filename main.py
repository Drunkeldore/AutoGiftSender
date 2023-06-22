from ppadb.client import Client as AdbClient
import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image
import time

#Need to find a better way to manage the timing than with time.sleep. Open to any suggestions. First time
#programming anything like this. It's been very fun.

#Default is 127.0.0.1 port 5037
#Phone Home IP: 10.99.34.58

client = AdbClient(host="127.0.0.1", port=5037)
#connecting to the first device, being tghe phone, the only device.
devices = client.devices()
if len(devices) == 0:
    print("no device attached")
    quit()
device = devices[0]

def plot_image(screenshot):
    poke_file = screenshot
    poke_img = Image.open(poke_file)

    img_array = np.array(poke_img)
    print(img_array.shape)
    plt.imshow(img_array)
    plt.show()

def take_plot_screenshot(): # capture screen and plot it. Save it if prompted with y.
    check_screenshot = input("Do you want to save a screenshot? Y or N: ")
    result = device.screencap()
    filename = "screen0.png"
    num = 0
    while os.path.exists(filename):
        filename = f"screen{num}.png"
        num += 1
    with open(filename, "wb") as fp:
        fp.write(result)
    plot_image(filename)

    if check_screenshot.lower() != "y":
        os.remove(f"./{filename}")


def rgb_checker(x, y):
    result = device.screencap()
    filename = "rgb.png"

    with open(filename, "wb") as fp:
        fp.write(result)
    image = Image.open(filename)
    rgb_value = image.getpixel((x, y))[:3] # Getting the rgb for the pink bar to know if we sent a gift
    os.remove(f"./{filename}")
    return rgb_value

def go_to_friendlist():
    friends_list = ["145 2032", "734 203"]
    device.shell(f"input tap {friends_list[0]}")
    device.shell(f"sleep 3 && input tap {friends_list[1]}")
    time.sleep(2)

def opening_gift():
    device.shell("input tap 586 1535")
    device.shell("input tap 533 1813")
    time.sleep(3)
    device.shell("input tap 865 2245")
    device.shell("input tap 865 2245")
    #Gift x 586 y 1535, rgb = (246, 245, 121)


def sending_gift():
    #Going through sending gifts then hitting back twice to return to friends
    gift_rgb = rgb_checker(586, 1535)
    gift_cords = ["214 1700", "370 754", "533 1857", "865 2245", "865 2245"]
    for each in gift_cords:

        if each == gift_cords[0] and gift_rgb == (246, 245, 121):
            opening_gift()
            print("Gift Opened!")
            continue

        device.shell(f"input tap {each}")
        time.sleep(1)

        if each == gift_cords[0] and rgb_checker(346, 1092) == (232, 128, 183):
            print('Already Sent Gift')
            device.shell("input tap 865 2245")
            device.shell("input tap 865 2245") # Back button to reset
            return

    time.sleep(1)
    print("Gift sent!")


def cycling_friends():
    four_friends_coords = ["150 835", "150 1194", "150 1527", "150 1887"]

    for _ in range(6):
        num = 1
        for each in four_friends_coords:
            device.shell(f"input tap {each}")
            print({num})
            time.sleep(1)
            sending_gift()
            time.sleep(1)
            num += 1
        # swiping down
        ### scroll coord for full page scroll = 163 2162 163 1615
        device.shell("input touchscreen swipe 163 2162 163 1737") ### scroll coord for full page scroll = 163 2162 163 1615

        time.sleep(2)



### FUNCTION USE PRE GUI ###

#take_plot_screenshot()
go_to_friendlist()
cycling_friends()

