#!/usr/bin/env python3

import sys

def is_horizontal(segment):
    return segment[0][1] == segment[1][1]


def is_vertical(segment):
    return segment[0][0] == segment[1][0]


def normalise_segment(input_segment):
    #segments can run all ways. we want to make this kind of standardised so we have less headaches when finding intersections

    #we want to end up with a segment that either runs up (increasing y coordinate) or to the right (increasing x coordinate)

    #deconstruct the tuple into two points:
    point_1 = input_segment[0]
    point_2 = input_segment[1]

    #now we check whether it runs horizontal or vertical:
    if is_vertical(input_segment): #if x coordinates match, then it is vertical, and we want to sort by y coordinate
        if point_1[1] >= point_2[1]: 
            return (point_2, point_1) #swap the coordinates if the first y coordinate is greater than the second
        else:
            return input_segment
    elif is_horizontal(input_segment): #if y coordinates match, then it is horizontal, and we want to sort by x coordinate
        if point_1[0] >= point_2[0]:
            return (point_2, point_1) #swap the coordinates if the first x coordinate is greater than the second
        else:
            return input_segment

    else: #oops it's broken, gtfo
        print(f'found a segment that is diagonal: {point_1}, {point_2}, this is bad and i can\'t deal with this. exiting!')
        sys.exit()

def wire_segments(wire):
    #output a list of ((x,y),(x,y)) tuples indicating the beginning and end of every wire segment (a straight horizontal or vertical line between two grid coordinates)

    #turn the string into a list of strings so we can iterate over it
    wire = wire.split(',')
    
    #origin point is (0,0); we are assuming this is the initial 'previous point'
    prev_point = (0,0)
    
    segments = []
    for i in wire:
        #iterate over all the directions

        direction = i[0].upper() #get the direction letter (U, D, L, R)
        length = int(i[1:]) #get the length of the wire as a number

        #store the previous point in vars:
        x = prev_point[0]
        y = prev_point[1]
        
        #generate new coordinates based on directions:
        if direction == 'U':
            y += length
        elif direction == 'D':
            y -= length
        elif direction == 'L':
            x -= length
        elif direction == 'R':
            x += length
        new_point = (x, y)
        
        segments.append(normalise_segment((prev_point, new_point))) #this is the actual segment we generate

        prev_point = new_point

    return segments


def intersection_point(segment1, segment2):
    #returns None if no intersection or an intersection coordinate tuple ((x1,y1),(x2,y2)) if an intersection point is found

    #first, get the 'No intersection' cases out of the way. 
    #the easiest: the segments run parallel. (for convenience we assume that segments don't overlap)
    
    #horizontal. both segments have two matching y coordinates.
    if is_horizontal(segment1) & is_horizontal(segment2):
        return None

    #vertical is basically the same, only checking x coordinates:
    if is_vertical(segment1) & is_vertical(segment2):
        return None

    #now we have a possibility for an intersection
    #we find the vertical segment first.
    if is_vertical(segment1):
        vertical_segment = segment1
        horizontal_segment = segment2
    else: 
        vertical_segment = segment2
        horizontal_segment = segment1

    #this makes our life easier because all the cases are now the same. saves half the amount of checks :)
    
    #here you will find the conditions for an intersection. dotn want to explain, should be fairly obvious. refer to the structure of the coordinate tuple up above
    if vertical_segment[0][0] >= horizontal_segment[0][0]:
        if vertical_segment[1][0] <= horizontal_segment[1][0]:
            if vertical_segment[0][1] <= horizontal_segment[0][1]:
                if vertical_segment[1][1] >= horizontal_segment[1][1]: 
                    #we have an intersection, and the intersection point is the x coordinate of the vertical segment, and the y coordinate of the horizontal segment:
                    return (vertical_segment[0][0], horizontal_segment[0][1])
    
    #that didn't work, so there's no intersection. return None
    return None


def find_all_intersections(wire1, wire2):
    #returns list of coordinates with all intersections between wire1, wire2. these are both wire_segments lists as defined above
    intersection_coords = []
    for i in wire1:
        for j in wire2:
            intersection = intersection_point(i, j)
            if intersection is not None and intersection != (0,0):
                intersection_coords.append(intersection)

    return intersection_coords

def manhattan_distance(point1, point2):
    #returns manhattan distance between two points
    return abs(point1[0]-point2[0])+abs(point1[1]-point2[1])


#---------------------
        
with open(sys.argv[1]) as f:
    wires = f.readlines()

#we assume two wires cause im lazy

wire_1 = wires[0]
wire_2 = wires[1]
segments_1 = wire_segments(wire_1)
segments_2 = wire_segments(wire_2)

ints = find_all_intersections(segments_1, segments_2)
distances = []
for i in ints:
    distances.append(manhattan_distance((0,0),i))

distances.sort()
print(distances[0])
