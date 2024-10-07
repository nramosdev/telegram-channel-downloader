# Telegram Channel Downloader

Este script permite descargar automáticamente archivos de un canal de Telegram específico. Desarrollado por Nicolás Ramos, este proyecto es útil para archivar o sincronizar contenido de canales de Telegram en tu dispositivo local.

## Características

- Descarga automática de archivos de un canal de Telegram especificado.
- Evita la descarga de archivos duplicados.
- Guarda el estado de la descarga para reanudar desde donde se dejó.
- Manejo de autenticación de Telegram, incluyendo autenticación de dos factores.

## Requisitos previos

- Python 3.7 o superior
- Una cuenta de Telegram
- API ID y API Hash de Telegram (obtenidos de https://my.telegram.org)

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/nramosdev/telegram-channel-downloader.git
   cd telegram-channel-downloader
   ```

2. Instala las dependencias necesarias:
   ```
   pip install telethon
   ```

## Configuración

1. Abre el archivo `telegram_downloader.py` en un editor de texto.

2. Reemplaza los siguientes valores con tu información:
   ```python
   api_id = 'TU_API_ID'
   api_hash = 'TU_API_HASH'
   phone = 'TU_NUMERO_DE_TELEFONO'
   channel_username = '@NombreDelCanal'
   ```

## Uso

1. Ejecuta el script:
   ```
   python telegram_downloader.py
   ```

2. Si es la primera vez que ejecutas el script, se te pedirá que introduzcas el código de verificación enviado a tu teléfono.

3. El script comenzará a descargar los archivos del canal especificado. Los archivos se guardarán en el directorio actual.

4. El progreso de la descarga se mostrará en la consola.

5. Si el script se interrumpe, puedes volver a ejecutarlo y continuará desde donde se quedó.

## Notas

- Asegúrate de tener permisos para descargar contenido del canal especificado.
- El script guarda el estado de la descarga en un archivo llamado `estado.json`. No elimines este archivo si quieres reanudar la descarga desde el último punto.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para sugerir cambios o mejoras.

## Contacto

Nicolás Ramos - hola@nramos.dev

Enlace del proyecto: [https://github.com/nramosdev/telegram-channel-downloader](https://github.com/nramosdev/telegram-channel-downloader)
