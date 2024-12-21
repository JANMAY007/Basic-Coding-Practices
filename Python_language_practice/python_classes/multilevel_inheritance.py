class Universe:
    @staticmethod
    def universe():
        return "universe"


class Galaxy(Universe):
    @staticmethod
    def galaxy():
        return "galaxy"


class SolarSystem(Galaxy):
    @staticmethod
    def solar_system():
        return "solar system"


ss = SolarSystem()
print(ss.universe())
print(ss.galaxy())
print(ss.solar_system())
