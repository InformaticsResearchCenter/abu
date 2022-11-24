import bluetooth
while True:
    list=bluetooth.discover_devices(lookup_names=True)
    print(list)