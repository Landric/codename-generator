from random import choice
from sys import argv

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
                'numbers',
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
        
    return "{0} {1}".format(first_part, second_part).replace('\n', '')
    
def generate_multiple_codenames(amount):
    codenames = []
    for i in range(amount):
        codenames.append(generate_codename())
        
    return codenames
    
if __name__ == "__main__":
    try:
        for codename in generate_multiple_codenames(int(argv[1])):
            print codename
    except IndexError:
        print generate_codename()
    except:
        print "Invalid argument: {0}".format(argv[1])