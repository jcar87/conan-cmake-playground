from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class pikachuRecipe(ConanFile):
    name = "squirtle"
    version = "1.0"
    package_type = "application"


    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"


    def layout(self):
        cmake_layout(self)
    
    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def requirements(self):
        self.requires("bulbasaur/1.0")
