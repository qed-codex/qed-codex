---
{
  "module": "src/Development/EtaleCohomology/EtaleSheaves/TwPairExists.lean",
  "declarations": [
    "LateralTheory.Fix.CupProductTensor.awFlip"
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

## Graded symmetry of Alexander-Whitney pairings

[Theorem AG.0828](https://andrewodesky.com/rh/lean/LateralTheory.Fix.CupProductTensor.awFlip/)

Let $R$ be a commutative ring and let $I,J,K$ be complexes of etale sheaves of $R$-modules on schemes. Let $\mu:I\otimes J\to K$ and $\nu:J\otimes I\to K$ be pairings of complexes. Assume that for homogeneous local sections $a\in I^s$, $b\in J^t$, $$\nu(b,a)=(-1)^{st}\mu(a,b).$$ Let $E_\bullet$ be a simplicial set-valued presheaf on schemes, and let $C(E)$ be the complex of free etale $R$-module sheaves on its simplices, with degree $-N$ for $N$-simplices and alternating face differential.

Let $\alpha,\beta$ be cocycles of degrees $n,m\in\mathbb Z$ in $\operatorname{Hom}^\bullet(C(E),I)$ and $\operatorname{Hom}^\bullet(C(E),J)$, respectively. If $\gamma,\gamma'$ are degree-$n+m$ cocycles representing their Alexander–Whitney products for $\mu$ and for $\nu$ in the opposite order, then $$[\gamma]=(-1)^{nm}[\gamma']\quad\text{in }H^{n+m}\operatorname{Hom}^\bullet(C(E),K).$$
