#include <iostream>
using namespace std;

int main()
{
    int a,b,c,m;
    cout << "\b请输入第1个数"<<endl;
    cin >> a ;
    cout << "\b请输入第2个数"<<endl;
    cin >>  b ;
    cout << "\b请输入第3个数"<<endl;
    cin >> c;
    m = a;
    if (b > m) m = b;/*m始终保存较大的值*/
    if (c > m) m = c;
    cout << "\b输入的三个数最大值为：" << m << endl;
}