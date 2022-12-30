# -*- coding: utf-8 -*-
################# NOT WORKING ###########


"""
Created on Sun Dec 25 16:09:39 2022

@author: Eddy Moros
"""

import glassdoor_scrapper as gs 
import pandas as pd 
#path is where the project is located
#change to / 
#add :chromedriver
path = "C:/Users/Eddy Moros/Desktop/Esteph_stuff/Python/ds_salary_project/chromedriver"

df = gs.get_jobs('data scientist',15,False,path, 15)

