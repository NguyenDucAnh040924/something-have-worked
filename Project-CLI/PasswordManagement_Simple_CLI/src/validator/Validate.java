package validator;

import objectmanagement.TenDoiTuong;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.regex.Pattern;

public class Validate {
    private static Scanner in = new Scanner(System.in);

    // Check topic input string _ Kiem tra chu de ma nguoi dung nhap
    public static String Topic() { // Done
        String topicInputter;
        System.out.print("Enter your Topic: ");
        while (true) {

            topicInputter = in.nextLine().trim();

            boolean mPattern = Pattern.matches("[a-zA-Z ]+", topicInputter);
            // Kiem tra neu mPattern true thi break, else nguoc lai
            if (mPattern) {
                break;
            } else {

            }
        }
        return topicInputter;
    }

    public static String input(String msg) {
        while (true) {
            try {
                System.out.println(msg);
                String inputString = in.nextLine().trim();
                if (inputString.isEmpty()) {
                    throw new Exception();
                }

                return inputString;
            } catch (Exception e) {
                System.out.println("Syntax Error!");
                System.out.println("Enter again: ");
            }

        }
    }


    public static String TenTaiKhoan() { // Done
        String TenTaiKhoanInputter;
        System.out.print("Enter your Account name: ");
        while (true) {

            TenTaiKhoanInputter = in.nextLine().trim();

            // Kiem tra ten co chua ky tu dac biet khong
            boolean tPattern = Pattern.matches("[\\w]+", TenTaiKhoanInputter); // Bo ky tu dac biet va dau cach
            // Kiem tra neu tPattern true thi break, else nguoc lai
            if (tPattern) {
                break;
            } else {
                System.out.println("Enter again: ");
            }
        }
        return TenTaiKhoanInputter;
    }


    public static String MatKhau() { // Done
        String MatKhauInputting;
        System.out.print("Enter your new Password: ");
        while (true) {

            MatKhauInputting = in.nextLine().trim();

            // Kiem tra mat khau co chua ky tu dac biet khong
            boolean tPattern = Pattern.matches("[\\w]+", MatKhauInputting); // Bo ky tu dac biet va dau cach
            // Kiem tra neu tPattern true thi break, else nguoc lai
            if (tPattern) {
                break;
            } else {
                System.out.println("Enter again: ");
            }
        }
        return MatKhauInputting;
    }

    // Kiem tra luc xoa, sua, thay doi mat khau (moi can dung) _ Khong co tham so
    public static boolean checkInputYesNo() {
        System.out.println("Please enter yes or no: >_<");
        while (true) {
            System.out.println("Enter your choice(Y/N): ");
            String YN = in.nextLine().trim();
            if (YN.isEmpty()) {
                System.err.println("Not Empty!");
                System.out.println("Enter again");
            } else if (YN.equalsIgnoreCase("y") || YN.equalsIgnoreCase("yes")) {
                return true;
            } else if (YN.equalsIgnoreCase("n") || YN.equalsIgnoreCase("no")) {
                return false;
            } else {
                System.err.println("Please input again T_T");
                System.out.println("Enter again");
            }
        }
    }

    // // Kiem tra luc xoa, sua, thay doi mat khau (moi can dung) _ Co tham so
    private static boolean checkInputYesNo(String YN) {
        //System.out.println("Please enter yes or no: >_<");
        while (true) {
            //System.out.println("Enter your choice(Y/N): ");
            //String YN = in.nextLine().trim();
            if (YN.isEmpty()) {
                System.err.println("Not Empty!");
                System.out.println("Enter again");
            } else if (YN.equalsIgnoreCase("y") || YN.equalsIgnoreCase("yes")) {
                return true;
            } else if (YN.equalsIgnoreCase("n") || YN.equalsIgnoreCase("no")) {
                return false;
            } else {
                System.err.println("Please input again T_T");
                System.out.println("Enter again");
            }
        }
    }

    // Kiem tra xem tai khoan trong cung 1 topic co ton tai hay chua(Phan biet ro rang ) - Kiem tra de add Account
    public static boolean checkExist(ArrayList<TenDoiTuong> tArrayList, String newTopic, String newTenTaiKhoan) { // Done
        //int size = tArrayList.size();
        for (TenDoiTuong o : tArrayList) {
            if (newTopic.equalsIgnoreCase(o.getTopic()) && newTenTaiKhoan.equals(o.getTenTaiKhoan())) {
                return false;
            }
        }
        return true;
    }

    // Kiem tra doi tuong co ton tai de xoa
    public static boolean checkExistObject(ArrayList<TenDoiTuong> oArrayList, TenDoiTuong objectName) {

        for (TenDoiTuong objData : oArrayList) {
            if (objectName.getTopic().equalsIgnoreCase(objData.getTopic())) { // Existed
                if (objectName.getTenTaiKhoan().equals(objData.getTenTaiKhoan())) { //Existed
                    // Duoc phep xoa
                    System.out.println("Duoc Phep Xoa Tai Khoan");
                    System.out.println("Do you want to delete Account: \nPlease enter 'Y' or 'N':");
                    String YN = in.nextLine().trim();
                    if (checkInputYesNo(YN)) {
                        oArrayList.remove(objData);
                        System.out.println("Xoa thanh Cong!");
                        return true;
                    }else{
                        System.out.println("Ban da tu choi xoa tai khoan!");
                        return false;
                    }

                } else {
                    System.out.println("Ten Tai Khoan Khong ton tai");
                    return false;
                }
            }
        }
        System.out.println("Ten topic khong ton tai!");
        return false;
    }


    // List All or List theo Topic
    // Kiem tra liet ke theo Topic or Full
    public static boolean checkTopicExist(ArrayList<TenDoiTuong> BaoCaoList, String topicExisted) {
        for (TenDoiTuong o : BaoCaoList) {
            if (topicExisted.equalsIgnoreCase(o.getTopic())) {
                return true;
            }
        }
        return false;
    }
}


