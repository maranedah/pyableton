import semver
import toml


def get_current_version():
    with open("pyproject.toml", "r") as toml_file:
        pyproject_data = toml.load(toml_file)
        version = pyproject_data["project"]["version"]        
    return version

def save_new_version(new_version):
    with open("pyproject.toml", "r") as toml_file:
        pyproject_data = toml.load(toml_file)
        pyproject_data["project"]["version"] = new_version
    toml.dump(pyproject_data, open("pyproject.toml", "w"))


def bump_version():
    current_version = get_current_version()
    new_version = semver.bump_patch(current_version)
    save_new_version(new_version)

    print(f"Version bumped from {current_version} to {new_version}")
    return new_version

if __name__ == "__main__":
    new_version = bump_version()
