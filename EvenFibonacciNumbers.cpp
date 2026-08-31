#include <iostream>

int main() {
    int F1 = 1;
    int F2 = 2;
    int ans = 0;

    while (F2 <= 4000000)
    {
        if (!(F2 & 1))
        {
            ans += F2;
        }
        
        int temp = F2;
        F2 = F1 + F2;
        F1 = temp;
    }

    std::cout << ans << "\n";
}