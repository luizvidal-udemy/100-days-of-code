from colorgram import extract


rgb_colors = []

colors = extract(
    "A:/luiz-vidal/github/100-days-of-code/day-018-intermediate-turtle-and-the-graphical-user-interface-gui/07-the-hirst-painting-project/image.png", 10
)


for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))


print(rgb_colors)
