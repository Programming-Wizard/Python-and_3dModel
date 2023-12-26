from ursina import *

def update():
    pass

if __name__ == "__main__":
    app = Ursina()
    # city_model = Entity(model = '82-obj/obj/Residential Buildings 010.obj')
    car_model = Entity(model = '8hd2hnno0ayo-aventador_sport/Avent_sport.obj')
    car_model.rotation_y = -90
    camera.position = (0,2.5,-15)
    camera.rotation_x = 10


    def update():
        if held_keys['a'] :
            car_model.position -= car_model.left * 0.1
            car_model.rotation_y -= 0.5
        if held_keys['d'] :
            car_model.position -= car_model.right * 0.1
            car_model.rotation_y += 0.5
        if held_keys['w'] :
            car_model.position += (0,0,0.1)
        if held_keys['s'] :
            car_model.position -= (0,0,0.1)
        
    app.run()