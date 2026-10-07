bookvault/
├── main.py              # CLI entry point, if __name__ == "__main__"
├── models/
│   ├── __init__.py
│   ├── base_book.py     # ABC
│   ├── book.py          # Book, EBook, AudioBook
│   └── library.py       # Library class
├── utils/
│   ├── __init__.py
│   ├── stats.py         # calculate_stats(), filter helpers, lambdas
│   └── importer.py      # CSV import, re ISBN validation, datetime stamps
├── exceptions.py        # InvalidRatingError, LibraryImportError
└── test/
    ├── __init__.py
    └── test_*.py


## Testing
test/
├── __init__.py
├── test_book.py        # __init__ validation, __str__, __eq__, __len__
├── test_library.py     # add, search, filter, sort, classmethod from_csv
├── test_stats.py       # average rating, page totals, genre counts
└── test_exceptions.py  # InvalidRatingError, LibraryImportError, pytest.raises