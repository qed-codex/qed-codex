---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/IsBaseEnlargementFixedCoefFieldOfCoeffEnlargemen.lean",
  "declarations": [
    "GlobalTheory.Mem.R3.Rw.DatExt0",
    "GlobalTheory.Mem.R3.Rw.Enl0"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## Extension of realisations under enlargement of a coefficient field

[Definition / hypothesis THETA.D026](https://andrewodesky.com/rh/lean/GlobalTheory.Mem.R3.Rw.DatExt0/)

Use the contexts, bases, frames, twist data and eventuality of ([Contexts, and statements that hold eventually in the parameters](https://andrewodesky.com/rh/lean/GlobalTheory.Mem.Top.EvG/)). Suppose two bases have the same preliminary data. Call the second an *enlargement with fixed $K_s$* of the first if, after embedding their fields in $\mathbb C$, their fields $K_s$ have the same image, and both the image of $\mathbb L_0$ and that of $\mathbb L$ for the first are contained in the corresponding images for the second.

The extension assumption says that eventually for large bases the following holds, under the exactness, preliminary-data and forced-prime conditions on the larger base. Given a pinned column input over that base, take a smaller base with the same frame, an enlargement with fixed $K_s$ as above, and a pinned column input with the same prime choices. For every later stage and realisation on the smaller base satisfying the field and group conditions, four conditions on the realisation and a list of seventeen further conditions, and every later stage on the larger base satisfying the field and group conditions and a volume condition, there is a realisation on the larger base satisfying the same four conditions and a compatibility condition with the smaller realisation. Its set of places is the set of all places whose residue characteristic belongs to the chosen set of primes of the larger twist data. The pinning, stages, field and group conditions, the four conditions, the seventeen conditions, the volume condition and the compatibility condition are not expanded.
