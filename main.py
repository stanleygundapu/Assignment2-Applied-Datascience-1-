#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 20:54:07 2023
@author: Stanley
"""

"""
# Libraries
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import skew
from scipy.stats import kurtosis


def readDataFrame(pathToFile):
    df = pd.read_csv(pathToFile)
    #creating a copy of original dataframe in to varibale
    transposedDf = df.copy()
    transposedDf[['Time' , 'Country Name']] = transposedDf[['Country Name' , 'Time']]
    transposedDf = transposedDf.rename(columns = {'Time': 'Country Name' , 'Country Name': 'Time'})

    # Return both the original and transposed DataFrames
    return df , transposedDf


def correlationMatrix(correlation_matrix):
    sns.set(style = 'white')  # Set the style of the plot
    plt.figure(figsize = (8 , 6))  # Set the size of the plot
    # Generate a heatmap with the correlation values
    sns.heatmap(correlation_matrix , annot = True , cmap = 'coolwarm' , linewidths = .5)
    plt.title('Correlation Matrix for Indicators' , fontsize = 18)
    # Show the plot
    plt.show()


def TimeRequiredToStartABusiness(data):
    # Set the figure size
    plt.figure(figsize = (12, 6))
    # num_indicators = len(data['Time required to start a business , female (days)'])
    # Exclude 'Country Name' from the count

    # Bar width and positions
    bar_width = 0.2
    bar_positions = np.arange(len(data['Time required to start a business, female (days)']))
    # Create bar plots for each indicator
    for i , indicator in enumerate(data[selected_indicators]):  # Exclude 'Country Name'
        plt.bar(bar_positions + i * bar_width , data[indicator] ,
                width = bar_width , label = indicator)

    # Set the labels and title
    plt.xlabel('Year')
    plt.ylabel('Values')
    plt.title('Grouped Bar Plot of Indicators for United Kingdom' , fontsize = 18)

    # Set the x-axis ticks and labels
    plt.xticks(bar_positions + bar_width , country_as_column_df['Time'])

    # Display the legend
    plt.legend()

    # Show the plot
    plt.show()


def startUpProcedures(data):
    # Set the figure size
    plt.figure(figsize = (10 , 6))
    countries = ['Sri Lanka' , 'Sweden' , 'United Kingdom' , 'Ukraine' , 'United States']
    # Plot a line for each country
    for country in countries:
        print(country)
        country_data = data[data['Country Name'] == country]
        plt.plot(country_data['Time'] ,
                 country_data['Start-up procedures to register a business (number) [IC.REG.PROC]'] ,
                 label = country)

    # Set labels and title
    plt.xlabel('Year')
    plt.ylabel('Startup Procedure')
    plt.title('Startup Procedure Over Years for Each Country' , fontsize = 18)

    # Display legend
    plt.legend()

    # Show the plot
    plt.show()


def total_tax_data_Graph(data):

    plt.figure(figsize = (8 , 8))
    plt.pie(data['Total tax and contribution rate'] , labels = data['Time'] ,
            autopct = '%1.1f%%' ,
            startangle = 90)
    # Set the title
    plt.title('Total tax and contribution rate for Sweden (2009-2019)' ,
              fontsize = 18)
    # Show the pie chart
    plt.show()


def TimeToStartBusinessPlot(data):
    # Set the figure size
    plt.figure(figsize = (10, 6))
    countries = ['Sri Lanka' , 'Sweden' , 'Switzerland' , 'United Kingdom' ,
                 'Ukraine' , 'United States']
    # Plot a line for each country
    for country in countries:
        country_data = data[data['Country Name'] == country]
        plt.plot(country_data['Time'] ,
                 country_data['Time required to start a business (days)'] ,
                 label = country)

    # Set labels and title
    plt.xlabel('Year')
    plt.ylabel('Time required to start a business')
    plt.title('Time required to start a business for Each Country' ,
              fontsize = 18)

    # Display legend
    plt.legend()

    # Show the plot
    plt.show()


