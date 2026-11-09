# AHAP Simulation Mission Report

**Run ID:** `Case_1E_AHAP_Fault_Snag`  
**Case 1E:** AHAP, T3 -> 10 % + 30 N tether snag [hero]  
**Duration:** 240.04 s  

## Barrier envelope (min_i(k_b,i(t) - |e1_i(t)|), t > 20 s)
* **Minimum margin observed:** `+0.0870` (stayed INSIDE the envelope the entire run)
* **Envelope relaxation active:** 0.00 % of ticks

## Faults
* **Injected:** 2:0.1 at t = 60 s
* **FDI mode:** declared

## Actuators
| Actuator | Position | Max thrust | Mean thrust | Declared health (end) |
| :--- | :--- | :--- | :--- | :--- |
| Thruster 1 | Bow Starboard Horizontal | 10.89 N | 1.54 N | 1.00 |
| Thruster 2 | Bow Port Horizontal | 16.08 N | 1.76 N | 1.00 |
| Thruster 3 | Aft Starboard Horizontal | 3.25 N | 0.41 N | 0.10 |
| Thruster 4 | Aft Port Horizontal | 21.85 N | 1.29 N | 1.00 |
| Thruster 5 | Starboard Vertical | 14.60 N | 1.73 N | 1.00 |
| Thruster 6 | Port Vertical | 13.21 N | 1.74 N | 1.00 |

## Tracking (against the true pose)
| Metric | Value |
| :--- | :--- |
| MAE 3D [m] | 0.0312 |
| RMS 3D [m] | 0.0494 |
| max 3D [m] | 0.328 |
| MAE after fault [m] | 0.0337 |
| peak 30 s after fault [m] | 0.059 |
| yaw MAE [deg] | 0.57 |
| max roll/pitch [deg] | 40.0 |
| min barrier margin [m|rad] | +0.087 |
| violations | 0 |
| allocation constrained [%] | 0.00 |
| envelope relaxed [%] | 0.00 |
| mean |thrust| [N] | 1.41 |
| allocation time [ms] | 0.020 |

Max depth 8.046 m, mean 8.001 m. ||W_hat|| at the end 0.000.
