#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import os
from typing import List, io


def chunk_file(chunk_number):
    return "chunk_%s.txt" % chunk_number


def save_chunk(chunk, chunk_number):
    chunk.sort()
    with open(chunk_file(chunk_number), "w") as out:
        out.writelines(chunk)


def merge_chunks(chunk_count, output):
    files: List[io] = [None] * chunk_count
    strings: List[str] = [None] * chunk_count

    for i in range(chunk_count):
        if os.path.exists(chunk_file(i)):
            files[i] = open(chunk_file(i), "r")
            strings[i] = files[i].readline()
        else:
            chunk_count = i
            strings[i] = ""
            break

    with open(output, "w") as out:
        while True:
            min = None
            min_index = -1
            for i in range(chunk_count):
                if strings[i] and (min is None or min > strings[i]):
                    min = strings[i]
                    min_index = i
            if min is None:
                break
            out.write(min)
            strings[min_index] = files[min_index].readline()
    for i in range(chunk_count):
        if files[i]:
            os.unlink(chunk_file(i))
            files[i].close()


def sort(chunk_count, chunk_size, input, output):
    chunk_number = 0
    with open(input, "r") as original:
        chunk = []
        for s in original:
            chunk.append(s)
            if len(chunk) >= chunk_size:
                save_chunk(chunk, chunk_number)
                chunk_number += 1
                chunk = []
            if chunk_number >= chunk_count:
                merge_chunks(chunk_count, output)
                os.rename(output, chunk_file(0))
                chunk_number = 1

    save_chunk(chunk, chunk_number)
    merge_chunks(chunk_count, output)
    for i in range(chunk_count):
        if os.path.exists(chunk_file(i)):
            os.unlink(chunk_file(i))


parser = argparse.ArgumentParser()
parser.add_argument("-c", "--count", help="Chunks count", type=int, default=10)
parser.add_argument("-s", "--chunk-size", help="Chunk size (lines count)", type=int, default=1000)
parser.add_argument("-i", "--input", help="Input filename", default="in.txt")
parser.add_argument("-o", "--output", help="Output filename", default="out.txt")
args = parser.parse_args()
sort(args.count, args.chunk_size, args.input, args.output)
