from typing import Dict
#TypedDict
from ivcap_sdk_service import Service, Parameter, Type, register_service
import logging

SERVICE = Service(
    name = "load-artifact",
    description = "Service to test loading and saving of artifacts",
    providerID = "ivcap:provider:0000-0000-0000",
    parameters = [
        Parameter(name="load", type=Type.ARTIFACT, description="Artifact to load"),
   ]
)

def load_artifact(args: Dict, logger: logging):
    logger.info(f"Called with {args}")
    with args.load.open(asBinary=False) as f:
        print(f.read())

register_service(SERVICE, load_artifact)