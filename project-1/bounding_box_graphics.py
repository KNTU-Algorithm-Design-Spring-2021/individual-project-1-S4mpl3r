from matplotlib import pyplot as plt


def drawPoints(X, Y, minX, maxX, minY, maxY):

    plt.scatter(X, Y)
    rectX = [minX, minX, maxX, maxX, minX]
    rectY = [minY, maxY, maxY, minY, minY]
    plt.grid(True, which='both')
    plt.plot(rectX, rectY, 'r')
    x = X.copy() + [X[0]]
    y = Y.copy() + [Y[0]]
    plt.plot(x, y, 'y')
    plt.show()


def findMinMax(i, j, arr):

    if i == j:
        return (arr[i], arr[i])

    elif j == i + 1:
        if arr[i] > arr[j]:
            return (arr[j], arr[i])
        else:
            return (arr[i], arr[j])

    else:
        mid = (i + j)//2
        min1, max1 = findMinMax(i, mid, arr)
        min2, max2 = findMinMax(mid + 1, j, arr)

        return(min(min1, min2), max(max1, max2))


def main():
    n = int(input())
    x_coordinates = []
    y_coordinates = []
    for i in range(n):
        x, y = input().split(' ')
        x_coordinates.append(int(x))
        y_coordinates.append(int(y))

    minimumX, maximumX = findMinMax(0, n-1, x_coordinates)
    minimumY, maximumY = findMinMax(0, n-1, y_coordinates)

    print(f"Left Bottom: {(minimumX, minimumY)}")
    print(f"Left Top: {(minimumX, maximumY)}")
    print(f"Right Bottom: {(maximumX, minimumY)}")
    print(f"Rifht Top: {(maximumX, maximumY)}")

    drawPoints(x_coordinates, y_coordinates,
               minimumX, maximumX, minimumY, maximumY)


if __name__ == "__main__":
    main()
