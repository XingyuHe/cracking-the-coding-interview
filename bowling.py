import collections
class Solution(object):

    score_list = []
    score_accum = []

    def addRounds(self, round_list):
        for pins in round_list:
            self.addPins(pins)

    def addPins(self, pins_knocked_down):

        if not self.score_list:
            self.score_list.append((pins_knocked_down,))

        else:
            last_frame = self.score_list[-1]
            if len(last_frame) == 2:
                self.score_list.append((pins_knocked_down,))
            elif last_frame[-1] == 10:
                self.score_list.append((pins_knocked_down,))
            else:
                self.score_list[-1] = last_frame + (pins_knocked_down, )


    def scores(self):

        # return current frame score and total score

        for frame_num in range(len(self.score_list) - 1, -1, -1):

            frame = self.score_list[frame_num]
            raw_score = sum(frame)
            print frame_num, frame, raw_score, self.score_accum
            if raw_score == 10 and len(frame) == 1:
                # strike
                next_frame = self.score_list[frame_num + 1]
                if len(next_frame) == 2:
                    bonus = next_frame[0] + next_frame[1]
                else:
                    bonus = next_frame[0] + self.score_list[frame_num + 2][0]

                self.score_accum.insert(0, raw_score + bonus)

            elif raw_score == 10 and len(frame) == 2:
                # spare
                bonus = self.score_list[frame_num + 1][0]
                self.score_accum.insert(0, raw_score + bonus)

            else:
                self.score_accum.insert(0, raw_score)

        return sum(self.score_accum), self.score_accum[-1]

solution = Solution()
solution.addRounds([10, 10, 9, 0])
print solution.score_list
print solution.scores()
