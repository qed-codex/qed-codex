---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/ThetaLawProofs/LineBundlePowSectionsEqThetaLevel.lean",
  "declarations": [
    "GlobalTheory.LevelDict.sections_eq_level"
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

## Line-bundle sections and theta functions of a fixed level

[Theorem AV.1036](https://andrewodesky.com/rh/lean/GlobalTheory.LevelDict.sections_eq_level/)

Assume ([Theta functions for a principally polarized complex abelian variety](https://andrewodesky.com/rh/lean/GlobalTheory.thetaUnifAV_closed/)), whose conditions are recalled below. Let $(A,L)$ be a principally polarized complex abelian variety of dimension $g\ge1$, with a rigidification of $L$ at zero, a nonzero section $\theta\in H^0(A,L)$, and a tangent basis $v_1,\ldots,v_g$. Choose a holomorphic group uniformization $e:\mathbb C^g\to A(\mathbb C)$ and a nowhere-zero holomorphic frame $\eta$ of $e^*L$. Suppose $\tau=\tau^t$ has positive definite imaginary part, $$\ker e=\mathbb Z^g+\tau\mathbb Z^g,$$ the frame agrees with the rigidification at zero, $de_0((2\pi i)^{-1}e_j)=v_j$, and $e^*\theta=\vartheta_{a,b}\eta$, where $a_j,b_j\in\{0,1/2\}$ and $$\vartheta_{a,b}(z)=\sum_{n\in\mathbb Z^g}\exp\bigl(\pi i(n+a)^t\tau(n+a)+2\pi i(n+a)^t(z+b)\bigr).$$ For every $l\ge0$, each $s\in H^0(A,L^{\otimes l})$ determines a unique entire function $F$ with $e^*s=F\eta^{\otimes l}$ satisfying $$F(z+m+\tau n)=\left[\exp\!\left(2\pi i\left(\frac{a^tm-b^tn-n^t\tau n}{2}-n^tz\right)\right)\right]^lF(z)\qquad(m,n\in\mathbb Z^g).$$ Conversely, each entire function satisfying this law determines a unique such section $s$.
