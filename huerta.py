import json

# Simulación de entrada JSON (este es tu BLOCK_INPUT)
BLOCK_INPUT = '{"LUZ": 28, "HUMEDAD": 57, "TEMPERATURA": 70}'

# Parse the input JSON
data = json.loads(BLOCK_INPUT)

# Extract values
LUZ = data['LUZ']
HUMEDAD = data['HUMEDAD']
TEMPERATURA = data['TEMPERATURA']

# Determine statuses
ESTADO_LUZ = 'iluminado' if LUZ > 40 else 'oscuro'
ESTADO_HUMEDAD = 'húmedo' if HUMEDAD > 37 else 'seco'
if TEMPERATURA >= 30:
    TEMPERATURA_ESTADO = 'caliente'
elif 20 <= TEMPERATURA < 30:
    TEMPERATURA_ESTADO = 'normal'
else:
    TEMPERATURA_ESTADO = 'frío'

# Format into a JSON object
status = {
    'ESTADO_LUZ': ESTADO_LUZ,
    'ESTADO_HUMEDAD': ESTADO_HUMEDAD,
    'TEMPERATURA_ESTADO': TEMPERATURA_ESTADO, 
}

# Output the JSON object
print(json.dumps(status, ensure_ascii=False, indent=4))  # Para formatear la salida