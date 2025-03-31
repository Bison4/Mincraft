from ursina import *
from perlin_noise import PerlinNoise
# гайд https://habr.com/ru/companies/selectel/articles/704040/
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
rote = 0
Sky()
window.exit_button.visible = False

boxes= []
# for i in range(20):
#     for j in range(20):
#         box = Button(
#             color = color.white,
#             model = 'cube',
#             position = (j,0,i),
#             texture='assets/лава.jpg',
#             parent= scene,
#             origin_y = 0.5
#         )
#         boxes.append(box)
block_pick = 1
grass_texture = load_texture("assets/n.png")
stone_texture = load_texture("assets/камень.jpg")
brick_texture = load_texture("assets/булыжник.png")
dirt_texture = load_texture("assets/лава.jpg")
wood_texture = load_texture("assets/дерево.png")
shreck_texture = load_texture("assets/test.png")

arm_texture = load_texture("assets/arm.png")
fish_texture = load_texture("assets/test.png")

hand = Entity(
    parent=camera.ui,
    model="models/arm",
    texture=arm_texture,
    scale=0.2,
    rotation=Vec3(150, -10, 0),
    position=Vec2(0.7, -0.7)
)
fish = Entity(
    parent=scene,
    model="models/Alaska Pollock",
    texture=fish_texture,
    scale=1,
    rotation=Vec3(0, 0, 0),
    position=(15,10,15)
)

class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=grass_texture, mod = "cube"):
        super().__init__(
            parent=scene,
            model= mod,
            texture=texture,
            position=position,
            origin_y=0.5,
            color=color.color(0, 0, random.uniform(0.9, 1)),
        )
    def input(self , key):
        global block_pick
        if key == "q" or key == "escape":
            quit()

        if key == "1":
            block_pick = 1
        if key == "2":
            block_pick = 2
        if key == "3":
            block_pick = 3
        if key == "4":
            block_pick = 4
        if key == "5":
            block_pick = 5
        if key == "6":
            block_pick = 6
        # Проверяем, наведен ли курсор мыши на объект
        if self.hovered:
            # Проверяем, нажата ли правая кнопка мыши
            if key == "right mouse down":
                # Воспроизводим звук

                # Создаем объект Voxel с нужной текстурой и позицией
                if block_pick == 1:
                    Voxel(position=self.position + mouse.normal, texture=grass_texture)
                if block_pick == 2:
                    Voxel(position=self.position + mouse.normal, texture=dirt_texture)
                if block_pick == 3:
                    Voxel(position=self.position + mouse.normal, texture=stone_texture)
                if block_pick == 4:
                    Voxel(position=self.position + mouse.normal, texture=brick_texture)
                if block_pick == 5:
                    Voxel(position=self.position + mouse.normal, texture=wood_texture)
                if block_pick == 6:
                    Voxel(position=self.position + mouse.normal, texture=shreck_texture, mod="models/head")

            # Проверяем, нажата ли левая кнопка мыши
            if key == "left mouse down":
                # Воспроизводим звук
                # Уничтожаем текущий объект
                destroy(self)

    # def input(key):
    #     for box in boxes:
    #         if box.hovered:
    #             if key == 'right mouse down':
    #                 new = Button(
    #                 color = color.white,
    #                 model = 'cube',
    #                 position = box.position + mouse.normal,
    #                 texture='assets/лава.jpg',
    #                 parent= scene,
    #                 origin_y = 0.5
    #                 )
    #                 boxes.append(new)
    #             if key == 'left mouse down':
    #                 boxes.remove(box)
    #                 destroy(box)
def update():
    if fish.rotation_y == 360:
        fish.rotation_y = 0
    fish.rotation_y += 10
# Создаем объект noise, который представляет собой шум Перлина
# Указываем параметры шума, такие как количество октав (octaves) - уровней детализации шума, и зерно (seed) - начальное значение для генерации
noise = PerlinNoise(octaves=2, seed=2023)
# Создаем переменную am которая определяет амплитуду шума - максимальное отклонение от среднего значения
amp = 10
# Создаем переменную, которая определяет частоту шума - количество повторений шума на единицу длины
freq = 24
# Указываем ширину и длину
terrain_width = 20

# Создаем двумерный список landscale, который будет хранить высоты блоков по координатам x и z
# Инициализируем список нулевыми значениями размером terrain_width на terrain_width
landscale = [[0 for i in range(terrain_width)] for i in range(terrain_width)]

# Создаем цикл for, который перебирает все позиции блоков
for position in range(terrain_width**2):
    # Вычисляем координату x
    x = floor(position / terrain_width)
    # Вычисляем координату z
    z = floor(position % terrain_width)
    # Вычисляем координату y
    # Для получения значения шума Перлина используем noise
    y = floor(noise([x / freq, z / freq]) * amp)

    # Присваиваем значение y в списке landscale по индексам x и z
    landscale[int(x)][int(z)] = int(y)


# Создаем двойной цикл for, который перебирает все координаты x и z
for x in range(terrain_width):
    for z in range(terrain_width):
        # Создаем объект block класса Voxel, который представляет собой интерактивный блок в игре
        # Указываем параметры блока, такие как позицию по трем осям (x, y и z), используя значение y из списка landscale по индексам x и z
        block = Voxel(position=(x, landscale[x][z], z))
player = FirstPersonController()
app.run()