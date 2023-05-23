def lb_to_kg(lb):
    return lb * 0.4535923


def feet_and_inch_to_m(feet, inch=0.0):
    return feet * 0.3048 + inch * 0.0254


def bmi(weight, height):

    if height < 1.0 or height > 2.5 \
            or weight < 20.0 or weight > 200.0:
        return None

    return weight / height ** 2


print(bmi(weight=lb_to_kg(176), height=feet_and_inch_to_m(5, 7)))
