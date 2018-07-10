

def rotate_pd_plotting_scatter_matrix(plts):
'''
Rotates the axis display name models

Example:
plts = pd.plotting.scatter_matrix(df[colnames[1:-1]], figsize=(10,10))
rotate_pd_plotting_scatter_matrix(plts)

'''

  for x in range(len(plts)):
    for y in range(len(plts)):
    # to get the axis of subplots
    ax = plts[x, y]
    # to make x axis name vertical  
    ax.xaxis.label.set_rotation(90)
    # to make y axis name horizontal 
    ax.yaxis.label.set_rotation(0)
    # to make sure y axis names are outside the plot area
    ax.yaxis.labelpad = 50