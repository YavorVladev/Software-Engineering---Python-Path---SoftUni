from project.movie_specification.movie import Movie
from project.validation.validation import Validation
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def __find_client(self, username: str):
        for c in self.users_collection:
            if c.username == username:
                return c

    def register_user(self, username: str, age: int):
        Validation.check_if_user_is_registered(username, self.users_collection)

        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        Validation.check_if_user_is_NOT_registered(username, self.users_collection)
        user = self.__find_client(username)
        Validation.check_if_movie_in_collection(movie, self.movies_collection)
        Validation.check_if_user_is_owner(user, movie)

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):

        client = self.__find_client(username)
        Validation.check_if_movie_is_NOT_in_collection(movie, self.movies_collection)
        Validation.check_if_user_is_owner(client, movie)

        for attr, value in kwargs.items():
            setattr(movie, attr, value)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):

        client = self.__find_client(username)
        Validation.check_if_movie_is_NOT_in_collection(movie, self.movies_collection)
        Validation.check_if_user_is_owner(client, movie)

        client.movies_owned.remove(movie)
        self.movies_collection.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):

        client = self.__find_client(username)
        Validation.VALIDATE_user_is_owner(client, movie)
        Validation.VALIDATE_user_already_liked_movie(client, movie)

        movie.likes += 1
        client.movies_liked.append(movie)
        return f"{client.username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):

        client = self.__find_client(username)
        Validation.VALIDATE_user_can_dislike_movie(client, movie)
        movie.likes -= 1
        client.movies_liked.remove(movie)
        return f"{client.username} disliked {movie.title} movie."

    def display_movies(self):

        if not self.movies_collection:
            return "No movies found."

        return "\n".join((m.details()) for m in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)))

    def __str__(self):
        output = [f"All users: "]
        if not self.users_collection:
            output[0] += "No users."
        else:
            output[0] += f"{', '.join(u.username for u in self.users_collection)}"

        output.append(f"All movies: ")
        if not self.movies_collection:
            output[1] += "No movies."
        else:
            output[1] += f"{', '.join(m.title for m in self.movies_collection)}"

        return '\n'.join(output)

