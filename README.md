# Web scraping workout with Python
Since I've just finished to watch _The Big Bang Theory_ sitcom, I found quite funny to strengthen my acquiring skills in Python
to build a small project in which I extract data from the [Wikipedia page of the sitcom](https://en.wikipedia.org/wiki/List_of_The_Big_Bang_Theory_episodes) 
and then try to adapt the same code to other series, in order to create a sort of common structure that, with few fine tunings, can be easily reused to scrape similar tabular data.  
Consider this as a little Python workout!

## Step 1 - Building the main structure: scraping _The Big Bang Theory_ data
In the *bbp_data_extraction* file, you can find how I implemented the scraping of the tabular data for all 12 seasons of the sitcom.
The idea was to create a modular structure, in which I defined a function for each specific attribute that I want to extract from the web page.   
In this case I focused on:
1) the overall episode number (function _extract_episode_)
2) U.S. viewers (function _extract_viewers_)
3) original air date (function _extract_dates_)  

For every attribute I have created a list in which to insert the values extracted for each season.  
Since the table for each season can be different for the number of rows (i.e. episodes), I have applied these three functions for each season.  
With each season’s iteration, I have appended the corresponding results in each of the three main lists (_total_episodes_, _total_viewers_, _total_dates_).  
After extracting all the data, I converted these main lists into a unique dataframe and then exported as a CSV file, for further data manipulation.

## Step 2 - Tailoring the script for other series
While scraping other series, I encountered some problems due to the different formatting of the tables, e.g. elements without a specific HTML tag or table rows with a different structure. I was able to solve these problems fairly quickly thanks to the modular structure of both the main script and the functions.  
My workflow consisted of replicating the problematic pieces of code in a test file, using actual values to get effective feedback with the values from the web page; when the problems were fixed, I applied the “large scale” variations  on the original function.  
As an example, I will show in more detail the problems encounterd when scraping data from [_How I Met Your Mother_](https://en.wikipedia.org/wiki/List_of_How_I_Met_Your_Mother_episodes) list of episodes' web page.  

### Step 2.1 - Example: scraping _How I Met Your Mother_ data  
In this case I found differences both for the episodes and for the viewers. Regarding the episodes, for seasons 7, 8 and 9 there were some episodes divided into two parts (one line with two episode numbers, e.g. episodes 159 and 160 refer to the unique episode _The Magician's Code_):  

![](/images/HIMYM_season_7.png)

This resulted in the extraction of a tag element in addition to the episode number, and that presence caused an error when converting the episode number to data type _int_.  

Since this exception appeared in different places in the table, I had to deal with it in different ways:

* Seasons 7 and 9 (double episode in the last table position): I simply added a new variable epi_list_new which excludes the last element of the table, which is a tag element (please refer to _extract_episode_HIMYM_branch_7_9_)
* Season 8: I added a new line where I deleted the tag element in the middle of the list (please refer to _extract_episode_HIMYM_branch_8_)  

Regarding the differences related to the scraping of the number of viewers, in some tables there were cells with a different HTML structure, as there were not the usual _href_ tags encountered in the previous table's structure (e.g. refer to the last column for episodes 50, 55 and 56):  

![](/images/HIMYM_season_2.png)  

I handled the different types of exceptions in the following way:

* Season 2: only one episode without the _href_ tag for number of viewers, in the middle of the table. I divided the original list of values in two sub-lists, where for the first I took the odd elements, and for the second only the even elements (please refer to _extract_viewers_HIMYM_branch_2_)
* Season 3: multiple episodes without _href_ tags, in various positions of the table. I applied the previous concept of splitting the original list, but this time into four sub-lists, taking odd and even values each time, depending on the table structure (please refer to _extract_viewers_HIMYM_branch_2_)  

## Step 3 - Take a look at the results  
Once I scraped all the tables of interest, I plotted them to get a rough idea of the data and, of course, to see the result of hours of labour and sweat!  
For example, looking at the following line plot, illustrating the comparison of mean U.S. viewers (in millions) for all the scraped series, we can see at first glance that for all the series considered there (except one, that will discuss shortly), there is a common pattern: just before the end, there is an inflection point after wich there is a little increase in the number of viewers.  


![](/images/Overall_mean_comparison.png)  

The exception is Scrubs: we can justify this different behavior with the fact that during the last season, there has been a little revolution in the cast, with some “historical” characters who have been little or no present at all.  
For further insights we should analyze the relationship with other series and TV shows aired in the same period and hours (e.g. American Idol), merge this data with other datasets and understand the context and the events that potentially influenced the series performance, but for now it’s out of the scope of this repository.  

## First Python project: wrapping it up and takeaways  
This little exercise was the first approach with Python and some of its useful libraries like BeautifulSoup, pandas, matplotlib etc.  
After spending weeks on MOOCs and books, I decided to get my hands dirty and play with the code, in order to test my new skills and, above all, strenghten them with a tiny project.  
  
The key takeaways of this first experience are:  

* Know how to scrape an HTML page with BeautifulSoup, paying attention to its different tags and structures and how to handle them  
* Create, merge and manipulate “actual” DataFrames  
* Realizing that the domain knowledge is essential in order to understand and overcome potential errors (e.g. plotting the mean of U.S. viewers I didn’t obtain all months, because of the series don’t have episodes aired between June and August)  
* Perform sanity check on data: everytime I obtained an output file with scraped data, I performed a random cross check with original tables, in order to see if errors occurred (and sometimes it did!)





