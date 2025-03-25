from ursina import *
# гайд https://habr.com/ru/companies/selectel/articles/704040/
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
player = FirstPersonController()
Sky()
window.exit_button.visible = False

boxes= []
for i in range(20):
    for j in range(20):
        box = Button(
            color = color.white,
            model = 'cube',
            position = (j,0,i),
            texture='assets/лава.jpg',
            parent= scene,
            origin_y = 0.5
        )
        boxes.append(box)
block_pick = 1
grass_texture = load_texture("assets/трава.png")
stone_texture = load_texture("assets/камень.jpg")
brick_texture = load_texture("assets/булыжник.png")
dirt_texture = load_texture("assets/лава.jpg")
wood_texture = load_texture("assets/дерево.png")

class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        super().__init__(
            parent=scene,
            model="cube",
            texture=texture,
            position=position,
            origin_y=0.5,
            color=color.color(0, 0, random.uniform(0.9, 1)),
        )
def input(key):
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
    for box in boxes:
        if box.hovered :
            if key == 'right mouse down':
                if block_pick == 1:
                    new = Voxel(position=  box.position + mouse.normal, texture=grass_texture)
                if block_pick == 2:
                    new = Voxel(position=  box.position + mouse.normal, texture=dirt_texture)
                if block_pick == 3:
                    new = Voxel(position=  box.position + mouse.normal, texture=stone_texture)
                if block_pick == 4:
                    new = Voxel(position=  box.position + mouse.normal, texture=brick_texture)
                if block_pick == 5:
                    new = Voxel(position= box.position + mouse.normal, texture=wood_texture)
                boxes.append(new)
            if key == 'left mouse down':
                boxes.remove(box)
                destroy(box)

arm_texture = load_texture("assets/arm.png")

hand = Entity(
    parent=camera.ui,
    model="models/arm",
    texture=arm_texture,
    scale=0.2,
    rotation=Vec3(150, -10, 0),
    position=Vec2(0.6, -0.6),
)



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


app.run()