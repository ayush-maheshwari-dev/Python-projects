class Book:

    def __init__(self, title, author, pages, genre, rating=None, status="unread"):

        if not title:
            raise ValueError("Title cannot be empty")

        self._title = title
        self._author = author
        self._pages = pages
        self._genre = genre

        self.rating = rating
        self.status = status

    # getter
    @property
    def rating(self):
        return self._rating

    # setter
    @rating.setter
    def rating(self, rating):
        if rating is not None and (rating < 1 or rating > 5):
            raise InvalidRatingError("Rating must be between 1 and 5")

        self._rating = rating

    # getter
    @property
    def status(self):
        return self._status

    # setter
    @status.setter
    def status(self, status):
        statuses = ["unread", "started", "half read", "quarter read", "read"]

        if status not in statuses:
            raise InvalidStatusError(
                f"Use following for status: {statuses}"
            )

        self._status = status