# Start by copying this code block into a new file called dataconversion.py in your unit 2 folder. This is an ungraded activity.

# Successfully convert all of the following variables to another type and print the result
# If the conversion prints without errors, you did the conversion correctly

a = 115         #int -> string
b = 3.14        #float -> string
c = "68"        #string -> int
d = "True"      #string -> boolean
e = True        #boolean -> string
f = False       #boolean -> string
g = '10110111'  #byte -> int
h = "2.54"      #string -> float
i = 100         #int -> float
j = 10.0        #float -> int
k = 254         #int -> byte

num = 115
num_str = str(115)

num_float = 3.14
float_str = str(num_float)

num_str = 68
num = int(num_str)

bool_str = "True"
bool_val = bool(bool_str)

bool_val = True
bool_str = str(bool_val)

bool_val = False
bool_str = str(bool_val)

binary_num = '10110111'
num = int(binary_num, 2)

float_str = "2.54"
num = float(float_str)

num = 100
num_float = float(num)

num_float = 10.0
num = int(num_float)

num = 254
binary_num = bin(num)