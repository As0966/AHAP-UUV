#!/usr/bin/env python3
"""prove_t3_share.py -- reproduces the Figure 5 statement of the ECC paper from the telemetry logs:
"once the fault is reported at 63 s, the allocation cuts the share of T3 in the horizontal thrust from 14% to 7%
 and shifts the load to T1, T2 and T5."

Definition: share of T3 = RMS(f3) / (RMS(f1)+RMS(f2)+RMS(f3)+RMS(f4)), commanded thruster forces (thrustN_n columns),
before the fault (20-60 s) and after the fault report (63-240 s), case 1E (AHAP), every realisation found.

  python3 prove_t3_share.py <dir with telemetry_log_Case_1E_AHAP_Fault_Snag__s*.csv>
"""
import glob, os, sys
import numpy as np, pandas as pd

d = sys.argv[1] if len(sys.argv) > 1 else '.'
files = sorted(glob.glob(os.path.join(d, 'telemetry_log_Case_1E_AHAP_Fault_Snag__s*.csv')))
if not files:
    sys.exit(f'no case-1E telemetry in {d}')
rms = lambda s: float(np.sqrt(np.mean(np.square(np.asarray(s, float)))))
W = {'before fault (20-60 s)': (20, 60), 'after report (63-240 s)': (63, 240)}
share = {k: [] for k in W}; load = {k: [] for k in W}
print(f'{"realisation":28s}' + ''.join(f'{k:>26s}' for k in W))
for fn in files:
    t = pd.read_csv(fn); row = []
    for k, (a, b) in W.items():
        m = (t.elapsed_time >= a) & (t.elapsed_time < b)
        f = [rms(t[f'thrust{j}_n'][m]) for j in range(1, 7)]
        share[k].append(100 * f[2] / sum(f[:4])); load[k].append(f); row.append(f'{share[k][-1]:25.1f}%')
    print(f'{os.path.basename(fn)[-8:-4]:28s}' + ''.join(row))
print(f'{"mean":28s}' + ''.join(f'{np.mean(share[k]):25.1f}%' for k in W))
print('\nRMS commanded force per thruster [N], mean over realisations:')
for k in W:
    print(f'  {k:24s}', '  '.join(f'T{j+1} {np.mean([l[j] for l in load[k]]):.2f}' for j in range(6)))
