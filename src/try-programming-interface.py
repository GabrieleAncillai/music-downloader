import music_kraken as mk
print(mk.__path__)

# mk.cli()

mk.fetch_source.Download()
# db = mk.utils.shared.database
# if len(db.get_custom_track([])) == 0:
    

mk.target.set_target.UrlPath(genre="test")

mk.fetch_audio.Download()

if __name__ == "__main__":
    db = mk.utils.shared.database
    for elem in db.get_custom_track([]):
        print(elem)
        print()
