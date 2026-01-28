import math


def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    if type(radiusOfCircle1) != int or type(radiusOfCircle2) != int or radiusOfCircle1<=0 or radiusOfCircle2 <=0:
        return "The values provided for one or both of the radius is not a valid integer, please input a valid positive integer"

    Area_for_the_radius_of_circle_1 = math.pi * (radiusOfCircle1 **2)
    Area_for_the_radius_of_circle_2 = math.pi * (radiusOfCircle2 **2)

    larger_area_of_the_two_circles = max(Area_for_the_radius_of_circle_1, Area_for_the_radius_of_circle_2)
    smaller_area_of_the_two_circles = min(Area_for_the_radius_of_circle_1, Area_for_the_radius_of_circle_2)

    percentage_of_the_larger_circle_area_that_can_be_covered_by_the_smaller_circle = smaller_area_of_the_two_circles/ larger_area_of_the_two_circles * 100
    return percentage_of_the_larger_circle_area_that_can_be_covered_by_the_smaller_circle



print(circleAreaCoverage(5,8))