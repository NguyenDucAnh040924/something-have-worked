package com.text.allAboutText;

import objectmanagement.TenDoiTuong;

import java.util.ArrayList;

public class Text {

    // return First Letter Uppercase
    public static String FirstLetterUppercase(String text){
        return text.substring(0,1).toUpperCase() + text.substring(1).toLowerCase();
    }


    private static void swap(int i, int j, ArrayList<TenDoiTuong> sapXepTopic){
        TenDoiTuong tmp = sapXepTopic.get(i);
        sapXepTopic.set(i,sapXepTopic.get(j));
        sapXepTopic.set(j,tmp);

    }

    public static void sapXepLetter(ArrayList<TenDoiTuong> BaoCao){
        int size = BaoCao.size();
        for(int i = 0; i< size; i++){
            for(int j = i+1; j<size; j++){
                if(BaoCao.get(i).getTopic().compareTo(BaoCao.get(j).getTopic()) > 0){
                    swap(i,j,BaoCao);
                }
            }
        }

    }


}
