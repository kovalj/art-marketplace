#! python3

class Art:
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return '%s. "%s". %s, %s. %s, %s.' % (self.artist, self.title, 
                                            self.year, self.medium,
                                            self.owner.name, self.owner.location)

class Marketplace:
    def __init__(self):
        self.listings = []
    
    def add_listing(self, new_listing):
        self.listings.append(new_listing)

    def remove_listing(self, expired_listing):
        self.listings.remove(expired_listing)

    def show_listings(self):
        for listing in self.listings:
            print('Martketplace item : {0}'.format(listing))
        else: 
            print("The Marketplace is empty!")

class Client:
    def __init__(self, name, location, is_museum):
        self.name = name
        self.is_museum = is_museum
        if is_museum:
            self.location = location
        else:
            self.location = 'Private Collection'
    
    def sell_artwork(self, artwork, price):
        if artwork.owner == self:
            new_listing = Listing(artwork, price, self)
            veneer.add_listing(new_listing)

    def buy_artwork(self, artwork):
        if artwork.owner != self:
            art_listing = None
            for listing in veneer.listings:
                if listing.art == artwork:
                    art_listing = listing
                    break
        elif art_listing != None:
            art_listing.art.owner = self
            veneer.remove_listing(art_listing)
  
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
        return '%s. %s.' % (self.art.title, self.price)

    # TODO: Create expiration dates for listings! Have out of date listings
    #  automatically removed from the marketplace.

# Create the Marketplace. 
veneer = Marketplace()

veneer.show_listings()

# Add a client.
edytta = Client(name='Edytta Halpirt', location=None, is_museum=False)

# Add an artwork.
girl_with_mandolin = Art(artist='Picasso, Pablo', 
                        title='Girl with a Mandolin (Fanny Tellier)',
                        medium='oil on canvas', 
                        year=1910, owner=edytta)

print(girl_with_mandolin)

mona = Client(name='The MOMA', location='New York', is_museum=True)

# Sell an artwork.
edytta.sell_artwork(girl_with_mandolin, "$6M (USD)")

veneer.show_listings()

# Buy an artwork.
mona.buy_artwork(girl_with_mandolin)

print(girl_with_mandolin)

veneer.show_listings()
