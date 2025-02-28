"""
Geçerli bir (IPv4) IP adresi verildiğinde, bu IP adresinin sağlam bir sürümünü döndürün.

Deski bir IP adresi, her "." dönemini "[.]" ile değiştirir.
----------------------------------------------------------------------------
Örnek 1:

Giriş: adres = "1.1.1.1"

Çıktı: "1[.] 1[.] 1[.] 1 inç
----------------------------------------------------------------------------
Örnek 2:

Giriş: adres = "255.100.50.0"

Çıktı: "255[.] 100[.] 50[.] 0"
"""

public class Solution {
    public string DefangIPaddr(string address) {
        string result = "";
        for(int i = 0;i<address.Length;i++){
            if(address[i] == '.'){
                result += "[.]";
            }
            else{
                result += address[i];
            }
        }
        return result;
        
    }
}