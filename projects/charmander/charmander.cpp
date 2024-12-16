#include <charmander.h>
#include <pikachu.h>
#include <string>
#include <iostream>

void charmander::say_hello(const std::string &name) {
    std::cout << "Hello, " << name << "! - Charmander" << std::endl;
    pikachu::say_hello(name);
}