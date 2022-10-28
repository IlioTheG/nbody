import subprocess
import timeit

def run(filename, n) -> None:
    subprocess.run("python" + " " + filename + " " + str(n), stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
results = []
fn = 'report.csv'
f = open(fn, 'w')
f.write('Iterations;Time(sec)\n')
for i in [5000, 500000, 5000000, 50000000]:
    exectimes = timeit.timeit(lambda: run('nbody_bench.py', i), number=1)
    results.append(exectimes)
    f.write('{};{}\n'.format(i, round(exectimes, 3)))
    print(f"'nbody_bench.py' {i} {exectimes}")
f.close()