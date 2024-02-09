from gpiozero import MotionSensor


def main():
    pir = MotionSensor(16)

    while True:

        pir.wait_for_motion()
        print("Algo se mueve!")
        pir.wait_for_no_motion()
        print("Ya no hay movimiento!")


if __name__ == "__main__":
    main()
