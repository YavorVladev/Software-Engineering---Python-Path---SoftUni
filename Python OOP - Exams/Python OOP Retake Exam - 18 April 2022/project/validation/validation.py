class Validation:

    @staticmethod
    def valid_user_username(username: str, message: str):
        if username.strip() == "":
            raise ValueError(message)

    @staticmethod
    def valid_user_age(age: int, message: str):
        if age < 6:
            raise ValueError(message)

    @staticmethod
    def valid_movie_title(title: str, message: str):
        if title.strip() == "":
            raise ValueError(message)

    @staticmethod
    def valid_movie_year(year: int, message: str):
        if year < 1888:
            raise ValueError(message)

    @staticmethod
    def valid_movie_owner(owner: object, message: str):
        if owner.__class__.__name__ != "User":
            raise ValueError(message)

    @staticmethod
    def age_restriction_check(age: int, class_type):
        if age < class_type._age_restriction:
            raise ValueError(f"{class_type.__class__.__name__} movies must be restricted for "
                             f"audience under {class_type._age_restriction} years!")

    @staticmethod
    def check_if_user_is_registered(username: str, username_list: list):
        if any(u.username == username for u in username_list):
            raise Exception("User already exists!")

    @staticmethod
    def check_if_movie_in_collection(movie, movie_collection):
        if movie in movie_collection:
            raise Exception("Movie already added to the collection!")

    @staticmethod
    def check_if_movie_is_NOT_in_collection(movie_class, movie_list: list):
        if movie_class not in movie_list:
            raise Exception(f"The movie {movie_class.title} is not uploaded!")

    @staticmethod
    def check_if_user_is_NOT_registered(username: str, user_list: list):
        if all(u.username != username for u in user_list):
            raise Exception("This user does not exist!")

    @staticmethod
    def check_if_user_is_owner(user, movie):
        if movie.owner.username != user.username:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")

    @staticmethod
    def VALIDATE_user_is_owner(user, movie):
        if movie in user.movies_owned:
            raise Exception(f"{user.username} is the owner of the movie {movie.title}!")

    @staticmethod
    def VALIDATE_user_already_liked_movie(user, movie):
        if movie in user.movies_liked:
            raise Exception(f"{user.username} already liked the movie {movie.title}!")

    @staticmethod
    def VALIDATE_user_can_dislike_movie(user, movie):
        if movie not in user.movies_liked:
            raise Exception(f"{user.username} has not liked the movie {movie.title}!")
