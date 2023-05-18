horas = int(input("Digite a hora: "))
minutos = int(input("Digite os minutos: "))

duracaoMinutos = int(input("Digite a duração em minutos: "))

# minutos = (duracaoMinutos + minutos) % 60
# horas += (duracaoMinutos + horas) // 60

# horas %= 24;

minutos = minutos + duracaoMinutos  # find a total of all minutes
# find a number of hours hidden in minutes and update the hour
horas = horas + minutos // 60
minutos = minutos % 60  # correct minutes to fall in the (0..59) range
horas = horas % 24  # correct hours to fall in the (0..23) range

print(horas, minutos, sep=":")
