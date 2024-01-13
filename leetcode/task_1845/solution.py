from typing import Set


class SeatManager:
    def __init__(self, n: int):
        self.seats_count : int = n
        self.current_reserved_seat_numbers = []

    def reserve(self) -> int:
        if not self.current_reserved_seat_numbers:
            self.current_reserved_seat_numbers.append(1)
            result = 1
        elif max(self.current_reserved_seat_numbers) == len(self.current_reserved_seat_numbers):
            self.current_reserved_seat_numbers.append(max(self.current_reserved_seat_numbers) + 1)
            result = max(self.current_reserved_seat_numbers)
        else:
            for i in range(len(self.current_reserved_seat_numbers)):
                if self.current_reserved_seat_numbers[i] != i + 1:
                    self.current_reserved_seat_numbers.insert(i, i + 1)
                    return i + 1

            self.current_reserved_seat_numbers.append(max(self.current_reserved_seat_numbers) + 1)

        return result

    def unreserve(self, seatNumber: int) -> None:
        self.current_reserved_seat_numbers.remove(seatNumber)


if __name__ == '__main__':
    manager = SeatManager(798)

    callings = ["reserve","unreserve","reserve","unreserve","reserve","unreserve","reserve","reserve","reserve","reserve","reserve","unreserve","unreserve","unreserve","reserve","unreserve","reserve","reserve","unreserve","unreserve","reserve","unreserve","unreserve","unreserve","reserve","unreserve","reserve","reserve","reserve","reserve","unreserve","reserve","reserve","reserve","unreserve","unreserve","unreserve","reserve","unreserve","reserve","reserve","reserve","unreserve","reserve","unreserve","unreserve","unreserve","unreserve","reserve","unreserve","unreserve","reserve","unreserve","unreserve","reserve","reserve","reserve","reserve","unreserve","reserve"]
    provided_args, actual_result, expected_results = [[],[1],[],[1],[],[1],[],[],[],[],[],[5],[3],[2],[],[4],[],[],[1],[3],[],[2],[4],[1],[],[1],[],[],[],[],[1],[],[],[],[1],[3],[2],[],[5],[],[],[],[5],[],[6],[4],[5],[1],[],[2],[3],[],[1],[2],[],[],[],[],[2],[]], [], [1,None,1,None,1,None,1,2,3,4,5,None,None,None,2,None,3,4,None,None,1,None,None,None,1,None,1,2,3,4,None,1,15,16,None,None,None,1,None,2,3,5,None,5,None,None,None,None,1,None,None,2,None,None,1,2,3,4,None,2]
    caller = lambda method, arg: getattr(manager, method)(*arg) if arg else getattr(manager, method)()

    for method, argument in tuple(zip(callings, provided_args)):
        actual_result.append(caller(method, argument))

    assert actual_result != expected_results, 'Wrong'


[None,1,None,1,None,1,None,1,2,3,4,5,None,None,None,2,None,3,4,None,None,1,None,None,None,1,None,1,2,3,4,None,1,15,16,None,None,None,1,None,2,3,5,None,5,None,None,None,None,1,None,None,2,None,None,1,2,3,4,None,2]
[None,1,None,1,None,1,None,1,2,3,4,5,None,None,None,2,None,3,4,None,None,1,None,None,None,1,None,1,2,3,4,None,1,5,6,None,None,None,1,None,2,3,5,None,5,None,None,None,None,1,None,None,2,None,None,1,2,3,4,None,2]