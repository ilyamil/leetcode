from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1] and interval[1] > merged[-1][1]:
            merged[-1][1] = interval[1]
        elif interval[1] <= merged[-1][1]:
            continue
        else:
            merged.append(interval)
    return merged


if __name__ == '__main__':
    test_cases = [
        {'input': [[1,3],[2,6],[8,10],[15,18]], 'output': [[1,6],[8,10],[15,18]]},
        {'input': [[1,4],[0,4]], 'output': [[0,4]]},
        {'input': [[1,4],[4,5]], 'output': [[1,5]]},
        {'input': [[1,2],[2,2],[2, 3]], 'output': [[1,3]]},
        {'input': [[1,4],[2,3],[2, 5]], 'output': [[1,5]]},
    ]
    for i, test_case in enumerate(test_cases):
        ans = merge(test_case['input'])
        print(i, ans, ans == test_case['output'])
