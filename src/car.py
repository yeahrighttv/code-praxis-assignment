'''Class module'''
class Car():
    '''
    This is the class for cars with variables for model and price
    '''
    wheels = 4

    def __init__(self, model = 'Unknown', price = 'Unknown',
                 damage = 0, engine = 'OFF'):
        self.model = model
        self.price = price
        self.damage = damage
        self.engine = engine
        self.uses = 1


    def present_car(self):
        '''
        Takes in the variables and gives a thorough description
        '''
        return f'This car is made by {self.model} and costs about ${self.price}'


    def change_engine_mode(self):
        '''
        Gives the current mode of the engine
        '''
        if self.engine == 'ON':
            self.engine = 'OFF'
        elif self.engine == 'OFF':
            self.engine = 'ON'


    def damage_car(self):
        '''
        Ticks one damage at a time, zero is undamaged and five is totally wrecked
        '''
        if self.damage == 5:
            print('It\'s already wrecked man..')
        elif self.damage < 5:
            self.damage += 1


    def price_reduction(self):
        '''
        Takes in the price variable and decreases it
        '''
        if self.uses == 0:
            print('Sorry, no discounts left I\'m afraid..')
        elif self.uses == 1:
            self.price *= 0.8
            self.uses -= 1


    def crashed(self):
        '''
        Takes in damage and makes it have the value five,
         takes in the engine and makes it 'OFF'
          and lastly takes in price to heavily reduce the price
        '''
        self.price *= 0.15
        for _ in range(5):
            self.damage_car()
        self.engine = 'OFF'
