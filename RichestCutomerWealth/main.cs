"""
Size bir m x n tamsayı ızgara hesabı verilir, burada hesaplar[i][j], müşterinin j. bankada sahip olduğu para miktarıdır. En zengin müşterinin sahip olduğu serveti iade edin.

Bir müşterinin serveti, tüm banka hesaplarında sahip olduğu para miktarıdır. En zengin müşteri, maksimum servete sahip olan müşteridir.

Örnek 1:

Giriş: hesaplar = [[1,2,3],[3,2,1]]

Çıktı: 6

Açıklama:

* 1. müşterinin serveti var = 1 + 2 + 3 = 6

* 2. müşterinin serveti var = 3 + 2 + 1 = 6

* Her iki müşteri de her biri 6'lık servetle en zengin olarak kabul edilir, bu nedenle 6'yı  iade edin.
"""
public class Solution {
    public int MaximumWealth(int[][] accounts) {
        
        int max = 0;

        for(int i= 0; i<accounts.Length; i++){
            int total = 0;
            for(int j= 0; j<accounts[0].Length; j++){
                total += accounts[i][j];
            }
            if(total > max){
                max = total;
            }
        }
        return max;
    }
}