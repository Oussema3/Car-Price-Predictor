Pre-specialization Project 
# Car-Price-Predictor
Knowing approximately ur future car price from AI is much better than middleman 
Table of content 


Team members
Technologies
Challenges
Risks
Infrastructure
Existing solutions

Team members



➧ Oussema Ajmi - Web scraping - Data preparation - Data modeling (Pandas - Matplotlib ..)
                                  Front-end and Back-end for the Web application - Linear regression

I currently want to put my first steps towards data science , so i should at first improve my skills in web scraping .Also ,I had an experience in data analysing ,thus Data preparation and data modeling will help me to improve my knowledge in that field , furthermore to get the chance to experience that in a real challenge that will get me to know the real using of these concepts(data preparation and data modeling) , When it comes to linear regression , I have been studying it this period ( because I am willing to take the machine learning specialization in my school ) and there is no better pre step 


   
Technologies
Python (beautifulsoup) : for Web scraping
Python (Pandas , matplotlib) : for Data preparation and data modeling
Jypyter notebook
Linear regression
Flask : for web deployment



Resources :
      - www.kaggle.com
      - Linear regression analysis theory and computing (book : written by Xin Yan)
      - Datacamp (E-learning platform)
      - Faster web deployment with python serverless functions (article : written by Don schenk)
      - Web scraping with beautiful soup ( youtube tutorial : Corey schafer)
      - deploy machine learning model flask heroku (medium article : written by Nutan)

Beautifulsoup Vs Selenium : 

- Web scraping is becoming a necessary task especially in the AI field because it is kinda the only provider of the big data that the model will use to predict . To do this task there is a multiple methods and tools such as Beautifulsoup and Selenium . In this project I will be using Beautifulsoup . It is true that Selenium is pretty effective and can handle task to a good extent , also provide a better interact with the website ,However Beautifulsoup is the best option for you if you have a small task at hand ;all you need to do is install the request module and the Html parser of your choice   

- Flask vs Django :
In This project I will use flask in the web deployment 
Flask is best for beginners while Django is for more advanced machine learning deployments. Flask is a microframework making it more reliant on extensions for functionality. Django is a full-stack web framework. It comes with more ready to access features.



Challenges

In Tunisia cars markets , there is an economic phenomenon that might affect the real prices and furthermore the market , this last is the existence of the middleman .
The existence of middlemen in every field normally causes the unworthy increase of the prices.
 that they gave wrong prices for sellers which don't normally knows the real worth of their cars , their job is to buy cars as sheep as they can , not only that , they also use their experience to buy these cars with abnormal prices ( again exploiting the lack of knowledge of the clients) 
My application allows the user ( whether it is the seller or the customer) to know the real worth of the concernant product .
This application allows users to accomplish the procedure of selling with no fraud or abusing 
And it will be targeting both sellers  and buyers of cars .





Risks
Technical : 

Overfitting : Overfitting is a concept in data science, which occurs when a statistical model fits exactly against its training data. When this happens, the algorithm unfortunately cannot perform accurately against unseen data, defeating its purpose. Generalization of a model to new data is ultimately what allows us to use machine learning algorithms every day to make predictions and classify data .
Lack of Data : this application is targeting mainly the Tunisian market , so the provided data should contain the prices in Tunisia , but sadly the existing web sites of selling and buying cars do not contain a lot of articles , this last can affect the accuracy and the precision of the prediction .
Data updating ; the prices is something very variable , so every specific period of time the date should be updated 

Non-Technical  :

When talking about cars there are a lot of features that can affect the real price , however these features can not  be added in the application because it needs the human intervention to evaluate it ( whether the car has an old accident etc )
confidence in IT : Unfortunately nowadays people in Tunisia are not that familiar with the AI concept , and I think it is hard for people to believe that there is just a block of code that will predict a price of car 




 

Infrastructure
For the branching and merging workflow , I am working on this project on my own so I will work on the master branch in the initial phase. Once I reach a stable state with the most basic functionalities, I will  branch it out.
For the deployment , I will do the development work then I will deploy it to a server once the  version is efficient and stable 
The data i ll be populating is a data gathered from tunisian websites using the web-scraping 
For testing, we will be using mainly pytest for flask


Existing Solutions

When I looked for similar product i found out that this is only existing as projects in Kaggle etc , but what i think is that such solution is not existed yet (at least no website)


