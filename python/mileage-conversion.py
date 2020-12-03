def l100kmtompg(liters):
    l2g = liters/3.785411784 #Converted litres to Gallons
    km2mi = 100*1000/1609.344 #100 km to miles
    mpg = km2mi/l2g
    return mpg
#
# put your code here
#

def mpgtol100km(miles):
    
    mi2m = 1609.344*miles #distance in metres
    gallon = 3.785411784 #litres
    mi2km = 100*1000 #100 km
    dist = mi2m/mi2km
    conv = gallon/dist
    return conv
#
# put your code here
#

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))