---
{
  "module": "src/Formalism/LocalToGlobal/TorsionIntegrality/EisensteinTranslationProducts/SemiChar.lean",
  "declarations": [
    "Formalism.L2.Th1.F.area",
    "Formalism.L2.Th1.F.herm",
    "Formalism.L2.Th1.F.opU",
    "Formalism.L2.Th1.F.s2",
    "Formalism.L2.Th1.F.sgStar",
    "Formalism.L2.Th1.F.th0",
    "Formalism.L2.Th1.F.wEta",
    "Formalism.L2.Th1.F.wSigma",
    "Formalism.L2.Th1.F.wZeta"
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

## Sigma functions and translations on a period lattice

[Definition / hypothesis ANT.D062](https://andrewodesky.com/rh/lean/Formalism.L2.Th1.F.wSigma/)

Let $\omega_1,\omega_2\in\mathbb C$ be linearly independent over $\mathbb R$, and put $\Lambda=\mathbb Z\omega_1+\mathbb Z\omega_2$. For $z\in\mathbb C$, define the Weierstrass sigma and zeta functions by $$\sigma_\Lambda(z)=z\prod_{0\ne\lambda\in\Lambda}\left(1-\frac z\lambda\right)\exp\left(\frac z\lambda+\frac{z^2}{2\lambda^2}\right),$$ $$\zeta_\Lambda(z)=\frac1z+\sum_{0\ne\lambda\in\Lambda}\left(\frac1{z-\lambda}+\frac1\lambda+\frac z{\lambda^2}\right).$$ This normalization gives $\sigma_\Lambda'(0)=1$.

For the same lattice, define $$\wp_\Lambda(z)=\frac1{z^2}+\sum_{0\ne\lambda\in\Lambda}\left(\frac1{(z-\lambda)^2}-\frac1{\lambda^2}\right)\qquad(z\in\mathbb C),$$ $$g_2(\Lambda)=60\sum_{0\ne\lambda\in\Lambda}\lambda^{-4},\qquad g_3(\Lambda)=140\sum_{0\ne\lambda\in\Lambda}\lambda^{-6}.$$ The pointwise value of $\wp_\Lambda$ on $\Lambda$ is zero.

Let $\eta:\mathbb C\to\mathbb C$ be the real-linear map determined by $\eta(\omega_j)=2\zeta_\Lambda(\omega_j/2)$ for $j=1,2$. Define $$A=|\operatorname{Im}(\overline\omega_1\omega_2)|,\qquad s_2=\frac{\eta(\omega_1)\overline\omega_2-\eta(\omega_2)\overline\omega_1}{\omega_1\overline\omega_2-\omega_2\overline\omega_1}.$$ The normalized sigma function and Hermitian form are $$S(z)=\sigma_\Lambda(z)e^{-s_2z^2/2},\qquad h(z,w)=\frac{z\overline w}{A}\qquad(z,w\in\mathbb C).$$ For $x\in\mathbb C$ and any function $F:\mathbb C\to\mathbb C$, define its Hermitian translate by $$(U_xF)(z)=F(z+x)\exp\left(-\pi h(z,x)-\frac\pi2h(x,x)\right)\qquad(z\in\mathbb C).$$

For $t,z\in\mathbb C$, the normalized translated sigma function is $$\theta_{0,\Lambda}(t,z)=\frac{(U_tS)(z)}{(U_tS)(0)}.$$
