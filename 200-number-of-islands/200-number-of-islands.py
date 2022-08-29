class Solution(object):
    
    def is_island(self, grid, i, j):
        
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
    
        grid[i][j] = '#'
        
        self.is_island(grid, i-1, j)
        self.is_island(grid, i+1, j)
        self.is_island(grid, i, j-1)
        self.is_island(grid, i, j+1)
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid[0])
        n = len(grid)
        
        no_islands = 0
        
        for i in range(n):
            for j in range(m):

                if grid[i][j] == '1':
                    self.is_island(grid, i, j)
                    no_islands += 1
                
        return no_islands
    
    


