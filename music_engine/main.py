from engine.controller import Controller

def main():
    controller = Controller()

    #User script example:
    controller.note('C4', 1.0)  #Add a C4 note with duration of 1 beat
    controller.note(64, 0.5, velocity=90)  #Add an E4 note with duration of 0.5 beats and velocity of 90
    controller.note(440.0, 2.0)  #Add an A4 note (440 Hz) with duration of 2 beats

    print("Current Sequence:")
    controller.show()

if __name__ == "__main__":
    main()