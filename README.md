PROJECT:-
#API MASHUP TO GET MOVIES RECOMMENDIATION

This project is  through the process of mashing up data from two different APIs to make movie recommendations.

(i) TasteDive API

(ii)OMDB API

TasteDive API & OMDB API

****The TasteDive API lets you provide a movie as a query input, and returns a set of related items.

****The OMDB API let us provide a movie title as a query input and get back data about the movie, including scores from various review sites (Rotten Tomatoes, IMDB, etc.).
Working Methodology:

This project involves following steps( basically these steps are  functions on implementation) : 


(01)-get_movies_from_tastedive
(02)-Extract_movie_titles
(03)-Get_related_titles
(04)-Get_movie_data
(05)-get_movie_rating
(06)-get_sorted_recommendations

              (1)*get_movies_from_tastedive
                     ** It should take one input parameter, a string that is the name of a movie .
                     **The function should return the 5 TasteDive results that are associated with that string.
                     ** It will be a python dictionary with just one key, ‘Similar’.

                               WORKING OF get_movies_from_tastedive(movie_name)--- 
 
{'Similar': {'Info': [{'Name': 'Venom', 'Type': 'movie'}], 'Results': [{'Name': 'Aquaman', 'Type': 'movie'}, {'Name': 'Deadpool 2', 'Type': 'movie'}, {'Name': 'Bumblebee', 'Type': 'movie'}, {'Name': 'Dark Phoenix', 'Type': 'movie'}, {'Name': 'Alita: Battle Angel', 'Type': 'movie'}]}} 

            
            (2) extract_movie_titles() :
                   ** A function that extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive.
           
           WORKING OF extract_movie_titles()--- 
 
['Aquaman', 'Deadpool 2', 'Bumblebee', 'Dark Phoenix', 'Alita: Battle Angel'] 


           03) get_related_titles() 
                    **Next function, called get_related_titles.
                    ** It takes a list of movie titles as input. It gets five related movies for each from TasteDive, extracts the titles for all of them, and combines them all                     into a single list. 
                    ** It Don’t include the same movie twice.
           
           WORKING OF get_related_titles()------------------------------- 
 
['Venom', 'Captain Marvel', 'Shazam!', 'Bumblebee', 'Deadpool 2', 'Ant-Man And The Wasp', 'Thor: Ragnarok', 'Aquaman', 'Avengers: Infinity War', 'Mortal Engines', 'Dark Phoenix', 'Men In Black: International', 'Alita: Battle Angel']

          4)**  get_movie_data()
                 ***Next task will be to fetch data from OMDB. The documentation for the API is at https://www.omdbapi.com/
                 ***It takes in one parameter which is a string that should represent the title of a movie you want to search. The function should return a dictionary with                        information about that movie.
                 
                 WORKING OF get_movie_data()--- 
 
{'Title': 'Venom', 'Year': '2018', 'Rated': 'PG-13', 'Released': '05 Oct 2018', 'Runtime': '112 min', 'Genre': 'Action, Adventure, Sci-Fi, Thriller', 'Director': 'Ruben Fleischer', 'Writer': "Jeff Pinkner (screenplay by), Scott Rosenberg (screenplay by), Kelly Marcel (screenplay by), Jeff Pinkner (screen story by), Scott Rosenberg (screen story by), Todd McFarlane (Marvel's Venom Character created by), David Michelinie (Marvel's Venom Character created by)", 'Actors': 'Tom Hardy, Michelle Williams, Riz Ahmed, Scott Haze', 'Plot': 'A failed reporter is bonded to an alien entity, one of many symbiotes who have invaded Earth. But the being takes a liking to Earth and decides to protect it.', 'Language': 'English, Mandarin, Malay', 'Country': 'China, USA', 'Awards': '3 wins & 9 nominations.', 'Poster': 'https://m.media-amazon.com/images/M/MV5BNzAwNzUzNjY4MV5BMl5BanBnXkFtZTgwMTQ5MzM0NjM@._V1_SX300.jpg', 'Ratings': [{'Source': 'Internet Movie Database', 'Value': '6.7/10'}, {'Source': 'Rotten Tomatoes', 'Value': '29%'}, {'Source': 'Metacritic', 'Value': '35/100'}], 'Metascore': '35', 'imdbRating': '6.7', 'imdbVotes': '343,622', 'imdbID': 'tt1270797', 'Type': 'movie', 'DVD': '18 Dec 2018', 'BoxOffice': 'N/A', 'Production': 'Columbia Pictures', 'Website': 'N/A', 'Response': 'True'}



           5)** get_movie_rating()
                 **A function called get_movie_rating, It takes an OMDB dictionary result for one movie    and extracts the Rotten Tomatoes rating as an integer. For example, if                  given the OMDB dictionary for “Black Panther”, it would return 97. If there is no Rotten Tomatoes rating, return 0.
                 
                 WORKING OF get_movie_rating()--- 
                 output:- 29
                 
           06)**    get_sorted_recommendations()
                    ***It takes a list of movie titles as an input. It returns a sorted list of related movie titles as output, up to five related movies for each input movie                       title.
                    ***The movies should be sorted in descending order by their Rotten Tomatoes rating, as returned by the get_movie_rating 
                  
                  WORKING OF get_sorted_recommendations()------- 
 
[(93, 'Thor: Ragnarok'), (90, 'Shazam!'), (90, 'Bumblebee'), (87, 'Ant-Man And The Wasp'), (85, 'Avengers: Infinity War'), (84, 'Deadpool 2'), (78, 'Captain Marvel'), (65, 'Aquaman'), (61, 'Alita: Battle Angel'), (29, 'Venom'), (26, 'Mortal Engines'), (22, 'Dark Phoenix'), (22, 'Men In Black: International')]



                     
