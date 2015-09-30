import pandas
import numpy

directory='/Users/harsh/Desktop/Data Management and Visualization/python/courseFiles'

dataG=pandas.read_csv('%s/GDPpercapitaconstant2000US.csv' % directory,low_memory=False)
dataG=dataG.replace('nan',0)


dataC=pandas.read_csv('%s/indicator CDIAC carbon_dioxide_emissions_per_capita.csv' % directory,low_memory=False)
dataC=dataC.replace('nan',0)