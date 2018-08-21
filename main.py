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
            print('{0}. "{1}". {2}, {3}. {4}, {5}.'.format(item.artist, 
                                                        item.title,
                                                        item.year,
                                                        item.medium,
                                                        item.owner.name,
                                                        item.location))  

class Client:
    def __init__(self, name, location, is_museum):
        self.name = name
        self.location = location
        self.is_museum = is_museum
    
    def sell_artwork(self, artwork, price):
        if artwork.owner == self:
            Listing(artwork, price, artwork.owner)
            veneer.add_listing(artwork)

    def buy_artwork(self, artwork):
        if artwork.owner != self:
            if artwork in veneer.listings:
                art_listing = artwork
                artwork.owner = self
                veneer.remove_listing(artwork)
  
    # TODO: Add a wallet instance variable to clients, update the buying and 
    # selling of artworks to also exchange dollar amounts.

    # TODO: Create a wishlist for your clients, things that are listed 
    # but they're not sure if they should purchase just yet.

class Listing:
    def __init__(self, art, price, stellar):
        self.art = art
        self.price = price
        self.stellar = stellar

    def __repr__(self):
        return 'Monet, Claude. "Vétheuil in the Fog", 1879. $1M'

    # TODO: Create expiration dates for listings! Have out of date listings
    #  automatically removed from the marketplace.

# Create the Marketplace. 
veneer = Marketplace()
veneer.show_listings()

# Add a client.
edytta = Client(name='Edytta Halpirt', location='Private Collection', is_museum=False)

# Add an artwork.
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

# Sell an artwork.
edytta.sell_artwork(girl_with_mandolin, "$6M")

veneer.show_listings()

# Buy an artwork.
mona.buy_artwork(girl_with_mandolin)

print('{0}. "{1}". {2}, {3}. {4}, {5}.'.format(girl_with_mandolin.artist, 
                                    girl_with_mandolin.title,
                                    girl_with_mandolin.year, 
                                    girl_with_mandolin.medium,
                                    girl_with_mandolin.owner.name,
                                    girl_with_mandolin.owner.location))

veneer.show_listings()