from numpy import log2

def sanitized_input(prompt, input_type=None, input_min=None, input_max=None):
    if input_min is not None and input_max is not None and input_max < input_min:
        raise ValueError("Minimum must be less than or equal to the maximum.")
    while True:
        user_input = input(prompt)
        if input_type is not None:
            try:
                user_input = input_type(user_input) 
            except ValueError:
                print("Input type must be {0}.".format(input_type.__name__))
                continue
        if input_max is not None and user_input >= input_max:
            print("Input must be less than {0}.".format(input_max))
        elif input_min is not None and user_input <= input_min:
            print("Input must be greater than {0}.".format(input_min))
        else:
            return user_input

x = sanitized_input ("Enter a value for x: ", float, 0)
y = sanitized_input ("Enter a value for y: ", float)

step1 = x**y
step2 = log2(x)

print ("X**y = ",step1)
print ("log(x) = ",step2)