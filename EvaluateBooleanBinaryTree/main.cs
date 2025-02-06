"""
Size aşağıdaki özelliklere sahip tam bir ikili ağacın kökü verilir:

Yaprak düğümleri 0 veya 1 değerine sahiptir, burada 0 Yanlış ve 1 Doğru'yu temsil eder.

Yapraksız düğümler 2 veya 3 değerine sahiptir, burada 2 boolean OR'yi ve 3 boolean VE'yi temsil eder.

Bir düğümün değerlendirilmesi aşağıdaki gibidir:

Düğüm bir yaprak düğümü ise, değerlendirme düğümün değeridir, yani Doğru mu Yanlış mı.

Aksi takdirde, düğümün iki çocuğunu değerlendirin ve değerinin boolean işlemini altların değerlendirmeleriyle uygulayın.

Kök düğümü değerlendirmenin boolean sonucunu döndürün.

Tam ikili ağaç, her düğümün 0 veya 2 çocuğu olduğu bir ikili ağaçtır.

Yaprak düğümü, sıfır çocuğu olan bir düğümdür.
"""

public class TreeNode {

     public int val;
     public TreeNode left;
     public TreeNode right;
     
     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
         this.val = val;
         this.left = left;
        this.right = right;
     }
 }
 
public bool EvaluateTree(TreeNode root) {
        
        if(root.val == 0){
            return false;
        }
        else if(root.val == 1){
            return true;
        }
        else if(root.val == 2){
            return EvaluateTree(root.left) || EvaluateTree(root.right);
        }
        else if(root.val == 3){
            return EvaluateTree(root.left) && EvaluateTree(root.right);
        }
        return false;
        
    }