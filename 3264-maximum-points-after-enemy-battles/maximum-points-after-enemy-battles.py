class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        total_energy = currentEnergy
        
        enemyEnergies.sort()
        if total_energy < enemyEnergies[0]:
            return 0
        for energy in enemyEnergies[1:]:
            total_energy += energy

        return total_energy // enemyEnergies[0]
        

