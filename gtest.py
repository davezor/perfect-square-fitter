import math
"""
Given a number find the largest perfect squares that fit inside of it and return as a list
"""

def solution(area):
    # Your code here
    temp = area
    area_list = []
    
    while temp > 0:
        # Check if we're square
        if math.sqrt(temp) % 1 == 0:
            area_list.append(temp)
            
            # Start working on next largest square
            temp = area - sum(area_list)
            continue
        
        temp = temp - 1

    return area_list
