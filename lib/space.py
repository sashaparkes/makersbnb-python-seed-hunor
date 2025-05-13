class Space:
    def __init__(self,id,name,description,price_per_night,host_id):
        self.id = id
        self.name = name
        self.description = description
        self.price_per_night = price_per_night
        self.host_id = host_id

    def __repr__(self):
        return f'Space({self.id}, {self.name}, {self.description}, £{self.price_per_night}/night, {self.host_id})'

    def __eq__(self,other):
        return self.__dict__ == other.__dict__