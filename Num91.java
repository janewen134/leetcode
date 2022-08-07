public class Num91 {


    public int numDecodings(String s) {
        int numLength = s.length();
        char[] numArray = s.toCharArray();
        int preNum = (numArray[0] - '0');
        int[] dp = new int[ numLength + 1];

        if (preNum == 0){ // invalid input
            return 0;
        } else if (numLength == 1){ // single letter
            return 1;
        }

        dp[0] = dp[1] = 1;

        for (int step = 2; step != numLength + 1; step++) {
            int curNum = (numArray[step - 1] - '0');
            if ((preNum == 0 || preNum > 2) && curNum == 0) {
                return 0;
            }
            if ((preNum == 1) || (preNum == 2 && curNum <= 6)) {
                if (curNum == 0) {
                    dp[step] = dp[step - 2];
                } else {
                    dp[step] = dp[step - 1] + dp[step - 2];
                }
            } else {
                dp[step] = dp[step - 1];
            }

            preNum = curNum;

        }
        return dp[numLength];
    }
}
