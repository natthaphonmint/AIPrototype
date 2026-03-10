# Install Miniconda (Linux) 

สรุปขั้นตอนเตรียมความพร้อมสำหรับรันโปรเจกต์บนเซิร์ฟเวอร์ Linux ตั้งแต่การลง Miniconda เพื่อจัดการ Environment ไปจนถึงเทคนิคการใช้คำสั่ง `screen` ที่ช่วยให้เรารันโค้ดทิ้งไว้ได้

🔗 **อ้างอิงจาก** [Miniconda Official Documentation](https://www.anaconda.com/docs/getting-started/miniconda/install#linux-2)

---

## 📥 1. การติดตั้งและกำหนดค่า Miniconda

### 1.1 การโหลดพร้อมติดตั้ง
ดำเนินการรันชุดคำสั่งต่อไปนี้ตามลำดับทีละบรรทัด เพื่อดาวน์โหลดและติดตั้ง Miniconda (สำหรับ Linux – x86_64)

```bash
mkdir -p ~/miniconda3
wget [https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh) -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```
### 1.2 การเปิดใช้งานระบบ (Activation)
หลังจากติดตั้งเสร็จสิ้น ให้ปิดแล้วเปิด Terminal ใหม่ หรือใช้คำสั่งด้านล่างเพื่อ refresh environment
```bash
source ~/miniconda3/bin/activate
```
### 1.3 การกำหนดค่าเริ่มต้น (Initialization)
ดำเนินการตั้งค่าเพื่อให้ Conda สามารถรองรับการทำงานร่วมกับ Shell ทุกรูปแบบ
```bash
conda init --all
```
  📌 ข้อสังเกต: หากการดำเนินการเสร็จสมบูรณ์ ระบบจะแสดงสถานะ (base) นำหน้าบรรทัดคำสั่ง เพื่อยืนยันความพร้อมในการใช้งาน
## 🧑‍💻 2. Python Command Line (VS Code Integration)
ระบบสภาพแวดล้อม Python ดังกล่าว ถูกจัดเตรียมไว้สำหรับการพัฒนาและประมวลผลชุดคำสั่งบนเซิร์ฟเวอร์ โดยมีรูปแบบการใช้งานดังนี้
* เปิดโปรแกรม VS Code ผ่าน Command Line
```bash
code
```
* เปิดหรือสร้างไฟล์ใน VS Code
```bash
code <file_name>
```
## 🖥️ 3. การใช้งาน Screen Session
`screen` มีวัตถุประสงค์เพื่อรองรับการประมวลผลของโปรแกรมบนเซิร์ฟเวอร์อย่างต่อเนื่อง
### 3.1 การจัดการ Screen เบื้องต้น
* สร้าง Screen ใหม่
```bash
screen -S <screen_name>
```
* กลับเข้า Screen ที่มีอยู่
```bash
screen -R
```
### 3.2 คำสั่งควบคุม Screen (Shortcuts)
* `Ctrl + A + D` → การออกจากเซสชันปัจจุบัน โดยระบบจะยังคงประมวลผลอยู่เบื้องหลัง
* `Ctrl + A + K + Y` → ออกจากและลบ session
* `Ctrl + A + [` → Freeze หน้าจอ (สามารถเลื่อนดูได้)
* `q + Enter` → ออกจากโหมด freeze
* `Ctrl + C` → หยุดโปรแกรมที่กำลังทำงาน
### 3.3 การแก้ไขปัญหากรณีชื่อเซสชันซ้ำซ้อนำ
หากมี Screen ชื่อซ้ำกัน ให้ทำตามขั้นตอนดังนี้
  ตรวจสอบ Screen ที่มีอยู่ทั้งหมด: สามารถกด `Tab` หลังคำสั่งเพื่อดูรายการ screen ที่มีทั้งหมดได้
```bash
screen -R <screen_name>
```
* 1. ระบุตัวตนเซสชันด้วยรหัส (ID)
```bash
screen -R id.<screen_name>
```
* 2. สั่งการลบเซสชัน
```bash
Ctrl + A + K + Y
```
