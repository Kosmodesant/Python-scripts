from pathlib import Path

filename = r"filepath\file.csv"
bkp_filename = filename + ".bkp"
Path(filename).rename(bkp_filename)
fn_in = Path(bkp_filename)
fn_out = Path(filename)
N = 100 # numbers of lines (from 1 to 100) to keep

with open(fn_in) as fin, open(fn_out, "w") as fout:
    for i, line in enumerate(fin):
        if i == N:
            break
        fout.write(line)
