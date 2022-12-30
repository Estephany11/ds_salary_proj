# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 18:05:22 2022

@author: Eddy Moros
"""

################# DATA CLEANING ################
import pandas as pd 
URL = "https://raw.githubusercontent.com/PlayingNumbers/ds_salary_proj/master/glassdoor_jobs.csv"

df = pd.read_csv(URL)

#Data columns: 
    # Index, nnamed, Job Title, Salary Estimate, Job Description, Company Name,....)
    # Headquarters, Size, Founded, Type of ownership, Industry, Sector, Revenue, Competitors
#Data size
    # (956,15)
# Data cleaning strategy: 
    # Remove salary text, 'employer provided salary:','per hour'
    # Company name text only 
    # State field
    # Age of company
    # Parsing of job description (jobs requiring python knowledge)

#Process

#1 Salary Parsing  
#Define "Hourly"and "employer provider' column, create column of 0,1 with if statement, 
    #lower return a string where all characters are lower case 

df['hourly']= df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided']= df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)
#Drop data with -1 in salary column
df = df[df['Salary Estimate'] != '-1']
## After cleaning we have a dataset of (742,15)
    #Drop text from salary column 
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
#Remove K and $
salary2 = salary.apply(lambda x: x.replace('K','').replace('$',''))
#Remove 'per hour' , EMPLOYER PROVIDENCE 
salary3 = salary2.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary:',''))

# Separate min salary and max salary 
df['min_salary']=salary3.apply(lambda x: x.split('-')[0])
df['max_salary']=salary3.apply(lambda x: x.split('-')[1])

#Convert datatype 
df['min_salary']=df['min_salary'].astype(int)
df['max_salary']=df['max_salary'].astype(int)
# Average salary
df['average_salary']=(df.min_salary+df.max_salary)/2

#Company name text only
#- There are company with a name followed by 3 digits number (positive rating)
#- There are company with a negative rating isn't followed by 3 digits number 
df['company_txt']= df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis=1)  
 

#State field 
df['job_state']=df['Location'].apply(lambda x: x.split(',')[1])
#Count number of values 
print(df.job_state.value_counts())

#Identify is the headquarters is the same as state
df['same_state']= df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis=1)

# Age of company 
df['age']= df["Founded"].apply(lambda x: x if x<1 else 2020-x)

#Job description
#Check out if one of these is required for the job position 

#Python
df['python']= df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
#Counting the number of jobs that have python
print(df['python'].value_counts())

#R studio 
 
df['r-studio']= df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
print(df['r-studio'].value_counts())

# spark 

df['spark'] =df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0) 
print(df['spark'].value_counts())

#excel 

df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
print(df['excel'].value_counts())

#aws 
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
print(df['aws'].value_counts())

#drop first column 
#print(df.columns)

df_final = df.drop(['Unnamed: 0'], axis=1)

#to csv
df_final.to_csv('salary_data_cleaned.csv', index=False)

#pd read the csv file: 
    
#pd.read_csv('salary_data_cleaned.csv'



