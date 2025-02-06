public class TreeNode {

     public int val;
     public TreeNode left;
     public TreeNode right;
     
     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null)
    {
         this.val = val;
         this.left = left;
        this.right = right;
     }
 }
 
public class Solution {

    List<int> list = new List<int>();
    void Preorder(TreeNode root){
        if(root == null){
            return;
        }
        list.Add(root.val);
        Preorder(root.left);
        Preorder(root.right);
    }
    public IList<int> PreorderTraversal(TreeNode root) {
        
        Preorder(root);

        return list;
    }
}