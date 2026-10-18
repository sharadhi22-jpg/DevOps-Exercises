import docker
from docker.errors import DockerException, APIError

client = docker.from_env()
container = None

try:
    print("Building Docker image...")
    image, logs = client.images.build(
        path=".",
        tag="flask-apparmor"
    )

    for log in logs:
        if "stream" in log:
            print(log["stream"], end="")

    print("\nDocker image built successfully!")

    print("\nChecking Docker security configuration...")
    info = client.info()
    print("Operating system:", info.get("OperatingSystem"))
    print("Docker version:", client.version().get("Version"))

    print("\nStarting container with AppArmor profile...")

    container = client.containers.run(
        "flask-apparmor:latest",
        name="flask-apparmor-python-test",
        ports={"5000/tcp": 5000},
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True
    )

    print("Container started:", container.short_id)

    details = client.api.inspect_container(container.id)
    security_options = details["HostConfig"].get("SecurityOpt")

    print("Requested security options:", security_options)

    print(
        "\nNote: Docker accepting a security option does not by itself "
        "prove that AppArmor enforcement is active."
    )

except (DockerException, APIError) as error:
    print("\nDocker operation failed:")
    print(error)

finally:
    if container is not None:
        try:
            print("\nStopping and removing container...")
            container.stop(timeout=5)
            container.remove()
            print("Container cleaned up.")
        except DockerException as error:
            print("Cleanup error:", error)

    client.close()
