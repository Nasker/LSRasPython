from gpiozero import MotionSensor

pir = MotionSensor(16)

while (True):
    
    pir.wait_for_motion()
    print("Algo se mueve!")
    pir.wait_for_no_motion()
    print("Ya no hay movimiento!")