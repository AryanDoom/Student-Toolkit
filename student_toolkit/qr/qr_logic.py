import qrcode
from PIL import Image

#storing the mapped urls and subject we do offer
url_map = { "maths1": "https://drive.google.com/drive/folders/1gYFT1RvJD5XmsquB99-vXC5xBWV9EzZZ",
            "maths2": "https://drive.google.com/drive/folders/1iaewOilIhQZZgfCKqDJeFC2lty7g9AQk",
            "chemistry": "https://drive.google.com/drive/folders/1yHNKMxDFvf_FopJ-ZCDNKRlGleTFQZcN",
            "mechanics": "https://drive.google.com/drive/folders/1JGEaaw-j-tzMTEhRoxM7gmtSEaK2ZT5j",
            "epd": "https://drive.google.com/drive/folders/1rkUuM3-W249sFgl1Eqn6zbx29AaTCHLB",
            "placeholder": "https://textbooks.example.com/",
            "python": "https://drive.google.com/file/d/17cVJ_8MPCULzXPcgt4if4O6fBAsfy1Uc/view",
            "physics": "https://drive.google.com/file/d/1KwxEcR4klXQwS-uKcO16PXHQPMmHDCAj/view",
            "electrical": "https://drive.google.com/drive/folders/16UDSJJ4c4N3StFjDbvdwRFuV-gFfWT3S", 
            "physicslab": "https://drive.google.com/file/d/1GMoZGnNMitVkx-VvcuIWr3qAQD7fnhqK/view", 
            "constitution": "https://drive.google.com/drive/folders/1viBbRv-CGnwFGfJLcC2os6t90fpMwQuG", 
            "evs": "https://drive.google.com/file/d/1IKXMDt1LeoBH4uyD7LiQx_8BmQaLbR0K/view?usp=drive_link" }



def generate_qr_image(subject):
    # Normalize input (makes user input flexible)
    subject_key = subject.replace(" ", "").lower()

    # Get URL
    book_url = url_map.get(subject_key, "")

    if not book_url:
        raise ValueError(f"Subject '{subject}' not found in database.")

    # QR code specifications
    qr = qrcode.QRCode(version=None, box_size=10, border=4)  # version like decides what size it will be (none lets it be whatever it wants to be uk)
    qr.add_data(book_url)
    qr.make(fit=True)  #again does the same , lets the qr code be whatever it wants to be

    img = qr.make_image(fill_color="#1e90ff", back_color="black")
    img = img.resize((200, 200))  #makes it a uniform size for the ui ( idk how but it will be too small or too big if this line is not there)

    return img
