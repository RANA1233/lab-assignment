#QUESTION_5
print("QUESTION_5: (Valid or Invalid triangle sides)", end='\n')
side_a=int(input("Enter the length of 1st side : "))
side_b=int(input("Enter the length of 2nd side : "))
side_c=int(input("Enter the length of 3rd side : "))
if side_a < side_b+ side_c and side_b < side_a + side_c and side_c < side_b + side_a:
    print("Yes")
else:
    print("No")    
    
