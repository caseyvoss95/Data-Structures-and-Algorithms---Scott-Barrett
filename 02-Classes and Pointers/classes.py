class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

cookieA = Cookie('blue')
cookieB = Cookie('maize')

print('Cookie A is', cookieA.get_color())
print('Cookie B is', cookieB.get_color())

cookieB.set_color('light maize')

print('\nCookie A is still', cookieA.get_color())
print('Cookie B is now', cookieB.get_color())