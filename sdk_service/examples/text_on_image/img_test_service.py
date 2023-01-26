import sys, os
sys.path.append(os.path.join(os.getcwd(), '../../src'))

import logging
from PIL import Image, ImageDraw, ImageFont

from ivcap_sdk_service import Service, Parameter, Type, SupportedMimeTypes, ServiceArgs
from ivcap_sdk_service import register_service, deliver_data, fetch_data, create_metadata

logger = None # set when called by SDK

SERVICE = Service(
    name = "simple-python-service",
    description = "A simple IVCAP service using the IVCAP Service SDK to create an image with text overlays",
    parameters = [
        Parameter(
            name='msg', 
            type=Type.STRING, 
            description='Message to display.'),
        Parameter(
            name='img-art', 
            type=Type.ARTIFACT, 
            description='Image artifact to use as background.',
            optional=True),
        Parameter(
            name='img-url', 
            type=Type.STRING, 
            description='Image url (external) to use as background.',
            optional=True),
        Parameter(
            name='width', 
            type=Type.INT, 
            description='Image width.',
            default=640),
        Parameter(
            name='height', 
            type=Type.INT, 
            description='Image height.',
            default=480),
    ]
)

def service(args: ServiceArgs, svc_logger: logging):
    global logger 
    logger = svc_logger

    # Create an image
    img = Image.new("RGBA", (args.width, args.height), "white")
    
    # Add background
    if args.img_url:
        f = fetch_data(args.img_url)
        background = Image.open(f)
        img.paste(background)
        f.close() # the above code does not close the file
    
    # Draw message
    canvas = ImageDraw.Draw(img)
    font = ImageFont.truetype('CaveatBrush-Regular.ttf', 100)
    center = (args.width / 2, args.height / 2)
    canvas.text(center, args.msg, font=font, anchor='mm', fill=(255, 130, 0))   
    
    meta = create_metadata('urn:ivcap.test:simple-python-service', **args._asdict())
    deliver_data("image.png", lambda fd: img.save(fd, format="png"), SupportedMimeTypes.JPEG, metadata=meta)
    
register_service(SERVICE, service)
