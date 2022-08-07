class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) 
    {
        if(mat.empty()) return {};
        int m=mat.size(),n=mat[0].size();
        vector<vector<int>> ans(m,vector<int>(n,100));
        //如果一次遍历分上下左右四个方向查找，则很难判断出界的情况
        //分两次，第一次从左上到右下更新，第二次从右下到左上更新
        for(int i=0;i<m;++i)
        {
            for(int j=0;j<n;++j)
            {
                if(mat[i][j]==0) //0
                {
                    ans[i][j]=0;
                }
                else //1,往左上两个方向找，此时[0,0]位置越界，我们暂时不找，但是可以遍历到[m-1,n-1]
                {
                    if(i>0) //除去第一行
                    {
                        ans[i][j]=min(ans[i][j],ans[i-1][j]+1); //上
                    }
                    if(j>0) //除去第一列
                    {
                        ans[i][j]=min(ans[i][j],ans[i][j-1]+1);//左
                    }
                    //至此，除了[0,0]，第一行往左找了，第一列往上找了，其他元素往左上两个方向找了
                }
            }
        }

         for(int i=m-1;i>=0;--i)
        {
            for(int j=n-1;j>=0;--j)
            {
                if(mat[i][j]!=0) //1,往右下两个方向找，此时[m-1,n-1]位置越界，我们刚才找过了，但是可以遍历到[0,0]
                {
                    if(i<m-1) //除去最后一行
                    {
                        ans[i][j]=min(ans[i][j],ans[i+1][j]+1); //下
                    }
                    if(j<n-1) //除去最后一列
                    {
                        ans[i][j]=min(ans[i][j],ans[i][j+1]+1);//右
                    }
                    //至此，除了[m-1,n-1]，最后一行往右找了，最后一列往下找了，其他元素往右下两个方向找了
                }
            }
        }
        //至此，所有元素完成方向遍历
        return ans;


    }
};

