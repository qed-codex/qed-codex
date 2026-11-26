---
{
  "module": "src/Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/SchurOrthogonalitySquareIntegrable.lean",
  "declarations": [
    "GlobalTheory.Published.SchurOrthogonalitySquareIntegrable",
    "GlobalTheory.Published.schurOrthogonalitySquareIntegrable'"
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

## Schur orthogonality for square-integrable representations

[Theorem REP.1117](https://andrewodesky.com/rh/lean/GlobalTheory.Published.schurOrthogonalitySquareIntegrable'/)

Let $G$ be a locally compact Hausdorff topological group with a regular bi-invariant Haar measure $dg$ on its Borel sets. Let $\pi$ be a strongly continuous irreducible unitary representation on a complex Hilbert space $H$. Irreducibility means that the only closed invariant complex subspaces are zero and $H$. Suppose some nonzero vectors $v_0,w_0$ have square-integrable matrix coefficient. Then every matrix coefficient is square integrable and there is $d_\pi>0$ such that $$\int_G\langle w,\pi(g)v\rangle\,\overline{\langle w',\pi(g)v'\rangle}\,dg=\frac{\langle v',v\rangle\langle w,w'\rangle}{d_\pi}.$$ The product integrand is integrable for all $v,w,v',w'\in H$. Inner products are linear in the second argument.
