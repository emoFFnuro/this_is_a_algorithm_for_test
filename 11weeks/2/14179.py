import sys , bisect
input = sys.stdin.readline

## use mathmatica method

dummy_n , dummy_m = map(int , input().split())
builds = list(map(int ,input().split()))

def countRainDrop(buildings):
    answer = 0
    for i in range(len(buildings)):
        left_high = max(buildings[:i+1])
        right_high = max(buildings[i:])
        pick_low = min(left_high , right_high)
        answer = answer + abs(buildings[i] - pick_low)
    return answer

print(countRainDrop(builds))