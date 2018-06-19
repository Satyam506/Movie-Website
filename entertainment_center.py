"""Stores details of movies and displays them on a website."""
import fresh_tomatoes
import media

def main():
   
    sherlock = media.Movie("Sherlock Holmes",
                          "https://www.dropbox.com/s/ulqtpwo1991b1zu/shrlock.jpg?raw=1",
                          "https://youtu.be/Egcx63-FfTE")
                        

    see = media.Movie("Now You See Me",
                          "https://www.dropbox.com/s/ex9o04a7k5yz4jl/see.jpg?raw=1",
                          "https://youtu.be/4OtM9j2lcUA")
                         

    shutter = media.Movie("Shutters Island",
                           "https://www.dropbox.com/s/rpo9pvc6dkw1ue4/shutter.jpg?raw=1",
                           "https://youtu.be/YDGldPitxic")
    
    dangal = media.Movie("Dangal",
                         "https://www.dropbox.com/s/z0z0i45s7ichux3/dangal.jpg?raw=1",
                         "https://youtu.be/x_7YlGv9u1g")


    john = media.Movie("John WICK",
                           "https://www.dropbox.com/s/xxqez8gxxn1os0m/john.jpg?raw=1",
                           "https://youtu.be/2AUmvWm5ZDQ")
                          

    deadpool = media.Movie("Deadpool",
                          "https://www.dropbox.com/s/yhxcum02s60dwme/deadpool.jpg?raw=1",
                          "https://youtu.be/D86RtevtfrA")
                         
  
    movies = [sherlock,see,shutter,dangal,john,deadpool]

   
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()

