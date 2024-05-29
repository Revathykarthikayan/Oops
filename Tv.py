class Television:
    brand = "Sony"
    price = 285000
    inches = 75 
 

    def __init__(self, channel=1, volume=50):
        self.channel = channel
        self.volume = volume

    def info(self):
        return f"Television brand is: {self.brand}, channel: {self.channel}, volume: {self.volume}"

    def set_channel(self, channel):
        if channel > 50:
            return 16
        else:
            return channel
        # if set_channel(0):
        #     print(set_channel())

    def set_volume(self, volume):
        current_volume = 50
        while volume > 100 or volume < 0:
            volume = current_volume
        else:
            return volume

    def reset(self):
        self.channel = 1
        self.volume = 50
        return f"Channel: {self.channel}, Volume: {self.volume}"


class LEDTV(Television):
    def __init__(self, channel=1, volume=50, screen_thickness=5,energy_usage=6 ,life_span=3):
        super().__init__(channel, volume)
        self.screen_thickness = screen_thickness
        self.energy_usage= energy_usage
        self.life_span=life_span



    def info(self):
        parent_info = super().info()
        return f"{parent_info}, screen_thickness: {self.screen_thickness}mm°, energy_usage: {self.energy_usage}, life_span {self.life_span}:"

class PlasmaTV(Television):
    def __init__(self, channel=1, volume=50, screen_thickness=8,energy_usage=6 ,life_span=3):
        super().__init__(channel, volume)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.life_span = life_span


    def info(self):
        parent_info = super().info()
        return f"{parent_info}, screen_thickness: {self.screen_thickness}mm, energy_usage: {self.energy_usage}, life_span {self.life_span}"


led_tv = LEDTV(channel=10, volume=30, screen_thickness=4)
plasma_tv = PlasmaTV(channel=15, volume=25, screen_thickness=6)
print(led_tv.info())
print("Status of LED TV:")
#given channel no. out of range for led
print(led_tv.set_channel(89))
print(led_tv.set_volume(45))
print()

print(plasma_tv.info())
print("Status of Plasma TV:")
#given volume out of range for plasma

print(plasma_tv.set_channel(34))
print(plasma_tv.set_volume(120))
print()
# reseting LED TV
print("LED RESET IS DONE")
print(led_tv.reset())


