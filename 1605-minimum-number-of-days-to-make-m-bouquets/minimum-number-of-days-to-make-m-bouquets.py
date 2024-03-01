class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def get_bouquets(day):
            adjacent_flowers = 0
            bouquet = 0 
            for bloom in range(len(bloomDay)):
                if bloomDay[bloom] <= day :
                    if bloom == 0 or day < bloomDay[bloom-1] :
                        adjacent_flowers = 1

                    else:
                        adjacent_flowers += 1
                
                if adjacent_flowers == k:
                    bouquet += 1
                    adjacent_flowers = 0
            print(bouquet)
            return bouquet


        low, high = 1, max(bloomDay)  
        
        while low <= high:
            mid = (low + high) // 2  
            
            if get_bouquets(mid) >= m:
                high = mid - 1  
            else:
                low = mid + 1  
        
        return low if low <= max(bloomDay) else -1
        