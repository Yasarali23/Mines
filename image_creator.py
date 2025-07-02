from PIL import Image, ImageDraw

def generate_board_image(mine_tiles, safe_tiles, save_path="board.png"):
    img = Image.new("RGB", (500, 500), color="white")
    draw = ImageDraw.Draw(img)
    size = 5
    tile_size = 100

    for i in range(25):
        row = i // size
        col = i % size
        x0, y0 = col * tile_size, row * tile_size
        x1, y1 = x0 + tile_size, y0 + tile_size

        tile_num = i + 1
        if tile_num in mine_tiles:
            color = "red"
        elif tile_num in safe_tiles:
            color = "green"
        else:
            color = "gray"

        draw.rectangle([x0, y0, x1, y1], fill=color, outline="black")
        draw.text((x0 + 40, y0 + 40), str(tile_num), fill="black")

    img.save(save_path)
    return save_path
