import ui.UserInterface;
import objectmanagement.TenDoiTuong;
import objectmanagement.ObjectInClass;
import manage.SettingUpTheManageFunction;

import java.util.ArrayList;

public class Main {
    private static ObjectInClass oj = new ObjectInClass();
    private static TenDoiTuong khoiTao = new TenDoiTuong(); // Đổi tên biến KhoiTao
    private static ArrayList<TenDoiTuong> baoCaoList = new ArrayList<>(); // Đổi tên biến BaoCao
    private static UserInterface ui = new UserInterface();
    private static SettingUpTheManageFunction sf = new SettingUpTheManageFunction();

    private static void hienThi(){
        // Du Lieu Mau
        // Dung De test cac chuc nang khac
        baoCaoList.add(new TenDoiTuong("Google", "TranVanA", "5678"));
        baoCaoList.add(new TenDoiTuong("LinkedIn", "LeThiB", "abcd"));
        baoCaoList.add(new TenDoiTuong("Reddit", "PhamVanC", "xyz1"));
        baoCaoList.add(new TenDoiTuong("Instagram", "NguyenVanD", "7890"));
        baoCaoList.add(new TenDoiTuong("Snapchat", "DoThiE", "5432"));
        baoCaoList.add(new TenDoiTuong("Pinterest", "VoVanF", "lmno"));
        baoCaoList.add(new TenDoiTuong("Facebook", "HoangThiG", "1011"));
        baoCaoList.add(new TenDoiTuong("Twitter", "NguyenHoangH", "1213"));

        // Kiem thu thanh cong
        ui.displayMenu(oj);
        manage.UserChoice.userChoice(1, oj.getDisplayMenuSize(),baoCaoList);

    }

    public static void main(String[] args) {
        hienThi();

    }
}
