from PIL import Image, ImageDraw

def make_icon(size, path, maskable=False):
    img = Image.new("RGBA", (size, size), (0,0,0,0))
    d = ImageDraw.Draw(img)
    pad = int(size*0.10) if maskable else 0
    bg_box = [pad, pad, size-pad, size-pad]
    radius = int(size*0.18)
    # leather cover background
    d.rounded_rectangle(bg_box, radius=radius, fill=(92,42,42,255))
    # brass corner accents
    corner = int(size*0.16)
    d.rectangle([bg_box[0], bg_box[1], bg_box[0]+corner, bg_box[1]+corner], fill=(201,162,39,255))
    d.rectangle([bg_box[2]-corner, bg_box[3]-corner, bg_box[2], bg_box[3]], fill=(201,162,39,255))
    # page/notebook block
    m = size*0.30
    page_box = [bg_box[0]+m*0.55, bg_box[1]+m*0.45, bg_box[2]-m*0.55, bg_box[3]-m*0.35]
    d.rounded_rectangle(page_box, radius=int(size*0.04), fill=(247,241,224,255))
    # ruled lines
    lx0 = page_box[0] + (page_box[2]-page_box[0])*0.15
    lx1 = page_box[2] - (page_box[2]-page_box[0])*0.15
    n_lines = 4
    for i in range(1, n_lines+1):
        ly = page_box[1] + (page_box[3]-page_box[1]) * (i/(n_lines+1))
        d.line([lx0, ly, lx1, ly], fill=(180,150,110,255), width=max(1,int(size*0.012)))
    # pen nib stroke (diagonal accent)
    d.line([page_box[0]+ (page_box[2]-page_box[0])*0.18, page_box[3]-(page_box[3]-page_box[1])*0.18,
            page_box[2]-(page_box[2]-page_box[0])*0.12, page_box[1]+(page_box[3]-page_box[1])*0.12],
           fill=(38,45,69,255), width=max(2,int(size*0.035)))
    img.save(path)

make_icon(192, "icon-192.png")
make_icon(512, "icon-512.png")
make_icon(512, "icon-512-maskable.png", maskable=True)
print("done")
