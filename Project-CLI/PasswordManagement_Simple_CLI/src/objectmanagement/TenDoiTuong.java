package objectmanagement;

import com.text.allAboutText.Text;

public class TenDoiTuong {
    private String Topic; // Chu de cua moi loai mat khau
    private String TenTaiKhoan; // Ten tai khoan
    private String MatKhau;

    // Constructor

    public TenDoiTuong(String topic, String tenTaiKhoan, String matKhau) {
        Topic = topic;
        TenTaiKhoan = tenTaiKhoan;
        MatKhau = matKhau;
    }

    public TenDoiTuong() {
    }

    public TenDoiTuong(String matKhau) {
        MatKhau = matKhau;
    }

    public TenDoiTuong(String topic, String tenTaiKhoan) {
        Topic = topic;
        TenTaiKhoan = tenTaiKhoan;
    }

    // Getter AND Setter

    public String getTopic() {
        return Topic;
    }

    public void setTopic(String topic) {
        Topic = topic;
    }

    public String getTenTaiKhoan() {
        return TenTaiKhoan;
    }

    public void setTenTaiKhoan(String tenTaiKhoan) {
        TenTaiKhoan = tenTaiKhoan;
    }

    public String getMatKhau() {
        return MatKhau;
    }

    public void setMatKhau(String matKhau) {
        MatKhau = matKhau;
    }

    @Override
    public String toString() {
        return "TenDoiTuong{" +
                "Topic='" + Topic + '\'' +
                ", TenTaiKhoan='" + TenTaiKhoan + '\'' +
                ", MatKhau='" + MatKhau + '\'' +
                '}';
    }

    public String toStringNotFull() {
        return "TenDoiTuong{" +
                "TenTaiKhoan='" + TenTaiKhoan + '\'' +
                ", MatKhau='" + MatKhau + '\'' +
                '}';
    }

    public String toStringFull() {
        Text txtF = new Text();
        return "TenDoiTuong{" +
                "Topic='" + txtF.FirstLetterUppercase(Topic) + '\'' +
                ", TenTaiKhoan='" + TenTaiKhoan + '\'' +
                ", MatKhau='" + MatKhau + '\'' +
                '}';
    }



}
