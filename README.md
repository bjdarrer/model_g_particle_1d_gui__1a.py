Model G Particle 1D — GUI Explorer (SAFE-ish)
- Built from Brendan's "model_g_particle_1d_safe__1d.py" and adapted into a GUI parameter explorer.
- Purpose: help you *search* for charged-polarity soliton states (proton-like vs electron-like polarity) by
  adjusting Model G parameters and seed forcing χ(x,t), then running quick simulations and computing diagnostics.

- Written by Brendan Darrer aided by ChatGPT 5.2 date: 5th March 2026 21:39 GMT
- adapted from: @ https://github.com/blue-science/subquantum_kinetics/blob/master/particle.nb and
"model_g_particle_1d_safe__1d.py"
- with ChatGPT 5.2 writing it and Brendan guiding it to produce a clean code.

Papers used for this simulation GUI explorer:
International Journal of General Systems,
Vol. 42, No. 5, May 2013, 1–24,
[1] Stationary Dissipative Solitons of Model G,
Matthew Pulver and Paul A. LaViolette,
Blue Science, Los Angeles, California USA,
Starburst Foundation, Schenectady, New York USA,
(Received 7 July 2012; final version received 12 February 2013),
https://starburstfound.org/downloads/physics/model_g.pdf , As (model_g (1)) below.

&

Darrer, Brendan & Coven, Justin & LaViolette, Paul. (2022).
[2] Subquantum kinetics: simulating subatomic particles in Model G with fluid dynamics.
https://www.researchgate.net/publication/362456406_Subquantum_kinetics_simulating_subatomic_particles_in_Model_G_with_fluid_dynamics , As (SQK_ModelG_with_fluid_dynamics_…) below.

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
    python3 model_g_particle_1d_gui__1a.py

...............INSTRUCTIONS ON USE OF GUI PARTICLE FINDER..................................

Can you help me find new subatomic particles in Model G of SQK, using the starburst simulator here: @ https://starburstfound.org/computer-simulation-of-model-g/ . This simulator is set up initially with parameters to model a neutral like particle similar to a neutron (Matt Pulver who found the neutron parameters, said it was like looking for a needle in a hey stack!). Can you help me use it model charged particles such as a proton or an electron in Model G (i.e. guiding me to input the correct parameters of these subatomic particles)? I attach papers here that may help guide you with this.

Thought for 47s

ChatGPT 5.2:

Yes — I can help you use the Starburst Model-G simulator systematically to hunt for charged soliton “particle” states (proton-like, electron-like), starting from Matt’s neutron-like parameter set and then doing controlled parameter continuation + diagnostics.

Below is a practical workflow you can apply in the web simulator UI even if it only exposes the dimensional inputs (A, B, k’s, D’s, seed χ), using the mapping and physical interpretation given in the two papers you attached. 

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

And you’ll want a stable localized soliton (Gaussian-ish core + oscillatory Turing tail) like in their figures. 

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

This is powerful because it tells you what to vary in the UI to move “in the same direction” as the dimensionless theory.

3) The single most important “charged-particle” trick: flip the seed polarity

In the 2013 paper, the particle is nucleated by adding a negative Gaussian seed χ into the X equation, i.e. χ is negative (their χ = −exp(…)). 

model_g (1)


That drives ϕX negative at the core, which corresponds to positive ϕY polarity (positive charge polarity). 

model_g (1)

Practical implication in the simulator

To search proton-like / positive polarity states: use the usual negative χ in X (the “neutron-like” setup is already seeded this way in many configs).

To search electron-like / negative polarity states: try the opposite sign seed, i.e. positive χ in X (or equivalently seed negative in Y if your UI supports choosing which field gets χ).

Caveat (important): The 2013 paper notes that in a globally subcritical “vacuum-like” state, negative charge polarity fluctuations may fail to nucleate a particle (their matter/antimatter polarity bias point). 

model_g (1)


In practice, that means: if “electron-like” won’t nucleate just by flipping χ, you likely must also shift the background closer to (or into) the supercritical regime (next section).

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

This matters because G↔X coupling is central to the bifurcation behavior (and thus whether a given polarity can self-stabilize). 

model_g (1)

Practical sweep:
Make small incremental changes, e.g.

k−2: 0.10 → 0.11 → 0.12 … (or)

k5: 0.90 → 0.88 → 0.86 …

Each time, retry the positive χ in X electron-seed attempt.

Step 4 — adjust diffusion ratio dy = D_Y/D_G

The 2013 soliton example has dy substantially larger than dx (dy=12, dx=1). 

model_g (1)


Your TF2-style example uses D_Y=1.95 with D_G=1, i.e. dy≈1.95, which is a different regime (it can still work, but it changes the pattern selection). 

SQK_ModelG_with_fluid_dynamics_…

So, if you’re having trouble getting alternative polarity states, do a controlled sweep of:

D_Y upward (keeping D_G fixed), e.g. 1.95 → 3 → 5 → 8 → 12
while maintaining stability (avoid instantly chaotic patterns).

5) How to tell “proton-like” vs “neutron-like” vs “electron-like” in the output

Because these are toy-solutions in a dimensionless RD system, you need a consistent operational definition inside the simulator:

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


Even if their “particle example” wasn’t tuned to enforce zero net charge in the naive integral sense, this gives you a repeatable way to rank candidates.

C. Size / wavelength targeting (for “electron-like” vs nucleon-like)

They emphasize that the Turing tail wavelength λ0 is a key “particle identifier” and is stable (boundary-independent). 

model_g (1)


So: if you eventually want “electron vs proton” separation, you will likely need to find parameter sets that generate different λ0 (then map λ0 to a target Compton wavelength via the physical scaling).

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

This is basically “continuation + diagnostics,” which is how Matt likely found the neutron-like set in the first place — just made less painful.

7) What I need from you to give “type-in-these-values” guidance (without more back-and-forth)

If you paste (or screenshot) the Starburst simulator’s actual input panel showing:

the exact parameter names it exposes (A/B/k’s/D’s/seed fields, etc.)

and the current neutron-like preset values,

…then I can translate the search plan above into specific candidate parameter sets in the simulator’s exact units/fields (e.g., “set k5 to 0.86; set k−2 to 0.12; flip χ sign; increase D_Y to 5,” etc.), and lay them out as “Trial 1… Trial 2… Trial 3…”

For now, the guidance above is the correct physics-to-UI control logic based directly on the attached papers’ definitions of the variables, polarity, and parameter mappings.

.................................................
