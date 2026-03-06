# =============================================================================
# STEP-BY-STEP COMMENTARY VERSION
# =============================================================================
# This file is the same runnable program as the original GUI explorer,
# but with "STEP 1, STEP 2, ..." comments added to explain what each section does.
#
# How to run:
#   python3 model_g_particle_1d_gui__1d_step.py
# =============================================================================

#!/usr/bin/env python3
"""
Model G Particle 1D — GUI Explorer (SAFE-ish)
- Built from Brendan's "model_g_particle_1d_safe__1d.py" and adapted into a GUI parameter explorer.
- Purpose: help you *search* for charged-polarity soliton states (proton-like vs electron-like polarity) by
  adjusting Model G parameters and seed forcing χ(x,t), then running quick simulations and computing
  diagnostics.

- Written by Brendan Darrer aided by ChatGPT 5.2 date: 5th March 2026 21:39 GMT
- ("1d" version updated 6th March 2026 06:03 GMT)
- ("1d_step" version updated 6th March 2026 06:30 GMT)
- adapted from: @ https://github.com/blue-science/subquantum_kinetics/blob/master/particle.nb and
"model_g_particle_1d_safe__1d.py"
- with ChatGPT 5.2 writing it and Brendan guiding it to produce a clean code.

Papers used for this simulation GUI explorer:

[1] International Journal of General Systems, Vol. 42, No. 5, May 2013, 1–24, Stationary Dissipative 
Solitons of Model G, Matthew Pulver and Paul A. LaViolette, Blue Science, Los Angeles, California USA, 
Starburst Foundation, Schenectady, New York USA, (Received 7 July 2012; final version received 
12 February 2013), https://starburstfound.org/downloads/physics/model_g.pdf , As (model_g (1)) below.

[2] Darrer, Brendan & Coven, Justin & LaViolette, Paul. (2022). Subquantum kinetics: simulating 
subatomic particles in Model G with fluid dynamics. 
https://www.researchgate.net/publication/362456406_Subquantum_kinetics_simulating_subatomic_particles_in_Model_G_with_fluid_dynamics , 
As (SQK_ModelG_with_fluid_dynamics_…) below.

Tested for: Ubuntu 24.04.3 LTS on i7-4790 (Optiplex 7020/9020), Python 3.10+

Key ideas (per SQK Model G):
- "Charge polarity" proxy: sign of pY at the core (x≈0) (and pX tends to opposite sign).
  * proton-like polarity: pY(core) > 0
  * electron-like polarity: pY(core) < 0
- You can flip χ sign to bias polarity: in the classic soliton example, χ is negative Gaussian in X-equation.
  This GUI lets you flip sign + sweep parameters.

Deps:
    pip3 install numpy scipy matplotlib

Optional (video export):
    pip3 install imageio imageio[ffmpeg]

Run:
    python3 model_g_particle_1d_gui__1d_step.py
    
Remember for Brendan's computer:
python3 -m venv tf-env
source tf-env/bin/activate
............................................................
Can you help me find new subatomic particles in Model G of SQK, using the starburst simulator here: 
@ https://starburstfound.org/computer-simulation-of-model-g/ . This simulator is set up initially 
with parameters to model a neutral like particle similar to a neutron (Matt Pulver who found the 
neutron parameters, said it was like looking for a needle in a hey stack!). Can you help me use it 
model charged particles such as a proton or an electron in Model G (i.e. guiding me to input the 
correct parameters of these subatomic particles)? I attach papers here that may help guide you with this.
Thought for 47s

ChatGPT 5.2:

Yes — I can help you use the Starburst Model-G simulator systematically to hunt for charged soliton 
“particle” states (proton-like, electron-like), starting from Matt’s neutron-like parameter set and 
then doing controlled parameter continuation + diagnostics.

Below is a practical workflow you can apply in the web simulator UI even if it only exposes the 
dimensional inputs (A, B, k’s, D’s, seed χ), using the mapping and physical interpretation given 
in the two papers you attached. 

model_g (1)

SQK_ModelG_with_fluid_dynamics_…

1) What “charge” means in Model G (what to look for)

Pulver & LaViolette explicitly identify:

ϕG ↔ gravitational potential

ϕX and ϕY ↔ electric potential variables (reciprocal relation)

Positive charge ↔ positive ϕY (and negative ϕX)

Negative charge ↔ negative ϕY (and positive ϕX) 

model_g (1)

So, in the simulator, a “charged particle” should show a core polarity consistent with:

proton-like: ϕY core > 0 (and ϕX core < 0)

electron-like: ϕY core < 0 (and ϕX core > 0)

And you’ll want a stable localized soliton (Gaussian-ish core + oscillatory Turing tail) like in 
their figures. 

model_g (1)

2) The key knobs you actually have in the simulator
A. The “official” dimensionless knobs (paper form)

Model G’s nondimensional form uses:
dx, dy, a, b, g, p, q, s, u, w 

model_g (1)

And the 2013 paper gives one working soliton set (their “particle” example):
dx=1, dy=12, a=14, b=29, g=0.1, p=1, q=1, s=0, u=0, w=0 

model_g (1)

B. The simulator-style dimensional knobs (what your TF2/Starburst setups usually expose)

Your 2022 “fluid dynamics” note shows a typical parameter block of the kind your tooling uses, e.g.:

A, B

k2, k−2, k5 (and in that particular configuration, several reverse terms set to 0)

D_G, D_X, D_Y

plus the seed fluctuation χ (amplitude/sign/width/time window) 

SQK_ModelG_with_fluid_dynamics_…

C. Mapping between them (so we can reason cleanly)

Pulver & LaViolette give the mapping (core pieces): 

model_g (1)

dx = D_X / D_G

dy = D_Y / D_G

g = k−2 / (k−2 + k5)

p = k2 / (k−2 + k5)

b = (k3 B)/(k−2 + k5) (if k3 is implicitly 1 in the simulator, then b ∝ B)

a ∝ A (with additional scaling constants)

This is powerful because it tells you what to vary in the UI to move “in the same direction” as 
the dimensionless theory.

3) The single most important “charged-particle” trick: flip the seed polarity

In the 2013 paper, the particle is nucleated by adding a negative Gaussian seed χ into the 
X equation, i.e. χ is negative (their χ = −exp(…)). 

model_g (1)


That drives ϕX negative at the core, which corresponds to positive ϕY polarity (positive charge polarity). 

model_g (1)

Practical implication in the simulator

To search proton-like / positive polarity states: use the usual negative χ in X (the “neutron-like” 
setup is already seeded this way in many configs).

To search electron-like / negative polarity states: try the opposite sign seed, i.e. positive χ in X 
(or equivalently seed negative in Y if your UI supports choosing which field gets χ).

Caveat (important): The 2013 paper notes that in a globally subcritical “vacuum-like” state, negative 
charge polarity fluctuations may fail to nucleate a particle (their matter/antimatter polarity bias point). 

model_g (1)


In practice, that means: if “electron-like” won’t nucleate just by flipping χ, you likely must also 
shift the background closer to (or into) the supercritical regime (next section).

4) How to push the background into a regime where “electron-like” might exist

Even without seeing the exact Starburst UI, the general strategy is:

Step 1 — keep the neutron-like soliton stable (baseline)

Start from the known “needle in haystack” baseline and confirm you get:

stable soliton

correct polarity (ϕY core positive, ϕX core negative)

good tail (not dissolving)

Step 2 — flip χ sign (electron attempt #1)

Only change: χ amplitude sign.

If it fails (no nucleation / blow-up / dissolves), revert χ and proceed to Step 3.

Step 3 — adjust g = k−2/(k−2+k5) by varying k−2 or k5

From your TF2-style config, you have k−2 and k5 available. 

SQK_ModelG_with_fluid_dynamics_…

Increasing k−2 (holding k5) increases g

Increasing k5 (holding k−2) decreases g

This matters because G↔X coupling is central to the bifurcation behavior (and thus whether a given 
polarity can self-stabilize). 

model_g (1)

Practical sweep:
Make small incremental changes, e.g.

k−2: 0.10 → 0.11 → 0.12 … (or)

k5: 0.90 → 0.88 → 0.86 …

Each time, retry the positive χ in X electron-seed attempt.

Step 4 — adjust diffusion ratio dy = D_Y/D_G

The 2013 soliton example has dy substantially larger than dx (dy=12, dx=1). 

model_g (1)


Your TF2-style example uses D_Y=1.95 with D_G=1, i.e. dy≈1.95, which is a different regime (it can 
still work, but it changes the pattern selection). 

SQK_ModelG_with_fluid_dynamics_…

So, if you’re having trouble getting alternative polarity states, do a controlled sweep of:

D_Y upward (keeping D_G fixed), e.g. 1.95 → 3 → 5 → 8 → 12
while maintaining stability (avoid instantly chaotic patterns).

5) How to tell “proton-like” vs “neutron-like” vs “electron-like” in the output

Because these are toy-solutions in a dimensionless RD system, you need a consistent operational 
definition inside the simulator:

A. Core polarity test (fast)

Read off the sign at r≈0:

proton-like: ϕY(0) > 0, ϕX(0) < 0

electron-like: ϕY(0) < 0, ϕX(0) > 0 

model_g (1)

B. “Net charge proxy” (better than eyeballing)

If your simulator shows integrals or lets you export profiles, compute:

Qproxy = ∫ ϕY(r) dV (or in 2D, ∫ϕY r dr; in 3D, ∫ϕY r² dr)

The 2013 paper explicitly defines “core integrals” and “full integrals” of the potentials as diagnostics. 

model_g (1)


Even if their “particle example” wasn’t tuned to enforce zero net charge in the naive integral sense, 
this gives you a repeatable way to rank candidates.

C. Size / wavelength targeting (for “electron-like” vs nucleon-like)

They emphasize that the Turing tail wavelength λ0 is a key “particle identifier” and is stable 
(boundary-independent). 

model_g (1)


So: if you eventually want “electron vs proton” separation, you will likely need to find parameter 
sets that generate different λ0 (then map λ0 to a target Compton wavelength via the physical scaling).

6) A concrete parameter-search recipe you can run today in the Starburst simulator

Here’s a disciplined “no-haystack panic” approach:

Lock the baseline (your neutron-like preset)

Save/export it as “BASE”.

Electron attempt ladder (minimal changes first)

E1: flip χ sign only (X-seed).

E2: E1 + increase seed magnitude 1.5×, 2×, 3× (keep widths same).

E3: E2 + adjust g via k−2 or k5 in ±5% steps.

E4: E3 + raise dy by increasing D_Y gradually.

Proton-like search (often easier)

Start from BASE (χ negative in X).

Sweep B (therefore b) upward/downward in small steps (±2–5%).

Goal: keep stable soliton but change Qproxy appreciably while maintaining positive core polarity.

Keep a notebook table

(A, B, k2, k−2, k5, D_G, D_X, D_Y, χ_amp, χ_width, χ_time)

outcome: stable? polarity? λ0? Qproxy?

This is basically “continuation + diagnostics,” which is how Matt likely found the neutron-like set 
in the first place — just made less painful.

7) What I need from you to give “type-in-these-values” guidance (without more back-and-forth)

If you paste (or screenshot) the Starburst simulator’s actual input panel showing:

the exact parameter names it exposes (A/B/k’s/D’s/seed fields, etc.)

and the current neutron-like preset values,

…then I can translate the search plan above into specific candidate parameter sets in the simulator’s 
exact units/fields (e.g., “set k5 to 0.86; set k−2 to 0.12; flip χ sign; increase D_Y to 5,” etc.), and 
lay them out as “Trial 1… Trial 2… Trial 3…”

For now, the guidance above is the correct physics-to-UI control logic based directly on the attached 
papers’ definitions of the variables, polarity, and parameter mappings.
............................................................
"""

