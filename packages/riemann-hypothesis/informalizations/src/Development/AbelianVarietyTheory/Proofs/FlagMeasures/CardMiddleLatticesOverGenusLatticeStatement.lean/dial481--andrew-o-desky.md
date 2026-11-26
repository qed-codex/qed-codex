---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/CardMiddleLatticesOverGenusLatticeStatement.lean",
  "declarations": [
    "GlobalTheory.T.card_middleLattices_over_genus_lattice"
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

## Counting intermediate lattices above a fixed genus lattice

[Theorem ANT.0215](https://andrewodesky.com/rh/lean/GlobalTheory.T.card_middleLattices_over_genus_lattice/)

Fix the source's full arithmetic datum with CM field $E/F$, integers $r,f\ge0$, Hermitian spaces $V,W$, a fixed map $\iota:W\to V$, a standard self-dual lattice $\Lambda_V\subset V$, and positive integer $g$ equal to its two specified auxiliary integers' product. Choose one of its finite parameter indices, with associated rational prime $p\ge3$, and assume $p$ splits completely in $E$.

Let $e_0,\ldots,e_{r-1}\in V$ be the prescribed linearly independent isotropic frame, and let $z$ be the prescribed vector for this parameter, perpendicular to that frame with $h(z,z)=-p$. Put $X=\langle e_0,\ldots,e_{r-1}\rangle_E$. Use the class of lattices defined below and choose $\Lambda$ in it. For any such lattice $\Lambda'$, put $$B(\Lambda')=(\Lambda'\cap X^\perp)+X,\quad j(w,a)=\iota(w)+az,\quad\mathcal L(\Lambda')=j^{-1}(B(\Lambda')),$$ $$M_0=\iota^{-1}(B(\Lambda)\cap z^\perp).$$ For every lattice $M$ in the Hermitian genus of $M_0$ in $W$, exactly $$(p-1)^f$$ distinct $\mathcal O_E$-submodules $\mathcal L\subset W\times E$ occur as $\mathcal L(\Lambda')$ with $\Lambda'$ in the prescribed class and $\{w:(w,0)\in\mathcal L\}=M$.
