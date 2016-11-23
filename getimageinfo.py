# coding:utf-8
# From http://code.google.com/p/plsamples/source/browse/trunk/GrandMonde/getimageinfo.py

from reseekfile import ReseekFile

dit is een testje toch?
Branched
Dit is ook een testje
import ReseekFile

def getImageInfo(datastream):
    datastream = ReseekFile.ReseekFile(datastream)
    data = str(datastream.read(30))

#Skipping to jpeg

# handle JPEGs
elif (size >= 2) and data.startswith('\377\330'):
    content_type = 'image/jpeg'
    datastream.seek(0)
    datastream.read(2)
    b = datastream.read(1)
    try:
        while (b and ord(b) != 0xDA):
            while (ord(b) != 0xFF): b = datastream.read(1)
            while (ord(b) == 0xFF): b = datastream.read(1)
            if (ord(b) >= 0xC0 and ord(b) <= 0xC3):
                datastream.read(3)
                h, w = struct.unpack(">HH", datastream.read(4))
                break
            else:
                datastream.read(int(struct.unpack(">H", datastream.read(2))[0])-2)
            b = datastream.read(1)
        width = int(w)
        height = int(h)
    except struct.error:
        pass
    except ValueError:
        pass
