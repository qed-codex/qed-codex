---
{
  "module": "src/Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/GaugeLatticeShifts/LieAveraging/LsSetresAvgW.lean",
  "declarations": [
    "Formalism.L2.SG.TermOp.Vanish.avgCore"
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

## Vanishing of an equivariant integral

[Theorem REP.1238](https://andrewodesky.com/rh/lean/Formalism.L2.SG.TermOp.Vanish.avgCore/)

Let $G$ be a locally compact second-countable Hausdorff topological group with its Borel measurable structure and a left and right invariant Haar measure $\mu$. Let $R\subseteq G$ be closed and $\Gamma\subseteq R$ a discrete subgroup. Suppose some compact $K\subseteq G$ meets every left $\Gamma$-orbit in $R$.

Let $V$ be a complex normed space and $\chi:G\to\mathbb C$ have continuous restriction to $R$, with $\chi(rr')=\chi(r)\chi(r')$ for $r,r'\in R$, $\chi|_\Gamma=1$, and $\chi(r_0)\ne1$ for some $r_0\in R$. Let $f:G\to V$ satisfy $f(rx)=\chi(r)f(x)$ for $r\in R$, $x\in G$. If $\Omega\subseteq G$ is measurable, every left $\Gamma$-orbit meets $\Omega$, and $x,\gamma x\in\Omega$ with $\gamma\in\Gamma$ implies $\gamma=1$, then $$\int_\Omega f(x)\,d\mu(x)=0.$$
