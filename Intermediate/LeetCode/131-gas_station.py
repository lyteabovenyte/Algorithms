"""
    https://leetcode.com/problems/gas-station
"""
from typing import List

def gas_station(gas: List[int], cost: List[int]) -> int:
    n, total_surplus, surplus, start_point = len(gas), 0, 0, 0

    for i in range(n):
        total_surplus += gas[i] - cost[i]
        surplus += gas[i] - cost[i]
        if surplus < 0:
            surplus = 0
            start = i + 1
    return -1 if (total_surplus < 0) else start

print(gas_station([5,1,2,3,4], [4,4,1,5,1]))
print("------")
print(gas_station([1,2,3,4,5], [3,4,5,1,2]))
print("------")
print(gas_station([2,3,4], [3,4,3]))