# Bullet-News Web App

#### This application that will help you preview news articles from various sources, 16/04/2021

#### By **Eston Kagwima**

## Description
You dont have to be frustrated when you miss the news!! This application utilises the [News Api](https://newsapi.org/) to help you list and preview news articles from various sources around the world and all relevant cartegories you may be interested in. It will also allow you to visit the official website of the news source and readmore about any selected  article . 

## Behaviour Driven Development(BDD)

Features:
- As a user, I would like to see various news sources on the homepage of the application.
- I would also want to select a news source and see all news articles from the selected news source in the application.
- I would want to see the image, description and the time a news article was created.
- I would want to click on an article and read the full article on the source website.


      Examples:
      |  Behavior                       |     user-input                                 |         RESULT
      | Display News sources            | Enter the homepage                             | See A list of various news sources                       |
      | Display articles from a source  | click on the name of the source eg BBC-News    | redirected article list with date description and image  |
      | Read more on the article        | click on read more below the article           | redirected to the article page on the source website     |

## Setup/Installation Requirements
- install Python3.9
- Clone this repository `git clone https://github.com/kagus-code/Bullet-News.git`
- Change directory to the project directory using  the `cd` command
- Open project on VSCode
- If you want to use virtualenv: `virtualenv ENV && source ENV/bin/activate`
- Install dependencies with pip: `pip install -r requirements.txt`
- Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = create_app('production') should be app = create_app    ('development')
- finally run `./start.sh`


## Technologies Used

- Python3.9
- Flask
- Flask-Bootstrap
- HTML


## link to live site on  HEROKU

https://buzz-news.herokuapp.com/

## Support and contact details

| Eston | ekagwima745@gmail.com |
| ----- | --------------------- |


### Known bugs 
- some of the articles retrieved from the [NewsApi](https://newsapi.org/) have no images. Incase of any more issues use the contact details provided above

### License

License
[MIT License](https://choosealicense.com/licenses/mit/)
Copyright (c) 2021 Eston Kagwima