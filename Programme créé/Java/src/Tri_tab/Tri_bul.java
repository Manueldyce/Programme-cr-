package Tri_tab;
import java.util.Scanner;
public class Tri_bul {
	static void tri_bulle(int[] tab) {
		int taille = tab.length;
		int tmp=0;
		for(int i=0; i <taille; i++) {
			for(int j=1; j<(taille-i);j++) {
				
				if (tab[j-1]>tab[j]) {
					tmp=tab[j-1];
					tab[j-1]= tab[j];
						tab[j]=tmp;						
					}
				}
			}
		}
	static void displaytab(int[] tab) {
		for(int i=0; i<tab.length;i++) {
			System.out.println(tab[i]+"");
			}
	}
	public static void main(String[] args) {
		//declaration
		Scanner var = new Scanner(System.in);
		System.out.println("Combien de nbr voulez-vous trier ? ");
		int Cnbr= var.nextInt();
		int arr[]= new int[Cnbr];
		
		
		System.out.println("Entrer-les: ");
		for(int h=0;h<Cnbr;h++) {
			int nbr= var.nextInt();
			arr[h]= nbr;
		}
		
		//Affichage 
		System.out.println("Tableau avant le tri a bulle");
		displaytab(arr);
		
		//Tri du tableau
		tri_bulle(arr);
		System.out.println("Apres le tri a bulle");
		displaytab(arr);
	}

}
