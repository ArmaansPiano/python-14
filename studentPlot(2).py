import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv
import plotly.graph_objects as go
df=pd.read_csv("studentMarks.csv")
data=df["Math_score"].tolist()
def random_set_of_mean(counter):
   dataset=[]
   for i in range(0,counter):
      random_index=random.randint(0,len(data)-1)
      value=data[random_index]
      dataset.append(value)
   mean=statistics.mean(dataset)
   return mean
mean_list=[]
for i in range(0,1000):
      set_of_means=random_set_of_mean(100)
      mean_list.append(set_of_means)
standard_deviation=statistics.stdev(mean_list)
mean=statistics.mean(mean_list)
print("mean is ->",mean)
first_std_deviation_start,first_std_deviation_end=mean-standard_deviation,mean+standard_deviation
second_std_deviation_start,second_std_deviation_end=mean-(2*standard_deviation),mean+(2*standard_deviation)
third_std_deviation_start,third_std_deviation_end=mean-(3*standard_deviation),mean+(3*standard_deviation)
#fig=ff.create_distplot([mean_list],["Math Score"],show_hist=False)
#fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
#fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode="lines",name="Standard Deviation 1 START"))
#fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="Standard Deviation 1 END"))
#fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode="lines",name="Standard Deviation 2 START"))
#fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="Standard Deviation 2 END"))
#fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.17],mode="lines",name="Standard Deviation 3 START"))
#fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode="lines",name="Standard Deviation 3 END"))
df=pd.read_csv("data3.csv")
data=df["Math_score"].tolist()
sample1=statistics.mean(data)
print("data3 mean is", sample1)
z_score=(sample1-mean)/standard_deviation
print("Z score is:", z_score)
fig=ff.create_distplot([mean_list],["Math Score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[sample1,sample1],y=[0,0.17],mode="lines",name="iPad Students"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="Standard Deviation 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="Standard Deviation 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode="lines",name="Standard Deviation 3 END"))
fig.show()