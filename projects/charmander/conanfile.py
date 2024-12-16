from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.files import rmdir
import os

class pikachuRecipe(ConanFile):
    name = "charmander"
    version = "1.0"
    package_type = "shared-library"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "charmander.cpp", "include/*", "CharmanderConfig.cmake.in"

    def layout(self):
        cmake_layout(self)
    
    def requirements(self):
        self.requires("pikachu/1.0")

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
        rmdir(self, os.path.join(self.package_folder, "lib", "cmake"))

    def package_info(self):
        self.cpp_info.libs = ["charmander"]
        self.cpp_info.set_property("cmake_file_name", "Charmander")
        self.cpp_info.set_property("cmake_target_name", "Charmander::charmander")
