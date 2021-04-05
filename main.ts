let disabled = 0
let scren: grove.TM1637 = null
let time_is_set = 0
let time_raw = ""
let time_lol = 0
let time_lol_x100 = 0
let time_lol_2 = 0
let time_final = 0
input.onButtonPressed(Button.A, function () {
    timeanddate.advanceBy(1, timeanddate.TimeUnit.Hours)
})
input.onButtonPressed(Button.AB, function () {
    disabled = 1
    basic.clearScreen()
    scren.point(false)
    scren.show(0)
    basic.pause(1000)
    disabled = 0
})
input.onButtonPressed(Button.B, function () {
    timeanddate.advanceBy(1, timeanddate.TimeUnit.Minutes)
})
basic.forever(function () {
    if (disabled == 0) {
        if (time_is_set == 0) {
            timeanddate.setTime(11, 30, 0, timeanddate.MornNight.PM)
        }
        time_is_set = 1
        time_raw = timeanddate.time(timeanddate.TimeFormat.HHMM24hr)
        time_lol = parseFloat(timeanddate.time(timeanddate.TimeFormat.HHMM24hr))
        time_lol_x100 = time_lol * 100
        if (time_lol == 0) {
            time_lol_x100 = 2400
        }
        time_lol_2 = parseFloat(time_raw.substr(3, 2))
        time_final = time_lol_x100 + time_lol_2
        scren = grove.createDisplay(DigitalPin.P0, DigitalPin.P14)
        scren.point(true)
        scren.show(time_final)
    }
})
