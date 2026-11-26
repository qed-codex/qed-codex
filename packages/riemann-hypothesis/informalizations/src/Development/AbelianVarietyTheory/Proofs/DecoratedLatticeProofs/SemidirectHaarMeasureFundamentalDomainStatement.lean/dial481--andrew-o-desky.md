---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SemidirectHaarMeasureFundamentalDomainStatement.lean",
  "declarations": [
    "GlobalTheory.T.semidirect_haar_measure_fundamental_domain"
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

## Integration over a semidirect-product fundamental domain

[Theorem THETA.0622](https://andrewodesky.com/rh/lean/GlobalTheory.T.semidirect_haar_measure_fundamental_domain/)

Fix the source's complete global arithmetic theta datum and two of its Hermitian spaces. Write $G,H$ for their adelic unitary groups and $\Gamma_G,\Gamma_H$ for their rational subgroups. Let $N\subseteq G$ be a closed subgroup and $s:H\to G$ a continuous homomorphism normalizing $N$. Assume that $$ns(h)=n's(h')\Longrightarrow n=n'\ \text{and}\ h=h',$$ for $n,n'\in N$, $h,h'\in H$, and that $$ns(h)\in\Gamma_G\quad\Longleftrightarrow\quad n\in\Gamma_G\ \text{and}\ h\in\Gamma_H.$$ Choose a Haar measure $\mu_H$ on $H$ and a fundamental domain $\mathcal F_H$ for $\Gamma_H$. Choose a Haar measure $\nu$ on $N$ and a fundamental domain $\mathcal N$ for $\Gamma_G\cap N$. Put $L=\langle N,s(H)\rangle$ and let $\mu_L$ be the pushforward of $\mu_H\times\nu$ under $(h,n)\mapsto ns(h)$. Assume $\mu_L$ is a Haar measure on $L$.

There is a fundamental domain $\mathcal R\subseteq L$ for $\Gamma_G\cap L$ such that, for every measurable $f:G\to\mathbb C$, $f|_{\mathcal R}$ is integrable exactly when $$\int_{\mathcal F_H}\int_{\mathcal N}|f(ns(h))|\,d\nu(n)\,d\mu_H(h)<\infty.$$ When these conditions hold, $$\int_{\mathcal R}f(r)\,d\mu_L(r)=\int_{\mathcal F_H}\int_{\mathcal N}f(ns(h))\,d\nu(n)\,d\mu_H(h).$$
