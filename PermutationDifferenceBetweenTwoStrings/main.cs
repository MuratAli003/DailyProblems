"""
Size iki dize s ve t verilir, böylece her karakter s'de en fazla bir kez ortaya çıkar ve t, s'nin bir permütasyonudur.

S ve t arasındaki permütasyon farkı, s'deki her bir karakterin oluşumunun indeksi ile t'de aynı karakterin oluşumunun indeksi arasındaki mutlak farkın toplamı olarak tanımlanır.

S ve t arasındaki permütasyon farkını döndürün.
-------------------------------------------------------------------------------------
Örnek 1:

Giriş: s = "abc", t = "bac"

Çıktı: 2

Açıklama:

* S = "abc" ve t = "bac" için, s ve t'nin permütasyon farkı aşağıdakilerin toplamına eşittir:

* S'deki "a" oluşumunun endeksi ile t'deki "a" oluşumunun endeksi arasındaki mutlak fark.

* S'deki "b" oluşumunun indeksi ile t'deki "b" oluşumunun indeksi arasındaki mutlak fark.

* S'deki "c" oluşumunun indeksi ile t'deki "c" oluşumunun indeksi arasındaki mutlak fark.

* Yani, s ve t arasındaki permütasyon farkı |0 - 1| + |1 - 0| + |2 - 2| = 2'ye eşittir.
"""

public class Solution {
    public int FindPermutationDifference(string s, string t) {
        
        int total = 0;

        for(int i = 0; i<s.Length; i++){
            total += Math.Abs(s.IndexOf(s[i]) - s.IndexOf(t[i]));
        }
        return total;
    }
}