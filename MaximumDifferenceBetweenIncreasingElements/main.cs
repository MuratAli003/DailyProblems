"""
N boyutunda 0 indeksli bir tamsayı dizi sayısı verildiğinde, nums[i] ve nums[j] (yani, nums[j] - nums[i]) arasındaki maksimum farkı bulun, öyle ki 0 <= i < j < n ve nums[i] < nums[j].

Maksimum farkı döndürün. Böyle bir i ve j yoksa, -1 döndürün.

-----------------------------------------------------------------------------------------------
Örnek 1:

Giriş: nums = [7,1,5,4]

Çıktı: 4

Açıklama:

Maksimum fark i = 1 ve j = 2, nums[j] - nums[i] = 5 - 1 = 4 ile ortaya çıkar.

I = 1 ve j = 0 ile farkın nums[j] - nums[i] = 7 - 1 = 6 olduğuna dikkat edin, ancak i > j, bu nedenle geçerli değildir.
"""

public int MaximumDifference(int[] nums) {
        
    int sub = -1;
        for (int i = 0; i < nums.Length-1; i++)
        {
            for (int j = i+1; j<nums.Length; j++)
            {
                if (((nums[j] - nums[i]) > sub) && nums[j] != nums[i])
                {
                    sub = nums[j] - nums[i];
                }
            }
        }

        return sub;
}