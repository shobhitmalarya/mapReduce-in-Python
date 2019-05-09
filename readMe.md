* * * * *

                                Map Reduce in Python

* * * * *

Name - Shobhit Malarya

* * * * *

Task Implemented --- Analyzing the number of article on crime in India's
major four cities (i.e Delhi, Mumbai , Chennai , Kolkata) between
2001-2018 as per dataset provided at
https://www.kaggle.com/therohk/india-headlines-news-dataset

NOTE -- The articles are counted on the basis on crime related keywords
["crime","assault","bribe","burglar","abuse","drug","fraud","homicid","kidnap","piracy","rape","robb","smuggl","terror","theft"]

* * * * *

How to run the program -

Without Hadoop -

    cat india-news-headlines.txt | python mapper.py | python reducer.py

With hadoop -

    hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.1.2.jar -mapper mapper.py -reducer reducer.py -input india-news-headlines.csv -output results/

* * * * *

The final results are plotted in a graph "results.png" in this same
directory
