import colorgram

colours = colorgram.extract("hirst_spot_painting.jpg", 30)
rgb_colour = []


for color in colours:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colour.append(new_color)

print(rgb_colour)
# Copying the output and pasting in main file colour list
