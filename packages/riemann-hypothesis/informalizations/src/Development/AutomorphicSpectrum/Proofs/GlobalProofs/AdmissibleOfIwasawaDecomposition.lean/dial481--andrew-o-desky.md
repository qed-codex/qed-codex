---
{
  "module": "src/Development/AutomorphicSpectrum/Proofs/GlobalProofs/AdmissibleOfIwasawaDecomposition.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.Hypotheses₂.HCA.analytic_uj"
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

## Analytic coefficients from factorial derivative bounds

[Theorem REP.1708](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Hypotheses%E2%82%82.HCA.analytic_uj/)

Let $J=\operatorname{diag}(\epsilon_1,\ldots,\epsilon_n)$ with $\epsilon_i\in\{1,-1\}$, and $G=\{g\in M_n(\mathbb C):g^*Jg=J\}$. Let $H$ be a complex Hilbert space and $\pi:M_n(\mathbb C)\to\mathcal B(H)$ satisfy $\pi(1)=1$ and $\pi(ab)=\pi(a)\pi(b)$ for $a,b\in G$. Assume every orbit map $g\mapsto\pi(g)u$ is continuous on $G$.

Let $v\in H$ have an orbit map that extends to a smooth real map on the ambient matrix space. Write $D_Xu=\left.\frac{d}{dt}\pi(\exp(tX))u\right|_{t=0}$ and $\|X\|_1=\sum_{a,b}|X_{ab}|$. Suppose there is $C>0$ such that, for every finite list $X_1,\ldots,X_m$ in the real Lie algebra of $G$, $$\|D_{X_1}\cdots D_{X_m}v\|\le C^{m+1}m!\prod_{i=1}^m\|X_i\|_1.$$ Then, for every $w\in H$, the function $g\mapsto\langle w,\pi(g)v\rangle$ locally extends from $G$ to a real-analytic function on the ambient matrix space.
