#include <pikachu.h>
#include <string>
#include <iostream>

void pikachu::say_hello(const std::string &name) {
    std::cout << "Hello, " << name << "! - Pikachu" << std::endl;
}