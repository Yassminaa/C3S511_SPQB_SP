#!/usr/bin/env python

import cdsapi
import numpy as np 
import os

c = cdsapi.Client()

# Here you define all the scripts parameters
stream =  'reanalysis-era5-single-levels'
var = 'surface_pressure'
day_list = ['01','02','03','04','05','06','07','08','09','10',
            '11','12','13','14','15','16','17','18','19','20',
            '21','22','23','24','25','26','27','28','29','30','31']
time = ['00:00','06:00','12:00','18:00']
file_fmt = 'netcdf'
target_grid = ['0.25','0.25']
yyyys = 1979
yyyye = 2019

yyyy = yyyys

while yyyy <= yyyye:

 for mm in ['01','02','03','04','05','06','07','08','09','10','11','12']:
             
    fout = '/data/ERA5_SPQB_V2/SP/'+'ERA5_SP_'+'0.25deg_'+str(yyyy)+str(mm)

    c.retrieve(stream,{
    'variable'      : 'surface_pressure',
    'product_type'  : 'reanalysis',
    'year'          : yyyy,
    'month'         : mm,
    'day'           : day_list,
    'grid'          : target_grid,
    'time'          : time,
    'format'        : file_fmt
    }, fout+'.nc')

    os.system('cdo daymean '+fout+'.nc '+fout+'_day.nc')
 
 yyyy += 1

