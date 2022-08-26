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
    # translate the input into index of the data structure
    option_idx = s.option_to_idx(option)
    # check if the user wants to exit the program
    if option_idx == -1:
        return r.bye()
    else:
        # ask the user for the text to search for
        input_text = r.imput_text()
        # the search function manage the serch and the auto complete
        marvel_search = s.search(MARVEL, option_idx, input_text)
        if marvel_search == []:
            # search has no result print the message and exit the program
            r.no_result()
        else:
            # save the len  of the search result to print ten result at the time for redeability
            len_marvel_search = len(marvel_search)
            while len_marvel_search > 10:
                # print in the backward order
                if len_marvel_search == len(marvel_search):
                    # print the first 10 results
                    r.bigger_than_10()
                    # print the last ten result and rest of len_marvel_search
                    r.table_maker(marvel_search[len_marvel_search-10:])
                    len_marvel_search -= 10
                    continue
                # ask if the user wants to print more results
                con = r.continue_printing()
                if con == "y":
                    # print the next ten results always in bakward order
                    r.table_maker(
                        marvel_search[len_marvel_search-10:len_marvel_search])
                    len_marvel_search -= 10
                    continue
                else:
                    break
            if len_marvel_search > 0:
                # if sstill some results print the last results
                r.last_result()
                r.table_maker(marvel_search[0:len_marvel_search])

    return r.bye()


# Run the main function
if __name__ == "__main__":
    main()
