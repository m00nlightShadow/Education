from functools import reduce


class Phone:
    _counter = 0

    def __init__(self, number: str):
        self.number = number

    def take_incoming_calls(self):
        self._counter += 1
   
    def show_counter_of_calls(self):
        return self._counter


phone_1 = Phone('0638894811')
phone_2 = Phone('0638865811')
phone_3 = Phone('0638894825')
phone_1.take_incoming_calls()
phone_1.take_incoming_calls()
phone_1.take_incoming_calls()
phone_2.take_incoming_calls()
phone_3.take_incoming_calls()
phone_3.take_incoming_calls()
phone_3.take_incoming_calls()
phone_3.take_incoming_calls()
phone_3.take_incoming_calls()
phone_3.take_incoming_calls()

list_of_calls = [phone_1.show_counter_of_calls(), phone_2.show_counter_of_calls(), phone_3.show_counter_of_calls()]


def counter_of_calls(counter_list):
    return reduce(lambda x, y: x + y, counter_list)


with open('Calls_info.txt', 'w+') as file:
    file.write(f'We received {counter_of_calls(list_of_calls)} calls')
