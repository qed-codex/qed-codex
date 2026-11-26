---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/TwoLevelFlagDomainCuspFormRanksShiftedWeights.lean",
  "declarations": [
    "GlobalTheory.ShareRanks.compT"
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

## Binomial bounds for three shifted cusp-form spaces

[Theorem AV.1192](https://andrewodesky.com/rh/lean/GlobalTheory.ShareRanks.compT/)

Fix the source's geometric flag-domain datum $\mathcal X$ over a CM field $E$, of rank $r$, with embedding set $\Psi$, Hermitian matrix $G$, index $0<p_0<r$, domain $D$, section sets $\mathcal S(\lambda)$, and dimension $d$. Assume its archimedean comparison package for weights $L,F\in(\mathbb Z^r)^\Psi$ and integer $T\ge0$. Define $$\kappa_i=2i-(r-1)\quad(0\le i<r),\qquad A=F-\kappa-(d+2)L.$$ For every $\tau\in\Psi$ and adjacent indices $i,i+1$ with $i+1\ne p_0$, assume $$L_{\tau,i}-L_{\tau,i+1}\ge1,\qquad A_{\tau,i}-A_{\tau,i+1}\ge0,$$ and assume $$L_{\tau,r-1}-L_{\tau,0}\ge1.9T,\qquad A_{\tau,r-1}-A_{\tau,0}\ge1.$$ Let $s\ge0$ be even with $s\le T$, and put $\Delta_{s,\tau,i}=-s/2$ for $i<p_0$ and $s/2$ otherwise. Suppose some $u\in\mathcal S(\Delta_s)$ is nonzero at a point of $D$.

There exists $\delta\ge0$ integral such that $d\ge2$, $11d^2\le T$, and the following bounds hold for restrictions of sections to the full flag domain determined by $\Psi,G,p_0$. At each weight $F+TL$ and $F+TL-\Delta_s$, every linearly independent family has size at most $$\delta\binom{T+2d+6}{d};$$ at weight $F+TL+2\Delta_s$, every such family has size at most $\delta\binom{T+3d+10}{d}$; and at weight $F+TL-\Delta_s$ there exists such a family of size $$\delta\binom{T+d}{d}.$$
