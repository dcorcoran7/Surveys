"""
This module is a collection of statistical functions for analyzing
the results of a non-nominal survey question.

To test your current solution, run the `test_my_solution.py` file.
Refer to the instructions on Canavs for more information.

Author name: David Corcoran
I have neither given nor received unauthorized assistance on
this assignment. I did not fabricate the answers to my
survey question.
"""
__version__ = 1

# 0) Question and Results
SURVEY_QUESTION = "How many inches tall are you?"
SURVEY_RESULTS = [67, 68, 70, 69, 67, 74, 73, 74, 70, 69]

# 1) count
'''This function sums the amount of values in the list results and
returns the variable total withe the amount
'''
def count(results):
    total = 0
    for num in results:
        total += 1
    return int(total)

# 2) summate
'''This funtion gathers all values in the list results and sums the numbers
based upon their numerical value. The varuable total is returned
'''
def summate(results):
    total = 0
    for num in results:
        total += num
    return int(total)

# 3) mean
'''This function uses the total of the summate function and divides it by the
total returned by the count fucntion. It takes in the ist results and returns the
average of all the values in the list rounded to 2 decimal places
'''
def mean(results):
    if results == []:
        return None
    else:
        mean = summate(results) / count(results)
        return round(mean, 2)

# 4) maximum
'''This function returns None if the list results is empty and returns the largest value
in the list if it is not empty
'''
def maximum(results):
    if results == []:
        return None
    else:
        highest = 0
        for num in results:
            if highest < num:
                highest = num
        return highest

# 5) minimum
'''This function returns None if the list results is empty and returns the smallest value
in the list if it is not empty
'''
def minimum(results):
    if results == []:
        return None
    else:
        lowest = 1000
        for num in results:
            if lowest > num:
                lowest = num
        return lowest

# 6) median
'''This function returns the middle value in the list results when the list is ordered by numerical value from
cmallest to largest. It takes the list results as an argument and returns the variable median 
'''
def median(results):
    if results == []:
        return None
    else:
        new_results = sorted(results)
        index = int((count(new_results)) / 2)
        median = new_results[index]
        return median

# 7) square
'''This function takes in the list results and returns each value in the list sqaured into a new list called squared_list
'''
def square(results):
    squared_list = [num ** 2 for num in results]
    return squared_list

# 8) standard_deviation
'''This function returns None if the list results is less than 2 and retursn the standard deviation if the list contains
more than 2 values. It uses the previous functions of square, summat, and count to create new variables to form a new standard deviation
equation called SD. The function returns SD rounded to 2 deciaml places
'''
def standard_deviation(results):
    if results == []:
        return None
    elif count(results) < 2:
        return None
    else:
        sum_squared = summate(square(results))
        sum_of_values = summate(results)
        count_of_values = count(results)
        SD = (((sum_squared) - (sum_of_values * sum_of_values) / (count_of_values)) / (count_of_values - 1)) ** 0.5
        return round(SD, 2)


# The following code can be used to try out your functions.
# Uncomment each line as you implement the functions to try them out.
# When you have implemented each function, copy the output from the
#   console into a comment below.
if __name__ == "__main__":
    print("We asked", count(SURVEY_RESULTS), "people the following question.")
    print('"'+SURVEY_QUESTION+'"')
    print("Here are the statistical results:")
    print("\tSum:", summate(SURVEY_RESULTS))
    print("\tMean:", mean(SURVEY_RESULTS))
    print("\tMedian:", median(SURVEY_RESULTS))
    print("\tMaximum:", maximum(SURVEY_RESULTS))
    print("\tMinimum:", minimum(SURVEY_RESULTS))
    print("\tSquare:", square(SURVEY_RESULTS))
    print("\tStandard Deviation:", standard_deviation(SURVEY_RESULTS))
   
# Your survey stats from your own unique question go here:
# We asked 10 people the following question.
#"How many inches tall are you?"
#Here are the statistical results:
#	Sum: 701
#	Mean: 70.1
#	Median: 70
#	Maximum: 74
#	Minimum: 67
#	Square: [4489, 4624, 4900, 4761, 4489, 5476, 5329, 5476, 4900, 4761]
#	Standard Deviation: 2.69