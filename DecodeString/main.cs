public class Solution 
{    
    public string DecodeString(string s)
        {
            Stack<int> nums = new Stack<int>();
            Stack<StringBuilder> strings = new Stack<StringBuilder>();
            StringBuilder output = new StringBuilder();
            
            int repeat = 0;

            foreach (char ch in s)
            {

                if (char.IsDigit(ch))
                {
                    repeat = repeat * 10 + (ch - '0');
                }
                else if (ch == '[')
                {
                    nums.Push(repeat);
                    strings.Push(output);
                    
                    output = new StringBuilder();
                    repeat = 0;
                }
                else if (ch == ']')
                {
                    StringBuilder decode = strings.Pop();
                    int x = nums.Pop();

                    for (int i = 0; i < x; i++)
                    {
                        decode.Append(output);
                    }

                    output = decode;

                }
                else
                {
                    output.Append(ch);
                }
            }

            return output.ToString();
        }        
    }
