from Bluetin_Echo import Echo


class UltraSound:
    """
    Class that wraps the Bluetin Echo Object
    """
    _speed_of_sound = 315  # Aquesta es una variable de classe,
    _n_samples = 1  # compartida entre totes les instàncies.

    def __init__(self, id_device, trigger_pin, echo_pin):
        """
        Class constructor
        :param id_device: and Id for the device to be identified
        :param trigger_pin: the number of the trigger pin of the sensor
        :param echo_pin: the number of the echo pin of the sensor
        """
        self._id_device = id_device
        self._trigger_pin = trigger_pin
        self._echo_pin = echo_pin
        self._echo = Echo(self._trigger_pin, self._echo_pin, self._speed_of_sound)
        self._current_reading = 0
        self._last_reading = self.read()
        self._callback_function = None

    def set_callback_function(self, callback_function):
        """
        Seteja la funció que es cridarà com a callback
        :param callback_function:
        :return:
        """
        self._callback_function = callback_function

    def _read(self):
        """
        Crida el mètode de lectura de la llibreria
        :return:
        """
        self._current_reading = int(self._echo.read('cm', self._n_samples))
        return self._current_reading

    def read(self):
        """
        Crida el mètode privat
        :return:
        """
        return self._read()

    def detect_change(self):
        """
        Detecta el canvi i crida la funció de callback
        :return:
        """
        current_reading = self.read()
        if current_reading != self._last_reading and current_reading != 0:
            if self._callback_function is not None:
                self._callback_function(current_reading)
            self._last_reading = current_reading

    def stop(self):
        """
        Stops the
        :return:
        """
        self._echo.stop()


def print_value(value):
    """
    prints the value and is called when it changes in the class
    :param value:
    :return:
    """
    print(f'Changed!:{value}')


if __name__ == "__main__":
    ID_DEVICE = 0
    TRIGGER_PIN = 17
    ECHO_PIN = 27
    ultra = UltraSound(ID_DEVICE, TRIGGER_PIN, ECHO_PIN)
    ultra.set_callback_function(print_value)
    while True:
        try:
            ultra.detect_change()
        except KeyboardInterrupt:
            print("Stopping")
            ultra.stop()
