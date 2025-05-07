"""
Bir dize komutunu yorumlayabilen bir Goal Ayrıştırıcıya sahipsiniz. Komut, bir sırayla "G", "()" ve/veya "(al)" alfabesinden oluşur. Goal Ayrıştırıcı, "G"yi "G" dizesi olarak "G" olarak, "()"i "o" dizesi olarak ve "(al)"i "al" dizesi olarak yorumlayacaktır. Yorumlanan dizeler daha sonra orijinal sırayla birleştirilir.

Dize komutu göz önüne alındığında, Goal Parser'ın komut yorumunu döndürün.

Örnek 1:

Giriş: komut = "G()(al)"

Çıktı: "Goal"

Açıklama: Goal Ayrıştırıcı komutu şu şekilde yorumlar:

* G -> G

* () -> o

* (Al) -> al

Nihai birleştirilmiş sonuç "Goal"tir.
"""
public class Solution {
    public string Interpret(string command) {
        StringBuilder output = new StringBuilder();

        for(int i = 0; i< command.Length; i++){
            if(command[i] == 'G'){
                output.Append(command[i]);
            }
            else if(command[i] == '(' && i + 1 < command.Length && command[i + 1] == ')'){
                output.Append('o');
            }
            else if(command[i] == '(' && i + 1 < command.Length && command[i + 1] == 'a'){
                output.Append("al");
            }
        }
        return output.ToString();
    }
}