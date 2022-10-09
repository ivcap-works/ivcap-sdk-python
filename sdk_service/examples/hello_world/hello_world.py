from typing import Dict
#TypedDict
from ivcap_service import Service, Parameter, Option, Type, register_service
import logging

SERVICE = Service(
    name = "HelloWorld",
    description = "Simple service which does a few simple things",
    providerID = "ivcap:provider:0000-0000-0000",
    parameters = [
        Parameter(name="msg", type=Type.STRING, description="Message to echo"),
        Parameter(name="times", type=Type.INT, default=2, description="Times to repeat"),
        Parameter(
            name='device',
            type=Type.OPTION,
            options=[Option(value='cpu'), Option(value='gpu')],
            default="gpu",
            description="Select which device to inference."),
    ]
)

def hello_world(args: Dict, logger: logging):
    for _ in range(args.times):
        logger.info(f"Hello {args.msg}")

register_service(SERVICE, hello_world)