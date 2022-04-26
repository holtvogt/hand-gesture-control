from controller.controller import Controller
from model.gesture_mode import GestureMode


def main():
    """The main method starting the gesture control application."""

    print("### Starting Gesture Controller 9000 ###\n")

    try:
        mode: int = _select_mode()
        controller: Controller = Controller()
        # Run chosen handler
        handlers = controller.get_handlers()
        handlers[mode].run()
    except KeyboardInterrupt:
        print("User closed the application manually\n")


def _select_mode() -> int:
    """Selects the mode to be used.

    :return: The selected user mode
    """

    selection: int = 0
    # Available gesture modes
    mode_names = [enum.mode_name for enum in GestureMode]
    mode_numbers = [enum.mode_number for enum in GestureMode]
    input_not_valid: bool = True
    while input_not_valid:
        print("Select a gesture mode:")
        for i, name in enumerate(mode_names):
            message = "\t{}: {}".format(i, name)
            if i != len(mode_names) - 1:
                message += "\n"
            print(message)

        # Make user choose from 1 to n modes
        try:
            selection = int(input("Enter selection: "))
        except ValueError:
            print("Selection does not exist. Please, try again\n")
            continue

        # Check if entered user mode number exists
        if selection in mode_numbers:
            input_not_valid = False
        else:
            print("Mode {} does not exist, yet. Please, try again\n".format(selection))

    return selection


if __name__ == "__main__":
    main()
