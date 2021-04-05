disabled = 0
time_is_set = 0
time_raw = ""
time_lol = 0
time_lol_x100 = 0
time_lol_2 = 0
time_final = 0
scren: grove.TM1637 = None

def on_button_pressed_a():
    timeanddate.advance_by(1, timeanddate.TimeUnit.MINUTES)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global disabled
    disabled = 1
    basic.clear_screen()
    basic.pause(1000)
    disabled = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global time_is_set, time_raw, time_lol, time_lol_x100, time_lol_2, time_final, scren
    if disabled == 0:
        if time_is_set == 0:
            timeanddate.set_time(11, 59, 0, timeanddate.MornNight.PM)
        time_is_set = 1
        basic.pause(200)
        time_raw = timeanddate.time(timeanddate.TimeFormat.HHMM2_4HR)
        basic.pause(200)
        time_lol = parse_float(timeanddate.time(timeanddate.TimeFormat.HHMM2_4HR))
        time_lol_x100 = time_lol * 100
        if time_lol_2 == 0:
            time_lol = 12
        time_lol_2 = parse_float(time_raw.substr(3, 2))
        basic.pause(200)
        time_final = time_lol_x100 + time_lol_2
        basic.pause(1000)
        scren = grove.create_display(DigitalPin.P0, DigitalPin.P14)
        scren.point(True)
        scren.show(time_final)
        basic.show_string("" + str((time_final)))
basic.forever(on_forever)
