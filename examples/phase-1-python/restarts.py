import json
import subprocess

out = subprocess.run(
    ["kubectl", "get", "pods", "-A", "-o", "json"],
    capture_output=True, text=True, check=True,
).stdout

for pod in json.loads(out)["items"]:
    for cs in pod["status"].get("containerStatuses", []):
        if cs["restartCount"] > 3:
            ns, name = pod["metadata"]["namespace"], pod["metadata"]["name"]
            print(f"{ns}/{name}  container={cs['name']}  restarts={cs['restartCount']}")
