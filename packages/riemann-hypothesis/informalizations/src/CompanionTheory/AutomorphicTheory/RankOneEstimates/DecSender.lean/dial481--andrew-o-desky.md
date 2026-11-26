---
{
  "module": "src/CompanionTheory/AutomorphicTheory/RankOneEstimates/DecSender.lean",
  "declarations": [
    "CompanionTheory.FamilyDerivativeExpansion.DecS.decay_infinite_range",
    "CompanionTheory.FamilyDerivativeExpansion.DecS.decay_low_range"
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

## Decay of matrix coefficients on the lowest compact type

[Theorem REP.1585](https://andrewodesky.com/rh/lean/CompanionTheory.FamilyDerivativeExpansion.DecS.decay_low_range/)

Let $k\ge1$, $r\ge0$, and $N=2r+k+1$. Let $H$ be the Hermitian matrix consisting of $r$ hyperbolic pairs and a middle block $\operatorname{diag}(1_k,-1)$, and put $G=U(H)$. Let $\epsilon\in\{\pm1\}^N$, $\lambda\in\mathbb R^N$ and $h\in\mathbb R$ satisfy $$\lambda_1>\cdots>\lambda_N,\quad\lambda_i-(N-1)/2\in\mathbb Z,\quad|\lambda_i-\lambda_j|\ge h\ \ (\epsilon_i\ne\epsilon_j),\quad h\ge120N^3.$$ Let $\sigma$ act on a complex Hilbert space and satisfy the discrete-series conditions in the conventions below for $(\epsilon,\lambda)$ on $G$. Fix a unitary matrix $P$ with $P^*\operatorname{diag}(\epsilon)P=H$. Let $w_1,w_2$ lie in the lowest compact-type subspace for the action $g\mapsto\sigma(P^{-1}gP)$ of $U(\epsilon)$.

There is $C\in\mathbb R$ such that $$|\langle w_2,\sigma(x)w_1\rangle|\le C\|x\|_{\mathrm F}^{-h/(8\sqrt{2(r+1)})}\qquad(x\in G),$$ where $\|x\|_{\mathrm F}=(\sum_{i,j}|x_{ij}|^2)^{1/2}$.

## Decay of discrete-series coefficients controlled by finitely many derivatives

[Theorem REP.1537](https://andrewodesky.com/rh/lean/CompanionTheory.FamilyDerivativeExpansion.DecS.decay_infinite_range/)

Let $k,r\ge0$, $N=2r+k+1$, and let $G$ be the source's matrix realization of $U(r+k,r+1)$, with $r$ hyperbolic pairs and a middle diagonal block $(1_k,-1)$. Fix a signature $\varepsilon$ and real parameters $\lambda_1>\cdots>\lambda_N$ with $\lambda_i-(N-1)/2\in\mathbb Z$. Let $\sigma$ act on a complex Hilbert space and satisfy the source's discrete-series conditions for $(\varepsilon,\lambda)$ after a Cayley identification with $G$. Assume $|\lambda_i-\lambda_j|\ge h$ whenever $\varepsilon_i\ne\varepsilon_j$.

Put $$a=\frac{h}{8\sqrt{2(r+1)}},\quad A_G=4(k+r)(r+1),\quad d_N=r(r-1)+2r(k+1)+r^2,$$ $$A_S=(2r+k)d_N,\qquad M=2(r^2+r+1),$$ and assume $$k\ge1,\quad h\ge120N^3,\quad a\ge2M(A_S+A_G)+A_G+3,\quad a\ge9(r+1)N^2+3A_G+3.$$ For every vector $v_0$ finite under the compact subgroup $G\cap U(N)$, there are $C\in\mathbb R$ and a finite list $\mathcal W$ of words in the real Lie algebra of $G$ such that, for every smooth $w$ and $x\in G$, $$|\langle v_0,\sigma(x)w\rangle| \le C\left(\sum_{W\in\mathcal W}\|D_Ww\|\right)\|x\|_{\mathrm F}^{1-a}.$$ Here $D_W$ is the iterated infinitesimal action and $\|x\|_{\mathrm F}=(\sum_{i,j}|x_{ij}|^2)^{1/2}$.
