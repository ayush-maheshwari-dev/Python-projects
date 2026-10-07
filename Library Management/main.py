import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Library Management CLI"
    )

    subparsers = parser.add_subparsers(dest="command")

    # add command
    add_parser = subparsers.add_parser(
        "add",
        help="Add a book to the library"
    )

    add_parser.add_argument(
        "name",
        help="Name of the book"
    )

    add_parser.add_argument(
        "author",
        help="Author of the book"
    )

    # list command
    subparsers.add_parser(
        "list",
        help="List all books in the library"
    )

    # read command
    read_parser = subparsers.add_parser(
        "read",
        help="Mark a book as read"
    )

    read_parser.add_argument(
        "name",
        help="Name of the book to mark as read"
    )

    # remove command
    remove_parser = subparsers.add_parser(
        "remove",
        help="Remove a book from the library"
    )

    remove_parser.add_argument(
        "name",
        help="Name of the book to remove"
    )

    args = parser.parse_args()

    if args.command == "add":
        print(f"Adding: {args.name} by {args.author}")

    elif args.command == "list":
        print("Listing books...")

    elif args.command == "read":
        print(f"Marking '{args.name}' as read")

    elif args.command == "remove":
        print(f"Removing: {args.name}")


if __name__ == "__main__":
    main()