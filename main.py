from humanfriendly.terminal import output
from rembg import remove
from PIL import Image
import requests
from io import BytesIO

# Tải ảnh từ trên mạng
response = requests.get("https://cdn.pixabay.com/photo/2023/11/07/20/24/cristiano-ronaldo-8373364_1280.jpg")
image_server = Image.open(BytesIO(response.content))
# Tải ảnh lên từ local
image_local = Image.open("./input/cristiano_ronaldo.jpg")

# Xóa background của ảnh
output_server = remove(image_server)
output_local = remove(image_local)

# Lưu ảnh
output_server.save("./output/output_server.png")
output_local.save("./output/output_local.png")
