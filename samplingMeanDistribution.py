import pandas as pd
import statistics
import random
import plotly.figure_factory as ff

df = pd.read_csv('medium_data.csv')

data = df['reading_time'].tolist()

population_mean = statistics.mean(data)
print('POPULATION MEAN IS {}'.format(population_mean))

# CODE TO FIND MEAN FOR RANDOM 30 DATA POINTS
def random_set_of_data_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

# FUNCTION TO PLOT GRAPH

def show_fig(mean_of_samples):
    df = mean_of_samples
    mean = statistics.mean(mean_of_samples)
    print("MEAN OF SAMPLING DISTRIBUTION",mean)
    
    
    fig =ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.show()



# FUNCTION TO GET MEAN OF 30 DATA POINTS 100 TIMES AND PLOT THE GRAPH

def setup():
    mean_of_samples = []
    for i in range(0,100):
        set_of_mean = random_set_of_data_mean(30)
        mean_of_samples.append(set_of_mean)

    show_fig(mean_of_samples)

# CALL SETUP
setup()

# IN THIS DATA WE CAN SEE THAT THE MEAN OF TOTAL DATA AND THE MEAN OF 30 DATA POINTS * 100 TIMES IS ALMOST SAME AND SET OF DATA POINTS FOLLOWS NORMAL DISTRIBUTION WHILE TOTAL DATA DOES NOT FOLLOW NORMAL DISTRIBUTION INSTEAD IT IS FOLLOWING SAMPLE MEAN DISTRIBUTION.
# THE STANDARD DEVIATION OF TOTAL DATA WILL BE 1/10th OF THE TOTAL DATA MEAN BECAUSE OF A FORMULA GIVEN BELOW
# FORMULA OF SAMPLING DATA
#Standard deviation of sampling mean distribution = Standard Deviation of Population / sqrt (number of data in each sample)


# BUT IN PROJECT I ONLY NEED TO FING MEAN SO I DID NOT SONE THE STANDARD DEVIATION
