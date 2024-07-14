from collections import defaultdict

def maxPeople(towns, cloud_start, cloud_end):
    towns = sorted(towns)
    cloud_start = sorted(cloud_start)
    cloud_end = sorted(cloud_end)

    start_i = 0
    end_i = 0
    active_clouds = set()

    cloud_coverage = defaultdict(int)
    free_population = 0
    for town_i in range(len(towns)):
        town_pos = towns[town_i][0]
        while start_i < len(cloud_start) and cloud_start[start_i][0] <= town_pos:
            active_clouds.add(cloud_start[start_i][1])
            start_i += 1
        while end_i < len(cloud_end) and cloud_end[end_i][0] < town_pos:
            active_clouds.remove(cloud_end[end_i][1])
            end_i += 1
        if len(active_clouds) == 1:
            towns[town_i][2] = list(active_clouds)[0]
            cloud_coverage[list(active_clouds)[0]] += towns[town_i][1]
        elif len(active_clouds) == 0:
            free_population += towns[town_i][1]

    return max(cloud_coverage.values(), default=0) + free_population

import sys

input = sys.stdin.read
data = input().splitlines()

num_towns = int(data[0].strip())
populations = [int(x) for x in data[1].strip().split()]
positions = [int(x) for x in data[2].strip().split()]
towns = [[pos, pop, -1] for pos, pop in zip(positions, populations)]
num_clouds = int(data[3].strip())
cloud_positions = [int(x) for x in data[4].strip().split()]
cloud_ranges = [int(x) for x in data[5].strip().split()]
cloud_start = [[cloud_positions[i]-cloud_ranges[i], i] for i in range(num_clouds)]
cloud_end = [[cloud_positions[i]+cloud_ranges[i], i] for i in range(num_clouds)]
result = maxPeople(towns, cloud_start, cloud_end)
print(result)
