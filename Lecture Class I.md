# 🐧 Class I — Ubuntu Command Line

> พื้นฐานการใช้งาน Terminal บน Linux (Ubuntu)  
> ทักษะเหล่านี้จำเป็นมากสำหรับการทำงานบน Server และ Cloud

---

## 📋 สารบัญ

1. [Check Current Directory](#-1-check-current-directory)
2. [List Files & Folders](#-2-list-files--folders)
3. [Change Directory](#-3-change-directory)
4. [File & Folder Management](#️-4-file--folder-management)
5. [Move File](#-5-move-file)
6. [Copy File & Folder](#-6-copy-file--folder)
7. [Manual Page](#-7-manual-page)
8. [Check System Resources](#️-8-check-system-resources)
9. [สรุปคำสั่งที่ใช้บ่อย](#-สรุปคำสั่งที่ใช้บ่อย)

---

## 🔍 1. Check Current Directory

คำสั่ง `pwd` (**P**rint **W**orking **D**irectory) ใช้แสดงตำแหน่ง path ของโฟลเดอร์ที่กำลังทำงานอยู่ในปัจจุบัน

```bash
pwd
```

**ตัวอย่าง output:**
```
/home/kanisorn/projects
```

---

## 📂 2. List Files & Folders

คำสั่ง `ls` ใช้แสดงรายการไฟล์และโฟลเดอร์ที่อยู่ใน directory ปัจจุบัน

```bash
ls               # แสดงรายการแบบพื้นฐาน
ls -l            # แสดงแบบละเอียด (Long format)
ls -lh           # แสดงขนาดไฟล์แบบอ่านง่าย (Human readable)
ls -ltr          # เรียงตามเวลาแก้ไข จากเก่าไปใหม่
ls -a            # แสดงไฟล์ซ่อน (hidden files ที่ขึ้นต้นด้วย .)
```

**ตัวอย่าง output ของ `ls -lh`:**

```
Permission  Users  Size   Date         File name
drwxr-xr-x  2     root   Jan 15 10:00  myfolder/
-rw-r--r--  1     user   Jan 14 09:30  script.py
-rw-r--r--  1     user   Jan 13 08:00  README.md
```

### 🔐 ความหมายของ Permission

```
drwxr-xr-x
│└──┴──┴──→ permission ของ others (คนอื่น)
│   └──┴──→ permission ของ group
│      └──→ permission ของ owner (เจ้าของ)
└─────────→ d = directory, - = file
```

| สัญลักษณ์ | ความหมาย |
|:---:|---|
| `r` | **read** — อ่านข้อมูลได้ |
| `w` | **write** — เขียนหรือแก้ไขได้ |
| `x` | **execute** — รันไฟล์ได้ |
| `-` | ไม่มีสิทธิ์ |
| `d` | directory (โฟลเดอร์) |

### คำอธิบาย Option ของ `ls -ltr`

| Option | ความหมาย |
|:---:|---|
| `-l` | Long format — แสดงรายละเอียดทั้งหมด |
| `-t` | เรียงตามเวลาที่แก้ไข |
| `-r` | Reverse — กลับลำดับ (ใหม่สุดอยู่ล่างสุด) |
| `-h` | Human readable — แสดงขนาดเป็น KB, MB, GB |

> 💡 **Tip:** สามารถรวม option ได้เลย เช่น `ls -ltrh` จะได้ทั้งเรียงเวลาและขนาดอ่านง่าย

---

## 📁 3. Change Directory

คำสั่ง `cd` (**C**hange **D**irectory) ใช้เปลี่ยนตำแหน่งที่กำลังทำงานอยู่

```bash
cd                    # กลับไปยัง Home directory (~)
cd <folder_name>      # เข้าโฟลเดอร์ที่ระบุ
cd ..                 # ย้อนกลับ 1 ระดับ
cd ../..              # ย้อนกลับ 2 ระดับ
cd /path/to/folder    # ย้ายไปยัง path ที่ระบุแบบ absolute
cd -                  # กลับไปยัง directory ก่อนหน้า
```

> 💡 **Tip:** กด `Tab` เพื่อให้ระบบเติมชื่อโฟลเดอร์/ไฟล์ให้อัตโนมัติ  
> 💡 **Tip:** ถ้าชื่อโฟลเดอร์มีช่องว่าง เช่น `My Folder` ให้ใช้ `cd "My Folder"` หรือ `cd My\ Folder`

---

## 🗂️ 4. File & Folder Management

### สร้างโฟลเดอร์

```bash
mkdir <folder_name>           # สร้างโฟลเดอร์
mkdir -p a/b/c                # สร้างโฟลเดอร์ซ้อนกันหลายชั้นพร้อมกัน
```

### สร้างหรือแก้ไขไฟล์ด้วย `vi`

```bash
vi <filename>          # เปิดหรือสร้างไฟล์
vi <filename>.py       # สร้างไฟล์ Python
```

**คำสั่งพื้นฐานใน vi:**

| คำสั่ง | ความหมาย |
|---|---|
| `i` | เข้า Insert Mode (เริ่มพิมพ์ได้) |
| `Esc` | ออกจาก Insert Mode |
| `:wq` | บันทึกและออกจากไฟล์ |
| `:q!` | ออกโดยไม่บันทึก |
| `:w` | บันทึกโดยไม่ออก |
| `dd` | ลบทั้งบรรทัด |
| `u` | Undo |

> 💡 **Tip:** ถ้าไม่ถนัด `vi` สามารถใช้ `nano` แทนได้ ใช้งานง่ายกว่ามาก

### เปิดดูเนื้อหาไฟล์

```bash
cat <filename>          # แสดงเนื้อหาทั้งไฟล์
less <filename>         # แสดงทีละหน้า (กด q เพื่อออก)
head <filename>         # แสดง 10 บรรทัดแรก
tail <filename>         # แสดง 10 บรรทัดสุดท้าย
tail -f <filename>      # แสดง log แบบ real-time (ติดตามการเปลี่ยนแปลง)
```

### ลบไฟล์และโฟลเดอร์

```bash
rm <filename>           # ลบไฟล์
rm -r <folder_name>     # ลบโฟลเดอร์ทั้งหมด (recursive)
rm -f <filename>        # บังคับลบโดยไม่ถาม (force)
rm -rf <folder_name>    # ลบโฟลเดอร์ทั้งหมดโดยไม่ถาม ⚠️ ระวัง!
```

> ⚠️ **Warning:** `rm -rf` ลบข้อมูลถาวรโดยไม่มี Recycle Bin ควรใช้ด้วยความระมัดระวัง

---

## 🚚 5. Move File

คำสั่ง `mv` (**M**o**v**e) ใช้ย้ายไฟล์/โฟลเดอร์ หรือใช้เปลี่ยนชื่อได้ด้วย

```bash
mv <source> <destination>        # ย้ายไฟล์
mv file.py ../otherfolder/.      # ย้ายไปโฟลเดอร์ก่อนหน้า
mv ../<filename> .               # ย้ายไฟล์จากโฟลเดอร์ข้างนอกมาที่ปัจจุบัน

# เปลี่ยนชื่อไฟล์ (ย้ายในที่เดิมแต่ตั้งชื่อใหม่)
mv old_name.py new_name.py
```

> 💡 **Tip:** `.` หมายถึง "ตำแหน่งปัจจุบัน" ใช้เป็น destination ได้เลย

---

## 📑 6. Copy File & Folder

คำสั่ง `cp` (**C**o**p**y) ใช้คัดลอกไฟล์หรือโฟลเดอร์

```bash
cp <source> <destination>          # คัดลอกไฟล์
cp script.py backup/script.py      # คัดลอกไปยัง path ที่ระบุ
cp ../<filename> .                 # คัดลอกจากโฟลเดอร์ข้างนอกมาที่ปัจจุบัน
cp -r <folder_source> <dest>       # คัดลอกโฟลเดอร์ทั้งชุด (recursive)
```

---

## 📖 7. Manual Page

คำสั่ง `man` (**Man**ual) ใช้เปิดคู่มือการใช้งานของทุกคำสั่งใน Linux

```bash
man <command>      # เปิดคู่มือของคำสั่งนั้น
man ls             # ดูคู่มือของ ls
man cp             # ดูคู่มือของ cp
```

**การนำทางใน Manual:**

| ปุ่ม | ความหมาย |
|---|---|
| `Space` / `f` | เลื่อนลงหน้าถัดไป |
| `b` | เลื่อนกลับหน้าก่อนหน้า |
| `/ keyword` | ค้นหาคำภายใน manual |
| `q` | ออกจาก manual |

> 💡 **Tip:** `man` มีให้ทุกคำสั่ง ถ้าลืมการใช้งานให้ `man` ก่อนเสมอ

---

## 🖥️ 8. Check System Resources

```bash
htop               # ดู CPU / RAM แบบ real-time (ต้องติดตั้งก่อน)
top                # คล้าย htop แต่มีมาให้ในระบบโดย default
df -h              # ดูพื้นที่ disk ที่ใช้/เหลืออยู่
free -h            # ดูการใช้งาน RAM
```

**ติดตั้ง htop:**
```bash
sudo apt update
sudo apt install htop -y
```

> 💡 **Tip:** กด `q` เพื่อออกจาก `htop` / `top`

---

## 📝 สรุปคำสั่งที่ใช้บ่อย

| คำสั่ง | ความหมาย |
|---|---|
| `pwd` | แสดง path ปัจจุบัน |
| `ls -lh` | แสดงไฟล์พร้อมขนาดอ่านง่าย |
| `ls -ltr` | แสดงไฟล์เรียงตามเวลา (ใหม่สุดอยู่ล่าง) |
| `cd <folder>` | เข้าโฟลเดอร์ |
| `cd ..` | ย้อนกลับ 1 ระดับ |
| `mkdir <n>` | สร้างโฟลเดอร์ |
| `vi <file>` | สร้าง/แก้ไขไฟล์ |
| `cat <file>` | อ่านเนื้อหาไฟล์ |
| `mv <src> <dest>` | ย้าย/เปลี่ยนชื่อไฟล์ |
| `cp <src> <dest>` | คัดลอกไฟล์ |
| `rm <file>` | ลบไฟล์ |
| `rm -r <folder>` | ลบโฟลเดอร์ทั้งหมด |
| `man <cmd>` | เปิดคู่มือคำสั่ง |
| `htop` | ดูการใช้งาน CPU/RAM |

---

← [README](../README.md) · [Class II — Virtual Machines →](./Lecture_Class_II.md)
