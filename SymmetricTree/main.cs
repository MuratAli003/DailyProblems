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

public class Solution {

    bool IsSame(TreeNode p,TreeNode q){

        if(p == null || q == null){

            return p == q;
        }

        return (p.val == q.val) && IsSame(p.left,q.right) && IsSame(p.right,q.left);
    }
    public bool IsSymmetric(TreeNode root) {
        
        return IsSame(root.left,root.right);

        
    }
}