message = "please input the first 2 end points, then 2 control points in order. For example: [1,1],[2,2],[1,3],[3,3]. (1,1) and (2,2) are end points in this example and (1,3),(3,3) are control points "
print (message)
def bezier(points):
    final_x = ""
    final_y = ""
    bx = 3*(points[2][0] - points[0][0])
    by = 3*(points[2][1] - points[0][1])
    cx = 3*(points[3][0] - points[2][0]) - bx
    cy = 3*(points[3][1] - points[2][1]) - by
    dx = points[1][0] - points[0][0] - bx - cx
    dy = points[1][1] - points[0][1] - by - cy

    final_x += str(points[0][0])
    final_y += str(points[0][1])

    final_x += " + "
    final_y += " + "

    final_x += str(bx)
    final_x += "t"
    
    final_y += str(by)
    final_y += "t"

    final_x += " + "
    final_y += " + "

    final_x += str(cx)
    final_x += "t^2"

    final_y += str(cy)
    final_y += "t^2"

    final_x += " + "
    final_y += " + "

    final_x += str(dx)
    final_x += "t^3"

    final_y += str(dy)
    final_y += "t^3"

    print("The Bezier curves are: ")
    print(final_x)
    print(final_y)


points = [[1,1],[2,2],[1,3],[3,3]] #example from powerpoint
bezier(points)

        

    

    
