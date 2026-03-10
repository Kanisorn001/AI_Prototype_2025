# 🧠 Class VI — AI Fundamentals & LLM Training

> ภาพรวมของ Artificial Intelligence ตั้งแต่พื้นฐาน Machine Learning  
> ไปจนถึงการ Train และ Deploy Large Language Model (LLM)

---

## 📋 สารบัญ

1. [What is AI?](#-1-what-is-ai)
2. [Machine Learning](#-2-machine-learning)
3. [Computer Vision](#-3-computer-vision)
4. [Transfer Learning](#-4-transfer-learning)
5. [Large Language Model (LLM)](#-5-large-language-model-llm)
6. [LLM Training Pipeline](#-6-llm-training-pipeline)
7. [RAG — Retrieval-Augmented Generation](#-7-rag--retrieval-augmented-generation)
8. [สรุป](#-สรุป)

---

## 🤖 1. What is AI?

**Artificial Intelligence (AI)** คือการสร้างระบบที่สามารถทำงานที่ต้องใช้ความฉลาดของมนุษย์ได้

```
AI ครอบคลุม 5 สาขาหลัก:

  👁️  Computer Vision   →  ให้คอมพิวเตอร์ "มองเห็น"
  💬  NLP               →  ให้คอมพิวเตอร์ "เข้าใจภาษา"
  📚  Machine Learning  →  ให้คอมพิวเตอร์ "เรียนรู้"
  🧠  Expert System     →  ให้คอมพิวเตอร์ "ตัดสินใจ"
  🦾  Robotics          →  ให้คอมพิวเตอร์ "ลงมือทำ"
```

> 💡 **สูตรสำคัญ:** `ML = Data + Computing Power`  
> ปัจจุบัน AI กว่า 99% ขับเคลื่อนด้วย Machine Learning

---

## 📊 2. Machine Learning

ML คือการสร้างฟังก์ชัน **f(x)** ที่ map input ไปหา output ได้  
โดยให้คอมพิวเตอร์เรียนรู้ pattern จากข้อมูลเอง แทนที่จะเขียน rule ทั้งหมดด้วยมือ

![ML Overview](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Artificial_Intelligence_%E2%80%94_An_Illustration.jpg/640px-Artificial_Intelligence_%E2%80%94_An_Illustration.jpg)

### Supervised Learning — เรียนจากตัวอย่าง

ใช้ข้อมูลที่มี **label** (คำตอบที่ถูกต้องกำกับอยู่แล้ว) สอนโมเดล  
เป้าหมาย: หา **f(x)** ที่ทำให้ค่า **loss น้อยที่สุด**

```
Input (X)                     Output (Y)
──────────────────────────    ──────────
รูปภาพ                   →   ชื่อวัตถุ
ข้อความ                  →   ความรู้สึก (positive/negative)
ค่าจากเซนเซอร์           →   การวินิจฉัยโรค
ราคาบ้าน (ขนาด, ทำเล)   →   ราคาที่ควรจะเป็น
```

**ประเภทของ Supervised Learning:**

| ประเภท | ลักษณะ Output | ตัวอย่าง |
|---|---|---|
| **Regression** | ตัวเลขต่อเนื่อง | ทำนายราคา, อุณหภูมิ |
| **Classification** | หมวดหมู่ | แยกดอกไม้, ตรวจสอบสแปม |

### Unsupervised Learning — เรียนโดยไม่มีคำตอบ

ใช้กับข้อมูลที่ **ไม่มี label** ให้โมเดลหา pattern เองโดยอิสระ

```
Input (X)                     สิ่งที่ได้
──────────────────────────    ──────────────────────────────
รูปภาพจำนวนมาก          →   กลุ่มของรูปที่คล้ายกัน
ข้อมูลลูกค้า             →   segment ลูกค้า
ข้อความภาษาธรรมชาติ     →   โครงสร้างและความหมาย
```

![Supervised vs Unsupervised](https://miro.medium.com/v2/resize:fit:1400/1*AZMDyaifxGVdwTV-1BN7kA.png)

---

## 👁️ 3. Computer Vision

ก่อนยุค Deep Learning — คอมพิวเตอร์ "เห็น" ภาพด้วยการแปลงรูปเป็นตัวเลขด้วยมือ

### วิธีแบบดั้งเดิม (Traditional CV)

```
ภาพต้นฉบับ
    ↓
แปลงเป็นขอบ (Edge Detection)
    ↓
แบ่งทิศทางเส้น (Gradient Direction)
    ↓
สร้าง Histogram of Oriented Gradients (HOG)
    ↓
ส่งเข้า ML Algorithm (เช่น SVM)
    ↓
ผลลัพธ์ (Classification)
```

### ยุค Deep Learning (CNN)

ปัจจุบันใช้ **Convolutional Neural Network (CNN)**  
ให้โมเดลเรียนรู้ feature จากภาพเองโดยอัตโนมัติ ไม่ต้องออกแบบ feature ด้วยมือ

```
ภาพ → [Conv Layer] → [Pooling] → [FC Layer] → ผลลัพธ์
         (หา feature)  (ย่อขนาด)  (ตัดสินใจ)
```

---

## 🔄 4. Transfer Learning

แนวคิด: **เรียนรู้ทั่วไปก่อน → แล้วค่อยเรียนรู้เฉพาะทาง**  
ประหยัดเวลาและข้อมูลอย่างมาก เพราะไม่ต้อง train ตั้งแต่ศูนย์

![Transfer Learning](https://www.researchgate.net/publication/329418720/figure/fig2/AS:700423865888769@1544189869351/Schematic-representation-of-transfer-learning-In-traditional-machine-learning-left.png)

### ขั้นตอน Transfer Learning

```
Step 1: Pre-training
─────────────────────────────────────────────
ใช้ Dataset ขนาดใหญ่ทั่วไป (เช่น ImageNet ~14M รูป, 1000 class)
โมเดลเรียนรู้ feature พื้นฐาน เช่น ขอบ, รูปทรง, สี, texture

Step 2: Fine-tuning
─────────────────────────────────────────────
นำโมเดลที่ pre-train แล้วมาสอนต่อด้วยข้อมูลเฉพาะทาง
เช่น รูปภาพโรคของพืช หรือ X-ray ปอด
ใช้ข้อมูลน้อยกว่ามาก แต่ได้ผลลัพธ์ที่ดี
```

**ตัวอย่างใช้งานจริง:**

| Pre-trained Model | Fine-tune ด้วย | ผลลัพธ์ |
|---|---|---|
| ImageNet (ภาพทั่วไป) | ภาพ X-ray | ตรวจจับโรคปอด |
| ImageNet | ภาพพืช | ระบุโรคของพืช |
| BERT (ภาษาอังกฤษ) | ข้อความทางการแพทย์ | วิเคราะห์เวชระเบียน |

> 💡 **สรุป:** Pre-train = สอนกว้างๆ ก่อน / Fine-tune = ปรับให้เก่งเรื่องที่ต้องการ

---

## 💬 5. Large Language Model (LLM)

LLM คือโมเดลภาษาขนาดใหญ่ที่เข้าใจและสร้างข้อความได้เหมือนมนุษย์  
สร้างขึ้นโดยให้โมเดลฝึก **ทำนายคำถัดไป (Next Token Prediction)** จากข้อความมหาศาล

### Next Token Prediction

```
Input:   "วันนี้อากาศดี ฉันอยากไป"
                                  ↓
Model ทำนาย:  "เที่ยว" (probability สูงสุด)

ทำซ้ำไปเรื่อยๆ จนได้ประโยคที่สมบูรณ์
```

### Transformer Architecture

LLM ใช้สถาปัตยกรรม **Transformer** ซึ่งใช้ **Attention Mechanism**  
ช่วยให้โมเดลเข้าใจความสัมพันธ์ระหว่างคำที่อยู่ห่างกันในประโยคได้

```
"The cat sat on the mat because it was tired"
                              ↑
           "it" หมายถึง "cat" — Attention ช่วยเชื่อมโยงได้
```

---

## 🏗️ 6. LLM Training Pipeline

กระบวนการสร้าง LLM แบ่งออกเป็น 4 ขั้นตอนหลัก:

![LLM Pipeline](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbcbbac21-7a0c-4049-9e09-0d4b06cc9d89_2880x1620.png)

### Stage 1 — Pre-training 🌍

```
ข้อมูล: ข้อความจากอินเทอร์เน็ต, หนังสือ, Wikipedia ทั้งหมด
เป้าหมาย: Next Token Prediction
ผลลัพธ์: Base Model (เช่น GPT, Llama, Mistral)
ขนาดข้อมูล: หลาย Trillion tokens
```

> ต้องการ GPU จำนวนมาก และเวลาหลายเดือน — ทำโดยบริษัทใหญ่เท่านั้น

---

### Stage 2 — Continued Pre-training 💻

```
ข้อมูล: ข้อความเฉพาะทาง เช่น code, เอกสารทางการแพทย์, ภาษาไทย
เป้าหมาย: Next Token Prediction เหมือนเดิม แต่เฉพาะ domain
ผลลัพธ์: โมเดลที่เก่งขึ้นในด้านที่ต้องการ

ตัวอย่าง: นำ Llama มา continued pre-train ด้วยโค้ด → เก่ง coding มากขึ้น
```

---

### Stage 3 — Instruction Fine-tuning 📋

```
ข้อมูล: ชุด (คำสั่ง, คำตอบที่ดี) จำนวนมาก
เป้าหมาย: ให้โมเดลทำตามคำสั่งที่เราต้องการได้

ก่อน fine-tune: โมเดลแค่ต่อประโยค
หลัง fine-tune: โมเดลตอบคำถาม, ช่วยงาน, ทำตามคำสั่งได้
```

**Agentic Fine-tuning** — สำหรับโมเดลที่ต้องใช้ tools:

```
Input:  "นัดหมายกับ Dr. Smith วันพรุ่งนี้ 10:00 น."
        + เครื่องมือที่มี: [calendar, email, search]
              ↓
Model:  เรียกใช้ calendar.create_event(...)
              ↓
Output: "นัดหมายเรียบร้อยแล้ว ✓"
```

---

### Stage 4 — Preference Fine-tuning (RLHF) 👍

ทำให้คำตอบของโมเดล "ถูกใจ" มากขึ้น ไม่ใช่แค่ถูกต้อง

![RLHF](https://images.ctfassets.net/kftzwdyauwt9/5yMGkExrRaJ3GpNJ8LKf2N/4fde89b40cf0e1b00e77e9a0d7e2c48f/RLHF_Diagram_2x.png?w=3840&q=90&fm=webp)

```
1. สร้างคำตอบหลายแบบสำหรับคำถามเดิม
2. มนุษย์ rank ว่าคำตอบไหนดีกว่า
3. train Reward Model จาก feedback เหล่านั้น
4. ใช้ Reinforcement Learning ปรับ LLM ให้ได้ reward สูงขึ้น

= RLHF (Reinforcement Learning from Human Feedback)
```

---

### Stage 5 — RAG Deployment 📚

ดูรายละเอียดในส่วนถัดไป →

---

## 🔍 7. RAG — Retrieval-Augmented Generation

**ปัญหาของ LLM:** ความรู้ถูกจำกัดอยู่ที่ข้อมูลตอน train เท่านั้น  
**RAG แก้ปัญหาด้วยการ:** ดึงข้อมูลที่เกี่ยวข้องมาเพิ่มให้ LLM แบบ real-time

![RAG Architecture](https://blogs.nvidia.com/wp-content/uploads/2023/11/Retrieval-Augmented-Generation-RAG-Blog-1280x680-1.png)

### RAG Pipeline

```
คำถามผู้ใช้
    ↓
แปลงเป็น Vector (Embedding)
    ↓
ค้นหาใน Vector Database (หา context ที่คล้ายกัน)
    ↓
ได้ context ที่เกี่ยวข้อง
    ↓
ส่ง [คำถาม + context] เข้า LLM
    ↓
LLM สร้างคำตอบจาก context ที่ให้
    ↓
คำตอบ
```

### Vector Database คืออะไร?

ข้อความทุกชิ้นถูกแปลงเป็น **vector (ตัวเลขหลายมิติ)**  
ข้อความที่มีความหมายใกล้กัน จะมี vector ที่ใกล้กันในพื้นที่มิติสูง

```
"แมวกินปลา"   → [0.2, 0.8, 0.1, ...]
"แมวชอบปลา"  → [0.21, 0.79, 0.12, ...]  ← ใกล้กัน ✓
"รถยนต์ไฟฟ้า" → [0.9, 0.1, 0.7, ...]   ← ห่างกัน ✗
```

> ⚠️ **ข้อควรระวัง:** ถ้าระบบดึง context ผิด LLM ก็จะตอบจาก context ที่ผิดด้วย

---

## 📝 สรุป

**สิ่งที่คนทั่วไปทำได้ (ไม่ต้องการ GPU มหาศาล):**

| Stage | ทำได้? | เหตุผล |
|---|:---:|---|
| Pre-training | ❌ | ต้องการ GPU หลายพันตัว + data ระดับ Trillion tokens |
| Continued Pre-training | ⚠️ | ต้องการทรัพยากรสูง แต่น้อยกว่า Pre-training |
| **Instruction Fine-tuning** | ✅ | ทำได้ด้วย GPU ระดับ consumer |
| Preference (RLHF) | ⚠️ | ซับซ้อน แต่มี library ช่วย เช่น TRL |
| **RAG Deployment** | ✅ | ใช้ API + Vector DB ได้เลย |

```
สำหรับผู้เริ่มต้น แนะนำโฟกัสที่:

  Stage 3 (Fine-tuning)  →  ปรับโมเดลให้ทำงานเฉพาะทาง
  Stage 5 (RAG)          →  เชื่อมโมเดลกับข้อมูลของเรา
```

---

← [Class VI — Web Service](./Lecture_Class_VI.md) · [README](../README.md)
