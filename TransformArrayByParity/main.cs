"""
Size bir tamsayı dizisi sayıları verilir. Aşağıdaki işlemleri belirtilen sırayla gerçekleştirerek numaraları dönüştürün:

* Her çift sayıyı 0 ile değiştirin.

* Her tek sayıyı 1 ile değiştirin.

* Değiştirilen diziyi azalmayan sırayla sıralayın.

* Bu işlemleri gerçekleştirdikten sonra ortaya çıkan diziyi döndürün.
-------------------------------------------------------------------------------------------
Örnek 1:

Giriş: nums = [4,3,2,1]

Çıktı: [0,0,1,1]

Açıklama:

* Çift sayıları (4 ve 2) 0 ile ve tek sayıları (3 ve 1) 1 ile değiştirin. Şimdi, sayılar = [0, 1, 0, 1].

* Numaraları azalmayan sırayla sıraladıktan sonra, nums = [0, 0, 1, 1].
"""
public class Solution {
    public int[] TransformArray(int[] nums) {
        
        int odd = 0;
        int even = 0;

        for(int i = 0;i<nums.Length;i++){
            if(nums[i] % 2 == 0){
                even += 1;
            }
            else{
                odd += 1;
            }
        }
        
        for(int i = 0; i< even;i++){
            nums[i] = 0;
        }
        for(int i = even; i< odd + even;i++){
            nums[i] = 1;
        }
        return nums;

    }
}