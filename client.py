"""Run-Length Encoding (RLE) & Delta ZigZag Serialization.
100% Python Standard Library.
"""

class RLEDeltaCoder:
    """RLE and Delta-ZigZag differential coder for dense integer arrays."""

    @staticmethod
    def rle_encode(data: list) -> list:
        if not data:
            return []
        runs = []
        prev = data[0]
        cnt = 1
        for val in data[1:]:
            if val == prev:
                cnt += 1
            else:
                runs.append((prev, cnt))
                prev = val
                cnt = 1
        runs.append((prev, cnt))
        return runs

    @staticmethod
    def rle_decode(runs: list) -> list:
        out = []
        for val, cnt in runs:
            out.extend([val] * cnt)
        return out

    @staticmethod
    def delta_zigzag_encode(integers: list) -> list:
        if not integers:
            return []
        out = []
        prev = 0
        for x in integers:
            diff = x - prev
            zz = (diff << 1) if diff >= 0 else (-diff << 1) - 1
            out.append(zz)
            prev = x
        return out

    @staticmethod
    def delta_zigzag_decode(encoded: list) -> list:
        out = []
        prev = 0
        for zz in encoded:
            diff = (zz >> 1) if (zz % 2 == 0) else -((zz + 1) >> 1)
            orig = prev + diff
            out.append(orig)
            prev = orig
        return out
