import os
import platform
import shutil

def run(cmd):
    ret = os.system(cmd)
    if ret != 0:
        raise Exception(f"Failed CMD: {cmd}")

platform = platform.system().lower()

build_dir = os.path.join( os.path.dirname(os.path.realpath(__file__)), "build", platform)
install_dir = os.path.join( os.path.dirname(os.path.realpath(__file__)), "install", platform)
shutil.rmtree(build_dir, ignore_errors=True)
shutil.rmtree(install_dir, ignore_errors=True)

os.makedirs(build_dir, exist_ok=True)
os.makedirs(install_dir, exist_ok=True)

# Strict dependency order (pikachu <- charmander <- bulbasaur <- squirtle)
projects = ["pikachu", "charmander", "bulbasaur", "squirtle"]
project_base_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "projects")

dep_dirs = [f'-D{project.capitalize()}_ROOT="{install_dir}/{project}"' for project in projects]

# Build projects and use vanilla CMake-generated config and targets (no Conan involved)
for project in projects:
    defines = " ".join(dep_dirs)
    print(f"-----------------Project: {project}-----------------")
    run(f"cmake --fresh -S {project_base_dir}/{project} -B {build_dir}/{project} -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX={install_dir}/{project} {defines}")
    run(f"cmake --build {build_dir}/{project} --config Release")
    run(f"cmake --install {build_dir}/{project} --config Release")


# Build using Conan CMakeDeps
for project in projects:
    run(f"conan create projects/{project}")

# Build using Conan new experimental CMakeDeps
for project in projects:
    run(f"conan create projects/{project} -c tools.cmake.cmakedeps:new=will_break_next")