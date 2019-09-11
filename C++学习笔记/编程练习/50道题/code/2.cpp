#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    double a,b,c,d,x1,x2;
    cout<< "\b请输入方程二次项的系数：" << endl;
    cin >> a ;
    cout << "\b请输入方程一次项的系数："<< endl;
    cin >> b ;
    cout << "\b请输入方程零次项的系数：" << endl;
    cin >> c;
    /*判断输入的系数是否合理*/
    if(a==0){
        if(b==0){
            cout << "error\n";
        }else{
            cout << "x="<< -c/b << endl;
        }
    }else{
        d = b * b - 4 * a* c;
        if(fabs(d) <= 1e-6){
            cout << "x1 = x2 = " << -b/(2*a) << endl;
        }else if(d > 1e-6){
                x1 = (-b+sqrt(d))/(2*a);
                x2 = (-b-sqrt(d))/(2*a);
                cout << "x1 =" << x1 << ", x2 = " << x2 << endl;
        }else{
               cout << "\b方程无实根\n";
           }
    }
}