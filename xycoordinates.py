
def find_coordinates():
    print("My Program")
    coords = [(2,4), (4,8)]
    [m,b] = define_line(coords)
    x = input("Input parameter x: ")
    y = solve_y(m, b, x)
    print("Output parameter y: {}".format(y))


def define_line(coords):
    m = (coords[0][1]-coords[1][1])/(coords[0][0]-coords[1][0])
    b = coords[0][1]-(m*coords[0][0])
    return m, b

def solve_y(m, b, x):
    y_value = (m*int(x)) + b
    return y_value

if "__name__" == "__main__":
    find_coordinates()
    
    
    
