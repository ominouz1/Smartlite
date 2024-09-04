import RPi.GPIO as GPIO


# GPIO pin to control the light

LIGHT_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LIGHT_PIN, GPIO.OUT)



# Initialize an empty stack
stack = []


def turn_on_light():
    GPIO.output(LIGHT_PIN, True)


def turn_off_light():
    GPIO.output(LIGHT_PIN, False)


def get_light_status():
    return GPIO.input(LIGHT_PIN) == GPIO.HIGH


def update_stack(is_entry):
    global stack
    if is_entry:
        stack.append(1)
        if len(stack) == 1:
            turn_on_light()
    else:
        if stack:
            stack.pop()
            if not stack:
                turn_off_light()


    return len(stack)


def set_light_manually(status):
    if status:
        turn_on_light()
    else:
        turn_off_light()
    return get_light_status()





