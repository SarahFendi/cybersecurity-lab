import subprocess

target = "127.0.0.1"

result = subprocess.run(
    ["nmap", "-sV", target],
    capture_output=True,
    text=True
)

print(result.stdout)
