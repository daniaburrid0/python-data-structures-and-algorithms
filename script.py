import search as s
import rich_helpers as r
import load as l


def main():
    # Start the console app
    # Print the title and description
    r.title()
    r.description()
    # load the csv file
    MARVEL = l.load_csv()
    # Ask the user for an option
    option = r.choose_option()
    option_idx = s.option_to_idx(option)
    if option_idx == -1:
        return r.bye()
    else:
        input_text = r.imput_text()
        marvel_search = s.search(MARVEL, option_idx, input_text)
        if marvel_search == []:
            r.no_result()
        else:
            r.table_maker(marvel_search)
    return r.bye()

# Run the main function
if __name__ == "__main__":
    main()