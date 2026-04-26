import os 
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
import matplotlib.pyplot as plt
from cs1033_evaluator import evaluate_lab7

MODEL_1_INPUT_FILE, MODEL_2_INPUT_FILE, MODEL_3_INPUT_FILE = input().split()
################################################################################
# Please do not edit anything above this line.


# Function to read a file and return speed list.
def get_speed(file_name):
    speed = []
################## YOUR CODE STARTS HERE. ######################################
# Read the file and get the values into the list.
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                parts = line.split()
                speed.append(int(parts[1]))  # second column is speed (km/h)
################## YOUR CODE ENDS HERE. ########################################     
    return speed


# Function gets the filename and returns the speeds in metres per second format.
def convert_kmph_to_ms(filename):
################## YOUR CODE STARTS HERE. ######################################
# Read the values using get_speed function and return the converted values as a list.
    speeds_kmph = get_speed(filename)
    speeds_ms = [round(s * 5 / 18, 4) for s in speeds_kmph]
    return speeds_ms
################## YOUR CODE ENDS HERE. ########################################


# Function gets the speeds as a list of integers in metres per second format and returns the acceleration.
def get_acceleration(speeds):
    #Acceleration list is initialized to zero.
    #i.e. acceleration at time=0 is zero.
    acceleration = [0]
################## YOUR CODE STARTS HERE. ######################################
    #Write the code to calculate the acceleration.
    for i in range(1, len(speeds)):
        delta_speed = speeds[i] - speeds[i - 1]  # m/s
        delta_time = 0.1                          # s (100 ms interval)
        accel = round(delta_speed / delta_time, 2)
        acceleration.append(accel)
################## YOUR CODE ENDS HERE. ########################################
    return acceleration


######## WRITE THE CODE FOR TASK 1.4 and 1.5 BELOW #############################

# Use MODEL_1_INPUT_FILE, MODEL_2_INPUT_FILE, MODEL_3_INPUT_FILE variable
# names instead of 'model1.txt', 'model2.txt', 'model3.txt' to read files

# Get speeds in m/s for each model
model1_speeds = convert_kmph_to_ms(MODEL_1_INPUT_FILE)
model2_speeds = convert_kmph_to_ms(MODEL_2_INPUT_FILE)
model3_speeds = convert_kmph_to_ms(MODEL_3_INPUT_FILE)

# Get acceleration lists for each model
model1_accel = get_acceleration(model1_speeds)
model2_accel = get_acceleration(model2_speeds)
model3_accel = get_acceleration(model3_speeds)

# Time axis in seconds: 0.0, 0.1, 0.2, ..., 1.0
time = [round(i * 0.1, 1) for i in range(len(model1_accel))]

# TASK 1.5 - Write maximum acceleration for each model to max_acceleration.txt
with open('max_acceleration.txt', 'w') as f:
    f.write("model1" + "\t\t\t" + str(max(model1_accel)) + "\n")
    f.write("model2" + "\t\t\t" + str(max(model2_accel)) + "\n")
    f.write("model3" + "\t\t\t" + str(max(model3_accel)) + "\n")

# TASK 1.4 - Plotting the lines with different styles
plt.plot(time, model1_accel, label='model_1')
plt.plot(time, model2_accel, label='model_2')
plt.plot(time, model3_accel, label='model_3')

# Adding labels and title
plt.xlabel('Time(s)')
plt.ylabel('Acceleration(ms-2)')
plt.title('Acceleration Vs Time')
plt.legend()
plt.show()

################################################################################
# Please do not edit anything below this line.
evaluate_lab7()

##################### End of the programme #####################################