# STEP 1 — Import libraries
# We load: numpy/scipy for math + solving, matplotlib for plotting, tkinter for GUI,
# threading/queue so the GUI stays responsive during long simulations.

import os
import time
import math
import threading
import queue
from dataclasses import dataclass, asdict

import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from scipy.integrate import solve_ivp

try:
    import imageio.v2 as imageio
    HAVE_IMAGEIO = True
except Exception:
    HAVE_IMAGEIO = False

import tkinter as tk
from tkinter import ttk, messagebox, filedialog


# --------------------- Model / numerics ---------------------

# STEP 2 — Define parameter containers (dataclasses)
# These are tidy bundles of parameters that appear in the GUI entry boxes.
# - ModelParams: dimensionless Model G coefficients
# - SeedParams: χ(x,t) forcing seed settings (polarity sign, amplitude, widths)
# - GridParams: spatial grid + solver controls


@dataclass
class ModelParams:
    # Dimensionless params (eqs17-style)
    a: float = 14.0
    b: float = 29.0
    dx: float = 1.0
    dy: float = 12.0
    p: float = 1.0
    q: float = 1.0
    g: float = 0.1
    s: float = 0.0
    u: float = 0.0
    v: float = 0.0   # advection-like term (0 in your safe file)
    w: float = 0.0

