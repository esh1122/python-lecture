class Cat:

    def __init__(self, name, color = '흰색'): #초기 설정 메소드 (반드시)
        self.name = name
        self.color = color

    def meow(self):
        print(f'내 이름은 {self.name}, 색깔은 {self.color}, 야옹~!')



nabi = Cat("나비")
nero = Cat("네로", "검정색")
nabi.meow()
nero.meow()