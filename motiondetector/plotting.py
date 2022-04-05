from motion_detector import df #calls the motion_detector code

from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S") #converts Start and End columns to string data types so they appear correctly in hover
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")
cds=ColumnDataSource(df)

p=figure(x_axis_type='datetime',height=100,width=500,sizing_mode="stretch_both",title="Motion Graph")
p.yaxis.minor_tick_line_color=None #removes numbers on y axis
p.ygrid[0].ticker.desired_num_ticks=1 #removes row lines

hover=HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])
p.add_tools(hover)

q=p.quad(left="Start",right="End",bottom=0,top=1,color="green", source=cds) #source=cds is telling bokeh to use the data source and what it is. Means you don't have to point to dataframe against each column

output_file("Graph.html")

show(p)