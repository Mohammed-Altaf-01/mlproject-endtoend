# Maths Score predictor ➗

<img src="readmestuff/mathslogo.jpg" style="width:100%;" >

Maths is a kind of subject which most of the Students suffer from, but there is a cache according the your skillset in reading and writing, you can predict what level of maths scores can you be able to achieve, also there are few other factors also but, that is very much relevant to the college student. So try it out here <a href="http://ec2-18-206-61-141.compute-1.amazonaws.com:8080/">click here to access</a>

# Table of Contents

- [Table of Contents](#table-of-contents)
- [Quickstart/Demo](#quickstartdemo)
- [DataSource](#datasource)
- [EDA](#Dataanalysis)
- [Model Building and Deployement](#deployement)
- [Installation](#installation)
- [License](#license)

# Quickstart/Demo

# DataSource

All the have been collected from the kaggle platform Students Performance
[link to the dataset](https://www.kaggle.com/datasets/rkiattisak/student-performance-in-mathematics)

The data is further cleaned and explored for further analysis and varioius models have been made and tested for the regression task of maths Score prediction

# EDA

There were a total of 8 features in a dataset of a thousand rows, with no null values.

#### Insight

- Three numerical and five categorical features, with each categorical feature having atleast of two unique values.
- description of the numerical data, all means are very close to each other - between 66 and 68.05;
- All standard deviations are also close - between 14.6 and 15.19;
- While there is a minimum score 0 for math, for writing minimum is much higher = 10 and for reading it is = 17

  <img src="readmestuff/kde average marks.jpg" style="width:100%;" >

  The above Histogram with probability distribution shows us the average marks of the students, those are between 50 to 80 approximately, and female students has higher average than the male student when compared with each other, shown in the second plot.

<img src="readmestuff/total score kde.jpg" style="width:100%;" >

Rather than average when compared with the total score, that is the score of all the subjects, female students tend to be always above the male students.

<img src="readmestuff/score violon plot.jpg" style="width:100%;" >

The chart above shows the distribution of marks for each subject included the reading writing and maths. For maths the average is between two boundaries 60-80, but for reading and writing score it is much lower around 55-80.

# Deployement

Regression models have been made using various algorithms such as RandomForest Regressors, Ridge Regression, Linear Regression, K nearest Neighbour Regressor,Decision Tree Regressor, Ada boost Regressor,XGboost Regressor and Cat Boost Regressor.

They were evaluated using metric R2Score, Mean absolute Error and Root Mean Square Error. After the evaluation, **Ridge Regressor** was the model with the highest accuracy of around 88 percent was used as final model, with MSE of around 14 marks.

# Installation

- Before the following steps make sure you have [git](https://git-scm.com/download), [Anaconda](https://www.anaconda.com/) or [miniconda](https://docs.conda.io/en/latest/miniconda.html) installed on your system
- Clone the complete project with `git clone https://github.com/Mohammed-Altaf-01/mlproject-endtoend.git` or you can just download the code and unzip it

- It is highly recommended to clone the main branch for running the project locally
- Once the project is cloned, open anaconda prompt in the directory where the project was cloned and paste the following block
  ```
  conda create -n StudentPerformanceenv python=3.10
  conda activate StudentPerformanceenv
  pip install -r requirements.txt
  ```
- And finally run the project with
  ```
  flask run
  ```
- Open the localhost url provided after running `app.py` and now you can use the project locally in your web browser.

[(Back to top)](#table-of-contents)

# License

[(Back to top)](#table-of-contents)

This is a personal project I have made using the modularized code and productionized it as a RESTFUL api instead of using the jupyter notebooks, anyonce can use this freely without any restrictions, but don't forget to tag 😊
