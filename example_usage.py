from client import RLEDeltaCoder

def main():
    data = [0, 0, 0, 0, 1, 1, 2, 2, 2, 0, 0]
    rle = RLEDeltaCoder.rle_encode(data)
    print("RLE Runs:", rle)
    print("Recovered:", RLEDeltaCoder.rle_decode(rle) == data)

    timestamps = [1000, 1002, 1005, 1004, 1010]
    zz = RLEDeltaCoder.delta_zigzag_encode(timestamps)
    print("ZigZag Delta:", zz)
    print("Recovered TS:", RLEDeltaCoder.delta_zigzag_decode(zz) == timestamps)

if __name__ == "__main__":
    main()
