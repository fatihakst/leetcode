int value(char r) {
    switch (r) {
        case 'I': return 1;
        case 'V': return 5;
        case 'X': return 10;
        case 'L': return 50;
        case 'C': return 100;
        case 'D': return 500;
        case 'M': return 1000;
        default: return 0;
    }
}


int romanToInt(char* s) {
    char *p = s;

while (*p != '\0') {
  
    p++;
}
    p--;	
	
    int total = 0;
    
  

    while (p>=s) {
      
	   int s1 = value(*p);
int s2 = 0;
int s3 = 0;

if (p - 1 >= s) s2 = value(*(p - 1));
if (p - 2 >= s) s3 = value(*(p - 2));
       
	    if (p>s && s1 > s2) {
            
			total += (s1 - s2);
           
		   
			
			int a = 2;
			
			while(p-a>=s ){
			
			int val= value(*(p - a));
			
			if(val<=s2 && val!=0){
			
			
			total -= val;
			
			s2 = val;
			a++;
			s3= value(*(p-a));
            }
            else{
            	break;
			}
            }
            
			p-=a;
            
        }
		
		 else {
            total += s1;
            p--;
        }
    }

    return total;
}