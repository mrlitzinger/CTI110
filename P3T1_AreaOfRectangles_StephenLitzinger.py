# Compare the area of two rectangles with lengths and widths entered by the user
# 03/02/20
# CTI-110 P3T1 - Area Of Rectangles
# Stephen Litzinger
#

def main():

# Get the users input for the length and width of two rectangles, was trying to condense inputs into less lines
##    print('We are going to compare the area of two rectangles.')
##    rec1L, rec1W = float(input('Please enter the length and width of your first rectangle separated by a comma.')).split()
##    rec2L, rec2W = float(input('Please enter the length and width of your second rectangle separated by a comma.')).split()

    print('We are going to compare the area of two rectangles.')
    rec1L = float(input('Please enter the length of your first rectangle.'))
    rec1W = float(input('Please enter the width of your first rectangle.'))
    rec2L = float(input('Please enter the length of your second rectangle.'))
    rec2W = float(input('Please enter the width of your second rectangle.'))

# Calculate the areas of each rectangle
    rec1A = rec1L * rec1W
    rec2A = rec2L * rec2W

# Display which rectangle has the larger area or show if they have an equal area
    if rec1A > rec2A:
        print('Your first rectangle has an area of ', rec1A, ' and your second rectangle has an area of ', rec2A, '. Your first rectangle has a larger area.')
    elif rec2A > rec1A:
        print('Your first rectangle has an area of ', rec1A, ' and your second rectangle has an area of ', rec2A, '. Your second rectangle has a larger area.')
    else:
        print('Your rectangles hava the same area of', rec1A)

main()
