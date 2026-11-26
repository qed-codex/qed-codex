---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/BlochKatoRightExact.lean",
  "declarations": [
    "GlobalTheory.BKRightExact.bkARightExact_of_tied",
    "GlobalTheory.BKRightExact.lift_periods"
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

## Surjectivity of period maps onto a crystalline quotient

[Theorem PHT.1164](https://andrewodesky.com/rh/lean/GlobalTheory.BKRightExact.lift_periods/)

Let $\ell$ be prime, $K/\mathbb Q_\ell$ and $L/\mathbb Q_\ell$ finite extensions, and fix the local period-ring data and identifications with Fontaine's crystalline and de Rham rings of ([De Rham subrepresentations and strict quotient maps](https://andrewodesky.com/rh/lean/GlobalTheory.DRSubQuot.deRham_sub_quot/)). Let $V,V'$ be finite-dimensional $L$-vector spaces with $L$-linear representations $\rho,\rho'$ of $G_K$. Suppose $f:V\twoheadrightarrow V'$ is $G_K$-equivariant and $V$ is crystalline in these period data. Then $V'$ is de Rham, and both maps $$D_{\mathrm{cris}}(V)\longrightarrow D_{\mathrm{cris}}(V'),\qquad D_{\mathrm{dR}}(V)\longrightarrow D_{\mathrm{dR}}(V')$$ induced by $f\otimes1$ are surjective.

## Right exactness of finite local cohomology for crystalline representations

[Theorem PHT.1457](https://andrewodesky.com/rh/lean/GlobalTheory.BKRightExact.bkARightExact_of_tied/)

Let $\ell$ be prime and fix local period rings, integral data and comparison identifications as in ([An invariant crystalline period matrix for an unramified representation](https://andrewodesky.com/rh/lean/GlobalTheory.UnrPer.exists_period_unramified/)). Let $K/\mathbb Q_\ell$ be finite inside the chosen algebraic closure. Let $L/\mathbb Q_\ell$ be a finite-dimensional coefficient field with its module topology and topological-ring structure, and let $\mathcal O$ be a discrete valuation domain with fraction field $L$ and open image in $L$.

Let $V,V'$ be finite-dimensional continuous crystalline $L$-representations of $G_K$, with their finite-dimensional module topologies and compatible scalar structures over $\mathbb Q_\ell$ and $\mathcal O$. If $f:V\twoheadrightarrow V'$ is equivariant and $L$-linear, then for every finite continuous cocycle $c':G_K\to V'$ there is a finite continuous cocycle $c:G_K\to V$ such that $f\circ c-c'$ is a coboundary. Thus $$H_f^1(K,V)\longrightarrow H_f^1(K,V')$$ is surjective, where finite cocycles are continuous cocycles that become coboundaries in the crystalline period ring, and finite cohomology is their quotient by coboundaries, as in ([Finite local cocycles modulo a power are reductions of integral cocycles](https://andrewodesky.com/rh/lean/GlobalTheory.BKTorsionRed.mem_HfQ_iff_red/)).
