---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CrystallineCoboundaryLiftStatement.lean",
  "declarations": [
    "GlobalTheory.T.crystalline_coboundary_lift"
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

## Crystalline and filtered consequences of a period-ring coboundary

[Theorem PHT.1611](https://andrewodesky.com/rh/lean/GlobalTheory.T.crystalline_coboundary_lift/)

Let $\ell$ be prime, $K/\mathbb Q_\ell$ finite, and fix the local crystalline and de Rham period rings, integral construction, and compatibility data specified in ([Crystallinity of a codimension-one extension and a period coboundary](https://andrewodesky.com/rh/lean/GlobalTheory.CrysExtCrit.coboundary_iff_isCrys/)). Write $B$ for the crystalline ring, $\varphi$ for its Frobenius, and $\iota:B\to B_{\mathrm{dR}}$ for the comparison map. Let $L/\mathbb Q_\ell$ be finite with its vector-space topology and topological-ring structure, and let $O$ be a discrete valuation domain with fraction field $L$ whose image in $L$ is open. Let $V$ be a finite-dimensional continuous $L$-representation of $G_K$, with its compatible $O$- and $\mathbb Q_\ell$-scalar structures, and assume it is de Rham.

For any function $c:G_K\to V$ and any $x\in V\otimes_{\mathbb Q_\ell}B$, if $$c(g)\otimes1=gx-x\qquad(g\in G_K),$$ then $$x-(1\otimes\varphi)x\in D_{\mathrm{cris}}(V),\qquad\exists d\in D_{\mathrm{dR}}(V):\ (1\otimes\iota)x-d\in\operatorname{Fil}^0(V\otimes B_{\mathrm{dR}}).$$ Here both period spaces are the Galois invariants of the indicated tensor spaces, and the filtration is induced by $B_{\mathrm{dR}}$.
