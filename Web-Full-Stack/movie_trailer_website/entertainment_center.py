import media
import fresh_tomatoes

# Create all instaces of classes Movies
toy_story = media.Movie("toy story",
                        "A story of a boy and his toy that come to life",
                        "https://ivid.akamaized.net/media/film/poster/1996/" +
                        "03/22/poster-film-toy-story-il-mondo-dei-giocattol" +
                        "i.jpg", "https://www.youtube.com/watch?v=KYz2wyB" +
                        "y3kc")

toy_story2 = media.Movie("toy story 2",
                         "A story of a boy and his toy that come to life",
                         "https://ia.media-imdb.com/images/M/MV5BMWM5ZDc" +
                         "xMTYtNTEyNS00MDRkLWI3YTItNThmMGExMWY4NDIwXkEyX" +
                         "kFqcGdeQXVyNjUwNzk3NDc@._V1_SY1000_CR0,0,677,1" +
                         "000_AL_.jpg", "https://www.youtube.com/watch?v" +
                         "=Lu0sotERXhI")

avatar = media.Movie("avatar",
                     "A story avatar",
                     "https://ia.media-imdb.com/images/M/MV5BMTYw" +
                     "OTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

furry = media.Movie("Fury", "A story fury",
                    "https://ia.media-imdb.com/images/M/M" +
                    "V5BMjA4MDU0NTUyN15BMl5BanBnXkFtZTgwM" +
                    "zQxMzY4MjE@._V1_SY1000_CR0,0,674,100" +
                    "0_AL_.jpg", "https://www.youtube.com" +
                    "/watch?v=-OGvZoIrXpg")

# Create array os movies
movies = [toy_story, toy_story2, avatar, furry]

# print(toy_story.__class__)
# print(media.Movie.__module__)
fresh_tomatoes.open_movies_page(movies)
