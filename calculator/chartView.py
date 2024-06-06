from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .views import Chart
import random
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
import random
from datetime import datetime
from mpl_toolkits.mplot3d import Axes3D
import random
matplotlib.use('Agg')

aString= ['calculator','people','chart','todoapp','exampleView','logout']

def generate_random_financial_data(start_date, end_date, num_points):
    dates = pd.date_range(start_date, end_date, periods=num_points)
    data = {
        'Open': np.random.rand(num_points) * 100,
        'High': np.random.rand(num_points) * 100,
        'Low': np.random.rand(num_points) * 100,
        'Close': np.random.rand(num_points) * 100
    }
    df = pd.DataFrame(data, index=dates)
    df['High'] = df[['Open', 'Close']].max(axis=1) + df['High'] / 10
    df['Low'] = df[['Open', 'Close']].min(axis=1) - df['Low'] / 10
    return df


class ChartView(Chart):

  def get(self, request):
    filenames = []
    #barchart
    objects = ['01/01/2019', '01/01/2020', '01/01/2021','01/01/2022','01/01/2023']
    y_pos = np.arange(len(objects))
    qty = [random.randint(1, 30) for _ in range(len(objects))]
    plt.bar(y_pos, qty, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Quantity')
    plt.title('Sales')
    plt.savefig('calculator/static/css/images/barchart.png')
    filenames.append('barchart.png')
    plt.clf()

    #linechart
    line_qty = [random.randint(1, 30) for _ in range(len(objects))]
    # Line chart
    plt.plot(y_pos, line_qty, marker='o')
    plt.xticks(y_pos, objects)
    plt.ylabel('Quantity')
    plt.title('Sales Line Chart')
    plt.savefig('calculator/static/css/images/linechart.png')
    filenames.append('linechart.png')
    plt.clf()

    # Data for the pie chart
    pie_labels = ['Category A', 'Category B', 'Category C']
    pie_values = [random.randint(100, 300) for _ in pie_labels]
    # Pie chart
    plt.pie(pie_values, labels=pie_labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
    plt.title('Sales Distribution')
    plt.savefig('calculator/static/css/images/piechart.png')
    filenames.append('piechart.png')
    plt.clf()
    
    # Sample data for 3D plot
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x**2 + y**2))
    # Set up a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis')
    # Save the plot as a file
    plt.savefig('calculator/static/css/images/3dplot.png')
    filenames.append('3dplot.png')
    plt.clf()
    # Sample data for the heatmap
    data = np.random.rand(10, 10)  # Generating random data for demonstration

    # Create the heatmap
    plt.imshow(data, cmap='hot', interpolation='nearest')
    #plt.colorbar()  # Optional: Adds a colorbar to the side
    # Save the heatmap as a file
    plt.savefig('calculator/static/css/images/heatmap.png')
    filenames.append('heatmap.png')
    plt.clf()

    context={'aString': aString, 'filenames': filenames}
    return render(request, self.template_name, context)


