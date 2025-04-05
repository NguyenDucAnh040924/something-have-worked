package manage;

// Library
import java.util.ArrayList;

// package
import objectmanagement.TenDoiTuong;
import objectmanagement.ObjectInClass;
import manage.SettingUpTheManageFunction;
import ui.UserInterface;



public class UserChoice {
    //private static ArrayList<TenDoiTuong> BaoCao = new ArrayList<>();
    private static TenDoiTuong newUser = new TenDoiTuong();
    private static ObjectInClass oj = new ObjectInClass();
    private static UserInterface ui = new UserInterface();

    public static void userChoice(int min, int max,ArrayList<TenDoiTuong> BaoCao) {
        // Setting MAX as a final constant
        final int MAX = max;

        do {

            SettingUpTheManageFunction sf = new SettingUpTheManageFunction();
            int choiceNumber = sf.choiceIntegerLimit("Enter choice number: ",min, max);
            oj.setChoiceNumber(choiceNumber);
            oj.setChoiceMaxNumber(max);

            switch (choiceNumber) {
                case 1:
                    // Done
                    sf.input(BaoCao,newUser);
                    break;
                case 2:
                    // Done
                    sf.XoaTaiKhoan(BaoCao);
                    break;
                case 3:
                    // Done
                    sf.SuaTaiKhoan(BaoCao);
                    break;
                case 4:
                    // Done
                    sf.LietKeDanhSach(BaoCao);
                    break;

                case 5:
                    //Done
                    sf.displayAllButFollowTopic(BaoCao);
                default:
                    if(choiceNumber == MAX){
                        // Handle the MAX case here
                        System.out.println("Exit Program Successfully! =.=");
                        System.exit(0);
                    }

            }
        } while (oj.getChoiceNumber() != max);
    }


}
