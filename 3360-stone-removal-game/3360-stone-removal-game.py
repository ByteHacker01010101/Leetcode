class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones = 10
        alice_turn = True

        while stones > 0 and n >= stones:
            n -= stones
            stones -= 1
            alice_turn = not alice_turn

        return not alice_turn