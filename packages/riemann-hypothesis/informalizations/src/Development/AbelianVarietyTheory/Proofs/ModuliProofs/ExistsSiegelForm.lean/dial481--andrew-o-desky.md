---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExistsSiegelForm.lean",
  "declarations": [
    "GlobalTheory.SiegelPeriod.exists_siegel_form"
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

## Siegel normal form for a polarized period lattice

[Theorem AV.1595](https://andrewodesky.com/rh/lean/GlobalTheory.SiegelPeriod.exists_siegel_form/)

Let $\Lambda$ be a free abelian group with an isomorphism $b:\mathbb Z^g\oplus\mathbb Z^g\to\Lambda$ and an integral bilinear form $E$ satisfying $$E(b(a,c),b(a',c'))=a\cdot c'-c\cdot a'.$$ Let $Q:\Lambda\to\mathbb C^g$ be additive and injective with discrete image whose real span is $\mathbb C^g$. Let $H$ be a Hermitian matrix such that $h_H(z,w)=z^tH\bar w$ is positive definite and $$\Im h_H(Qx,Qy)=E(x,y).$$ Let $A,B$ be the matrices with columns $Q(b(e_j,0))$ and $Q(b(0,e_j))$. There are matrices $h,\tau$ with $$h\in\operatorname{GL}_g(\mathbb C),\quad h^{-1}=B,\quad\tau=hA,\quad\tau^t=\tau,\quad\Im\tau>0,$$ $$h_H(z,w)=(hz)^t(\Im\tau)^{-1}\overline{hw},\qquad hQ(b(a,c))=\tau a+c.$$ The last identity holds for all $a,c\in\mathbb Z^g$, and the preceding one for all $z,w\in\mathbb C^g$.
