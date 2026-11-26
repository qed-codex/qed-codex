---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/ExistsImagQuadOrderPairAndEvenTheta.lean",
  "declarations": [
    "GlobalTheory.MomOne.exists_pair_and_isTh"
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

## A normalized even theta function for a quadratic lattice

[Theorem ANT.0894](https://andrewodesky.com/rh/lean/GlobalTheory.MomOne.exists_pair_and_isTh/)

Let $d$ be prime with $d\equiv7\pmod{16}$, and put $$\Lambda=\mathbb Z+\mathbb Z\frac{1+i\sqrt d}{2},\qquad G_{2k}=\sum_{0\ne\lambda\in\Lambda}\lambda^{-2k}\quad(k=2,3),\qquad \Delta=(60G_4)^3-27(140G_6)^2.$$ There are complex numbers $\omega_1,\omega_2$, linearly independent over $\mathbb R$, with $\Lambda=\mathbb Z\omega_1+\mathbb Z\omega_2$. The Weierstrass invariants of $L=(\omega_1,\omega_2)$ satisfy $g_2(L)^3-27g_3(L)^2=\Delta$.

Put $h(z,w)=2z\overline w/\sqrt d$ for $z,w\in\mathbb C$. There is also an entire function $\theta:\mathbb C\to\mathbb C$ with $\theta(0)=1$, $\theta(-z)=\theta(z)$, and $$e^{\pi i|x|^2}\theta(z+x)\exp\left(-\pi h(z,x)-\frac\pi2h(x,x)\right)=\theta(z) \qquad(x\in\Lambda,\ z\in\mathbb C).$$ Every zero $z$ of $\theta$ satisfies $z-\tfrac12\in\Lambda$.
