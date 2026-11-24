# Case Study 35: Text Compression Using Character Runs (RLE)
# Syllabus: Strings, Loops, Conditionals, Operators, Lists

test_strings = [
    "AAAAABBBCCDAA",
    "ABCDEF",
    "WWWWWWWWWWWWBWWWWWWWWWWWWBBB",
    "AABB"
]

print("=== RUN-LENGTH ENCODING (RLE) ANALYSIS ===")

for text in test_strings:
    if len(text) == 0:
        print("Empty string -> Skipped")
        continue

    encoded = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded += text[i - 1] + str(count)
            count = 1

    encoded += text[-1] + str(count)

    orig_len = len(text)
    enc_len = len(encoded)

    print(f"\nOriginal : {text} (Length: {orig_len})")
    print(f"Encoded  : {encoded} (Length: {enc_len})")

    if enc_len < orig_len:
        saved_pct = ((orig_len - enc_len) / orig_len) * 100.0
        print(f"Result   : BENEFICIAL (Saved {orig_len - enc_len} chars, {saved_pct:.1f}% reduction)")
    else:
        print(f"Result   : NOT BENEFICIAL (Use original '{text}')")
