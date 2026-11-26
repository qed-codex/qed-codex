---
{
  "module": "src/Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/LogarithmicSubstitution/TwoTorsionKernelUniqueHolds.lean",
  "declarations": [
    "Formalism.L2.Th1.B.KNorm.torsion_norm_bound_holds",
    "Formalism.L2.Th1.B.KNorm.two_torsion_kernel_norm_unique"
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

## A coordinate bound for two-primary torsion with good reduction

[Theorem PHT.1109](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.B.KNorm.torsion_norm_bound_holds/)

Let $K$ be an ultrametric normed field with $|2|=1/2$. Let $W/K$ be a Weierstrass curve whose coefficients satisfy $|a_1|,|a_2|,|a_3|,|a_4|,|a_6|\le1$ and whose discriminant satisfies $|\Delta|=1$. If $P\in W(K)$ satisfies $[2^k]P=0$ for some $k\ge0$ and $[2]P\ne0$, then its affine $x$-coordinate satisfies $$|x(P)|<4.$$

## Uniqueness and coordinate size of formal two-torsion

[Theorem PHT.1010](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.B.KNorm.two_torsion_kernel_norm_unique/)

Let $K$ be an ultrametric normed field with $|2|=1/2$. Let $W/K$ be a Weierstrass curve with $$|a_1|,|a_2|,|a_3|,|a_4|,|a_6|\le1,\qquad|\Delta_W|=|a_1|=1.$$ Let $P\in W(K)$ be nonzero, satisfy $2P=0$, and have $|x(P)|>1$. Then $|x(P)|=4$. Every nonzero $Q\in W(K)$ with $2Q=0$ and $|x(Q)|>1$ equals $P$.
