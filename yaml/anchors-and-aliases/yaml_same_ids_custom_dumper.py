# yaml_same_ids_custom_dumper.py
import yaml


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


interfaces = dict(
    Ethernet1=dict(description="Uplink to core-1", speed=1000, mtu=9000),
    Ethernet2=dict(description="Uplink to core-2", speed=1000, mtu=9000),
)

prop_vals = ["pim", "ptp", "lldp"]

interfaces["Ethernet1"]["properties"] = prop_vals
interfaces["Ethernet2"]["properties"] = prop_vals

# Show IDs referenced by "properties" key
print("Ethernet1 properties object id:", id(interfaces["Ethernet1"]["properties"]))
print("Ethernet2 properties object id:", id(interfaces["Ethernet2"]["properties"]))

# Dump YAML to stdout
print("\n##### Resulting YAML:\n")
print(yaml.dump(interfaces, Dumper=NoAliasDumper))


# Dump YAML to file
with open("yaml_files/interfaces_same_ids_no_alias.yml", "w") as fout:
    yaml.dump(interfaces, fout, Dumper=NoAliasDumper)
