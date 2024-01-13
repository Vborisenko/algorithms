class Solution:
    @staticmethod
    def isPathCrossin(path: str) -> bool:
        coordinates = [(0, 0)]

        for unit_direction in path:
            dir_map = {
                'N': (0, 1),
                'S': (0, -1),
                'E': (1, 0),
                'W': (-1, 0)
            }
            coordinates.append(
                (
                    coordinates[-1][0] + dir_map[unit_direction][0],
                    coordinates[-1][1] + dir_map[unit_direction][1],
                )
            )

        return not len(coordinates) == len(set(coordinates))


if __name__ == '__main__':
    # coordinate_string = input()
    coordinate_string = 'NESWW'

    assert not (coordinate_string.replace('N', '')
            .replace('S', '')
            .replace('W', '')
            .replace('E', '')), 'Extra symbols'

    print(Solution.isPathCrossin(coordinate_string))
