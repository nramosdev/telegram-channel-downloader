# Copyright (c) 2024 Nicolás Ramos <hola@nramos.dev>
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from telethon.sync import TelegramClient
from telethon.tl.types import InputMessagesFilterDocument
from telethon.errors import SessionPasswordNeededError
import os
import json

# Configuración
api_id = 'TU_API_ID'
api_hash = 'TU_API_HASH'
phone = 'TU_NUMERO_DE_TELEFONO'
channel_username = '@EpubLibreLibros'
estado_archivo = 'estado.json'

def guardar_estado(ultimo_id):
    with open(estado_archivo, 'w') as f:
        json.dump({'ultimo_id': ultimo_id}, f)

def cargar_estado():
    if os.path.exists(estado_archivo):
        with open(estado_archivo, 'r') as f:
            return json.load(f).get('ultimo_id', 0)
    return 0

async def descargar_archivos():
    async with TelegramClient('sesion', api_id, api_hash) as client:
        try:
            if not await client.is_user_authorized():
                await client.send_code_request(phone)
                try:
                    await client.sign_in(phone, input('Introduce el código que recibiste: '))
                except SessionPasswordNeededError:
                    await client.sign_in(password=input('Introduce tu contraseña de dos pasos: '))

            ultimo_id = cargar_estado()
            async for mensaje in client.iter_messages(channel_username, filter=InputMessagesFilterDocument, min_id=ultimo_id):
                if mensaje.document:
                    nombre_archivo = mensaje.document.attributes[0].file_name
                    print(f"Procesando mensaje con archivo: {nombre_archivo}")
                    ruta_archivo = os.path.join(os.getcwd(), nombre_archivo)
                    if os.path.exists(ruta_archivo):
                        print(f"Archivo ya existe: {nombre_archivo}, omitiendo descarga.")
                        continue

                    archivo = await mensaje.download_media()
                    print(f"Archivo descargado: {archivo}")
                    guardar_estado(mensaje.id)

        except Exception as e:
            print(f"Error: {e}")

session_file = 'sesion.session'
if os.path.exists(session_file):
    os.remove(session_file)

async def main():
    await descargar_archivos()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())