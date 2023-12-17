def checker(var_1):
    if type(var_1) != str:
        raise TypeError(f"Sorry, we can’t workf"
                        f"we need class str")
        else:
        return var_1

first_var = 10
checker(first_var)
new*
class BuildingEror(Exception):
    def __str__(self):
        return f"With so much material the house cannot be built!"

    def check_material(amount_of_material,
                       limit_value):
        if amount_of_material > limit_value:
            return "enough material"
        else:
            raise BuildingEror(amount_of_material)
        materials = 123
        check_material(materials, 300)
