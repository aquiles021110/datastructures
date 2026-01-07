class appartment:
    def __init__(self,price,rooms,bathrooms,location,parking):
        self.price=price
        self.rooms=rooms
        self.bathrooms=bathrooms
        self.location=location
        self.parking=parking
    def show(self):
        print(f'Price:{self.price},Rooms:{self.rooms},Bathrooms: {self.bathrooms},Location:{self.location},Parking:{self.parking}')
app1=appartment(760,3,1,'City',False)
app1.show()