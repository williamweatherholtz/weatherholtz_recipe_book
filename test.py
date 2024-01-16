from book import BookMaker

def test_book():
    b = BookMaker(
        title= "Weatherholtz Family Recipes",
        author= "Will Weatherholtz",
        root_dir= "sections",
        cover_img= "images/weatherholtz_fam_cover.png",
        version= 1,
        )
    b.make()

if __name__ == "__main__":
    test_book()