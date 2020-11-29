import pye57
e57 = pye57.E57("test.e57")
projTypes = [
    "visualReferenceRepresentation",
    "pinholeRepresentation",
    "sphericalRepresentation",
    "cylindricalRepresentation"
]
imgTypes = [
    "jpegImage",
    "pngImage",
    "imageMask"
]
imf = e57.image_file
root = imf.root()
count = imf.root().childCount()
data3d = root["data3D"]
count = data3d.childCount()
images2d = root["images2D"]
count = images2d.childCount()

for proj in projTypes:
    try:
        images2d[0].isDefined(proj)
        present = pye57.libe57.StructureNode(images2d[0].get(proj))
        ptype = proj
        for item in imgTypes:
            try:
                present.isDefined(item)
                itype = item
                break
            except:
                pass
    except:
        pass

for ind,image in enumerate(images2d):
    name = pye57.libe57.StringNode(image.get("name")).value()
    presentation = pye57.libe57.StructureNode(image.get(ptype))
    ImageSize = pye57.libe57.BlobNode(presentation.get(itype)).byteCount()
    Image = pye57.libe57.BlobNode(presentation.get(itype))
    filepath = "/home/chenhsi/Projects/pye57 folder/"+"image_"+str(ind)+".jpg"
    Image.saveImage(ImageSize, filepath)

