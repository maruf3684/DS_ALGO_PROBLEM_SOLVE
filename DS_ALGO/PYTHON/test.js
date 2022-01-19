var isPalindrome = function(x) {
    ans=0
    xx=x
    if (x<0){
    return false}
    
    while(x!=0){
        ans=(ans*10)+x%10
        x=parseInt( x/10)
        console.log("loop",x);
    }
    console.log(ans);
    console.log(xx);
    return ans==xx
};

isPalindrome(121)
