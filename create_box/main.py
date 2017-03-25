"""This is the entry point of the program."""


def create_box(height, width, character):
    row = 0
    if height >= 1 and width >= 1: 
        while row < height:
            return (width * character + '\n')*height
    else:
        return 'height and width need to be greater or equal to 1'
        
def create_outlined_box(height, width, character):
    row = 1
    box = ''            
    line1 = (width * character + '\n')
    line2 = (character + (' ' * (width - 2)) + character + '\n')
    
    if height >= 3 and width >= 3: 
        box += line1                # first row
        while row < (height-1):   # while row < (height-1):
            box += line2
            row = row + 1       
        box += line1                # last row
    return box
    
# box = create_outlined_box(5, 4, '@')
# print(box)

if __name__ == '__main__':
    create_box(3, 4, '*')
    create_outlined_box(4,4,'@')
    

"""
height = 3

height - 3 = 0





"""