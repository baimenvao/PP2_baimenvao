import json
import os


script_dir = os.path.dirname(__file__)
json_path = os.path.join(script_dir, "sample-data.json")

with open(json_path, "r") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
print(f"{'-'*50} {'-'*20} {'-'*7} {'-'*6}")

for item in data["imdata"]:
    attr = item["l1PhysIf"]["attributes"]
    dn = attr.get("dn", "")
    descr = attr.get("descr", "")
    speed = attr.get("speed", "inherit")
    mtu = attr.get("mtu", "")
    print(f"{dn:<50} {descr:<20} {speed:<7} {mtu:<6}")