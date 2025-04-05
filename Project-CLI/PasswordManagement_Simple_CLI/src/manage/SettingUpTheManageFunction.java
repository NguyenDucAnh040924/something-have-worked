package manage;

import com.text.allAboutText.Text;
import validator.Validate;
import objectmanagement.TenDoiTuong;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class SettingUpTheManageFunction {
    private static Validate validate = new Validate();
    private static TenDoiTuong tenDoiTuongExist = new TenDoiTuong();

    protected static void input(ArrayList<TenDoiTuong> iArrayList, TenDoiTuong tenDoiTuong) { // Done
        String topicUser = validator.Validate.Topic();
        String TenTaiKhoan = validator.Validate.TenTaiKhoan();
        tenDoiTuong.setTopic(topicUser);
        tenDoiTuong.setTenTaiKhoan(TenTaiKhoan);
        AddTaiKhoan(iArrayList, tenDoiTuong);
    }

    protected static int choiceIntegerLimit(String msg, int min, int max) {
        Scanner in = new Scanner(System.in);
        while(true) {
            try {
                System.out.println(msg); // Message
                String choiceNumberString = in.nextLine();
                int choiceNumber = Integer.parseInt(choiceNumberString);
                if (choiceNumber < min || choiceNumber > max) {
                    throw new NumberFormatException();
                }
                return choiceNumber;
            } catch (NumberFormatException e) {
                System.out.println("Please enter your choice number from " + min + " to " + max);
                System.out.println("Enter again: ");
            }

        }
    }

    // Done
    private static void AddTaiKhoan(ArrayList<TenDoiTuong> tArrayList, TenDoiTuong tNewDoiTuong) {

        if (!Validate.checkExist(tArrayList, tNewDoiTuong.getTopic(), tNewDoiTuong.getTenTaiKhoan())) {
            System.out.println("The Account Existed!");
            return;
        } else {
            String matKhauMoi = Validate.MatKhau();
            tNewDoiTuong.setMatKhau(matKhauMoi);
            tArrayList.add(new TenDoiTuong(tNewDoiTuong.getTopic(), tNewDoiTuong.getTenTaiKhoan(), tNewDoiTuong.getMatKhau()));
            System.out.println("Add Successfully");
        }

    }


    protected static void XoaTaiKhoan(ArrayList<TenDoiTuong> xArrayList) {
        /* ---- Pseudo Code ------
         *  input topic, ten tai khoan
         *   kiem tra xem tai khoan co ton tai khong
         *   if false -> print None Exist
         *   else true -> thuc hien lenh duoi
         *
         *   kiem tra topic co ton tai ko if true -> kiem tra ten doi tuong co ton tai khong if true -> Chay Lenh nay
         *  else return;
         * Lenh nay  (
         * if true -> check Yes or No
         *       if No -> return
         *       else -> remove account
         *   else false -> neu topic va ten tai khoan EMPTY or Sai -> nhap lai
         *   if enter 0 -> exit to main menu
         * )
         * */
        String topicNeedDeleted = validate.input("Enter topic need deleted: ");
        String nameNeedDeleted = validate.input("Enter account name need deleted: ");

        TenDoiTuong deleteObject =  new TenDoiTuong(topicNeedDeleted,nameNeedDeleted);
        validate.checkExistObject(xArrayList,deleteObject);
    }

    protected static void SuaTaiKhoan(ArrayList<TenDoiTuong> sArrayList) {
        System.out.println("Edit account mode: ");
        String topicFound = validate.input("Enter topic");
        String tenTaiKhoan = validate.input("Enter ten tai khoan ban muon tim: ");

        TenDoiTuong doiTuongCanSua = new TenDoiTuong(topicFound, tenTaiKhoan);


        // Xem lai luong chay. Tai sao khong set newPassword
        if(!validate.checkExist(sArrayList, doiTuongCanSua.getTopic(), doiTuongCanSua.getTenTaiKhoan())){
            System.out.println("Duoc phep doi mat khau!");
            String newPassword = validate.MatKhau();
            for(TenDoiTuong x : sArrayList){
                if(doiTuongCanSua.getTopic().equalsIgnoreCase(x.getTopic())
                        && doiTuongCanSua.getTenTaiKhoan().equalsIgnoreCase(x.getTenTaiKhoan())){
                    x.setMatKhau(newPassword);
                    System.out.println("Thay doi mat khau Thanh Cong!");
                }
            }
        }


    }

    // Done
    protected static void LietKeDanhSach(ArrayList<TenDoiTuong> LIST_ArrayList) {
        System.out.println("Enter topic: ");
        Scanner sc = new Scanner(System.in);
        String topic = sc.nextLine();
        DisplayList(LIST_ArrayList, topic,sc);

    }

    private static void DisplayList(ArrayList<TenDoiTuong> dArrayList, String Topic, Scanner sc) {
        // 1. Ton tai trong list
        if (validate.checkTopicExist(dArrayList, Topic)) {
            System.out.println("TK Ton Tai");
            displayFollowTopic(dArrayList, Topic);
        }
        // 2. Topic khong nhap gi
        else if (Topic.isEmpty()) {
            Text txtSort = new Text();
            boolean YN = validate.checkInputYesNo();
            if (YN) {
                System.out.println("Print All TK");
                // Neu khong nhap (Topic is EMPTY)
                txtSort.sapXepLetter(dArrayList);
                for (TenDoiTuong listAll : dArrayList) {
                    System.out.println(listAll.toStringFull());
                }

            } else {
                System.out.println("Print Theo Chu de cua TK");
                System.out.println("Enter topic wanna find: ");
                String TopicFounded = sc.nextLine().trim();
                displayFollowTopic(dArrayList, TopicFounded);

            }

        }
        // 3. Khong ton tai trong list or nhap sai
        else {
            System.out.println("Meo ton tai");
            return;
        }


    }

    protected static void displayFollowTopic(ArrayList<TenDoiTuong> dArrayList, String Topic) {
        for (TenDoiTuong listTopic : dArrayList) {
            if (Topic.equalsIgnoreCase(listTopic.getTopic())) {
                System.out.println(listTopic.toStringFull());
            }
        }
    }

    private static String toStringTopic(String txt) {
        Text txtF = new Text();
        return txtF.FirstLetterUppercase(txt) + ": \n";
    }


    protected static void displayAllButFollowTopic(ArrayList<TenDoiTuong> daArrayList){
        // Group accounts by topic
        Map<String, ArrayList<TenDoiTuong>> groupedTopics = new HashMap<>();
        for (TenDoiTuong obj : daArrayList) {
            groupedTopics.computeIfAbsent(obj.getTopic(), k -> new ArrayList<>()).add(obj);
        }

        // Print each topic with its accounts and passwords
        for (Map.Entry<String, ArrayList<TenDoiTuong>> entry : groupedTopics.entrySet()) {
            System.out.println(entry.getKey() + ":"); // Topic name
            System.out.println("Ten tai khoan, Mat Khau: ");
            for (TenDoiTuong account : entry.getValue()) {
                System.out.println(account.getTenTaiKhoan() + ", " + account.getMatKhau());
            }
            System.out.println();
        }
    }


}
