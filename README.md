Model G Particle 1D — GUI Explorer (SAFE-ish)
- Built from Brendan's "model_g_particle_1d_safe__1d.py" and adapted into a GUI parameter explorer.
- Purpose: help you *search* for charged-polarity soliton states (proton-like vs electron-like polarity) by
  adjusting Model G parameters and seed forcing χ(x,t), then running quick simulations and computing diagnostics.

- Written by Brendan Darrer aided by ChatGPT 5.2 date: 5th March 2026 21:39 GMT
- adapted from: @ https://github.com/blue-science/subquantum_kinetics/blob/master/particle.nb and
"model_g_particle_1d_safe__1d.py"
- with ChatGPT 5.2 writing it and Brendan guiding it to produce a clean code.

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
