#include <iostream>
#include <string>	
// #include "Lista_Simple.cpp"
#pragma once
using namespace std;

class NodoPila
{
private:
    /* data */
public:
    int id;
    int x;
    int y;
    NodoPila* next;
    NodoPila(int _id,int _x, int _y){
        id = _id;
        x =_x;
        y =_y;
        next = NULL;
    }
};