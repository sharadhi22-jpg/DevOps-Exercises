import docker
from docker.errors import DockerException, APIError

client = docker.from_env()
container = None

try:
    print("Starting container for security tests...")

    container = client.containers.run(
        "flask-apparmor:latest",
        name="flask-apparmor-security-test",
        ports={"5000/tcp": 5000},
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True
    )

    print("Container started:", container.short_id)

    print("\nTest 1: Attempt to read /etc/passwd")

    result = container.exec_run(
        ["cat", "/etc/passwd"]
    )

    print("Exit code:", result.exit_code)
    print("Output:")
    print(result.output.decode(errors="replace"))

    print("\nTest 2: Attempt to execute /bin/bash")

    result = container.exec_run(
        ["/bin/bash", "-c", "echo shell-execution-test"]
    )

    print("Exit code:", result.exit_code)
    print("Output:")
    print(result.output.decode(errors="replace"))

    print(
        "\nReminder: These results alone do not prove AppArmor "
        "caused an operation to succeed or fail."
    )

except (DockerException, APIError) as error:
    print("\nSecurity test could not run:")
    print(error)

finally:
    if container is not None:
        try:
            container.stop(timeout=5)
            container.remove()
            print("\nContainer stopped and removed.")
        except DockerException as error:
            print("Cleanup error:", error)

    client.close()