@dataclass
class SeedParams:
    # χ(x,t) = sign * amp * exp(-(x/sx)^2/2) * exp(-((t-Tseed)/st)^2/2)
    sign: int = -1          # -1 tends to proton-like polarity in classic seed
    amp: float = 1.0
    sx: float = 1.0
    st: float = 3.0
    Tseed: float = 10.0
    nseeds: int = 1
    sep: float = 3.303/2    # separation for 2-seed case (matches your file)

@dataclass
class GridParams:
    L: float = 20.0
    nx: int = 401
    Tfinal: float = 30.0
    max_step: float = 0.05
    rtol: float = 1e-6
    atol: float = 1e-6
    dense: bool = True

# STEP 3 — Seed helper functions
# χ(x,t) is built as a product of a spatial Gaussian and a time Gaussian.
# These helpers build those Gaussians and combine them for 1/2/3 seed sites.



def _bell(s: float, x: np.ndarray) -> np.ndarray:
    s = float(s)
    if s <= 0:
        return np.zeros_like(x)
    return np.exp(- (x/s)**2 / 2.0)


def make_chi(xgrid: np.ndarray, t: float, sp: SeedParams) -> np.ndarray:
    env_t = _bell(sp.st, t - sp.Tseed)
    if sp.nseeds == 1:
        env_x = _bell(sp.sx, xgrid)
    elif sp.nseeds == 2:
        env_x = _bell(sp.sx, xgrid + sp.sep) + _bell(sp.sx, xgrid - sp.sep)
    else:
        # 3-seed: left, center, right
        env_x = _bell(sp.sx, xgrid + 3.314) + _bell(sp.sx, xgrid) + _bell(sp.sx, xgrid - 3.314)
    return float(sp.sign) * float(sp.amp) * env_x * env_t

# STEP 4 — Core physics + numerics engine (ModelG1D)
# This class turns the 1D PDE system into something SciPy can integrate.
# It:
#   1) builds an x-grid
#   2) computes the homogeneous steady state (G0, X0, Y0)
#   3) defines finite-difference derivatives (grad, laplacian)
#   4) defines the RHS function f(t,y) that solve_ivp needs
#   5) runs the solver and computes diagnostics



