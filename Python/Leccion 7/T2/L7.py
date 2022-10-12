import time
def ir_a_casa():
    tiempo = int(time.strftime('%H'))
    if tiempo >=19:
        return("hora de ir a casa")
    else:
        tiempo = 19 - tiempo
        if tiempo == 1:
            return (f"falta {tiempo} hora para ir a casa")
        else:
            return (f"falta {tiempo} horas para ir a casa")
        