
import os
import sys
from typing import Dict, Callable, Sequence, Dict
from argparse import ArgumentParser, ArgumentError
from collections import namedtuple
# import traceback

from .ivcap import init, get_config
from .logger import logger, sys_logger 
# from .utils import read_yaml_no_dates
from .service import Service
from .config import Command, INSIDE_CONTAINER

def run(args: Dict, handler: Callable[[Dict], int]) -> int:
    sys_logger.info(f"Calling '{handler}' with '{args}'")
    code = handler(args, logger)
    return code

def register_service(service: Service, handler: Callable[[Dict], int]):
    init(None, service.append_arguments)
    cmd = get_config().SERVICE_COMMAND

    if cmd == Command.SERVICE_RUN:
        sys_logger.info(f"IVCAP SDK Service '{os.getenv('GIT_TAG', '?')}/{os.getenv('GIT_COMMIT')}' built on {os.getenv('IVCAP_BUILD')}.")
        cfg = get_config()
        if INSIDE_CONTAINER:
            sys_logger.info(f"Starting order '{cfg.ORDER_ID}' for service '{service.name}' on node '{cfg.NODE_ID}'")
        try:
            code = run_service(service, cfg.SERVICE_ARGS, handler)
            sys.exit(code)
        except ArgumentError as perr:
            sys_logger.fatal(f"arg error '{perr}'")
        except Exception as err:
            sys_logger.exception(err)
            # sys_logger.error(f"Unexpected {err}, {type(err)}")
            # sys_logger.debug(traceback.format_exc())
            sys.exit(-1)
    elif cmd == Command.SERVICE_FILE:
        print(service.to_yaml())
    elif cmd == Command.SERVICE_HELP:
        ap = ArgumentParser(description=service.description, add_help=False)
        service.append_arguments(ap)
        ap.print_help()
    else:
        sys_logger.error(f"Unexpected command '{cmd}'")

def run_service(service: Service, args: Sequence[str], handler: Callable[[Dict], int]) -> int:
    ap = ArgumentParser(description=service.description)
    # Need to wait for 3.10
    # ap = ArgumentParser(description=service.description, exit_on_error=False)
    service.append_arguments(ap)
    pargs = ap.parse_args(args)
    args = vars(pargs)
    ST = namedtuple('ServiceArgs', args.keys())
    at = ST(**args)
    return run(at, handler)
    