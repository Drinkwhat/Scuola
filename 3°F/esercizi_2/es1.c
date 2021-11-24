// Generare la serie dei quadrati dei primi n numeri naturali (n letto da input).

#include <math.h>
#include <stdio.h>
void main(){
	int n;
	int i = 1;
	int risultato;
	printf("Inserisci numeri: ");
	scanf("%d", &n );
	
	for (i; i <= n; i++){
		risultato = pow(i, 2);
		printf("%d ", risultato);
		
	}
}

