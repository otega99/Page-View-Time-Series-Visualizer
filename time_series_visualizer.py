import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df.date=pd.to_datetime(df.date,format="%Y-%m-%d")
df.set_index('date',inplace=True)

# Clean data
df = df[(df['value']<df['value'].quantile(0.975))& (df['value']>df['value'].quantile(0.025))]


def draw_line_plot():
    # Draw line plot
    fig=plt.figure()
    plt.plot(df.index,df['value'],color='red')
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([df.index.year,df.index.month]).mean().unstack()

    # Draw bar plot
    fig=df_bar.plot(kind='bar',xlabel='Years',ylabel='Average Page Views',figsize=(16,14)).get_figure() 
    plt.legend(['January','February','March','April','May','June','July','August','September','October','November','December'])




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box=df_box.sort_values(by='date')
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    df_box['month_num']=df_box.date.dt.month
    df_box=df_box.sort_values('month_num')
    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2,figsize=(20,8))
    fig1=sns.boxplot(x=df_box.year,y=df_box.value,ax=axes[0])
    fig1.axes.set_title("Year-wise Box Plot (Trend)", fontsize=16)
    fig1.set_xlabel("Year", fontsize=14)
    fig1.set_ylabel("Page Views", fontsize=14)
    fig2=sns.boxplot(x=df_box.month,y=df_box.value,ax=axes[1])
    fig2.axes.set_title("Month-wise Box Plot (Seasonality)", fontsize=16)
    fig2.set_xlabel("Month", fontsize=14)
    fig2.set_ylabel("Page Views", fontsize=14)




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
