# MIS480: Module 8: Option #1: Capstone Project -- Business Intelligence Solutions for U.S. Organization

### Motivation:

For my Capstone Project, I wanted to create a product that would have real-world benefits. So, I selected a fleet analysis for the company that I worked for.
The overall goal was to create an algorithm to predict when each company truck would reach 200,000 miles, which appeared to be on the higher side of a truck's
anticipated life expectancy. According to an iSeeCars study, 2.8% and 2.4% of Toyota Tacoma and Ford F-150s have over 200,000 miles 
compared to vehicles across their segment (WAKELIN, 2022). These percentages represent that the mentioned trucks are twice as likely to reach 200,000 miles 
compared to the other vehicles used in the analysis (WAKELIN, 2022). Addons to my project that I plan to complete in the future include:

* More efficient code (ie. loops with dataframes) 
* Addition of predictive dates for maintenance/service of vehicles to aid in scheduling and substitute truck coordination
* Creation of a dashboard

### Limitations:

Throughout the creation of this project, I have identified a few limitations that hinder the algorithm's performance. The company I work for does not utilize
a database for tracking/maintaining the mileage for each truck. All data was collected manually and inputted by myself over a three or four-day period. Due to time
constraints and the lack of a database, I only procured six months' worth of mileage data, limiting the algorithm's overall accuracy and predictive abilities.
Not to mention the possibility of human error in manually entering 1500+ data points. In addition to manually entering the data, there were many missing 
or not submitted mileage reports -- presenting incomplete data. I used imputation to fill in those missing data points.

### Build Status: 

Last Updated: 06/05/2022. 
As of the last update the code is incomplete. 

### Screenshots: 

### Sample view of four of the trucks from the fleet and their mileage over time. Blank values were filled with 
### linear interpolation. 
![Dashboard 1](https://user-images.githubusercontent.com/80931300/172066498-9fe41d5f-9be3-41d4-866f-9628f494731f.png)

### Average and Median Miles Driven By All Trucks. 
![Dashboard 1 (1)](https://user-images.githubusercontent.com/80931300/172066785-9e62cae8-1b9f-476d-923d-995712184b68.png)

### Model Output Prediction vs Actual Graph 
![Screenshot 2022-06-05 150424](https://user-images.githubusercontent.com/80931300/172070623-d5b6faee-1ce3-4ef7-90ca-5aacc5181735.png)

### Model Output Error 
![2](https://user-images.githubusercontent.com/80931300/172070627-316fe4f3-8737-4473-9c23-73e4bf74770b.png)


### Forecast for Truck 187
![newplot](https://user-images.githubusercontent.com/80931300/173206123-651f0ea5-8aae-466b-8cbc-f758ddc73cb9.png)


### Forecast for Truck 191
![newplot (1)](https://user-images.githubusercontent.com/80931300/173206125-e6df5b94-47e8-49f1-8f4e-5019a5905306.png)


### Forecast for Truck 222
![newplot (2)](https://user-images.githubusercontent.com/80931300/173206126-81226295-d9e8-4603-a125-149852c3ec3b.png)


### Forecast for Truck 241
![newplot (3)](https://user-images.githubusercontent.com/80931300/173206129-2f8d433b-a3e5-42d4-9d95-ec69e53e3ca6.png)



### Developer Tech:

![python](https://user-images.githubusercontent.com/80931300/171454184-234efe87-d1f6-4b16-8593-edded51f5506.png)![datascience](https://user-images.githubusercontent.com/80931300/171454403-5a9f23bb-3384-4730-b918-ff6705b42813.png)

### References
Filho, M. (2010). Mario Filho | Data Science | Machine Learning. Mario Filho | Data Science | Machine Learning. https://www.mariofilho.com/how-to-predict-multiple-time-series-with-scikit-learn-with-sales-forecasting-example/

‌Wakelin, N. (2022, February 28). Best gas mileage trucks. Best Gas Mileage Trucks - iSeeCars.com. Retrieved June 5, 2022, from https://www.iseecars.com/articles/best-gas-mileage-trucks 
