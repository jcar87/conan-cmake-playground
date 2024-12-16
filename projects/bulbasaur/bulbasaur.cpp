#include <bulbasaur.h>
#include <charmander.h>
#include <string>
#include <iostream>

void bulbasaur::say_hello(const std::string &name) {
    std::cout << "Hello, " << name << "! - Bulbasaur" << std::endl;
    charmander::say_hello(name);
}