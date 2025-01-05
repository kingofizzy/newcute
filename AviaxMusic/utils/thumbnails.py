import os
import re
import textwrap
import aiofiles
import aiohttp
from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from youtubesearchpython.__future__ import VideosSearch
from config import YOUTUBE_IMG_URL
from AviaxMusic import app


def rectangle(img, size):
    return img.resize(size, Image.ANTIALIAS)


async def gen_thumb(videoid):
    if os.path.isfile(f"cache/{videoid}.png"):
        return f"cache/{videoid}.png"

    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"]
                title = re.sub("\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown"
            try:
                views = result["viewCount"]["short"]
            except:
                views = "Unknown"
            try:
                channel = result["channel"]["name"]
            except:
                channel = "Unknown"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"cache/thumb{videoid}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()

        youtube = Image.open(f"cache/thumb{videoid}.png")
        zyoutube = Image.open(f"cache/thumb{videoid}.png")
        bg = Image.open(f"assets/Thumbnail.png")
        image1 = youtube.resize((1280, 720))
        image2 = image1.convert("RGBA")
        background = image2.filter(ImageFilter.BoxBlur(20))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(1.1)

        # rectangle code
        rectangle_size = (439, 270)
        y = rectangle(zyoutube, rectangle_size)
        enhancer = ImageEnhance.Brightness(y)
        y = enhancer.enhance(1.1)
        background.paste(y, (793, 105))  

        image3 = bg.resize((1280, 720))
        image5 = image3.convert("RGBA")
        result_img = Image.alpha_composite(background, image5)
        draw = ImageDraw.Draw(result_img)
        font = ImageFont.truetype("assets/font2.ttf", 52)
        font2 = ImageFont.truetype("assets/font2.ttf", 27)
        font3 = ImageFont.truetype("assets/font2.ttf", 25)
        

        short_title = title[:39]
        if len(short_title) > 20:
            first_line = short_title[:20]
            second_line = short_title[20:]
        else:
            first_line = short_title
            second_line = ""


        try:
            draw.text(
                (80, 180),
                f"{first_line}",
                fill="white",
             #   stroke_width=1,
              #  stroke_fill="black",
                font=font,
            )
            if second_line:
                draw.text(
                    (80, 240),
                    f"{second_line}",
                    fill="white",
                  #  stroke_width=1,
                  #  stroke_fill="black",
                    font=font,
                )
            draw.text(
                (80, 510),
                f"00:00",
                fill="white",
              #  stroke_width=1,
               # stroke_fill="black",
                font=font2,
            )
            draw.text(
                (600, 510),
                f"{duration}",
                fill="white",
              #  stroke_width=1,
             #   stroke_fill="black",
                font=font2,
            )
            draw.text(
                    (580, 460),
                    f"{views}",
                    fill="white",
                  #  stroke_width=1,
                    #stroke_fill="black",
                    font=font3,
            )
            draw.text(
                    (83, 460),
                    f"{channel}   ",
                    fill="white",
                 #   stroke_width=1,
                  #  stroke_fill="black",
                    font=font3,
            )
        except Exception as e:
            print(e)
            pass

        result_img.save(f"cache/{videoid}.png")
        return f"cache/{videoid}.png"

    except Exception as e:
        print(e)
        return YOUTUBE_IMG_URL


async def gen_qthumb(videoid):
    if os.path.isfile(f"cache/{videoid}.png"):
        return f"cache/{videoid}.png"

    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"]
                title = re.sub("\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown"
            try:
                views = result["viewCount"]["short"]
            except:
                views = "Unknown"
            try:
                channel = result["channel"]["name"]
            except:
                channel = "Unknown"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"cache/thumb{videoid}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()

        youtube = Image.open(f"cache/thumb{videoid}.png")
        zyoutube = Image.open(f"cache/thumb{videoid}.png")
        bg = Image.open(f"assets/Thumbnail.png")
        image1 = youtube.resize((1280, 720))
        image2 = image1.convert("RGBA")
        background = image2.filter(ImageFilter.BoxBlur(20))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(1.1)

        # rectangle code
        rectangle_size = (439, 270)
        y = rectangle(zyoutube, rectangle_size)
        enhancer = ImageEnhance.Brightness(y)
        y = enhancer.enhance(1.1)
        background.paste(y, (793, 105))  # i think its works

        image3 = bg.resize((1280, 720))
        image5 = image3.convert("RGBA")
        result_img = Image.alpha_composite(background, image5)
        draw = ImageDraw.Draw(result_img)
        font = ImageFont.truetype("assets/font2.ttf", 52)
        font2 = ImageFont.truetype("assets/font2.ttf", 27)
        font3 = ImageFont.truetype("assets/font2.ttf", 25)
        

        short_title = title[:39]
        if len(short_title) > 20:
            first_line = short_title[:20]
            second_line = short_title[20:]
        else:
            first_line = short_title
            second_line = ""
 

        try:
            draw.text(
                (80, 180),
                f"{first_line}",
                fill="white",
                stroke_width=1,
                stroke_fill="black",
                font=font,
            )
            if second_line:
                draw.text(
                    (80, 240),
                    f"{second_line}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="black",
                    font=font,
                )
            draw.text(
                (80, 510),
                f"00:00",
                fill="white",
                stroke_width=1,
                stroke_fill="black",
                font=font2,
            )
            draw.text(
                (600, 510),
                f"{duration}",
                fill="white",
                stroke_width=1,
                stroke_fill="black",
                font=font2,
            )
            draw.text(
                    (580, 460),
                    f"{views}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="black",
                    font=font3,
            )
            draw.text(
                    (83, 460),
                    f"{channel}   ",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="black",
                    font=font3,
            )
        except Exception as e:
            print(e)
            pass

        result_img.save(f"cache/{videoid}.png")
        return f"cache/{videoid}.png"

    except Exception as e:
        print(e)
        return YOUTUBE_IMG_URL
