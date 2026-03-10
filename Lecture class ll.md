# Cloud Virtual Machines 

## 1. Cloud Services 3 ประเภทหลัก
กติแล้วบริการคลาวด์จะแบ่งออกเป็น 3 หมวดใหญ่ๆ ตามระดับการจัดการ:
* **Infrastructure as a Service (IaaS)**
* **Platform as a Service (PaaS)**
* **Software as a Service (SaaS)**

**🔗 พิกัดสำหรับเริ่มต้นใช้งาน:**
* **สมัคร:** Microsoft Azure for Students (https://azure.microsoft.com/en-us/free/students)
* **เข้าสู่ระบบ:** Azure Portal (https://portal.azure.com)

---

## 2. พื้นฐาน Virtual Machine (VM)
**Virtual Machine (VM)** คือ Server เสมือนที่ทำงานอยู่บนคลาวด์ ซึ่งสามารถใช้งานได้เหมือนเครื่อง Linux จริงๆ

* **💡ขั้นตอนการสร้าง VM บนเว็บไซต์:** `Azure Portal` → `Education` → `Virtual Machines` → `Create a virtual machine`

---

## 3. การเข้าถึงและตรวจสอบ Server

### 🔑การเชื่อมต่อด้วย SSH (Secure Shell)
ใช้สำหรับเชื่อมต่อจากเครื่องของเราไปยัง VM (เปรียบเสมือนเปลือกหอยที่ค่อยๆ หุ้ม ค่อยๆ เข้า)
```bash
ssh username@IPaddress
```
* username: ชื่อผู้ใช้ที่ตั้งไว้ตอนสร้าง VM
* IPaddress: Public IP ของ VM
## 4. จัดการผู้ใช้งาน (Users & Groups)
เพิ่ม User ใหม่: สำหรับให้เพื่อนหรือผู้ร่วมงานเข้าใช้งาน VM เดียวกัน
```bash
sudo adduser <ชื่อเพื่อน>
```
เพิ่มสิทธิ์ผู้ดูแลระบบ (SuperUser/sudo): ให้ User อื่นสามารถรันคำสั่งระดับผู้ดูแลระบบได้
```bash
sudo adduser <ชื่อเพื่อน>
```
จัดการ Group: ย้าย User ไปอยู่ Group เดียวกัน (เช่น ชื่อเพื่อนเป็น Group, ชื่อเราเป็น Folder)
```bash
sudo usermod <ชื่อเพื่อน> <ชื่อเรา>
```
ตรวจสอบ Group: ดูว่ามีใครอยู่ใน Server หรือ User อยู่ใน Group ใดบ้าง
```bash
sudo groups <ชื่อเรา>
```
## 5. ย้ายไฟล์ข้ามเครื่องด้วย SCP (Secure Copy)
ใช้สำหรับการส่งและดึงไฟล์ระหว่าง เครื่องของเรา ↔ Cloud (VM)
  ⚠️ ข้อสำคัญ: ต้องรันคำสั่งนี้บนเครื่องของเราเท่านั้น ห้ามรันภายใน VM
รูปแบบคำสั่งพื้นฐาน
```bash
scp <source_path> <destination_path>
```
* ส่งไฟล์จาก เครื่องเรา → Cloud
```bash
scp <path_file>/<filename> username@IP:~<folder>/.
```
* ดึงไฟล์จาก Cloud → เครื่องเรา
```bash
scp username@IP:<path_file>/<filename> <destination_path>/.
```
* คัดลอกทั้งโฟลเดอร์
```bash
scp -r <folder_source> username@IP:~<folder>/.
```
## 📝 6. สรุป Workflow ตอนใช้งานจริง
กรณีที่ 1 การส่งไฟล์จากเครื่องไป VM
1. ใช้คำสั่ง `scp` บนเครื่องของเรา
2. เข้าสู่ VM ด้วยคำสั่ง `ssh`
3. ตรวจสอบความเรียบร้อยของไฟล์บน VM ด้วยคำสั่ง `ls`
กรณีที่ 2 การดึงไฟล์จาก VM มาที่เครื่อง
1. ออกจาก VM ก่อนด้วยคำสั่ง `exit`
2. ใช้คำสั่ง `scp` เพื่อดึงไฟล์บนเครื่องของเรา
## 7. การจัดการ Python Environment (Miniconda)
* Miniconda ใช้สำหรับจัดการ Python environment เพื่อช่วยแยก Package และเวอร์ชันของ Python ได้อย่างเป็นระบบ
* หากต้องการให้ `(base)` แสดงขึ้นมาโดยอัตโนมัติทุกครั้ง ให้ทำการรันคำสั่งตั้งค่า environment ตามลำดับที่กำหนด
## 8. การ Logout
* ออกจากฟังก์ชันหรือโปรแกรม (เช่น รัน Python ค้างไว้): `exit()`
* ออกจาก Virtual Machine (Log out): `exit`
