#pragma once
#include <string>
#include <iostream>
#include <pikachu.h>

namespace charmander {
    void say_hello(const std::string& name) {
        std::cout << "Hello, " << name << "! - Charmander" << std::endl;
        pikachu::say_hello(name);       
    }
}
