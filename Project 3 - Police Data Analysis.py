#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


data=pd.read_csv(r"C:\Users\kumak\Desktop\selfstudy\Python\Project 3 - Police Data Analysis.csv")
data


# In[7]:


#first step clean my data :


# In[8]:


#iwould like to have an idea about the type of data iam wroking with :
data.dtypes


# In[9]:


#now iwould like to see how many missing values i have and where 
data.isnull().sum()


# In[10]:


#iwill attempt to try to clean all at once first


# In[11]:


#i have missing values in some rows in which i do have float :
object_columns = data.select_dtypes(include=['object','float64']).columns
data[object_columns] = data[object_columns].fillna('Unknown')


# In[12]:


data.isnull().sum()


# In[13]:


#Q. 2) Question ( Based on Filtering + Value Counts ) 


# In[16]:


# Step 1: Filter and Extract Data
filtered = data[data['driver_gender'].isin(['M','F'])]
filtered


# In[33]:


gender_violation_counts = filtered.groupby('driver_gender')['violation'].value_counts()
gender_violation_counts


# In[47]:


# Define colors for the bars
colors = ['blue', 'orange', 'green', 'purple', 'red']

# Create a bar plot with custom colors
ax = gender_violation_counts.plot(kind='bar', color=colors)

# Adding labels and title
plt.xlabel('Driver Gender')
plt.ylabel('Number of Violations')
plt.title('Violation Counts by Gender')

# Customize the legend
ax.legend(title='Violation Types')

# Display the plot
plt.show()


# In[42]:


#For Speeding , were Men or Women stopped more often ? 
speeding_records =data[data.violation =='Speeding'].driver_gender.value_counts()
speeding_records


# In[ ]:


#iwill add some quickl visuqlisation


# In[44]:


# Define colors for the bars
colors = ['blue', 'pink']
# Create a bar plot
plt.bar(speeding_records.index, speeding_records.values, color=colors)

# Adding labels and title
plt.xlabel('Driver Gender')
plt.ylabel('Number of Speeding Records')
plt.title('Speeding Records by Driver Gender')

# Display the plot
plt.show()


# In[ ]:


#3) Question ( Groupby ) - Does gender affect who gets searched during a stop ?


# In[48]:


searched = filtered.groupby('driver_gender')['search_conducted'].value_counts()
searched


# In[49]:


#another way:
data.groupby('driver_gender').search_conducted.sum()


# In[50]:


#see value count
data.search_conducted.value_counts()


# In[ ]:


#Q. 4) Question ( mapping + data-type casting ) - What is the mean stop_duration ?


# In[60]:


#recall the data (before)
data


# In[62]:


data.stop_duration.value_counts()


# In[63]:


data['stop_duration']=data['stop_duration'].map({'0-15 Min':7.5,'16-30 Min':24,'30+ Min ':45})


# In[64]:


data['stop_duration']


# In[66]:


#recall the data (after)
data


# In[85]:


data['stop_duration'].mean()


# In[ ]:


#Q. 5) Question ( Groupby , Describe ) - Compare the age distributions for each violation.


# In[79]:


#the result are messy hence we will choose another way
comparison=filtered.groupby('driver_age').violation.sum()
comparison


# In[ ]:


#data.groupby('coloumn_1').coloumn2.describe()


# In[88]:


describe=data.groupby('driver_age').violation.describe()
describe


# In[97]:


data.groupby('violation').driver_age.describe()


# In[ ]:




