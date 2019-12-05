from graphics import * 

def main(): 
    print("This program plots the growth of a 10-year invesment.")
    
    # Get principal & interest rate
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annualizd interest rate: "))

    # Create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1,0), ' 0.0k').draw(win)
    Text(Point(-1,2500), ' 2.5k').draw(win)
    Text(Point(-1,5000), ' 5.0k').draw(win)
    Text(Point(-1,7500), ' 7.5k').draw(win)
    Text(Point(-1,10000), '10.0k').draw(win)

    # Draw bar for initial principal 
    bar = Rectangle(Point(0,0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw a bar for each subsequent year
    for year in range(1,11):
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year+1, principal))
        bar.setFill("gold")
        bar.setWidth(2)
        bar.draw(win)

    input("Press <Enter> to quit.")
    win.close()

main()

def click(): 
    win = GraphWin("Click Me!")
    for i in range(10):
        p = win.getMouse()
        print("You clicked at:" , p.getX(), p.getY())

click() 

def triangle(): 
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    # Get and draw three vertices of triangle 
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # Use Polygon object to draw the triangle 
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("blue")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # Wait for another click to exit
    message.setText("Click anywhere to quit")
    win.getMouse()

triangle() 

def fourth(): 
    win = GraphWin("Click and Type", 400, 400)
    for i in range(10):
        pt = win.getMouse()
        key = win.getKey()
        label = Text(pt, key)
        label.draw(win)

fourth()

def ctof(): 
    win = GraphWin("Celsius Converter", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    # Draw the interface
    Text(Point(1,3), "  Celsius Temperature:").draw(win)
    Text(Point(1,1), " Fahrenheit Temperature:").draw(win)
    inputText = Entry(Point(2.25, 3), 5)
    inputText.setText("0.0")
    inputText.draw(win)
    outputText = Text(Point(2.25,1),"")
    outputText.draw(win)
    button = Text(Point(1.5,2.0),"Convert It")
    button.draw(win)
    Rectangle(Point(1,1.5), Point(2, 2.5)).draw(win)

    # wait for a mouse click 
    win.getMouse()

    # convert input
    celsius = float(inputText.getText())
    fahrenheit = 9.0/5.0 * celsius + 32 

    # display output and change button 
    outputText.setText(round(fahrenheit, 2))
    button.setText("Quit")

    # wait for click and then quit 
    win.getMouse()
    win.close()

ctof()