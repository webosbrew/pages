#!/usr/bin/env nix-shell
#!nix-shell -p python3Packages.pyyaml python3 -i python3

# Generates template API YAML file from "Services Survey" script data:
# https://gist.github.com/Informatic/0033ba3bdb2f88f244da6edb01c268ed

import json
import yaml
import sys

with open(sys.argv[1]) as fd:
    data = json.load(fd)
    for service_name, service in data["services"].items():
        if not service.get("categories"):
            continue
        if len(sys.argv) > 2 and sys.argv[2] != service_name:
            continue
        svc = {
            "service": service_name,
            "paths": {},
        }
        for category_path, category in service["categories"].items():
            for method_name, method in category["methods"].items():
                path = f'{category_path.rstrip("/")}/{method_name}'
                svc["paths"][path] = {
                    "summary": "",
                    "subscribable": False,
                    "requiredPermissions": list(
                        set(method["provides"]).difference({"all"})
                    ),
                    "request": {"type": "object", "required": [], "properties": {}},
                    "response": {"type": "object", "properties": {}},
                }
        print(yaml.dump(svc, sort_keys=False, Dumper=yaml.Dumper))
