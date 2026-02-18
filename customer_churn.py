import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\saini\Downloads\archive\WA_Fn-UseC_-Telco-Customer-Churn.csv")

# check the top and  last values 
print(data.head())
print(data.tail())

# check the info of the data set 
print(data.info())

# check the shape  of the  data set 
print(data.shape)

# check the null values 
print(data.isnull())  # having  0 null value in the output


print(data.describe)

# QUE -  Why customer are leaving
# QUE - Which customers  are at risk
# QUE - how to reduce  churnn 
# QUE -  How churn  impact   revenue 


data["SeniorCitizen"] = data["SeniorCitizen"].apply(lambda x: "Yes" if x == 1 else "No")
print(data["SeniorCitizen"] )

# print(data)

# random 25 rows 
random_rows = data.sample(n=25)
print(random_rows)

random_25_rows = data.iloc[0:100:5]
print(random_25_rows)



print(data.dropna(inplace=True))  # fix the values  


# Drop customer id 
print(data.drop("customerID" , axis=1  , inplace=True))


# chnage data type
data["TotalCharges"]=pd.to_numeric(data["TotalCharges"] , errors="coerce")
print(data.dtypes)


# How many  customers are leaving
leaving_customer = data[data["Churn"] =="Yes"]
print(leaving_customer)

print(data["Churn"].value_counts())


# cross tab is majorly  used to analyis relationship b/w  to catogorical variables using  frequency counts .


# What is the over all churn rate ?

churn_counts = data["Churn"].value_counts()
churn_rate = (churn_counts / churn_counts.sum()) * 100
print(churn_rate)

# Normalize method - 

# churn_rate = (data["Churn"].value_counts(normalize=True)*100)
# print(churn_rate)


# Which gender churns more ?
gender_churn = pd.crosstab(data["gender"], data["Churn"] , normalize=True)*100
print(gender_churn)


# Which contract has lowesst  churn.
Lowest_churn = pd.crosstab(data["Contract"], data["Churn"])
print(Lowest_churn)


# Payment method has loweest churn
payment_method = pd.crosstab(data["PaymentMethod"], data["Churn"])
print(payment_method)


# Show churn % inside each gender.
gender_churn1 = pd.crosstab(data["gender"]  , data["Churn"], normalize="index" )*100
print(gender_churn1)
 

#Which tenure group churn most?

# tenure_churn = pd.crosstab(data["tenure"] , data["Churn"] , normalize=True )*100
# print(tenure_churn)

bins =  [0,12,24,48,60, 100]
labels = ["0-1Y" , "1-2Y" , "2-4Y" , "4-5Y", "5Y+"]
Tenure_Group =  pd.cut(data["tenure"] , bins = bins , labels = labels)
print(Tenure_Group)


# Monthly charges 
bins = [0,100,500,1000,1500,2000]
labels = ["Avg Payer", "Normal payer" , "pro member" ,"elite"  , "elite+"]
Monthly_charges = pd.cut(data["MonthlyCharges"] , bins=bins , labels =labels )
print(Monthly_charges)


# Build Risk scoring
data["RiskScore"] = 0

data.loc[data["Contract"] == "Month-to-month","RiskScore"] +=3 
data.loc[data["InternetService"] == "Fiber Optics", "RiskScore"] +=2
data.loc[data["PaymentMethod"] == "Electronic check	", "RiskScore"] +=2
data.loc[data["tenure"] <12, "RiskScore"]  +=3

data["RiskLevel"] = pd.cut(data["RiskScore"],bins=[0,2,4,6,8,10],labels=["Least","Low","Average","Medium","High"])
print(data["RiskLevel"])

#percentage of the Risklevel comes  in the churn 
RiskLevel_churn = pd.crosstab(data["RiskLevel"], data["Churn"] , normalize="index")*100
print(RiskLevel_churn)

#Plot Graph for better anaylises

# Count of Customers Churned  Percentage of Customers Churned

ax = sns.countplot(x="Churn" , data = data)
ax.bar_label(ax.containers[0])
plt.title("Count of customers by churn ")
plt.show()


# for percentage data of the churn 
plt.pie(churn_counts,labels=churn_counts.index, autopct='%1.1f%%' )
plt.title("percentage of churned customers")
plt.show()


# bar graph  for gender and churn 

ax = sns.countplot(data=data, x="gender", hue="Churn")
plt.title("Count of Customers by Gender and Churn")
plt.show()

#for SeniorCitizen and churn
ax = sns.countplot(data=data, x="SeniorCitizen", hue="Churn")
plt.title("Count of Customers by SeniorCitizen and Churn")
plt.show()


# stacted  bar plot 

ct = pd.crosstab(data['SeniorCitizen'], data['Churn'], normalize='index') * 100

ax = ct.plot(kind="bar", stacked=True, figsize=(7,5))

for container in ax.containers:
    ax.bar_label(container, fmt="%.1f%%")

ax.set_xticklabels(["Not Senior", "Senior"])

plt.title("Churn by Senior Citizen (Percentage)")
plt.ylabel("Percentage")
plt.xlabel("Customer Type")
plt.legend(title="Churn")
plt.show()


# histogram  on tenure 

sns.histplot( data = data, x="tenure",  bins=75  , hue = "Churn")
plt.xlabel("Tenure")
plt.ylabel("Frequency")
plt.title("Histogram of Tenure")
plt.show()


# count of cutomers and contracts - bar graph 
# plt.bar(x = "Contract" , y= )


# subplots - 



