from pyfirmata import Arduino, util


def main():
    board = Arduino("COM10")
    pin_motor_pwm = board.get_pin('d:5:p')  # pin 2 din arduino ----- pwm
    pin_in_one = board.get_pin('d:8:o')
    pin_in_two = board.get_pin('d:9:o')
    # turatie = input("Ce turatie doriti? : ")

    pin_in_one.write(1)
    pin_in_two.write(0)
    pin_motor_pwm.write(1)


if __name__ == '__main__':
    main()