def labourtaxContributions(data):
    data['Total tax and contribution rate'] = pd.to_numeric(data['Total tax and contribution rate'] ,
                                                                    errors = 'coerce')
    # Filter data for the United States in 2019
    us_data_2019 = data[(data['Country Name'] == 'United States')].dropna()
    plt.figure(figsize = (8 , 8))
    plt.pie(us_data_2019['Total tax and contribution rate'] , labels = us_data_2019['Time']
            , autopct = '%1.1f%%' ,
            startangle = 90)
    # Set the title
    plt.title('Total tax and contribution rate for United States (2013-2019)' , fontsize = 18)
    # Show the pie chart
    plt.show()


time_as_column_df , country_as_column_df = readDataFrame('Stanley.csv')
print("Time as column Dataframe")
print(time_as_column_df.head())
print("Country as column Dataframe")
print(country_as_column_df.head())

actualData = country_as_column_df.copy()

#STATISTICAL TECHNIQUES
print("STATISTICAL TECHNIQUES")

method_describes = pd.to_numeric(country_as_column_df['Total tax and contribution rate'] ,
                                 errors = 'coerce').describe()
print('First Method : Describes')
print(method_describes)

median = pd.to_numeric(country_as_column_df['Total tax and contribution rate'] ,
                       errors = 'coerce').median()
print("Second Method : Median")
print("Median value for total tax and contribution rate " , median)

data_for_kurtosis = pd.to_numeric(country_as_column_df['Total tax and contribution rate'] ,
                                  errors = 'coerce').dropna()
value_of_kurtosis =  kurtosis(data_for_kurtosis , fisher = False)
print("Third Method : Kurtosis")
print("kurtosis value for total tax and contribution rate is " , value_of_kurtosis)

data_for_skewness = pd.to_numeric(country_as_column_df['Total tax and contribution rate'] ,
                                  errors = 'coerce').dropna()
value_of_skewness = skew(data_for_skewness)
print("Fourth Method : Skewness")
print("Skewness value for total tax and contribution rate is " , value_of_skewness)

#Visualizations
#Visualization 1:
country_as_column_df['Total tax and contribution rate'] = \
    pd.to_numeric(country_as_column_df['Total tax and contribution rate'] , errors = 'coerce').dropna()
country_as_column_df['Labor tax and contributions'] = \
    pd.to_numeric(country_as_column_df['Labor tax and contributions'] , errors = 'coerce').dropna()
selected_indicators = ['Total tax and contribution rate' ,
                       'Labor tax and contributions']
correlation_matrix = country_as_column_df[selected_indicators].corr()
print("corr" , correlation_matrix)
#plot 1
correlationMatrix(correlation_matrix)

#VISUALIZATION 2:
country_as_column_df['Time required to start a business, female (days)'] = \
    pd.to_numeric(country_as_column_df['Time required to start a business, female (days)'] , errors = 'coerce')
country_as_column_df['Time required to start a business, male (days)'] = \
    pd.to_numeric(country_as_column_df['Time required to start a business, male (days)'] , errors = 'coerce')
country_as_column_df['Time required to start a business (days)'] = \
    pd.to_numeric(country_as_column_df['Time required to start a business (days)'] , errors = 'coerce')
selected_indicators = ['Time required to start a business, female (days)' ,
                       'Time required to start a business, male (days)' ,
                       'Time required to start a business (days)']

country_as_column_df = \
    country_as_column_df[country_as_column_df['Country Name'] == 'United Kingdom']

#Bar plot
TimeRequiredToStartABusiness(country_as_column_df)

#VISUALIZATION 3:
actualData['Time'] = pd.to_numeric(actualData['Time'] , errors = 'coerce')
lineGraphData = actualData[(actualData['Time'] >= 2010) & (actualData['Time'] <= 2015)]
startUpProcedures(lineGraphData)

#VISUALIZATION 4:
total_tax_data = actualData[actualData['Country Name'] == 'Sweden']
total_tax_data_Graph(total_tax_data)

#VISUALIZATION 5:
TimeToStartBusinessPlot(actualData)

#VISUALIZATION 6:
# df_2019 = actualData[actualData['Time'] == 2019]
us_data_2019 = actualData[(actualData['Time'] >= 2013) & (actualData['Time'] <= 2019)]
us_data_2019 = us_data_2019.copy()
labourtaxContributions(us_data_2019)














