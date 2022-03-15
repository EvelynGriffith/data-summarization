# Data Summarization

## Evelyn Griffith

## Program Input and Output

### What is the output from running the following commands?

`poetry run datasummarizer --data-file input/data.txt`

```🔬 The data file contains 100 data values in it! Let's get summarizing!

🧮 The computed mean is 0.9919614640914002!
```

### What are the first five lines of the contents of the file that is input into the `datasummarizer`?

```2.5169521900e+0
1.8703141360e+0
-3.4505452520e-2
2.3580068020e+0
1.5516879500e+0
```

## Source Code and Configuration Files

### Describe in detail how your provided source code works

#### A function that summarizes a data set by computing the mean

```def compute_mean(numbers: List[float]) -> float:
    """Compute the mean for a list called numbers which contains floats."""
    # sum the list of the numbers
    Sum = sum(numbers)
    # determine the length of the list of numbers
    Size = len(numbers)
    # as long as the computation will not be an
    # undefined division by zero, compute the mean
    for i in numbers:
        if i in numbers != 0:
            mean = Sum / Size
            return mean
    # https://stackoverflow.com/questions/58400652/average-returning-a-value-even-when-list-is-empty
    # if the list was empty, then return a mean that is "not a number"
    return float("NaN")
```

This function's purpose is to compute the mean of a set of numbers in a file called data.txt. The first line of code is the function specification. This line will name the function as well as allow us to specify the types of inputs and outputs we will have within the function. In this case they are floats and Lists. The next few lines are specifying variables that will do basic computations such as add up all of the numbers in the list and add up the amount of numbers in the list. The rest of the function is a for loop that will allow the function to determine whether or not a number is 0. If the number is not zero it will calculate the mean and return that. If it is not able to return the mean, the function will return a float that is "not a number" as is seen in the funal line of the function.

#### A function that transforms data into a list of floating-point values

```def transform_string_to_number_list(data_text: str) -> List[float]:
    """Transform a string called data_text into a number to store into a list as a float."""
    # create an empty list of values called data_number_list
    data_number_list = []
    # iterate through the data_text using the splitlines function
    for line in data_text.splitlines():
        # convert every one of the text-based values to a floating-point value
        data_number_list.append(float(line))
    # return the list of floating-point values that represent the
    # values that were converted from a string to a float
    return data_number_list
```

This function is going to transform a number from a string into a float value, and then append that value to a list called data_number_list. The first line of the function is, as always, the function specification. It will define the type values for the inputs and outputs for the function, which in this case are a string and a list of floats.This second line in the function is an empty list called data_number_list. This is important because it allows for a space to be created so that when we append a value to the list, it will be able to go to that list. The next thing is a for loop. This for loop is going to iterate through the file called data.txt and split up each line so that so that we can then convert the individual lines (which are numbers) into a float. This line will then append that float to the data_number_list list. Then finally the function will return data_number_list once the file no longer has another number for it to append.

## Professional Development

### What was the greatest technical challenge that you faced and how did you overcome it? Why?

The biggest challeng I had during this lab was understanding the NaN or "Not a Number" concept/implementation. My problem was that I didnt understand that the test cases were considering an empty list to return a value that is considered not a number, so I didnt know how to return that value as Not a Number. I just typed `return: Not a number` and expected that to work. What I needed to do was return a float("NaN") so that the computer knows what to return.

### After completing this assignment, what is one task that you want to practice more? Why?

I think I should study the commands of python further so that the NAN problem doesnt occur again. I think that this could be especially useful because it will allow me to understand all code more and know how to code more on my own without the help of todos.

### After completing this assignment, what is one experience for which you are grateful? Why?

I am really proud of myself for being able to complete this lab almost entirely on my own. I feel like I am making a lot of progress toward being able to code without the todos guiding me and that makes me really happy.
