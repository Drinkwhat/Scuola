#include <stdio.h>
#include <stdbool.h>
void main(){
	int n;
	printf("Inserisci il numero: ");
	scanf("%d", &n);
	int i = 2;
	bool b = true;
	for (i;i < n; i++){
		if (n % i == 0){
			b = false;		
			break;
		}		
	}
	if (b == true){
	
		printf("� primo");
	}
	else{
		printf("non � primo");
	}
}

