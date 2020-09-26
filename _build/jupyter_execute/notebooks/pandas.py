# pandas 101

This section provides a brief introduction to pandas. The pandas library is a key component for performing data science in Python for a number of reasons. First (and most importantly), it provides two data types, series and data frame, that allow you to store and manipulate data in a way that is useful for analysis. Second, it is incredibly useful for importing and exporting data in a wide variety of formats. Finally, it allows users to generate descriptive analyses, including both summary statistics and visualizations. This section provides an introduction to the main capabilities of pandas relevant to data analysis. 

Most of the things that you will want to do in Python require importing libraries. By convention, pandas is imported as `pd`. Additionally, we enable the ability for pandas graphics to be displayed within the notebook with `%matplotlib inline`. 

%matplotlib inline

import pandas as pd

# Reading data

In the summer of 2017, the Washington Post produced a [report](https://www.washingtonpost.com/graphics/2018/investigations/unsolved-homicide-database/) on murder clearance rates in U.S. cities. The also released the [data](https://github.com/washingtonpost/data-homicides) they collected on Github as a csv file. We can create a new dataframe, called `df`, using the [pandas](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html) `read_csv` method.  

df = pd.read_csv('data/homicide.csv')

By default, `read_csv` assumes a comma separator, but this could be customized by adding the  `sep=` parameter. So a pipe-delimited version of the file could be read with:

~~~python
df = pd.read_csv('data/homicide.psv', sep='|')
~~~

Additionally, read_csv can access files directly from the web.

```python
csv_url = 'https://raw.githubusercontent.com/washingtonpost/data-homicides/master/homicide-data.csv'

df = pd.read_csv(csv_url)
```



# Learning about your dataframe

After loading a dataframe, best practice is to get a sense of the data with the `head`, `sample`, `info` and `describe` methods. `head` shows the first five rows of the dataframe.

df.head()

In addition to the data in the csv file, an index has been created to identifiy each row. By default, this is an interger starting with 0. 

It can also be useful to examine random rows from the data frame using `sample`. In this case, I'll look at four random rows.

df.sample(4)

If the dataset is wide, middle columns will not be displayed. Also, if text fields are long, only the first few characters will be shown. These can both be adjusted using pandas [display settings](https://pandas.pydata.org/pandas-docs/stable/options.html). 

`info` can be used to explore the data types and the number of non-missing cases for each variable.

df.info()

`describe` provides summary statistics for all the numeric variables. 

df.describe()

The column headers can be extracted using `keys`.

#### df.keys()

If you wanted to look at the bottom of the dataframe, you can use `tail`. Both `head` and `tail` allow you to change the number of rows displayed from the default five.

df.tail(3)

`sample` displays random rows from the dataframe.

df.sample(5)

## Dataframe Exercise 1

Display the first four rows of the dataframe `df`.  


# Type your answer here


df.head(4)

# Working with variables


As a reminder of the contents of the dataframe, here's a radom row.

df.sample(1)

You can access the contents of a specific column (also knows as a feature or variable) by enclosing the name in brackets, similar to the process that returns the value of a dictionary key.

df['victim_age']

This returns a series containing the index and values for the column. As this has many values, pandas only displays the top and bottom 30 cases. 

The same `describe` method can be called on a single column.

df['victim_age'].describe()

`value_counts` methods returns the value frequencies in descending order.

df['state'].value_counts()

## Dataframe Exercise 2
Explore the `disposition` and `victim_race` columns in the dataframe.  

# Your answer here

display(df['disposition'].value_counts())

display(df['victim_race'].value_counts())

If you wanted to store the results, the `values` method can be used to produce an array containing all the values in order.

ages = df['victim_age'].values
len(ages)

first_age = ages[0]
display(first_age)

## Dataframe Exercise 3
Can you display seven values from somewhere in the middle of our age variable?


# Your answer here

ages[452:459]

## Titanic Exercise 1

A well-known data set is the list of Titanic passengers. A version can be found in the data folder called, "titanic.csv". Open the file as a new dataframe <code>titanic_df</code>. How many cases? How many columns? What can you find out about the data?





# Plots

pandas also has plotting capabilies, such as histograms (`hist`) and a correlation matrix (`scatter_matrix`).  

df['victim_age'].hist();

df['victim_race'].hist();

Plots of individual variables, or series in pandas terminology, are attributes of the data type. That is, you start with the thing you want to plot, in this case `df['victim_age']`, and append what you want to do, such as `.hist()`. 

A second type of plots, such as scatter plots, are methods of the dataframe. 

df.plot.scatter(x='lon', y='lat')

You could look at the other dataframe plotting methods on the helpful [pandas visualizations page](https://pandas.pydata.org/pandas-docs/stable/visualization.html). Alternatively, typing tab after `df.plot.` also reveals your options.

<img src="images/auto.png"  width="150px" align="left" /><p>






Want to know about `hexbin`? Again, the helpful webpage linked above is useful, but you can also append a question mark to the end of the command to bring up the documentation. 


```df.plot.hexbin?```

<img src="images/docstring.png" width = "80%" align="left"/>

A third group of plots are part of the pandas plotting library. In these cases, the thing you want to plot is the first, or only, parameter passed, as is the case with the correlation matrix. 

pd.plotting.scatter_matrix(df);

Finally, you can also create subplots using the `by` option. Note that `by` accepts a series, or dataframe column, rather than a column name. 

df['victim_age'].hist(by = df['victim_sex'],
                      bins = 20);

By default, `by` produces separate x and y scales for each subgraph. This is why it appears to be a relatively large number of deaths of very young females. The numbers between men and women at this age are comparable, but the very large number of male deaths in their 20s results in very different xscales for the graphs. This option can be changed with the `sharex` or `sharey` option. 

df['victim_age'].hist(by = df['victim_sex'],
                      bins   = 20,
                      sharex = True,
                      sharey = True);



#### Other descriptives

Pandas also has a method for producing crosstabs. 

pd.crosstab(df['victim_race'], df['disposition'])

Note that since this is a pandas method, and not one of a specific dataframe, you need to be explicit about which datatframe each variable is coming from. That is why the first parameter is not `'victim_race'` but `df['victim_race']`. 

`normalize` can be used to display percentages instead of frequencies. A value of `index` normalized by row, `columns` by column, and `all` by all values.

pd.crosstab(df['victim_race'], df['disposition'], normalize='index')

Since this returns a dataframe, it can be saved or plotted.

cross_tab = pd.crosstab(df['victim_race'], df['disposition'], normalize='index')

cross_tab

cross_tab.to_csv('data/crosstab.csv')

## Titanic Exercise 2

In your Titanic dataframe, run a crosstab between sex and survived. Anything interesting?





In order to highlight a meaningful characteristic of the data, you can sort before plotting. 

cross_tab.sort_values(by='Closed by arrest')

cross_tab.sort_values(by='Closed by arrest').plot(kind   = 'barh',
                                                  title  = 'Disposition by race')

#### Subsets

Similar to a list, a dataframe or series can be sliced to subset the data shown. For example, `df[:2]` will return the first two rows of the dataframe. (This is identical to `df.head(2)`.)

df[:2]

df.head(2)

This also works for specific columns.

df['reported_date'][:3]

#### Dates

Unfortunately, pandas does not automatically understand that the `reported_date` variable is a date variable. Luckily, we can use the `to_datetime` method to create a new variable from the `reported_date` variable that pandas is able to interpret as a set of dates. The format is `%Y%m%d` because the original date is in the "YYYMMDD" format, and `coerce` places missing values where the data can be translated, rather than stopping variable creation completely. 

df['reported_date'].head()

df['date'] = pd.to_datetime(df['reported_date'], 
                            format='%Y%m%d', 
                            errors='coerce')

df['date'][:3]

From the new series, we can extract specific elements, such as the year.

df['year'] = df['date'].dt.year

As before, `value_counts` and plots can give some sense of the distribution of the values.

df['year'].value_counts()

`value_counts` returns a pandas series with an index equal to the original values (in this case the year), and the series values based on the frequency. Since years have an inherent order, it makes sense to sort by the index before we plot them.

df['year'].value_counts().sort_index(ascending = False).plot(kind='barh')

`crosstab` can also create groups based on more than one variable for the x or y axis. In that case, you pass a list rather than a single variable or series. To make this more clear, you can create the lists before creating the crosstab.

y_vars = [df['state'], df['city']]
x_vars = df['year']

pd.crosstab(y_vars, x_vars)

Crosstab returns a dataframe with the column and index names from the values in the original dataset. Since a list was passed, the datatframe has a `MultiIndex`. This can be useful for cases where you have nested data, like cities with states or annual data on multiple countries.

pd.crosstab(y_vars, x_vars).index.names

### Index

df.head()

By default, the index is a series that starts with 0. If your data includes a set of unique identifiers, however, it is helpful to use this as the index, especially if you intend on merging your data with other data sources. In this dataframe, each row has a unique value for `uid`.

df.set_index('uid', inplace=True)

df[:5]

## Titanic Exercise 3

In your Titanic dataframe, set the index to the <code>PassengerId</code> column. Confirm that it did want you wanted it to do.





#### Subsetting

You can view a subset of a dataframe based on the value of a column. 

Let's say that you wanted to look at the cases where the victim's first name was "Juan". You could create a new series which is either `True` or `False` for each case.

df['victim_first'] == 'JUAN'

You could store this new true/false series. If you placed this in brackets after the name of the dataframe, pandas would display only the rows with a True value.

is_juan = df['victim_first'] == 'JUAN'
df[is_juan]

More commonly, the two statements are combined.

df[df['victim_first'] == 'JUAN']

With this method of subsetting, pandas isn't return a new dataframe; it is simply hiding some of the rows. If you want to create a new dataframe based on this subset, you'll need to append `copy()` to the end. 

new_df = df[df['victim_first'] == 'JUAN'].copy()

new_df.head()

As this selection method returns a dataframe, it can be stored. The following creates two dataframes, containing just the cases from 2016 and 2017 respectively.

df_2017 = df[df['year'] == 2017].copy()
df_2016 = df[df['year'] == 2016].copy()


df_2017['year'].value_counts()

df_2016['year'].value_counts()

`value_counts` confirms that you've grabbed the correct cases.

Alternatively, you may want to limit your dataset by column. In this case, you create a list of the columns you want. This list is also placed in brackets after the name of the dataframe.

## Titanic Exercise 4

Create a new dataframe with just the female passengers. Check your work.





#### More subsets

columns_to_keep = ['victim_last', 'victim_first', 'victim_race', 'victim_age', 'victim_sex']

df[columns_to_keep]

As before, you can you use `copy` to create a new dataset.

victim_df = df[columns_to_keep].copy()

victim_df.head()

As with the row selection, you don't need to store the column names in a list first. By convention, these two steps are combined. However, combining the steps does create an awkward pair of double brackets.

place_df = df[['city', 'state', 'lat', 'lon']].copy()

place_df.head()

#### Merging

There are several different ways to combine datasets. The most straightforward is to merge two different datasets that share a common key. To merge `place_df` with  `victim_df`, for example, you can use the datframe `merge` method. 

merged_df = place_df.merge(victim_df, left_index=True, right_index=True)

merged_df.head()

### Stacking dataframes

We can also combine datasets using through *concatenation*. Using the pandas `concat` method, we can join pandas objects along a specified axis. As an example, look at the dataframe we created looking only at the year 2016:


df_2016 = df[df['year'] == 2016]
len(df_2016)

Let's say we decide we'd like to combine this dataframe with a dataframe looking at the year 2017:

df_2017 = df[df['year'] == 2017]
len(df_2017)

We can use `concat` to combine the dataframes into a single dataframe, `recent_df`:

recent_df = pd.concat([df_2017, df_2016])

len(recent_df)

To return to a previous example, we can use `concat` to merge our victim and location dataframes as well. Here, we'll want to specify that we're concatenating along colums. we'll indicate this by setting `axis` to 1.

pd.concat([victim_df, place_df], axis = 1)

### New features

We can use the features already available in our dataframe to create additional features. For example, if we wanted to create a feature representing victims' year of birth, we could define a feature generating the difference between the age of homocide victims and the years homocides occurred. 

df['birth_year'] = df['year'] - df['victim_age_numeric']

df['birth_year'].describe()

Another example might involve generating a feature indicating whether or not homocide victims were minors:

df['minor'] = df['victim_age'] <= 18

df['minor'][:10]

Using the `mean` pandas method, we're then able to determine the proportion of homocide victims who were minors. 

df['minor'].mean()

## Titanic Exercise 5

Create a new variable in your Titanic dataframe that identifies people who paid fares in the top 25% of all fares paid.





### Back to some pandas string manipulation fun.

def title_case(text):
    return text.title()

title_case('JUAN')

### The apply magic

df['victim_first'].apply(title_case)

df['victim_first2'] = df['victim_first'].apply(title_case)

df['victim_first2'].head(10)

df[['victim_first', 'victim_first2']].head(10)

## Titanic Exercise 6

Write a function that extracts the last name from the name field on your Titanic dataframe. 
Create a new variable called <code>Family Name</code> to store the results. What is the most common family name?





Working on more than one column

def victim_name(row):
    first_name = row['victim_first']
    last_name  = row['victim_last']
    name       = last_name + ', ' + first_name
    name       = title_case(name)
    return name

df.apply(victim_name, axis=1)

df['victim_name'] = df.apply(victim_name, axis=1)

df.head()