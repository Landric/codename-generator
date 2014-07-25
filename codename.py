from random import choice

FIRST_HALF = ['colours',
                'dates',
                'herbs_spices',
                'minerals',
            ]
            
SECOND_HALF = ['colours',
                'dates',
                'herbs_spices',
                'fruits_vegetables',
                'minerals',
            ]
            
            
def generate_codename():
    
    first_part = ''
    second_part = ''
    
    first_file = choice(FIRST_HALF)
    
    ammended = SECOND_HALF[:]
    if first_file in SECOND_HALF:
        ammended.remove(first_file)

    second_file = choice(ammended)
    
    with open('text/{0}.txt'.format(first_file)) as file:
        first_part = choice(file.readlines()).upper()
        
    with open('text/{0}.txt'.format(second_file)) as file:
        second_part = choice(file.readlines()).upper()
        
    print "{0} {1}".format(first_part, second_part).replace('\n', '')
    
if __name__ == "__main__":
    generate_codename()