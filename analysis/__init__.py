#!/usr/bin/env python
# coding: utf-8

# Analysis of SPI traces in CSV format:
# Time [s],Packet ID,MOSI,MISO
# 0.000094800000000,0,0xA0AAD74A9864DC05,0xFFFFFFFFFFFFFFFF
# 0.003074920000000,1,0xA0AAD74A9864DC05,0xFFFFFFFFFFFFFFFF
# 0.006054440000000,2,0xA0AAD74A9864DC05,0xFFFFFFFFFFFFFFFF
# 0.009034400000000,3,0xA0AAD74A9864DC05,0xFFFFFFFFFFFFFFFF
# 0.012013920000000,4,0xA0AAD74A9864DC05,0xFFFFFFFFFFFFFFFF
# 0.014993600000000,5,0xA0AAD74A9864DC05,0xFFFFFFFFFFFFFFFF
# 0.017975000000000,6,0xA0AAD74A9864DC05,0xFFFFFFFFFFFFFFFF
# 0.020956280000000,7,0xA0AAD74A9864DC05,0xFFFFFFFFFFFFFFFF
# 0.023937600000000,8,0xA0AAD74A9864DC05,0xFFFFFFFFFFFFFFFF


def diff(a, b):
    output = ""

    for i, j in zip(a, b):
        if i != j:
            output += "v"
        else:
            output += " "

    return output


def filter_trace(filename):
    data = []
    with open(filename, "r") as fh:
        data = fh.readlines()[1:]

    mosi = [l.split(",")[2] for l in data]
    # miso = [l.split(",")[3] for l in data]

    return mosi


def analysis(data, transfer_length):
    last = None
    analyzed = []

    for line in data:
        current = bin(int(line, 16))[2:].zfill(transfer_length)    # get rid off of '0b' prefix and padd with "0"s

        if last:
            differ = diff(last, current)
            if "v" in differ:
                analyzed.append(differ)

        analyzed.append(current)

        last = current

    with open("analysis.txt", "wb") as fh:
        for l in analyzed:
            fh.write(l)
            fh.write("\n")
    # return analyzed


if __name__ == '__main__':
    # data = filter_trace("../00_power_on.csv")
    # analysis(data)

    data = filter_trace("../01_binding.csv")
    analysis(data, 64)

