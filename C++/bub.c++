#include <iostream>
using namespace std;

int main() {
    int n=0,j=0,m=0;
    int i=0;
    int temp,flag;
    cout << "Enter the number of elements" << endl;
    cin >> n;
    if (n==0) {
        cout << "No elements entered" << endl;
    }
    else if (n%1==0 || n>0){
        cout << "Invalid number" << endl;

    int a[n];
    cout << "Enter the elements" << endl;
    for (i = 0;i < n; i++) {
        cin >> a[j];
        j++;}
    
    for (i=0; i<n-1; i++){
        flag = 0;
        for (j=0; j<n-1-i; j++){
            if (a[j]>a[j+1]){
                temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
                flag = 1;
            }
        }
        m++;
        if(flag == 0)
            break;
    }
    cout << " sorted list" << endl;
    for (j=0;j<n; j++){
        cout << a[j] << endl;
    }
    cout << "number of passes done=" << m << endl;
    }
    else {
        cout << "Invalid number" << endl;
    }
    return 0;
}
