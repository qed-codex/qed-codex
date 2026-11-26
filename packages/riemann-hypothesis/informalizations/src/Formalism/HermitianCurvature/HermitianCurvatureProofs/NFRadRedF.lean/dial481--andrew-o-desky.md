---
{
  "module": "src/Formalism/HermitianCurvature/HermitianCurvatureProofs/NFRadRedF.lean",
  "declarations": [
    "Formalism.FourierDecayAlt.P.representation_smooth"
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

## Local smooth extension of a continuous finite-dimensional representation

[Theorem REP.0877](https://andrewodesky.com/rh/lean/Formalism.FourierDecayAlt.P.representation_smooth/)

Let $k,r\ge0$, $N=2r+k+1$, and use coordinates $0,\ldots,N-1$. Let $J$ be the Hermitian matrix pairing $e_a$ with $e_{N-1-a}$ for $0\le a<r$, having entries $+1$ on $e_r,\ldots,e_{r+k-1}$ and $-1$ on $e_{r+k}$, and zero otherwise. Let $z\in\mathbb C^N$ be supported on coordinates $r,\ldots,r+k$, with $z^*Jz<0$, and put $$K_z=\{g:g^*Jg=J,\ ge_a=e_a,\ ge_{N-1-a}=e_{N-1-a}\ (0\le a<r),\ gz=z\}.$$ Let $H$ be a finite-dimensional normed complex vector space, and let $\pi:\operatorname{Mat}_N(\mathbb C)\to\mathcal L(H)$ satisfy $\pi(1)=1$ and $\pi(ab)=\pi(a)\pi(b)$ for $a,b\in K_z$. Suppose $\pi$ is continuous on $K_z$. For every $h_0\in K_z$, there are an open neighborhood $V$ of $h_0$ in $\operatorname{Mat}_N(\mathbb C)$ and a real $C^\infty$ function $P:V\to\mathcal L(H)$ such that $P(h)=\pi(h)$ on $V\cap K_z$.
