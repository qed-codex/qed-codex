---
{
  "module": "src/Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedVolumeStatements/GenericRatioOfBoundHolds.lean",
  "declarations": [
    "Formalism.L2.SG.Closed.MirabolicBound_holds"
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

## A dimension bound for generic finite-field representations

[Theorem REP.0287](https://andrewodesky.com/rh/lean/Formalism.L2.SG.Closed.MirabolicBound_holds/)

Let $F$ be a finite field of cardinality $q$, $k\ge0$, and $\psi:F\to\mathbb C^\times$ a nontrivial additive character. Let $\pi$ be an irreducible representation of $\operatorname{GL}_k(F)$ on a finite-dimensional complex vector space $V$. Suppose there is a nonzero linear functional $\lambda:V\to\mathbb C$ such that $$\lambda(\pi(u)v)=\psi\left(\sum_{j=1}^{k-1}u_{j,j+1}\right)\lambda(v)$$ for every upper unitriangular $u$. Then $$\prod_{j=1}^{k-1}(q^j-1)\le\dim_{\mathbb C}V,$$ with empty product one.
