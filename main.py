import arcade
import time
import arcade.gui
import arcade.gui.events
from arcade.experimental.uislider import UISlider
from arcade.gui import UIManager, UIAnchorWidget, UILabel
from arcade.gui.events import UIOnChangeEvent


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(1800, 1000, "Flat", resizable=False)
        arcade.set_background_color(arcade.color.DARK_CYAN)
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.manager1 = arcade.gui.UIManager()
        self.manager1.enable()
        self.manager2 = arcade.gui.UIManager()
        self.manager2.enable()
        self.manager3 = arcade.gui.UIManager()
        self.manager3.enable()
        self.manager4 = arcade.gui.UIManager()
        self.manager4.enable()
        self.manager5 = UIManager()
        self.manager5.enable()
        self.manager6 = UIManager()
        self.manager6.enable()
        self.manager7 = UIManager()
        self.manager7.enable()
        self.manager8 = UIManager()
        self.manager8.enable()
        self.manager9 = UIManager()
        self.manager9.enable()
        self.manager10 = UIManager()
        self.manager10.enable()
        self.manager11 = UIManager()
        self.manager11.enable()

        self.total_time = 0.0
        self.timer_text = arcade.Text(
            text="00:00",
            start_x=1350,
            start_y=150,
            color=arcade.color.BLUSH,
            font_size=70,
            anchor_x="center",
        )

        self.collusion = False
        self.button_off_clicked = True
        self.button_on_clicked = False
        self.button_start_clicked = False
        self.button_fire_clicked = False
        self.button_rob_clicked = False
        self.button_put_out_clicked = False
        self.button_catch_clicked = False
        self.button_water_clicked = False
        self.flat = None
        self.player1 = None
        self.player2 = None
        self.player3 = None
        self.ground = None
        self.label_ground = None
        self.water_ground = None
        self.ground_off = None
        self.player4 = None
        self.player1 = arcade.Sprite("1.png", 0.2)
        self.player1.center_x = 400
        self.player1.center_y = 700
        self.flat = arcade.Sprite("3.png", 1.2)
        self.flat.center_x = 500
        self.flat.center_y = 600
        self.player2 = arcade.Sprite("2.png", 0.2)
        self.player2.center_x = 180
        self.player2.center_y = 400
        self.player2.change_x = 1
        self.player2.change_y = 1
        self.ground = arcade.create_rectangle_filled(500, 240, 750, 50,
                                                     arcade.color.BONDI_BLUE)
        self.label_ground = arcade.create_rectangle_filled(500, 950, 750, 30,
                                                           arcade.color.DUTCH_WHITE)
        self.water_ground = arcade.create_rectangle_filled(500, 30, 200, 50,
                                                           arcade.color.BONDI_BLUE)
        self.ground_off = arcade.create_rectangle_filled(500, 600, 750, 700,
                                                         arcade.color.NAVAJO_WHITE)
        self.ground_second_part = arcade.create_rectangle_filled(1350, 600, 900, 1400,
                                                                 arcade.color.CREAM)
        self.border = arcade.create_rectangle_filled(900, 500, 10, 1400,
                                                     arcade.color.BLUSH)

        self.text_water_box = arcade.gui.UIBoxLayout(space_between=0)
        self.text_water = arcade.gui.UITextArea(text="Create water",
                                               width=900,
                                               height=50,
                                               font_size=15,
                                               text_color=
                                                arcade.color.BONDI_BLUE,
                                               font_name="calibri")
        self.text_water_box.add(self.text_water.with_space_around(bottom=0))
        self.manager6.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                align_x=835,
                anchor_y="center_y",
                align_y=-100,
                child=self.text_water_box)
        )
        self.text_create_box = arcade.gui.UIBoxLayout(space_between=0)
        self.text_create = arcade.gui.UITextArea(text=
                                                 "You can create external actions",
                                                width=900,
                                                height=50,
                                                font_size=30,
                                                text_color=
                                                 arcade.color.BLUSH,
                                                font_name="calibri")
        self.text_create_box.add(self.text_create.with_space_around(bottom=0))
        self.manager10.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                align_x=600,
                anchor_y="center_y",
                align_y=300,
                child=self.text_create_box)
        )
        self.sign = arcade.Sprite("7.png", 0.2)
        self.sign.center_x = 1350
        self.sign.center_y = 670
        self.text_automata_box = arcade.gui.UIBoxLayout(space_between=0)
        self.text_automata = arcade.gui.UITextArea(text=
                                                   "Model of finite automat",
                                                width=900,
                                                height=50,
                                                font_size=25,
                                                text_color=
                                                   arcade.color.WHITE,
                                                font_name="calibri")
        self.text_automata_box.add(self.text_automata.with_space_around(bottom=0))
        self.manager7.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                align_x=-140,
                anchor_y="center_y",
                align_y=480,
                child=self.text_automata_box)
        )
        self.player4 = arcade.Sprite("4.png", 0.2)
        self.player4.center_x = 825
        self.player4.center_y = 870
        self.alarm_sound = arcade.Sound("1.wav")
        self.default_style = {
            "font_name": ("calibri", "arial"),
            "font_size": 15,
            "font_color": arcade.color.WHITE,
            "border_width": 2,
            "border_color": arcade.color.PINK,
            "bg_color": arcade.color.BOLE,
            "bg_color_pressed": arcade.color.CHAMPAGNE,
            "border_color_pressed": arcade.color.PINK,
            "font_color_pressed": arcade.color.BLACK,
        }
        self.cool_style = {
            "font_name": ("calibri", "arial"),
            "font_size": 15,
            "font_color": arcade.color.WHITE,
            "border_width": 2,
            "border_color": arcade.color.BONDI_BLUE,
            "bg_color": arcade.color.BLUE_SAPPHIRE,
            "bg_color_pressed": arcade.color.CHAMPAGNE,
            "border_color_pressed": arcade.color.BONDI_BLUE,
            "font_color_pressed": arcade.color.BLACK,
        }
        self.box5 = arcade.gui.UIBoxLayout(space_between=20)
        self.button_instr = arcade.gui.UIFlatButton(text=
                                                    "Instructions",
                                                    width=200,
                                                    height=50,
                                                    style=self.cool_style)
        self.button_about = arcade.gui.UIFlatButton(text="Info",
                                                    width=200,
                                                    height=50,
                                                    style=self.cool_style)
        self.box5.add(self.button_instr)
        self.box5.add(self.button_about)
        self.manager11.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                align_x=600,
                anchor_y="center_y",
                align_y=-400,
                child=self.box5))
        self.box1 = arcade.gui.UIBoxLayout(space_between=20)
        self.button_off = arcade.gui.UIFlatButton(text="OFF",
                                                  width=200,
                                                  height=50,
                                                  style=
                                                  self.default_style)
        self.button_on = arcade.gui.UIFlatButton(text="ON",
                                                 width=200,
                                                 height=50,
                                                 style=self.default_style)
        self.button_start = arcade.gui.UIFlatButton(text="Start",
                                                    width=200,
                                                    height=50,
                                                    style=self.default_style)
        self.box1.add(self.button_off)
        self.box1.add(self.button_on)
        self.box1.add(self.button_start)
        self.manager1.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                align_x=-400,
                anchor_y="center_y",
                align_y=-400,
                child=self.box1)
        )
        self.box2 = arcade.gui.UIBoxLayout(space_between=20)
        self.button_fire = arcade.gui.UIFlatButton(text="Create fire",
                                                   width=200,
                                                   height=50,
                                                   style=self.default_style)
        self.button_rob = arcade.gui.UIFlatButton(text="Create movement",
                                                  width=200,
                                                  height=50,
                                                  style=self.default_style)
        self.box2.add(self.button_fire)
        self.box2.add(self.button_rob)
        self.manager2.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                align_x=450,
                anchor_y="center_y",
                align_y=0,
                child=self.box2)
        )
        self.box3 = arcade.gui.UIBoxLayout(space_between=20)
        self.box4 = arcade.gui.UIBoxLayout(space_between=20)
        self.button_catch = arcade.gui.UIFlatButton(text=
                                                    "Catch the thief",
                                                    width=200,
                                                    height=50,
                                                    style=self.default_style
                                                    )
        self.button_put_out = arcade.gui.UIFlatButton(text="Put out the fire",
                                                      width=200,
                                                      height=50,
                                                      style=self.default_style
                                                      )
        self.box3.add(self.button_put_out)
        self.box4.add(self.button_catch)
        self.manager5.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                align_x=700,
                anchor_y="center_y",
                align_y=35,
                child=self.box3)
        )
        self.manager8.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                align_x=700,
                anchor_y="center_y",
                align_y=-35,
                child=self.box4)
        )
        self.slider1 = UISlider(value=0, width=200, height=50)
        self.label = UILabel(text=f"{self.slider1.value:02.0f}",
                             font_size=17,
                             font_name="Kenney Future",
                             text_color=arcade.color.BONDI_BLUE)
        self.manager9.add(UIAnchorWidget(
            anchor_x="center_x",
            align_x=450,
            anchor_y="center_y",
            align_y=-150,
            child=self.slider1))
        self.manager9.add(UIAnchorWidget(
            anchor_x="center_x",
            align_x=450,
            anchor_y="center_y",
            align_y=-120,
            child=self.label))

        @self.slider1.event()
        def on_change(event: UIOnChangeEvent):
            self.label.text = f"{self.slider1.value:02.0f}"
            self.label.fit_content()
        self.text = "System is off"
        self.text_box = arcade.gui.UIBoxLayout(space_between=20)
        self.text_label = arcade.gui.UITextArea(text=self.text,
                                                width=450,
                                                height=40,
                                                font_size=24,
                                                font_name=
                                                "Kenney Future")
        self.text_box.add(self.text_label.with_space_around(bottom=0))
        self.manager3.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                align_x=-540,
                anchor_y="center_y",
                align_y=-260,
                child=self.text_box)
        )
        self.text_name_box = arcade.gui.UIBoxLayout(space_between=0)
        self.text_name = arcade.gui.UITextArea(text="Apartment security control system",
                                               width=900,
                                               height=50,
                                               font_size=20,
                                               text_color=arcade.color.BONDI_BLUE,
                                               font_name="Arial")
        self.text_name_box.add(self.text_name.with_space_around(bottom=0))
        self.manager4.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                align_x=-150,
                anchor_y="center_y",
                align_y=440,
                child=self.text_name_box)
        )

        # Push button OFF
        @self.button_off.event("on_click")
        def on_click_off(event):
            if self.button_off_clicked:
                pass
                # on_click_on(event)
            else:
                if self.button_on_clicked or self.button_start_clicked:
                    self.button_off_clicked = True
                    arcade.set_background_color(arcade.color.DARK_CYAN)
                    self.text = "System is off"
                    self.text_label = arcade.gui.UITextArea(text=self.text,
                                                            width=450,
                                                            height=40,
                                                            font_size=24,
                                                            font_name="Kenney Future")
                    self.text_box.clear()
                    self.text_box.add(self.text_label.with_space_around(bottom=0))
                    self.button_start_clicked = False
                    self.button_on_clicked = False
                    self.button_fire_clicked = False
                    self.button_rob_clicked = False
                    self.button_put_out_clicked = False
                    self.button_catch_clicked = False
                    self.button_water_clicked = False
                if (self.button_fire_clicked or
                        self.button_rob_clicked or
                        self.button_water_clicked):
                    return

        # Push button ON
        @self.button_on.event("on_click")
        def on_click_on(event):
            self.time_on = time.time()
            if self.button_off_clicked:
                self.button_on_clicked = True
                arcade.set_background_color(arcade.color.DARK_CYAN)
                self.text = "System is on"
                self.text_label = arcade.gui.UITextArea(text=self.text,
                                                        width=450,
                                                        height=40,
                                                        font_size=24,
                                                        font_name="Kenney Future")
                self.text_box.clear()
                self.text_box.add(self.text_label.with_space_around(bottom=0))
                self.button_start_clicked = False
                self.button_off_clicked = False
                self.button_fire_clicked = False
                self.button_rob_clicked = False
                self.button_put_out_clicked = False
                self.button_catch_clicked = False
                self.button_water_clicked = False
                # time.sleep(10)
                # on_click_start(event)
                # while time.time() - self.time_on <= 1:
                    # pass
                # on_click_start(event)
            else:
                return

        # Push button Start
        @self.button_start.event("on_click")
        def on_click_start(event):
            if (self.button_on_clicked
                    or self.button_put_out_clicked
                    or self.button_catch_clicked):
                self.button_start_clicked = True
                self.button_off_clicked = False
                self.button_on_clicked = False
                self.button_fire_clicked = False
                self.button_rob_clicked = False
                self.button_put_out_clicked = False
                self.button_catch_clicked = False
                self.button_water_clicked = False
                arcade.set_background_color(arcade.color.DARK_CYAN)
                self.text = "System is observing..."
                self.text_label = arcade.gui.UITextArea(text=self.text,
                                                        width=500,
                                                        height=40,
                                                        font_size=24,
                                                        font_name="Kenney Future")
                self.text_box.clear()
                self.text_box.add(self.text_label.with_space_around(bottom=0))
                self.manager3.clear()
                self.manager3.add(
                    arcade.gui.UIAnchorWidget(
                        anchor_x="center_x",
                        align_x=-515,
                        anchor_y="center_y",
                        align_y=-260,
                        child=self.text_box)
                )
            else:
                return

        # push button Movement
        @self.button_rob.event("on_click")
        def on_click_rob(event):
            if (self.button_off_clicked
                    or self.button_on_clicked
                    or self.button_rob_clicked):
                return
            elif self.button_fire_clicked:
                self.collusion = True
                self.button_rob_clicked = True
                return
            self.player2.center_x = 180
            self.player2.center_y = 400
            self.player2.change_x = 1
            self.player2.change_y = 1
            self.button_rob_clicked = True
            self.button_start_clicked = False
            self.button_off_clicked = False
            self.button_on_clicked = False
            self.button_fire_clicked = False
            self.button_put_out_clicked = False
            self.button_catch_clicked = False
            self.button_water_clicked = False
            self.text = "Alarm - Intrusion!!!"
            self.text_label = arcade.gui.UITextArea(text=self.text,
                                                    width=500,
                                                    height=40,
                                                    font_size=24,
                                                    text_color=arcade.color.PINK,
                                                    font_name="Kenney Future")
            self.text_box.clear()
            self.text_box.add(self.text_label.with_space_around(bottom=0))
            self.alarm_sound.play(0.2)
            arcade.set_background_color(arcade.color.BABY_PINK)

        # push button catch

        # Push button fire
        @self.button_fire.event("on_click")
        def on_click_fire(event):
            if (self.button_off_clicked
                    or self.button_on_clicked
                    or self.button_fire_clicked):
                return
            elif self.button_rob_clicked:
                self.collusion = True
                self.button_fire_clicked = True
                return
            self.button_fire_clicked = True
            self.button_rob_clicked = False
            self.button_off_clicked = False
            self.button_on_clicked = False
            self.button_put_out_clicked = False
            self.button_catch_clicked = False
            self.button_water_clicked = False
            self.button_start_clicked = False
            self.text = "Alarm - Fire!!!"
            self.text_label = arcade.gui.UITextArea(text=self.text,
                                                    width=500,
                                                    height=40,
                                                    font_size=24,
                                                    text_color=arcade.color.PINK,
                                                    font_name="Kenney Future")
            self.text_box.clear()
            self.text_box.add(self.text_label.with_space_around(bottom=0))
            self.alarm_sound.play(0.2)
            arcade.set_background_color(arcade.color.BABY_PINK)

        @self.button_catch.event("on_click")
        def on_click_catch(event):
            if self.button_rob_clicked and not self.button_fire_clicked:
                self.button_catch_clicked = True
                self.button_fire_clicked = False
                self.button_rob_clicked = False
                self.button_off_clicked = False
                self.button_on_clicked = False
                self.button_put_out_clicked = False
                self.button_water_clicked = False
                self.button_start_clicked = False
                on_click_start(event)
            elif self.button_fire_clicked and self.collusion:
                self.button_catch_clicked = True
                self.button_fire_clicked = False
                self.button_rob_clicked = False
                self.button_off_clicked = False
                self.button_on_clicked = False
                self.button_put_out_clicked = False
                self.button_water_clicked = False
                self.button_start_clicked = False
                self.collusion = False
                on_click_fire(event)
            else:
                return

        # push button put out
        @self.button_put_out.event("on_click")
        def on_click_put_out(event):
            if self.button_fire_clicked and not self.button_rob_clicked:
                self.button_put_out_clicked = True
                self.button_fire_clicked = False
                self.button_rob_clicked = False
                self.button_off_clicked = False
                self.button_on_clicked = False
                self.button_catch_clicked = False
                self.button_water_clicked = False
                on_click_start(event)
            elif self.button_rob_clicked and self.collusion:
                self.button_put_out_clicked = True
                self.button_fire_clicked = False
                self.button_rob_clicked = False
                self.button_off_clicked = False
                self.button_on_clicked = False
                self.button_catch_clicked = False
                self.button_water_clicked = False
                self.collusion = False
                on_click_rob(event)
            else:
                return

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.UP:
            self.player2.change_y = 3
        elif key == arcade.key.DOWN:
            self.player2.change_y = -3
        elif key == arcade.key.RIGHT:
            self.player2.change_x = 3
        elif key == arcade.key.LEFT:
            self.player2.change_x = -3

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.UP:
            self.player2.change_y = 1
        elif key == arcade.key.DOWN:
            self.player2.change_y = 1
        elif key == arcade.key.RIGHT:
            self.player2.change_x = 1
        elif key == arcade.key.LEFT:
            self.player2.change_x = 1

    def update(self, delta_time: float):
        self.player2.update()
        self.player1.update()
        self.player4.update()
        if self.player2.center_x > 836:
            self.player2.change_x = -1
        if self.player2.center_y < 318:
            self.player2.change_y = 1
        if self.player2.center_x < 163:
            self.player2.change_x = 1
        if self.player2.center_y > 886:
            self.player2.change_y = -1
        if not self.button_off_clicked:
            self.total_time += delta_time
            minutes = int(self.total_time) // 60
            seconds = int(self.total_time) % 60
            self.timer_text.text = f"{minutes:02d}:{seconds:02d}"
        else:
            self.timer_text.text = f"00:00"
            self.total_time = 0.0

    def on_draw(self):
        self.clear()
        if not self.button_off_clicked:
            self.flat.draw()
        else:
            self.ground_off.draw()
        self.ground.draw()
        self.label_ground.draw()
        self.water_ground.draw()
        self.ground_second_part.draw()
        self.border.draw()
        self.sign.draw()
        self.manager1.draw()
        self.manager2.draw()
        self.manager3.draw()
        self.manager4.draw()
        self.manager6.draw()
        self.manager7.draw()
        self.manager9.draw()
        self.manager10.draw()
        self.timer_text.draw()
        # self.manager11.draw()
        if self.button_start_clicked:
            self.player4.draw()
        if self.button_fire_clicked:
            self.player1.draw()
            self.manager5.draw()
        if self.button_rob_clicked:
            self.player2.draw()
            self.manager8.draw()
        if (self.slider1.value > 0
                and not self.button_off_clicked and not self.button_on_clicked
                and not self.button_rob_clicked
                and not self.button_fire_clicked):
            self.player3 = arcade.Sprite("6.png",
                                         (self.slider1.value / 350)
                                         )
            self.player3.center_x = 400
            self.player3.center_y = 800
            self.player3.draw()
            if self.slider1.value <= 30:
                self.button_start_clicked = True
                self.button_fire_clicked = False
                self.button_rob_clicked = False
                self.button_off_clicked = False
                self.button_on_clicked = False
                self.button_put_out_clicked = False
                self.button_catch_clicked = False
                self.button_water_clicked = False
                arcade.set_background_color(arcade.color.DARK_CYAN)
                self.text = "System is observing..."
                self.text_label = arcade.gui.UITextArea(text=self.text,
                                                        width=500,
                                                        height=40,
                                                        font_size=24,
                                                        font_name="Kenney Future")
                self.text_box.clear()
                self.text_box.add(self.text_label.with_space_around(bottom=0))
                self.manager3.clear()
                self.manager3.add(
                    arcade.gui.UIAnchorWidget(
                        anchor_x="center_x",
                        align_x=-515,
                        anchor_y="center_y",
                        align_y=-260,
                        child=self.text_box)
                )
            if self.slider1.value > 30:
                self.button_water_clicked = True
                self.button_start_clicked = False
                self.button_fire_clicked = False
                self.button_rob_clicked = False
                self.button_off_clicked = False
                self.button_on_clicked = False
                self.button_put_out_clicked = False
                self.button_catch_clicked = False
                self.text = "Alarm - Water!!!"
                self.text_label = arcade.gui.UITextArea(text=self.text,
                                                        width=500,
                                                        height=40,
                                                        font_size=24,
                                                        text_color=arcade.color.PINK,
                                                        font_name="Kenney Future")
                self.text_box.clear()
                self.text_box.add(self.text_label.with_space_around(bottom=0))
                arcade.set_background_color(arcade.color.BABY_PINK)
        self.manager.draw()

    def on_message_box_close(self, button_text):
        print(f"User pressed {button_text}.")


game = MyGame()
arcade.run()
