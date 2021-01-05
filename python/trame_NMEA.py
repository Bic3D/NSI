import webbrowser

trame_ex = "$GPGGA,064036.289,4836.5375,N,00740.9373,E,1,04,3.2,200.2,M,,,,0000*0E"
zoom = "16"

def origin(trame):
    first_element = trame.split(",")[0][1:3]

    if first_element == "BD" or first_element == "GB":
        return "Beidou"
    elif first_element == "GA":
        return "Galileo"
    elif first_element == "GP":
        return "GPS"
    elif first_element == "GL":
        return "GLONASS"
    else:
        print("Erreur: trame invalide")
        return

def infos(trame, openweb = False):
    time = trame.split(",")[1]
    lat = trame.split(",")[2]
    lat_dir = trame.split(",")[3]
    lon = trame.split(",")[4]
    lon_dir = trame.split(",")[5]

    time_text = "heure     : "+time[0:2]+" : "+time[2:4]+" : "+time[4:6]

    lat_d = lat[0:2]
    lat_m = lat[2:4]
    lat_s = str(float(lat[4:]) * 60)

    lon_d = lon[0:3]
    lon_m = lon[3:5]
    lon_s = str(float(lon[5:]) * 60)

    lat_text = "lattitude : " + lat_d + "° " + lat_m + "' " + lat_s + '" ' + lat_dir
    lon_text = "longitude : " + lon_d + "° " + lon_m + "' " + lon_s + '" ' + lon_dir

    text = time_text + "\n" + lat_text + "\n" + lon_text
    
    if openweb:
        lattitude = float(lat_d) + float(lat_m)/60 + float(lat_s)/3600
        longitude = float(lon_d) + float(lon_m)/60 + float(lon_s)/3600
        webbrowser.open("https://www.openstreetmap.org/#map="+zoom+"/"+str(lattitude)+"/"+str(longitude))
    
    return text


print(infos(trame_ex, True))