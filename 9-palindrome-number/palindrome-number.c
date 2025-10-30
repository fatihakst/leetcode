bool isPalindrome(int x) {

    if (x<0)
    return false;

    long long yen=0;
    int i=x;

    while(i>0){

    int dig= i%10;

     yen = (yen*10)+dig;
     i=i/10;
    }
    
    if (x==yen)
    return true;
    else
    return false;
 

}