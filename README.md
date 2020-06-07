# Recommender Systems Applied to Steam Network Data

## Summary
A recommender system is a model that seeks to predict the preferences a user would give to a collection of items. Today recommender systems form the basis of the targeted advertisements and product suggestions we see throughout commercial industry. Broadly speaking, recommender systems fall into three major classes: content-based filtering, collaborative filtering, and novel hybrid methods. Content-based filtering involves creating "profiles" of different classes of items and recommending users items that fall into the same or similar profiles to items they have already rated. Meanwhile, collaborative filtering involves identifying similar users based upon known common ratings, then recommending items to a target user based on what other similar users have rated highly. 

Both methods can be implemented using a variety of approaches and algorithms. Content-based filtering is often implemented via k-means clustering, bayesian classifiers, decision trees, and artificial neural networks. Collaborative filtering is often implement via nearest-neighbor algorithms or by latent factor models that rely on matrix factorization. 

For this project I will implementing a latent factor collaborative filtering model on the Steam dataset collected in 2015 by O'Neill, Vazirpour, Wu, and Zappala (available here: https://steam.internet.byu.edu/). Steam is a videogame distribution service and gaming network with hundreds of millions of users and roughly 34,000 games available on the platform. This dataset contains a near exhaustive scrape of the Steam network at the time of retrieval. In particular, it contains records of every public user's games, the amount of time they have spent playing each game, the user's friends list, a list of the "steam groups" a user belongs to, the age of the user's account, their last active day, and many other features. For this project, I will just be looking at the games each user owns and take that as implicit feedback data.

## Repository Guide

The "Notebooks" folder contains three iPython notebooks. "Project Overview" explains how I processed the BYU data and explains the math behind Latent Factor recommendation system models and how we can train them using a method known as alternating least squares. "Data Exploration" contains some basic exploratory data analysis of the data. "Tuning and Evaluation" contains our implementation, tuning, and testing of this model using PySpark. I recommend reading them in this order: "Project Overview" --> "Data Exploration" --> "Tuning and Evaluation"

The "Code" folder contains two python files that have the code I used to process the BYU data. Unfortunately I am unable to upload the original data files since they exceed the maximum file size allowed by Github. However, one could get them by downloading the .sql from the BYU site, splitting it, and locating the files containing the the Games_1 table. "text_parsing.py" has the code for parsing the raw .txt data from the BYU source and is similar to what is described in the "Project Overview" notebook. "joining_sampling.py" has the code for sampling the data and combining it into one large numpy array for the rest of the analysis.

## Additional Reading/ Resources

[1] "Matrix Factorization Techniques for Recommender Systems" by Bell, Koren, Volinsky (2009)

[2] "Recommender Systems: The Textbook" by Aggarwal (2016)

[3] "Building a Recommendation System in TensorFlow: Overview" (Google cloud article, [link](https://cloud.google.com/solutions/machine-learning/recommendation-system-tensorflow-overview))

[4] "Collaborative Filtering" (Google Machine Learning course, [link](https://developers.google.com/machine-learning/recommendation/collaborative/basics))
