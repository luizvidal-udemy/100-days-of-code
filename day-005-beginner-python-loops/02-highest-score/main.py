student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]

# total_exam_score = sum(student_scores)

# total_exam_score_manual = 0

# for score in student_scores:
#     total_exam_score_manual += score

# print(total_exam_score_manual)

highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score

print(highest_score)