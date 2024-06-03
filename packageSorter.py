# calculate volume
# A package is BULKY if its volume (Width x Height x Length)
# is greater than or equal to 1,000,000 cm³ or when one of its dimensions (W, H, L) is greater or equal to 150 cm.
# A package is HEAVY when its mass is greater or equal to 20 kg.

def volumeCalc(W, H, L):

    # width * height * length
    return W * H * L

def sort(W, H, L, mass):

    volume = volumeCalc(W, H, L)

    # determines if 'bulky'
    if volume >= 1000000 or W >= 150 or H >= 150 or L >= 150:

        # yes 'bulky' | yes 'heavy'
        if mass >= 20:
            return "REJECTED"

        # yes 'bulky' | no 'heavy'
        else:
            return "SPECIAL"

    # no 'bulky' | yes 'heavy'
    elif mass >= 20:
        return "SPECIAL"

    # no 'bulky' | no 'heavy'
    else:
        return "STANDARD"


# prints Standard
width, height, length, mass = 90, 100, 100, 15
print( sort(width, height, length, mass) )

# prints Special
width, height, length, mass = 90, 160, 100, 15
print( sort(width, height, length, mass) )

# prints Special
width, height, length, mass = 200, 200, 200, 15
print( sort(width, height, length, mass) )

# prints Rejected
width, height, length, mass = 200, 200, 200, 25
print( sort(width, height, length, mass) )
