"""
1.	İki dizi veriliyor:
	•	sandwiches (sandviçlerin yığılı olduğu yığın, en üstteki sandviç sandwiches[0])
	•	students (öğrencilerin sırada beklerkenki tercihleri, sıranın en önündeki öğrenci students[0])
2.	Kurallar:
	•	Eğer sıranın en önündeki öğrenci, yığının en üstündeki sandviç tipini tercih ediyorsa:
	•	Öğrenci sandviçi alır, sıradan çıkar ve yığının tepesindeki sandviç de gider.
	•	Eğer öğrenci sandviçi istemiyorsa:
	•	Öğrenci sıranın sonuna gönderilir.
	•	Bu işlem, yığının en üstündeki sandviç alınamayınca durur (yani, artık sıradaki öğrencilerden hiçbiri yığının en üstündeki sandviçi istemiyorsa).
3.	Amaç:
	•	Yemek yiyemeyen öğrenci sayısını döndürmek.


Giriş: öğrenciler = [1,1,0,0], sandviçler = [0,1,0,1]

Çıktı: 0

Açıklama:

- Ön öğrenci üstteki sandviçten ayrılır ve çizginin sonuna geri döner ve öğrencileri = [1,0,0,1] yapar.

- Ön öğrenci üstteki sandviçten ayrılır ve çizginin sonuna geri döner ve öğrencileri = [0,0,1,1] yapar.

- Ön öğrenci üstteki sandviçi alır ve sırayı terk ederek öğrencileri = [0,1,1] ve sandviçleri = [1,0,1] yapar.

- Ön öğrenci üstteki sandviçi terk eder ve çizginin sonuna geri döner ve öğrencileri = [1,1,0] yapar.

- Ön öğrenci üstteki sandviçi alır ve sırayı terk ederek öğrencileri = [1,0] ve sandviçler = [0,1] yapar.

- Ön öğrenci üstteki sandviçi bırakır ve sıranın sonuna geri döner ve öğrencileri = [0,1] yapar.

- Ön öğrenci en üstteki sandviçi alır ve sırayı terk ederek öğrencileri = [1] ve sandviçleri = [1] yapar.

- Ön öğrenci üstteki sandviçi alır ve sırayı terk ederek öğrencileri = [] ve sandviçleri = [] yapar.

Bu nedenle tüm öğrenciler yemek yiyebilir.

"""

def countStudents(students, sandwiches):
    
        son = len(students) - 1

        while len(students) > 0:

            if son == 0:

                if students[0] != sandwiches[0]:
                    break
                else:

                    students.pop(0)
                    sandwiches.pop(0)

                    son = len(students) - 1

            else:

                if students[0] != sandwiches[0]:

                    student = students.pop(0)
                    students.append(student)
                    son -= 1

                else:

                    students.pop(0)
                    sandwiches.pop(0)

                    son = len(students) - 1
        
        return len(students)
