This folder contains both the bespoke created classifier "Project Classifier" and the TextBlob classifier "Text Blob Classifier".
 To be able to run the project classifier one of the training data CSV files will be needed (can be found under CSV Files in the 
root document) and also one of the companies CSV files that has not already been classified (these can be found under company results CSV)
. These files need to be present in the root of the script that is running and the script has to be 
modified to run with the csv files chosen. For the Project Classifier the function that runs takes two arguments, the first is 
the name of the Companys CSV that has not already been classified (e.g. google_tweets.csv) the second argument is the name of 
what the output file will be called. On line 32 of the code it can be seen that the name of the training data is present when 
calling another function, if a different training data set is used this value must be changed accrodingly.


The Text Blob Classifier script is much like the pne before but instead does not require training data. The function still 
takes two areguments, the name of the file that is to be classified and the name of what the ouptput file will be called.

The best way to use these scripts is by copying all the CSV files from the CSV Files folder and pasting them into the root
of this folder. This is so the classifiers have access to any files that might be needed.