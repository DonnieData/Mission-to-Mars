# Mission-to-Mars
Automating data extraction and storage with python and NoSQL Database 

## Resources
- Python 3.7.6, Flask 1.1.2, JupyterLab 2.26, VS Code 1.51.1
- MongoDB 4.4.2
- HTML5, Bootstrap 3

## Overview 
The purpose of this project is to build a web application using [Flasks framework](https://flask.palletsprojects.com/), as a custom interface to share and format scraped data in the form of a web page. 


## Web Application Components 

#### Web Scraping 
A built-out [python script]() containg necessary parameters and code to perform specified web scrapping to collect and format data( raw text strings, image urls, etc).


#### MongoDB
The non-relational database is used to store the scrapped data within a BSON format.This is necessary since there is no specific or orderly structure to the data.  

#### Flask App 
A [seperate python script]() is used to define the frame work. This allows communication between the between the scraping script and the NoSQL database, as well as the html components needed to display the webpage. 


#### HTML
in order to display the data in a specific format, an html layout is built. Containg paramters that allow the Flask App to pass through data. 



## Final Product 
