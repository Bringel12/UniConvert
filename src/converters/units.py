FACTORS = {
    "Comprimento": {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
    },
    "Massa": {
        "mg": 0.000001,
        "g": 0.001,
        "kg": 1,
        "tonelada": 1000,
    },
    "Volume": {
        "mL": 0.000001,
        "L": 0.001,
        "m³": 1,
    },
    "Tempo": {
        "segundos": 1,
        "minutos": 60,
        "horas": 3600,
        "dias": 86400,
    },
    "Armazenamento digital": {
        "B": 1,
        "KB": 1000,
        "MB": 1000**2,
        "GB": 1000**3,
        "TB": 1000**4,
    },
}


def convert_units(value, category, source, target):
    """Converte unidades de uma categoria compatível."""
    value = float(value)

    if category == "Temperatura":
        return convert_temperature(value, source, target)

    if category not in FACTORS:
        raise ValueError("Categoria de conversão inválida.")

    units = FACTORS[category]

    if source not in units or target not in units:
        raise ValueError("Selecione unidades válidas.")

    # Converte primeiro para a unidade-base.
    base_value = value * units[source]
    return base_value / units[target]


def convert_temperature(value, source, target):
    """Converte entre Celsius, Fahrenheit e Kelvin."""
    supported = {"°C", "°F", "K"}

    if source not in supported or target not in supported:
        raise ValueError("Unidade de temperatura inválida.")

    # Converte a temperatura de origem para Celsius.
    if source == "°C":
        celsius = value
    elif source == "°F":
        celsius = (value - 32) * 5 / 9
    else:
        celsius = value - 273.15

    if celsius < -273.15:
        raise ValueError("A temperatura não pode ser inferior a zero Kelvin.")

    # Converte Celsius para a unidade de destino.
    if target == "°C":
        return celsius
    elif target == "°F":
        return celsius * 9 / 5 + 32
    else:
        return celsius + 273.15


def get_categories():
    """Retorna as categorias disponíveis."""
    return list(FACTORS.keys()) + ["Temperatura"]


def get_units(category):
    """Retorna as unidades disponíveis para a categoria."""
    if category == "Temperatura":
        return ["°C", "°F", "K"]

    return list(FACTORS.get(category, {}).keys())