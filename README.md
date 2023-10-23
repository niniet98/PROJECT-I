# DA - Data-cleaning & Data-wrangling

## Overview
The goal of this project is to perform data analysis on a messy data set Shark Attack using different techniques of data cleaning and manipulation in order to get answers to the asked questions.

## Requirements
This code was written in Python and Jupyter Notebook.

Have been used the following libraries:
- Numpy
- Pandas
- matplotlib.pyplot
- Seaborn

## Instructions
If you have the original dataset, add it in the `data` folder and run the `main.py` to see the art of magic. If not, just keep reading and then make your own conclusions.

## Process
**1. Exploring data:** First contact with the dataset in order to know what is the data about.

**2. Research questions:** Before starting with the messy dataset, I've raised 3-5 questions related with the provided information in the dataset.
    
**3. Cleaning data:** With the performed questions, I've cleaned the dataset dropping data I do not care about and null rows that bothers.

**4. Transforming data:** Standardizing data of interest to get a clean dataset with the data I need to answer the questions.

**5. Visualizing data:** Plotting subsets of data to visualize the data in order to extract conclusions for the raised questions.

# Story-telling based on the data analysis
## Does shark attacks have increased over the years?

In a first approach related to this question I made a graph tracing the evolution of shark atacks over the years but I saw that between 1543 and 1800 there was almost no activity, so I filtered the data in order to show the evolution over the years since 1800.

![trace_evolution](https://github.com/niniet98/PROJECT-I/blob/main/images/trace_evolution.png?raw=true)

Having a deep look to the graph, is highlighted that shark attacks have increased over the years, but why? Maybe because they are angry with humanity for the clima change or it's just because each human generation becomes more dumb?

## Are surfers and swimmers the most exposed to shark attacks?

For the graph presented below, I computed the average number of shark attacks by activity to identify those activities that exceed the mean. This allows us to make a detailed comparison of the frequency of shark attacks in relation to various activities. By highlighting the activities that are above the average, we can gain a clearer insight into which ones potentially pose a higher risk in terms of encounters with sharks.

![common_activity](https://github.com/niniet98/PROJECT-I/blob/main/images/most_common_activity.png?raw=true)

As the most common activities during shark attacks there's surfing on the top, and then fishing followed of swimming.
In a quick research on internet I've read that sharks may confuse a human on a surboard with a sealion because of its shape, that it's similar,  but that the bite is usually not as lethal in humans.

**Which Gender Dominates the Scene?**

In addition, I wanted to show the attacks in the mentioned activities by gender, and it can be seen that the male gender is the most attacked.

![common_activity_sex](https://github.com/niniet98/PROJECT-I/blob/main/images/most_common_activity_sex.png?raw=true)

## Are the young people the most attacked by sharks?

According to the graph below, 50% of the people injured by sharks are between 17 and 35 years old and the median is at 24 years old, which means that 25% of the people attacked are between 17 and 24 years old. Then there are some outliers which are rare data, i.e., according to the data set provided, it is rare for a 70 year old person to be attacked.

![age_attack_pattern](https://github.com/niniet98/PROJECT-I/blob/main/images/age_attack_patterns.png?raw=true)

With this information we can relate the previous conclusion to this, highlighting that younger people are the ones who tend to perform activities in the sea where there are more shark attacks.

## Are sharks more active at night?

For this hypothesis I have made a graph but with half of the data, since the rest was not reported in the dataset. I do not know if it is very valid since this information cannot be contrasted without half of the data but it does not answer the question I have raised, as I have always thought that marine life at night is more active than during the day.

![shark_activity](https://github.com/niniet98/PROJECT-I/blob/main/images/shark_activity.png?raw=true)

## Are men the ones who provoke sharks the most and that's why they end up torn apart?

It is clear that men sometimes act without thinking (no offense). It was only necessary to bring out this graph to confirm what we already know (thanks to society, obviously). The graph shows the overall number of provoked shark attacks and obviously men are the ones who do it the most, but I don't understand it. I would like to think that it is because they are the vast majority who practice activities in the water.
For all the men reading this, can you answer the question?

![men_behavior](https://github.com/niniet98/PROJECT-I/blob/main/images/men_behavior.png?raw=true)

# CONCLUSIONS
- Clima change is doing a lot of **DAMAGE** to the earth and humans are losing neurons in each generation.
- Be alert while surfing, there may be a shark lurking around that wants to take a bite out of you.
- Young people like the madness, the adrenaline rush.
- I still don't know when sharks are most active.
- I still don't undersand why men are that dumb. (no offense)

