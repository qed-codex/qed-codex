---
{
  "module": "src/Formalism/HarderNarasimhan/HarderNarasimhanProofs/MuChar.lean",
  "declarations": [
    "Formalism.HN.slope_characterization"
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

## Characterization and attainment of extreme lattice slopes

[Theorem ARAK.1132](https://andrewodesky.com/rh/lean/Formalism.HN.slope_characterization/)

Let $R$ be a ring, $V$ an $R$-module, $E$ a finite-dimensional real inner product space, and $\rho:V\to E$ additive. Let $0\ne L\subseteq V$ be an $R$-submodule on which $\rho$ is injective, with $\rho(L)$ discrete. For $N\subseteq L$ put $r(N)=\operatorname{rk}_{\mathbb Z}\rho(N)$, $d(N)=-\log\operatorname{covol}\rho(N)$, and $\mu(N)=d(N)/r(N)$, taking $d(0)=\mu(0)=0$ and covolumes in the real span. Call $N$ saturated if $\rho(N)=\rho(L)\cap\operatorname{span}_{\mathbb R}\rho(N)$. Let $\mu_{\max}(L)$ be the supremum of $\mu(N)$ over nonzero $R$-submodules $N\subseteq L$, and let $\mu_{\min}(L)$ be the infimum of the slopes of the lattices obtained by orthogonally projecting $\rho(L)$ along $\operatorname{span}_{\mathbb R}\rho(N)$ for proper saturated $R$-submodules $N$. For every $\theta\in\mathbb R$, $$\mu_{\max}(L)\le\theta\ \Longleftrightarrow\ d(N)\le\theta r(N)\quad\text{for every }N\subseteq L,$$ $$\theta\le\mu_{\min}(L)\ \Longleftrightarrow\ \theta\bigl(r(L)-r(N)\bigr)\le d(L)-d(N)\quad\text{for every }N\subseteq L.$$ Some nonzero saturated $N\subseteq L$ satisfies $\mu(N)=\mu_{\max}(L)$, and $$\mu_{\min}(L)\le\mu(L)\le\mu_{\max}(L).$$
