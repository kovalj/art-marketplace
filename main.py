#! python3

class Art:
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return 'Monet, Claude. "Vétheuil in the Fog". 1879, oil on canvas.'

class Marketplace:
    def __init__(self):
        self.listings = []
    
    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, remove_listing):
        self.listings.remove(remove_listing)

    def show_listings(self):
        for item in self.listings:
            print('{0}. "{1}". {2}, {3}.'.format(girl_with_mandolin.artist, 
                                                    girl_with_mandolin.title,
                                                    girl_with_mandolin.year,
                                                    girl_with_mandolin.medium))  

class Client:
    def __init__(self, name, location, is_museum):
        self.name = name
        self.location = location
        self.is_museum = is_museum
    
    def sell_work(self, artwork, price):
        if artwork.owner == self:
            pass

class Listing:
    def __init__(self, art, price, stellar):
        self.art = art
        self.price = price
        self.stellar = stellar

    def __repr__(self):
        return 'Monet, Claude. "Vétheuil in the Fog", 1879. Price: $1000'

veneer = Marketplace()
veneer.show_listings()

edytta = Client(name='Edytta Halpirt', location='Private Collection', is_museum=False)

girl_with_mandolin = Art(artist='Picasso, Pablo', 
                        title='Girl with a Mandolin (Fanny Tellier)',
                        medium='oil on canvas', 
                        year=1910, owner=edytta)

print('{0}. "{1}". {2}, {3}. {4}, {5}.'.format(girl_with_mandolin.artist, 
                                    girl_with_mandolin.title,
                                    girl_with_mandolin.year, 
                                    girl_with_mandolin.medium,
                                    girl_with_mandolin.owner.name,
                                    girl_with_mandolin.owner.location))

mona = Client(name='The MOMA', location='New York', is_museum=True)