# HINT: You may need to make an additional function
#       to print the remaining players in a match
joined_players = []

def join_mode():
        # TODO: Edit the loop and its contents below
        #       to handle join mode.
    no_of_players = 0

    while no_of_players < 16:
            ign_to_join = input()
            if ign_to_join not in joined_players:
                no_of_players += 1
                joined_players.append(ign_to_join)
            else:
                print("oops")




def score_mode():
        # TODO: Edit the loop and its contents below
        #       to handle score mode.
    total_no_players = 16

    while total_no_players > 0:
        ign_to_eliminate = input()
        if ign_to_eliminate in joined_players:
            joined_players.remove(ign_to_eliminate)
            total_no_players -= 1
        else:
            print("oops")

        if int(len(joined_players)) == 8:
            print("Top 8:")
            for x in range(int(len(joined_players))):
                print(joined_players[x])

        if int(int(len(joined_players))) == 4:
            print("Top 4:")
            for x in range(int(len(joined_players))):
                print(joined_players[x])

        if int(int(len(joined_players))) == 2:
            print("Finals:")
            for x in range(int(len(joined_players))):
                print(joined_players[x])

        if int(int(len(joined_players))) == 1:
            print(f"And the winner is {joined_players[0]}")
            break


def main():
    join_mode()
    score_mode()


if __name__ == '__main__':
    main()