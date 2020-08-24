from tkinter import *




from riotwatcher import LolWatcher, ApiError



def requestSummonerData():

    summonerName = input("what is your IGN")
    region = input("what is your region")

    return (summonerName,region)

def main():

    root = Tk()


    region = "na"
    summonerName = "Top Never Tilts"

    api_key = "YOUR API KEY"
    watcher = LolWatcher(api_key)
    my_region = region + "1"
    me = watcher.summoner.by_name(my_region, summonerName)

    my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])

    theLabel = Label(root, text = my_ranked_stats[0]['tier'])
    theLabel.pack()
    root.mainloop()

    print(my_ranked_stats)
    print(my_ranked_stats[0]['tier'])
    print(me)


# This starts my program!
if __name__ == "__main__":
    main()
