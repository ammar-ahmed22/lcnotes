from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Combine and sort by position, descending
        pos_speed = sorted([(p, s) for p, s in zip(position, speed)], key=lambda x: x[0], reverse=True)
        print(pos_speed)

        limiting_car_times = []
        for p, s in pos_speed:
            time_to_target = (target - p) / s
            if not limiting_car_times or time_to_target > limiting_car_times[-1]:
                limiting_car_times.append(time_to_target)

        return len(limiting_car_times)
        



if __name__ == "__main__":
    # Include one-off tests here or debugging logic that can be run by running this file
    # e.g. print(solution.two_sum([1, 2, 3, 4], 3))
    solution = Solution()
