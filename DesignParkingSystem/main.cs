"""
Bir otopark için bir park sistemi tasarlayın. Otoparkta üç çeşit park yeri vardır: büyük, orta ve küçük, her boyut için sabit sayıda yuva.

ParkingSystem sınıfını uygulayın:

ParkingSystem(int big, int medium, int small) ParkingSystem sınıfının nesnesini başlatır. Her park yeri için slot sayısı, inşaatçının bir parçası olarak verilir.

Bool addCar(int carType) Otoparka girmek isteyen araba için carType'ın bir park yeri olup olmadığını kontrol eder. carType üç çeşit olabilir: sırasıyla 1, 2 ve 3 ile temsil edilen büyük, orta veya küçük. Bir araba yalnızca kendi araba tipindeki bir park alanına park edebilir. Boş yer yoksa, yanlış iade edin, aksi takdirde arabayı o büyüklükteki alana park edin ve doğru döndürün.
-----------------------------------------------------------------------------------
Örnek 1:

Giriş

["Park Sistemi", "addCar", "addCar", "addCar", "addCar"]

[[1, 1, 0], [1], [2], [3], [1]]

Üretim

[Boş, doğru, doğru, yanlış, yanlış]

Açıklama

* ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);

* parkingSystem.addCar(1); // return true çünkü büyük bir araba için 1 boş yuva var

* parkingSystem.addCar(2); // return true çünkü orta boy bir araba için 1 boş yuva var

* parkingSystem.addCar(3); // return false çünkü küçük bir araba için boş yer yok

* parkingSystem.addCar(1); // return false çünkü büyük bir araba için boş yer yok. Zaten işgal edildi.
"""

public class ParkingSystem {

    int[] parkingSystem = new int[3];
    public ParkingSystem(int big, int medium, int small) {
        this.parkingSystem[0] = big;
        this.parkingSystem[1] = medium;
        this.parkingSystem[2] = small;
        

    }
    
    public bool AddCar(int carType) {
        if(carType == 1){
            if(parkingSystem[0] > 0){
                parkingSystem[0]-=1;
                return true;
            }
            return false;
        }
        else if(carType == 2){
            if(parkingSystem[1] > 0){
                parkingSystem[1]-=1;
                return true;
            }
            return false;
        }
        else{
            if(parkingSystem[2] > 0){
                parkingSystem[2]-=1;
                return true;
            }
            return false;
        }
    }
}