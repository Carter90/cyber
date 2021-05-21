#include <stdio.h>
#include <stdint.h>
int main(){
	char seed1[] = __TIME__; //seeds the random number generator with the time
	srand(seed1);
	int random_num=(rand() % 4);
	printf("Greetings\n");
	//scanf()
	double credits = 0.0;
	int health = 100;
	
	//char *outcomes[] ="Sweet a stack of cash", "Golblin Jumps out and scares you acedilty drop some cash", "You encournter an Obama and get some change", "Nessi  takes her toel of $3.50", "Trip over a rock ... ooof", 
	double outcome_credits[]={1,2,3,4};
	
	//Nort, East, South, West;
	char direction;
	while(health>0){
		printf("random number: %i\n", random_num);
		printf("Health: %i, Mula: %d\n", health, credits);
		printf("Type in the direction you want to go[N,E,S,W] or q to quit:");
		scanf("%c", &direction);
		printf("You inputed: '%c'", direction);
	} //end while alive

	if (health > 0){
		printf("Alright you made it out alive"); // Cheating?
	} //end if made it out alive
	else{
		printf("Bummer");
	} // end else dead
} //end main
