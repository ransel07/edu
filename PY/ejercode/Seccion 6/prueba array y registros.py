# Crea un array de registros con tuplas
registros = [
    ('Juan', 'juan@example.com', '555-555-1212'),
    ('Ana', 'ana@example.com', '555-555-1213'),
    ('Pedro', 'pedro@example.com', '555-555-1214'),
]

# Accede a los campos de cada elemento del array
#for nombre, email, telefono in registros:
    #print(f'Nombre: {nombre}, Email: {email}, Teléfono: {telefono}')




# Crea un array de registros con diccionarios
registros = [
    {'nombre': 'Juan', 'email': 'juan@example.com', 'telefono': '555-555-1212'},
    {'nombre': 'Ana', 'email': 'ana@example.com', 'telefono': '555-555-1213'},
    {'nombre': 'Pedro', 'email': 'pedro@example.com', 'telefono': '555-555-1214'},
    {'nombre': 'Marta', 'email': 'marta@example.com', 'telefono': '555-555-1215'}
]

# Accede a los campos de cada elemento del array
for registro in registros:
    print(f'Nombre: {registro["nombre"]}, Email: {registro["email"]}, Teléfono: {registro["telefono"]}')