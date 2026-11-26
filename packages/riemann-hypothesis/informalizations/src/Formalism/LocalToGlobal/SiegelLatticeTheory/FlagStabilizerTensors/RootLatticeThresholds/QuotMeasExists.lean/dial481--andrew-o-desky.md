---
{
  "module": "src/Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/QuotMeasExists.lean",
  "declarations": [
    "Formalism.L2.SG.Pf.QuotMeasExists.quotM_exists"
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

## A measure giving integration along a closed matrix subgroup

[Theorem ALG.0296](https://andrewodesky.com/rh/lean/Formalism.L2.SG.Pf.QuotMeasExists.quotM_exists/)

Let $G,S\subseteq M_m(\mathbb C)$ be closed matrix groups with $S\subseteq G$. Let $\mu_G,\mu_S$ be nonzero sigma-finite Borel measures on $M_m(\mathbb C)$ supported on $G,S$, respectively, invariant under left multiplication by their groups. There is a Borel measure $\nu$ on $M_m(\mathbb C)$ such that for every nonnegative measurable $f:M_m(\mathbb C)\to[0,\infty]$, $$\int f(x)\,d\mu_G(x)=\int\!\int f(sx)\,d\mu_S(s)\,d\nu(x).$$
