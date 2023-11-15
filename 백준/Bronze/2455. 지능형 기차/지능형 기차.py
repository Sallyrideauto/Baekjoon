out_1, in_1 = map(int, input().split())
out_2, in_2 = map(int, input().split())
out_3, in_3 = map(int, input().split())
out_4, in_4 = map(int, input().split())

passengers = []

passengers.append(in_1)

station_2 = in_1 - out_2 + in_2
passengers.append(station_2)

station_3 = station_2 - out_3 + in_3
passengers.append(station_3)

station_4 = station_3 - out_4
passengers.append(station_4)

print(max(passengers))