class ModelG1D:
    # STEP 4.1 — Initialise the model
    # Build the 1D x-grid and compute the steady background values (G0, X0, Y0).
    # The evolving variables pG, pX, pY are perturbations around that background.

    def __init__(self, mp: ModelParams, gp: GridParams, sp: SeedParams):
        self.mp = mp
        self.gp = gp
        self.sp = sp

        self.x = np.linspace(-gp.L/2, gp.L/2, int(gp.nx))
        if len(self.x) < 5:
            raise ValueError("nx too small; use >= 101")
        self.dx_space = self.x[1] - self.x[0]

        # Homogeneous steady state (G0, X0, Y0)
        a = mp.a; b = mp.b; p = mp.p; q = mp.q; g = mp.g; s = mp.s; u = mp.u; w = mp.w
        denom = (q - g*p)
        if abs(denom) < 1e-12:
            raise ValueError("Invalid params: q - g*p too close to 0")
        self.G0 = (a + g*w) / denom
        self.X0 = (p*a + q*w) / denom
        self.Y0 = ((s*self.X0**2 + b) * self.X0 / (self.X0**2 + u)) if abs(self.X0**2 + u) > 1e-12 else 0.0
    # STEP 4.2 — Laplacian (2nd derivative)
    # Approximates u_xx using central differences.


    def laplacian(self, u: np.ndarray) -> np.ndarray:
        dudxx = np.zeros_like(u)
        dx2 = self.dx_space**2
        dudxx[1:-1] = (u[2:] - 2*u[1:-1] + u[:-2]) / dx2
        return dudxx
    # STEP 4.3 — Gradient (1st derivative)
    # Approximates u_x using central differences.


    def grad(self, u: np.ndarray) -> np.ndarray:
        dudx = np.zeros_like(u)
        dudx[1:-1] = (u[2:] - u[:-2]) / (2*self.dx_space)
        return dudx
    # STEP 4.4 — Pack/unpack the state for SciPy


    def pack(self, pG, pX, pY):
        return np.concatenate([pG, pX, pY])

    def unpack(self, y):
        nx = len(self.x)
        return y[:nx], y[nx:2*nx], y[2*nx:3*nx]
    # STEP 4.5 — RHS dy/dt = f(t,y)
    # Implements the discretised Model G equations + seed forcing χ.


    def rhs(self, t: float, y_flat: np.ndarray) -> np.ndarray:
        mp = self.mp
        pG, pX, pY = self.unpack(y_flat)

        lapG = self.laplacian(pG)
        lapX = self.laplacian(pX)
        lapY = self.laplacian(pY)

        dGdx = self.grad(pG)
        dXdx = self.grad(pX)
        dYdx = self.grad(pY)

        chi_vec = make_chi(self.x, t, self.sp)

        Xtot = pX + self.X0
        Ytot = pY + self.Y0

        nonlinear_s = mp.s * (Xtot**3 - self.X0**3)
        nonlinear_xy = (Xtot**2 * Ytot - self.X0**2 * self.Y0)

        dpGdt = lapG - mp.q * pG + mp.g * pX - mp.v * dGdx
        dpXdt = mp.dx * lapX - mp.v * dXdx + mp.p * pG - (1.0 + mp.b) * pX + mp.u * pY - nonlinear_s + nonlinear_xy + chi_vec
        dpYdt = mp.dy * lapY - mp.v * dYdx + mp.b * pX - mp.u * pY + (-nonlinear_xy + nonlinear_s)

        # Dirichlet boundaries (keep edges at 0)
        dpGdt[0] = dpGdt[-1] = 0.0
        dpXdt[0] = dpXdt[-1] = 0.0
        dpYdt[0] = dpYdt[-1] = 0.0

        return self.pack(dpGdt, dpXdt, dpYdt)
    # STEP 4.6 — Run the solver (solve_ivp / BDF)


    def run(self, y0: np.ndarray | None = None, t_eval: np.ndarray | None = None):
        nx = len(self.x)
        if y0 is None:
            y0 = np.zeros(3*nx, dtype=float)

        if t_eval is None:
            # modest default: 200 frames
            t_eval = np.linspace(0.0, self.gp.Tfinal, 200)

        sol = solve_ivp(
            fun=self.rhs,
            t_span=(0.0, float(self.gp.Tfinal)),
            y0=y0,
            method="BDF",
            t_eval=t_eval,
            max_step=float(self.gp.max_step),
            rtol=float(self.gp.rtol),
            atol=float(self.gp.atol),
            dense_output=bool(self.gp.dense),
        )
        return sol
    # STEP 4.7 — Diagnostics (polarity, charge proxy, size proxy)


    def diagnostics(self, y_flat: np.ndarray) -> dict:
        pG, pX, pY = self.unpack(y_flat)
        # core index (closest to x=0)
        i0 = int(np.argmin(np.abs(self.x)))
        core = {
            "pY_core": float(pY[i0]),
            "pX_core": float(pX[i0]),
            "pG_core": float(pG[i0]),
        }

        # "charge proxy": integral of pY over space (simple 1D proxy)
        Qproxy = float(np.trapezoid(pY, self.x))

        # size proxy: full-width half-max of |pY|
        absY = np.abs(pY)
        peak = float(absY.max())
        if peak > 1e-12:
            half = 0.5 * peak
            idx = np.where(absY >= half)[0]
            if len(idx) >= 2:
                fwhm = float(self.x[idx[-1]] - self.x[idx[0]])
            else:
                fwhm = 0.0
        else:
            fwhm = 0.0

        # polarity label
        if core["pY_core"] > 0:
            pol = "positive-polarity (proton-like)"
        elif core["pY_core"] < 0:
            pol = "negative-polarity (electron-like)"
        else:
            pol = "neutral/zero"

        return {
            **core,
            "Qproxy_int_pYdx": Qproxy,
            "pY_peak_abs": peak,
            "pY_fwhm_abs": fwhm,
            "polarity_label": pol,
        }


