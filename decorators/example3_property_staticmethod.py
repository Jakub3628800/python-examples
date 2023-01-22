"""@property and @staticmethod are builtins, you don't need to import them."""


class Color:

    red: int
    green: int
    blue: int

    def __init__(self, red: int, green: int, blue: int) -> None:
        self.red = red
        self.blue = blue
        self.green = green

    @staticmethod
    def clamp(x: int) -> int:
        return max(0, min(x, 255))

    @property
    def hex(self) -> str:
        return "#{0:02x}{1:02x}{2:02x}".format(self.clamp(self.red), self.clamp(self.green), self.clamp(self.blue))


white = Color(255, 255, 255)
print(white.hex)

# Output: #ffffff
