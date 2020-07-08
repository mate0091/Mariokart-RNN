import keyboard as k


player_control = True


def get_bits():
    bits = []

    if k.is_pressed('up'):
        bits.append(1)
    else:
        bits.append(0)

    if k.is_pressed('down'):
        bits.append(1)
    else:
        bits.append(0)

    if k.is_pressed('left'):
        bits.append(1)
    else:
        bits.append(0)

    if k.is_pressed('right'):
        bits.append(1)
    else:
        bits.append(0)

    if k.is_pressed('c'):
        bits.append(1)
    else:
        bits.append(0)

    if k.is_pressed('v'):
        bits.append(1)
    else:
        bits.append(0)

    if k.is_pressed('x'):
        bits.append(1)
    else:
        bits.append(0)

    if k.is_pressed('d'):
        bits.append(1)
    else:
        bits.append(0)

    if k.is_pressed('a'):
        bits.append(1)
    else:
        bits.append(0)

    if k.is_pressed('s'):
        bits.append(1)
    else:
        bits.append(0)

    return bits


def setup():
    k.on_press_key('p', switch_player_key)


def switch_player_key(e):
    global player_control

    player_control = not player_control


def get_ai_or_player():
    global player_control

    return player_control


def send_bits(bits):
    if bits[0] == 1:
        k.press('up')
    else:
        k.release('up')

    if bits[1] == 1:
        k.press('down')
    else:
        k.release('down')

    if bits[2] == 1:
        k.press('left')
    else:
        k.release('left')

    if bits[3] == 1:
        k.press('right')
    else:
        k.release('right')

    if bits[4] == 1:
        k.press('c')
    else:
        k.release('c')

    if bits[0] == 1:
        k.press('v')
    else:
        k.release('v')

    if bits[0] == 1:
        k.press('x')
    else:
        k.release('x')

    if bits[0] == 1:
        k.press('d')
    else:
        k.release('d')

    if bits[0] == 1:
        k.press('a')
    else:
        k.release('a')

    if bits[0] == 1:
        k.press('s')
    else:
        k.release('s')