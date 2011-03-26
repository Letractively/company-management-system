from django import template
register = template.Library()

def numberToText(value):
    numbers = {1:"First", 2:"Second", 3:"Third", 4:"Fourth", 5:"Fifth", 6:"Sixth", 7:"Seventh", 8:"Eighth",
               9:"Nineth", 10:"Tenth", 11:"Eleventh", 12:"Twelveth", 13:"Thirteenth", 14:"Fourteenth",
               15:"Fifteenth", 16:"Sixteenth", 17:"Seventeenth", 18:"Eighteenth", 19:"Nineteenth", 20:"Twentieth",
               21:"Twenty First", 22:"Twenty Second", 23:"Twenty Third", 24:"Twenty Fourth", 25:"Twenty Fifth",
               26:"Twenty Sixth", 27:"Twenty Seventh", 28:"Twenty Eighth", 29:"Twenty Ninth", 30:"Thirtieth",
               31:"Thirty First", 32:"Thirty Second", 33:"Thirty Third", 34:"Thirty Fourth", 35:"Thirty Fifth",
               36:"Thirty Sixth"}
    for k, v in numbers.iteritems(): 
        if(k==value): return v
    return value