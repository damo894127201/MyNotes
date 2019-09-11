#include <iostream>
using namespace std;

int main(){
    int a;
    cout << "\b请输入你的成绩：\n";
    cin >> a ;
    if (a >= 90){
        cout << "\b你的等级是：A";
    }else if (a >= 80){
        cout << "\b你的等级是：B";
    }else if (a >= 70){
        cout << "\b你的等级是：C";
    }else if (a >= 60){
        cout << "\b你的等级是：D";
    }else{
        cout << "\b你的等级是：E";
    }
}