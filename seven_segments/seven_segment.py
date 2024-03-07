class SevenSegmentDisplay:
    def __init__(self, number_segment):
        self.count = 0
        self.number_segment = number_segment
        self.segments = ([])

    @staticmethod
    def display_horizontal():
        print("*  *  *  *")

    @staticmethod
    def display_vertical_left():
        print("""
        *
        *
        *""")

    @staticmethod
    def display_vertical_right():
        print("""
         *
         *
         *
              """)

    @staticmethod
    def display_vertical_left_and_right():
        print("*        *")
        print("*        *")
        print("*        *")

    def control_segment(self):
        self.display_horizontal()
        self.display_vertical_left_and_right()
        self.display_horizontal()
        self.display_vertical_left_and_right()
        self.display_horizontal()

    def put_in_a_list(self):
        my_list = []
        my_list += self.number_segment
        for number in my_list:
            self.count += 1
            if number not in ['0', '1']:
                raise ValueError(f"Character at {self.count} is invalid")
            if len(my_list) > 7:
                raise RuntimeError("Input should not be more than 7 numbers")
        return my_list

    def print(self):
        list1 = self.put_in_a_list()
        self.control_horizontal_printing(list1[0])
        self.control_vertical_printing(list1[1], list1[5])
        self.control_horizontal_printing(list1[6])
        self.control_vertical_printing(list1[2], list1[4])
        self.control_horizontal_printing(list1[3])

    def control_horizontal_printing(self, option: str):
        if option == '1':
            self.display_horizontal()

    def control_vertical_printing(self, option1, option2):
        if option1 == '1' and option2 == '1':
            self.display_vertical_left_and_right()
        elif option2 == '1' and option1 == '0':
            self.display_vertical_left()
        elif option2 == '0' and option1 == '1':
            self.display_vertical_right()


if __name__ == "__main__":
    segment = SevenSegmentDisplay("1011101")
    segment.print()
