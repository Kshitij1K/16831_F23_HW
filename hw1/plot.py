import matplotlib.pyplot as plt

if __name__ == '__main__':
    size_of_layers = [
        10,
        20,
        30,
        40,
        50,
        60,
        70,
        80,
        90,
        100,
        110,
        120,
        130,
        140,
        150
    ]

    average_return = [
        182.4239349,
        408.1988831,
        327.388671,
        606.4108276,
        831.769165,
        944.0764771,
        915.4614868,
        725.2844238,
        851.3737183,
        1018.110657,
        891.4194946,
        970.8242188,
        565.677002,
        620.8210449,
        662.9210815
    ]

    standard_deviation = [
        56.75343704,
        235.8331451,
        175.1949158,
        319.973938,
        332.7864685,
        250.9167938,
        399.526825,
        284.3948364,
        305.9950256,
        191.7259674,
        287.5805054,
        325.8865967,
        222.6263733,
        347.928009,
        285.4765015
    ]

    # Also connect all the points with a line
    plt.plot(size_of_layers, average_return)
    
    plt.errorbar(size_of_layers, average_return, standard_deviation, linestyle='None', marker='^')

    # Increase the size of these labels

    plt.xlabel('Size of Hidden Layers', fontsize=35)
    plt.ylabel('Average Return', fontsize=25)
    plt.title('Average Return vs. Size of Layers', fontsize=25)
    plt.show()
