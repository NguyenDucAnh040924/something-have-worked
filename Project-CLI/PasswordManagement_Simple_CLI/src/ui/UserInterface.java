package ui;

import objectmanagement.ObjectInClass;

public class UserInterface {

    public static void logo(){
        System.out.println("\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
        System.out.println("\t\t\t\t|\t\t\t\t\t\t\t\t\t\t\t|");
        System.out.println("\t\t\t\t|\t\t\t\tQUAN LY MAT KHAU\t\t\t|");
        System.out.println("\t\t\t\t|\t\t\t\t\t\t\t\t\t\t\t|");
        System.out.println("\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
        System.out.println();
    }

    public static void displayMenu(ObjectInClass oj){
        String [] display = {"Them","Xoa","Edit password","List topic","display All But Follow Topic","Exit."};
        int displayLength = display.length;
        oj.setDisplayMenuSize(displayLength);
        int i = 0;
        while(i < displayLength){
            System.out.println(i+1+". "+display[i]);
            i++;
        }
        System.out.println("------------------------------");
    }


}
