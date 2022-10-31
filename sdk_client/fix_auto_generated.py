import os
import fnmatch

for root, dir, files in os.walk(f"{os.getcwd()}/sdk_client/ivcap_client/api"):
    svc = root.split("/")[-1]
    #print(f"dir: {svc}:{root}")
    for el in fnmatch.filter(files, f"{svc}*.py"):
        orig = f"{root}/{el}"
        newn = f"{root}/{svc}_{el[len(svc):]}"
        #print(f"{orig} -> {newn} ")
        os.rename(orig, newn)