[2026-05-27] \
Originally thought to use set to trace the unique character, then move l = r when duplciate is found.

This won't work because if str[l] != str[r], then the position will be wrong (e.g. <axb>xab -> axb<x>ab, which l should be ax<bx>ab)

Ask Ai for tips but he gives me the answer straight away