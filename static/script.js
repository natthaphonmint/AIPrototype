/* static/js/script.js */
function showLoading() {
    const btnText = document.getElementById('btnText');
    const loader = document.getElementById('loader');
    const submitBtn = document.getElementById('submitBtn');

    // ซ่อนข้อความ แสดงตัวหมุน และปิดปุ่มกด
    btnText.style.display = 'none';
    loader.style.display = 'block';
    submitBtn.style.opacity = '0.8';
    submitBtn.style.cursor = 'wait';
}