# --------------------- GUI ---------------------

# STEP 5 — GUI application (Tkinter)
# The App class creates the window, tabs, buttons, plot, and diagnostics display.
# Key design choice: simulation runs in a worker thread so the GUI doesn’t freeze.


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Model G 1D Particle Explorer — Charged-State Search GUI")
        self.geometry("1200x720")

        self._worker_thread = None
        self._q = queue.Queue()

        # Default configs
        self.mp = ModelParams()
        self.sp = SeedParams()
        self.gp = GridParams()

        self._build_ui()
        self.after(100, self._poll_queue)

        # Matplotlib figure
        self.fig = plt.Figure(figsize=(7.2, 4.2), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title("pY (Y), pG (G), pX/10 (X scaled)")
        self.ax.set_xlabel("x")
        self.ax.grid(True)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        self._last_sol = None
        self._last_model = None
    # STEP 5.1 — Build UI widgets (tabs, entries, buttons, status)


    def _build_ui(self):
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        left = ttk.Frame(self, padding=10)
        left.grid(row=0, column=0, sticky="ns")
        left.columnconfigure(0, weight=1)

        self.plot_frame = ttk.Frame(self, padding=10)
        self.plot_frame.grid(row=0, column=1, sticky="nsew")
        self.plot_frame.rowconfigure(0, weight=1)
        self.plot_frame.columnconfigure(0, weight=1)

        # --- Parameter notebooks
        nb = ttk.Notebook(left)
        nb.grid(row=0, column=0, sticky="nsew")

        tab_model = ttk.Frame(nb, padding=8)
        tab_seed  = ttk.Frame(nb, padding=8)
        tab_grid  = ttk.Frame(nb, padding=8)
        tab_scan  = ttk.Frame(nb, padding=8)
        nb.add(tab_model, text="Model Params")
        nb.add(tab_seed,  text="Seed χ")
        nb.add(tab_grid,  text="Grid/Time")
        nb.add(tab_scan,  text="Scan")

        # --- Model Params entries
        self.model_vars = {}
        for r, (k, v) in enumerate(asdict(self.mp).items()):
            ttk.Label(tab_model, text=k).grid(row=r, column=0, sticky="w", pady=2)
            var = tk.StringVar(value=str(v))
            ent = ttk.Entry(tab_model, textvariable=var, width=16)
            ent.grid(row=r, column=1, sticky="e", pady=2)
            self.model_vars[k] = var

        # --- Seed params
        self.seed_vars = {}
        seed_fields = asdict(self.sp)
        for r, (k, v) in enumerate(seed_fields.items()):
            ttk.Label(tab_seed, text=k).grid(row=r, column=0, sticky="w", pady=2)
            var = tk.StringVar(value=str(v))
            ent = ttk.Entry(tab_seed, textvariable=var, width=16)
            ent.grid(row=r, column=1, sticky="e", pady=2)
            self.seed_vars[k] = var

        ttk.Button(tab_seed, text="Set proton-like seed (sign=-1)", command=self._set_proton_seed).grid(row=len(seed_fields)+1, column=0, columnspan=2, sticky="ew", pady=6)
        ttk.Button(tab_seed, text="Set electron-like seed (sign=+1)", command=self._set_electron_seed).grid(row=len(seed_fields)+2, column=0, columnspan=2, sticky="ew", pady=2)

        # --- Grid/time
        self.grid_vars = {}
        for r, (k, v) in enumerate(asdict(self.gp).items()):
            ttk.Label(tab_grid, text=k).grid(row=r, column=0, sticky="w", pady=2)
            var = tk.StringVar(value=str(v))
            ent = ttk.Entry(tab_grid, textvariable=var, width=16)
            ent.grid(row=r, column=1, sticky="e", pady=2)
            self.grid_vars[k] = var

        # --- Scan tab
        ttk.Label(tab_scan, text="Scan variable (one of: a b dx dy p q g s u v w amp sx st Tseed):").grid(row=0, column=0, sticky="w", pady=2)
        self.scan_var = tk.StringVar(value="dy")
        ttk.Entry(tab_scan, textvariable=self.scan_var, width=12).grid(row=0, column=1, sticky="e")

        ttk.Label(tab_scan, text="Start").grid(row=1, column=0, sticky="w", pady=2)
        self.scan_start = tk.StringVar(value="8")
        ttk.Entry(tab_scan, textvariable=self.scan_start, width=12).grid(row=1, column=1, sticky="e")

        ttk.Label(tab_scan, text="Stop").grid(row=2, column=0, sticky="w", pady=2)
        self.scan_stop = tk.StringVar(value="14")
        ttk.Entry(tab_scan, textvariable=self.scan_stop, width=12).grid(row=2, column=1, sticky="e")

        ttk.Label(tab_scan, text="Steps").grid(row=3, column=0, sticky="w", pady=2)
        self.scan_steps = tk.StringVar(value="7")
        ttk.Entry(tab_scan, textvariable=self.scan_steps, width=12).grid(row=3, column=1, sticky="e")

        self.scan_flip_seed = tk.BooleanVar(value=False)
        ttk.Checkbutton(tab_scan, text="Flip seed sign each trial (alt polarity)", variable=self.scan_flip_seed).grid(row=4, column=0, columnspan=2, sticky="w", pady=4)

        ttk.Label(tab_scan, text="Quick-run Tfinal override (blank = use Grid/Time):").grid(row=5, column=0, sticky="w", pady=2)
        self.scan_Tfinal = tk.StringVar(value="12")
        ttk.Entry(tab_scan, textvariable=self.scan_Tfinal, width=12).grid(row=5, column=1, sticky="e")

        ttk.Button(tab_scan, text="Run scan", command=self.on_scan).grid(row=6, column=0, columnspan=2, sticky="ew", pady=8)

        # --- Control buttons under notebook
        btns = ttk.Frame(left)
        btns.grid(row=1, column=0, sticky="ew", pady=10)
        btns.columnconfigure(0, weight=1)
        btns.columnconfigure(1, weight=1)

        ttk.Button(btns, text="Run (single)", command=self.on_run).grid(row=0, column=0, sticky="ew", padx=3)
        ttk.Button(btns, text="Stop", command=self.on_stop).grid(row=0, column=1, sticky="ew", padx=3)

        ttk.Button(btns, text="Save last run (NPZ)", command=self.on_save_npz).grid(row=1, column=0, sticky="ew", padx=3, pady=4)
        ttk.Button(btns, text="Export MP4 (optional)", command=self.on_export_mp4).grid(row=1, column=1, sticky="ew", padx=3, pady=4)

        # Diagnostics readout
        self.diag_box = tk.Text(left, height=12, width=45)
        self.diag_box.grid(row=2, column=0, sticky="ew")
        self.diag_box.insert("end", "Diagnostics will appear here after a run.\n")

        # Status bar
        self.status = tk.StringVar(value="Ready.")
        ttk.Label(left, textvariable=self.status, wraplength=340).grid(row=3, column=0, sticky="ew", pady=8)

    def _set_proton_seed(self):
        self.seed_vars["sign"].set("-1")

    def _set_electron_seed(self):
        self.seed_vars["sign"].set("+1")
    # STEP 5.2 — Parse entry values into floats/ints/bools


    def _parse(self):
        # Parse model params
        mp = ModelParams()
        for k, var in self.model_vars.items():
            try:
                setattr(mp, k, float(var.get()))
            except Exception:
                raise ValueError(f"Bad model param '{k}': {var.get()}")

        sp = SeedParams()
        for k, var in self.seed_vars.items():
            raw = var.get().strip()
            try:
                if k in ("sign", "nseeds"):
                    setattr(sp, k, int(float(raw)))
                else:
                    setattr(sp, k, float(raw))
            except Exception:
                raise ValueError(f"Bad seed param '{k}': {raw}")

        gp = GridParams()
        for k, var in self.grid_vars.items():
            raw = var.get().strip()
            try:
                if k in ("nx",):
                    setattr(gp, k, int(float(raw)))
                elif k in ("dense",):
                    setattr(gp, k, bool(str(raw).lower() in ("1", "true", "yes", "y")))
                else:
                    setattr(gp, k, float(raw))
            except Exception:
                raise ValueError(f"Bad grid param '{k}': {raw}")

        return mp, sp, gp
    # STEP 5.3 — Single run: launch worker thread, return results via Queue


    def on_run(self):
        if self._worker_thread and self._worker_thread.is_alive():
            messagebox.showinfo("Busy", "A run is already in progress.")
            return
        try:
            mp, sp, gp = self._parse()
        except Exception as e:
            messagebox.showerror("Parse error", str(e))
            return

        self.status.set("Running solver (single run)...")
        self.diag_box.delete("1.0", "end")
        self.diag_box.insert("end", "Running...\n")
        self._stop_flag = False

        def worker():
            try:
                model = ModelG1D(mp, gp, sp)
                t_eval = np.linspace(0.0, gp.Tfinal, 240)
                sol = model.run(t_eval=t_eval)
                if self._stop_flag:
                    self._q.put(("status", "Stopped."))
                    return
                self._q.put(("result", ("single", model, sol, mp, sp, gp)))
            except Exception as ex:
                self._q.put(("error", str(ex)))

        self._worker_thread = threading.Thread(target=worker, daemon=True)
        self._worker_thread.start()
    # STEP 5.4 — Scan: sweep one variable, run many short simulations


    def on_scan(self):
        if self._worker_thread and self._worker_thread.is_alive():
            messagebox.showinfo("Busy", "A run/scan is already in progress.")
            return
        try:
            mp0, sp0, gp0 = self._parse()
        except Exception as e:
            messagebox.showerror("Parse error", str(e))
            return

        varname = self.scan_var.get().strip()
        try:
            start = float(self.scan_start.get())
            stop  = float(self.scan_stop.get())
            steps = int(float(self.scan_steps.get()))
            if steps < 2:
                raise ValueError("Steps must be >= 2")
        except Exception as e:
            messagebox.showerror("Scan setup error", str(e))
            return

        T_override = self.scan_Tfinal.get().strip()
        if T_override:
            try:
                gp0.Tfinal = float(T_override)
            except Exception:
                messagebox.showerror("Scan setup error", f"Bad Tfinal override: {T_override}")
                return

        flip_each = bool(self.scan_flip_seed.get())

        self.status.set(f"Scanning {varname} from {start} to {stop} in {steps} steps...")
        self.diag_box.delete("1.0", "end")
        self.diag_box.insert("end", f"Scan: {varname} [{start}..{stop}] steps={steps}\n\n")
        self._stop_flag = False

        def set_field(obj, name, val):
            if hasattr(obj, name):
                setattr(obj, name, val)
                return True
            return False

        def worker():
            rows = []
            grid_vals = np.linspace(start, stop, steps)
            for i, val in enumerate(grid_vals):
                if self._stop_flag:
                    break

                mp = ModelParams(**asdict(mp0))
                sp = SeedParams(**asdict(sp0))
                gp = GridParams(**asdict(gp0))

                # Assign the scan variable
                ok = set_field(mp, varname, float(val)) or set_field(sp, varname, float(val))
                if not ok:
                    self._q.put(("error", f"Unknown scan variable: {varname}"))
                    return

                # Optional alternation of seed sign
                if flip_each and hasattr(sp, "sign"):
                    sp.sign = -sp.sign if (i % 2 == 1) else sp.sign

                try:
                    model = ModelG1D(mp, gp, sp)
                    t_eval = np.linspace(0.0, gp.Tfinal, 200)
                    sol = model.run(t_eval=t_eval)
                    diag = model.diagnostics(sol.y[:, -1])
                    rows.append((val, sp.sign, diag, sol.success))
                    self._q.put(("scan_progress", (i+1, steps, val, diag["polarity_label"])))
                except Exception as ex:
                    rows.append((val, sp.sign, {"error": str(ex)}, False))
                    self._q.put(("scan_progress", (i+1, steps, val, "ERROR")))

            self._q.put(("result", ("scan", rows, mp0, sp0, gp0, varname, start, stop, steps)))

        self._worker_thread = threading.Thread(target=worker, daemon=True)
        self._worker_thread.start()

    def on_stop(self):
        self._stop_flag = True
        self.status.set("Stop requested (will stop after current solve finishes).")
    # STEP 5.5 — Poll worker Queue (update GUI from main thread)


    def _poll_queue(self):
        try:
            while True:
                item = self._q.get_nowait()
                kind = item[0]
                if kind == "error":
                    self.status.set("Error.")
                    messagebox.showerror("Run error", item[1])
                elif kind == "status":
                    self.status.set(item[1])
                elif kind == "scan_progress":
                    n, N, val, pol = item[1]
                    self.status.set(f"Scan {n}/{N} — {self.scan_var.get()}={val:.6g} — {pol}")
                elif kind == "result":
                    self._handle_result(item[1])
        except queue.Empty:
            pass
        self.after(100, self._poll_queue)
    # STEP 5.6 — Update plot + diagnostics (single) or rankings (scan)


    def _handle_result(self, payload):
        mode = payload[0]
        if mode == "single":
            _, model, sol, mp, sp, gp = payload
            self._last_sol = sol
            self._last_model = model

            # Plot last frame
            y_last = sol.y[:, -1]
            pG, pX, pY = model.unpack(y_last)

            self.ax.clear()
            self.ax.plot(model.x, pY, label="pY (Y)", linewidth=1.5)
            self.ax.plot(model.x, pG, label="pG (G)", linewidth=1.0)
            self.ax.plot(model.x, pX/10.0, label="pX/10 (X scaled)", linewidth=1.0)
            self.ax.set_title(f"t={sol.t[-1]:.3f} (success={sol.success})")
            self.ax.set_xlabel("x")
            self.ax.grid(True)
            self.ax.legend(loc="best")
            self.canvas.draw()

            diag = model.diagnostics(y_last)
            self.diag_box.delete("1.0", "end")
            self.diag_box.insert("end", "=== Diagnostics (final state) ===\n")
            for k, v in diag.items():
                self.diag_box.insert("end", f"{k}: {v}\n")
            self.diag_box.insert("end", "\n=== Tips ===\n")
            self.diag_box.insert("end", "- For proton-like polarity: seed sign=-1 typically.\n")
            self.diag_box.insert("end", "- For electron-like polarity: try sign=+1; if it won't nucleate, adjust dy and g.\n")
            self.diag_box.insert("end", "- If soliton dissolves: reduce amp or shorten Tseed window; or adjust dy upward.\n")

            self.status.set(f"Done. {diag['polarity_label']}")
        elif mode == "scan":
            _, rows, mp0, sp0, gp0, varname, start, stop, steps = payload
            self.status.set("Scan complete.")
            self.diag_box.insert("end", "\n=== Scan results ===\n")

            # Show top candidates by |pY_core| (strong polarity) and by |Qproxy|
            scored = []
            for val, sign, diag, ok in rows:
                if not ok or "error" in diag:
                    continue
                score = abs(diag.get("pY_core", 0.0))
                scored.append((score, val, sign, diag))
            scored.sort(reverse=True, key=lambda t: t[0])

            self.diag_box.insert("end", f"Scanned {len(rows)} trials over {varname}.\n")
            self.diag_box.insert("end", "Top candidates (by |pY_core|):\n")
            for j, (score, val, sign, diag) in enumerate(scored[:10], start=1):
                self.diag_box.insert("end", f"{j:>2}. {varname}={val:.6g} sign={sign:+d}  pY_core={diag['pY_core']:.4g}  Qproxy={diag['Qproxy_int_pYdx']:.4g}  {diag['polarity_label']}\n")

            # Save a CSV log prompt
            if messagebox.askyesno("Save scan log?", "Save scan results to a CSV file?"):
                path = filedialog.asksaveasfilename(
                    defaultextension=".csv",
                    filetypes=[("CSV", "*.csv"), ("All files", "*.*")]
                )
                if path:
                    import csv
                    with open(path, "w", newline="") as f:
                        w = csv.writer(f)
                        w.writerow([varname, "seed_sign", "success", "pY_core", "pX_core", "Qproxy_int_pYdx", "pY_peak_abs", "pY_fwhm_abs", "polarity_label", "error"])
                        for val, sign, diag, ok in rows:
                            if ok and "error" not in diag:
                                w.writerow([val, sign, ok, diag.get("pY_core"), diag.get("pX_core"), diag.get("Qproxy_int_pYdx"),
                                            diag.get("pY_peak_abs"), diag.get("pY_fwhm_abs"), diag.get("polarity_label"), ""])
                            else:
                                w.writerow([val, sign, ok, "", "", "", "", "", "", diag.get("error", "")])
                    self.status.set(f"Scan log saved: {path}")
        else:
            self.status.set("Unknown result payload.")
    # STEP 5.7 — Save results to NPZ


    def on_save_npz(self):
        if self._last_sol is None:
            messagebox.showinfo("Nothing to save", "Run a simulation first.")
            return
        path = filedialog.asksaveasfilename(
            defaultextension=".npz",
            filetypes=[("NPZ", "*.npz"), ("All files", "*.*")]
        )
        if not path:
            return

        sol = self._last_sol
        model = self._last_model
        np.savez_compressed(
            path,
            t=sol.t,
            y=sol.y,
            x=model.x,
            params_model=np.array([asdict(self.mp)], dtype=object),
            params_seed=np.array([asdict(self.sp)], dtype=object),
            params_grid=np.array([asdict(self.gp)], dtype=object),
        )
        self.status.set(f"Saved: {path}")
    # STEP 5.8 — Export MP4 (requires imageio)


    def on_export_mp4(self):
        if not HAVE_IMAGEIO:
            messagebox.showerror("Missing dependency", "imageio not installed. Try: pip install imageio imageio[ffmpeg]")
            return
        if self._last_sol is None:
            messagebox.showinfo("Nothing to export", "Run a simulation first.")
            return

        path = filedialog.asksaveasfilename(
            defaultextension=".mp4",
            filetypes=[("MP4", "*.mp4"), ("All files", "*.*")]
        )
        if not path:
            return

        sol = self._last_sol
        model = self._last_model

        # Render frames to memory (for small number of frames)
        t_eval = sol.t
        fps = max(8, int(len(t_eval) / max(1, float(model.gp.Tfinal)/2)))
        self.status.set(f"Rendering MP4 (frames={len(t_eval)}, fps={fps})...")

        fig = matplotlib.figure.Figure(figsize=(9, 4.5), dpi=120)
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        ax.set_xlabel("x")
        ax.grid(True)

        writer = imageio.get_writer(path, fps=fps)
        try:
            for k in range(len(t_eval)):
                yk = sol.y[:, k]
                pG, pX, pY = model.unpack(yk)

                ax.clear()
                ax.plot(model.x, pY, label="pY (Y)", linewidth=1.5)
                ax.plot(model.x, pG, label="pG (G)", linewidth=1.0)
                ax.plot(model.x, pX/10.0, label="pX/10 (X scaled)", linewidth=1.0)
                ax.set_title(f"t={t_eval[k]:.3f}")
                ax.set_xlabel("x")
                ax.grid(True)
                ax.legend(loc="best")
                ax.set_ylim(-1.2, 1.2)

                canvas.draw()
                w, h = fig.canvas.get_width_height()
                frame = np.frombuffer(canvas.buffer_rgba(), dtype=np.uint8).reshape((h, w, 4))
                writer.append_data(frame[:, :, :3])  # drop alpha
        finally:
            writer.close()

        self.status.set(f"MP4 saved: {path}")

# STEP 6 — Program entry point
# Creates the App window and enters Tkinter's main event loop.



def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
