import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 
	"A story about a boy and his toys that come to life", 
	"http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg", 
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
	"A marine on an alien planet",
	"http://www.impawards.com/2009/posters/avatar_xlg.jpg",
	"https://www.youtube.com/watch?v=cRdxXPV9GNQ")

forrest_gump = media.Movie("Forrest Gump",
	"A man seeks reasons behind why life is like a box of chocolates",
	"https://images-na.ssl-images-amazon.com/images/M/MV5BYThjM2MwZGMtMzg3Ny00NGRkLWE4M2EtYTBiNWMzOTY0YTI4XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_UY268_CR10,0,182,268_AL_.jpg",
	"https://www.youtube.com/watch?v=EtYNngO7eq4")

it = media.Movie("It", 
	"A movie about a scary clown",
	"https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/It_1990_Promotional_Poster.JPG/250px-It_1990_Promotional_Poster.JPG",
	"https://www.youtube.com/watch?v=FnCdOQsX5kc")

interstellar = media.Movie("Interstellar", 
	"A movie about exploring outer space",
	"https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_UY1200_CR69,0,630,1200_AL_.jpg",
	"https://www.youtube.com/watch?v=v7OVqXm7_Pk")

deadpool = media.Movie("Deadpool",
	"Superhero comedy", 
	"https://images-na.ssl-images-amazon.com/images/M/MV5BMjQyODg5Njc4N15BMl5BanBnXkFtZTgwMzExMjE3NzE@._V1_UY268_CR1,0,182,268_AL_.jpg",
	"https://www.youtube.com/watch?v=tj4acHoPzbU")

movies = [toy_story, avatar, forrest_gump, it, interstellar, deadpool]
fresh_tomatoes.open_movies_page(movies)

