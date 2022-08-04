from movements import movement_dict
from operator import itemgetter
from datetime import datetime
from random import choice

class Workout():
    def __init__(self):
        self.main_movement = self.get_main_movement()
        self.warmup_movements = self.get_warmup_movements()
        self.stretch_movements = self.get_stretch_movements()


    def __str__(self):
        return self.create_workout_string()


    def get_main_movement(self):
        main_movements = movement_dict.get('main')
        return choice(main_movements)


    def get_warmup_movements(self):
        main_type = self.main_movement['type']

        main_specific_movements = [movement for movement in movement_dict.get('warmup') if main_type in movement['type']]
        shoulder_movements = [movement for movement in movement_dict.get('warmup') if 0 in movement['type']]

        warmup_movements = []
        warmup_movements.append(choice(shoulder_movements))
        warmup_movements += main_specific_movements
        
        while len(warmup_movements) < 3:
            selection = choice(movement_dict.get('warmup'))

            if selection not in warmup_movements and 0 not in selection['type']:
                warmup_movements.append(selection)

        warmup_movements = sorted(warmup_movements, key=itemgetter('type'))

        return warmup_movements

    def get_stretch_movements(self):
        stretch_movements = []

        while len(stretch_movements) < 3:
            selection = choice(movement_dict.get('stretches'))

            if selection not in stretch_movements:
                stretch_movements.append(selection)

        return stretch_movements


    def create_main_string(self):
        main_str = '\nStrength:\n-----------------\n'

        if self.main_movement['type'] in [2,3]:
            main_str += choice(['5x5 ', '4x6 ', '3x8 '])
            main_str += self.main_movement.get('name')

        if self.main_movement['type'] == 5:
            main_str += choice(['5x16 ', '4x20 ', '3x24 '])
            main_str += self.main_movement.get('name')

        if self.main_movement['type'] == 4:
            main_str += choice(['5x50m ', '2x100m '])
            main_str += self.main_movement.get('name')

        return main_str


    def create_warmup_string(self):
        warmup_str = 'Activation: 2 rounds\n-----------------\n'

        for movement in self.warmup_movements:
            warmup_str += movement.get('name') + '\n'

        return warmup_str

    def create_stretches_string(self):
        stretches_str = '\n\nStretch: 2 rounds\n-----------------\n'
        
        for movement in self.stretch_movements:
            stretches_str += '45s ' + movement.get('name') + '\n'

        return stretches_str


    def create_workout_string(self):
        today = datetime.now().strftime('%B %d, %Y')
        date_str = f'{today}\n\n'
        warmup_str = self.create_warmup_string()
        main_str = self.create_main_string()
        stretches_str = self.create_stretches_string()

        return date_str + warmup_str + main_str + stretches_str
