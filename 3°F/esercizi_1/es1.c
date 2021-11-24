//Scrivere un programma che calcoli e restituisca in output la somma dei primi n numeri naturali (con n inserito da tastiera).

# include <stdio.h>

void main()
{
	int n;
	int i = 1;
	int somma = 0;
	printf("Quanti numeri devi sommare? \n\n\n");
	scanf("%d", &n);
	for (i; i <=n; i++)
	{
		somma = somma + i;
	}
	printf("Il risultato %d", somma);
}
