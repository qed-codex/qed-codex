---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/CubicalLineBundles/IsLieNormSqIffEqPiDivCovolume.lean",
  "declarations": [
    "GlobalTheory.isLieNormSq_iff_eq_pi_div_covolume"
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

## The tangent norm of an elliptic period lattice

[Theorem AV.0873](https://andrewodesky.com/rh/lean/GlobalTheory.isLieNormSq_iff_eq_pi_div_covolume/)

Assume ([Theta functions for a principally polarized complex abelian variety](https://andrewodesky.com/rh/lean/GlobalTheory.thetaUnifAV_closed/)) and the polarized-base-change package specified below. Let $R$ be a commutative ring, $(A,L)/R$ a principally polarized abelian scheme of relative dimension one, $v\in\operatorname{Lie}(A/R)$, and $s:R\to\mathbb C$. Let $\Lambda=\mathbb Z\omega_1+\mathbb Z\omega_2\subseteq\mathbb C$ be an elliptic period lattice. Suppose that, for every polarized complex fibre $(A',L')$ of $(A,L)$ at $s$, every tangent lift $v'$ of $v$, and every holomorphic uniformization $e:\mathbb C\to A'(\mathbb C)$ with differential $de(w)=v'$, one has $$w\ne0,\qquad z\in\Lambda\ \Longleftrightarrow\ zw\in\ker e.$$ Then $\pi/|\operatorname{Im}(\omega_1\bar\omega_2)|>0$, and, for every $r\in\mathbb R$, $$r\text{ is a squared Lie norm of }v\text{ at }s \quad\Longleftrightarrow\quad r=\frac{\pi}{|\operatorname{Im}(\omega_1\bar\omega_2)|}.$$
