import pyqrcode
import png
from pyqrcode import QRCode

s = "https://hudhamasjithmeenodaikkaddu.blogspot.com/2022/09/masjidhul-hudha-jummah-mosque.html"

url = pyqrcode.create(s)

url.svg("mosque.svg", scale=8)

url.png("mosque.png", scale=6)