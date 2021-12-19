#!/usr/bin/env nix-shell
#!nix-shell -p python3Packages.pyyaml python3 -i python3

# Renders API YAML file to user-readable markdown file. See luna-render-yml.py
# for reference.

# Usage:
#   scripts/luna-render-md.py content/pages/luna/apis/com.webos.service.eim.yml > content/pages/luna/apis/eim.yml

import yaml
import sys


def flatten_schema(schema, prefix=""):
    for name, p in schema.get("properties", {}).items():
        yield {"name": prefix + name, **p}
        if p.get("type") == "array":
            yield from flatten_schema(p.get("items"), prefix + name + "[].")
        if p.get("type") == "object":
            yield from flatten_schema(p, prefix + name + ".")


def render_schema(schema):
    found = False
    for prop in flatten_schema(schema):
        description = prop.get("description", "*missing description*")
        enum_info = ""
        if "enum" in prop:
            enum_info = " (supported values: {})".format(
                ", ".join(f"`{e}`" for e in prop["enum"])
            )
        req = "**" if prop["name"] in schema["required"] else ""
        print(
            f" * [`{prop['type']}`] {req}`{prop['name']}`{req} - {description}{enum_info}"
        )
        found = True
    if not found:
        print(" * *No information...*")


with open(sys.argv[1]) as fd:
    data = yaml.load(fd)

    print(f"Title: Luna service - {data['service']}")
    print()
    print("# Methods")
    for method_name, method in data["paths"].items():
        if not method.get("summary"):
            continue

        print(f"## `luna://{data['service']}{method_name}`")
        print(f"{method['summary']}")
        print()
        if method.get("requiredPermissions"):
            print(
                "**Required permissions**:",
                ", ".join(
                    [
                        "<u>`%s`</u>" % perm if perm in ["public"] else "`%s`" % perm
                        for perm in method["requiredPermissions"]
                    ]
                ),
            )

        print("### Request")
        render_schema(method.get("request"))
        print()

        print("### Response")
        render_schema(method.get("response"))
        print()
