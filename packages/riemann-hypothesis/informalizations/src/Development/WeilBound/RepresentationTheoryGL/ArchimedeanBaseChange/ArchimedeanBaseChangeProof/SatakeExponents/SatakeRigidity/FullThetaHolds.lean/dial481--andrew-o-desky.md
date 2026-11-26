---
{
  "module": "src/Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/SatakeRigidity/FullThetaHolds.lean",
  "declarations": [
    "PositivityTheory.Rg.BcB.F.Rig.locRigid_holds"
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

## Local rigidity of discrete automorphic decompositions

[Theorem AGR.0063](https://andrewodesky.com/rh/lean/PositivityTheory.Rg.BcB.F.Rig.locRigid_holds/)

Let $E$ be a CM number field. Consider two collections of discrete automorphic representations $V_i$ of $\operatorname{GL}_{n_i}(\mathbb A_E)$ and $V'_j$ of $\operatorname{GL}_{n'_j}(\mathbb A_E)$, with positive ranks and $\sum_i n_i=\sum_j n'_j=n$. Specify their smooth irreducible local components $\pi_{i,w},\pi'_{j,w}$ and infinitesimal-character multisets $m_{i,\tau},m'_{j,\tau}$. Assume that at every complex embedding $\tau$ there are decreasing integral tuples $\lambda_\tau,\lambda'_\tau\in\mathbb Z^n$ such that $$\sum_i m_{i,\tau}=\{\lambda_{\tau,k}+(n-1)/2-k:0\le k<n\},\qquad\sum_j m'_{j,\tau}=\{\lambda'_{\tau,k}+(n-1)/2-k:0\le k<n\}.$$ Suppose that outside finitely many finite places all these local components are spherical and the unions of their Satake multisets agree. There is a bijection $i\leftrightarrow j(i)$ such that $$[\pi_{i,w}]=[\pi'_{j(i),w}]\qquad\text{for every }i\text{ and every finite place }w.$$ The brackets denote the local irreducible representation classes, including their ranks.
