def calcular_promedio_temperaturas(ciudades, temperaturas, num_dias, num_semanas):
    for i, ciudad in enumerate(ciudades):
        print(f"\nCiudad: {ciudad}")
        for j in range(num_semanas):
            promedio_semana = sum(temperaturas[i][j]) / num_dias
            print(f"  Semana {j + 1}: Promedio de temperatura = {promedio_semana:.2f}°C")

ciudades = ["Quito", "Salinas", "Ambato", "Cuenca", "Oriente"]

temperaturas = [
    [
        [22, 24, 23, 25, 22, 21, 23],
        [23, 24, 22, 23, 24, 22, 23],
        [24, 25, 24, 22, 23, 24, 25],
        [22, 23, 21, 22, 24, 23, 23],
    ],
    [
        [28, 29, 30, 31, 28, 29, 30],
        [30, 31, 29, 28, 29, 30, 31],
        [29, 28, 30, 31, 30, 29, 30],
        [30, 31, 29, 28, 30, 31, 30],
    ],
    [
        [18, 19, 18, 17, 19, 20, 19],
        [20, 21, 19, 20, 21, 19, 20],
        [19, 20, 18, 17, 19, 21, 20],
        [18, 19, 17, 18, 20, 21, 19],
    ],
    [
        [15, 16, 17, 15, 16, 14, 15],
        [16, 17, 16, 15, 14, 16, 17],
        [17, 18, 19, 17, 18, 19, 18],
        [16, 15, 16, 14, 15, 17, 16],
    ],
    [
        [30, 31, 32, 33, 30, 31, 32],
        [32, 33, 31, 30, 32, 31, 33],
        [31, 32, 30, 33, 32, 31, 30],
        [32, 31, 30, 33, 32, 30, 31],
    ]
]

num_dias = 7
num_semanas = 4

calcular_promedio_temperaturas(ciudades, temperaturas, num_dias, num_semanas)
